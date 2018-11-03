from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom
import random
import time

def modifymac():
	conn = libvirt.open('qemu:///system')
	if conn == None:
		print('Failed to open connection to qemu:///system', file=sys.stderr)
    		exit(1)

	try:  # getting a list of all domains (by ID) on the host
    		domains = conn.listDomainsID()
	except:
    		raise Exception('Failed to find any domains')

	dic=[]
	ip_dic=[]
#	tup={104,105}
	for domain_id in domains:
        	# Open that vm
        	dom = conn.lookupByID(domain_id)
        	if dom == None:
                	print('Failed to find the domain '+dom.name(), file=sys.stderr)
                	exit(1)

		#code to get mac address of different interfaces of all vm's present in the hypervisor
		print("---------- Current running on VM:  "+dom.name()+'.......................')
        	raw_xml = dom.XMLDesc(0)
        	xml = minidom.parseString(raw_xml)
        	interfaceTypes = xml.getElementsByTagName('interface')
        	for interfaceType in interfaceTypes:
                	interfaceNodes = interfaceType.childNodes
                	for interfaceNode in interfaceNodes:
                        	if interfaceNode.nodeName[0:1] != '#' and interfaceNode.nodeName=='mac':
                                	for attr in interfaceNode.attributes.keys():
                                        	if interfaceNode.attributes[attr].name=='address':
							val=interfaceNode.attributes[attr].value
							print('present MAC address:'+val)
                                                	while interfaceNode.attributes[attr].value in dic:
								interfaceNode.attributes[attr].value=randomMAC()
							dic.append(interfaceNode.attributes[attr].value)
							if val!=interfaceNode.attributes[attr].value:
								print(dom.name()+' has conflicting MAC address and new resolved MAC address '+interfaceNode.attributes[attr].value)
								raw_xml= xml.toxml()
        							#print(raw_xml)
        							conn.defineXML(raw_xml)
        							dom.shutdown()
        							time.sleep(20)
        							if not dom.isActive():
                							dom.create()
        							raw_xml = dom.XMLDesc(0)
        							#print(raw_xml)

		
		#code for resolving the IP address of different machines in a hypervisor
		
		try:
                	ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
        	except:
                	continue

		for (name, val) in ifaces.iteritems():
                	if val['addrs']:
                        	for ipaddr in val['addrs']:
                                	if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4 and ipaddr['addr']!='127.0.0.1':
                                        	print('present IP address:'+ipaddr['addr'])
						if ipaddr['addr'] in ip_dic:
							print(dom.name()+' has conflictings IP shutting down so that it loses IP')
							dom.shutdown()
                                                	time.sleep(20)
                                                	if not dom.isActive():
                                                		dom.create()
						else:
							ip_dic.append(ipaddr['addr'])
	conn.close()
	exit(0)							

def randomMAC():
	mac = [ 0x00, 0x16, 0x3e,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))



def main():
        if len(sys.argv)==1:
                modifymac()
        else:
                print('please pass required number of parameters as given in readme')			

if __name__ == "__main__":
        main()			
