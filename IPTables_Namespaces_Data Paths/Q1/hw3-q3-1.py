from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom
import time
import random

def modifyMACandIP():
	#print("enetered into this function")
	#tup=["qemu+ssh://ece792@192.168.124.5/system"]

	tup=[]
	for i in range(1,len(sys.argv)):
        	tup.append('qemu+ssh://'+sys.argv[i]+'/system')

	dic=[]
	ip_dic=[]
	for hyp in tup:
        	conn = libvirt.open(hyp)
        	if conn == None:
                	print('Failed to open connection to qemu:///system', file=sys.stderr)
                	exit(1)
        	try:  # getting a list of all domains (by ID) on the host
                	domains = conn.listDomainsID()
        	except:
                	raise Exception('Failed to find any domains')

        	for domain_id in domains:
                	# Open that vm
                	dom = conn.lookupByID(domain_id)
                	if dom == None:
                        	print('Failed to find the domain '+dom,name(), file=sys.stderr)
                       	 	exit(1)


               		print('----------------------details of VM- '+dom.name()+'----------------------')
                	#code to get mac address of different interfaces of all vm's present in the hypervisor
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
								print("MAC of VM : "+dom.name()+"is:  "+val)
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
                



                	#code to get ip address of different L3 interfaces present on all vm's present in the hypervisor
                	try:
                        	ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
                	except:
                        	continue 
          
                	#print("The interface IP addresses:")
                	for (name, val) in ifaces.iteritems():
                        	if val['addrs']:
                                	for ipaddr in val['addrs']:
						if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4 and ipaddr['addr']!='127.0.0.1':
                                        		print('IP address of VM: '+dom.name() +"is :"+ipaddr['addr'])
							if ipaddr['addr'] in ip_dic:
                                        			print(dom.name()+' has conflictings IP shutting down so that it loses IP')
                                                		dom.shutdown()
                                                		time.sleep(20)
                                                		if not dom.isActive():
                                                			dom.create()
                                       			else:
                                           			ip_dic.append(ipaddr['addr'])
        	conn.close()

def randomMAC():
        mac = [ 0x00, 0x16, 0x3e,
                random.randint(0x00, 0x7f),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff) ]
        return ':'.join(map(lambda x: "%02x" % x, mac))



def main():
        if len(sys.argv)>1:
                modifyMACandIP()
        else:
                print('please pass required number of parameters as given in readme')

if __name__ == "__main__":
        main()


