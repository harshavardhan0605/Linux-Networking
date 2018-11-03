from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom


conn = libvirt.open('qemu:///system')
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

	
	print('MAC and IP address for VM-'+dom.name())
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
                				print('MAC address: '+
                 				interfaceNode.attributes[attr].value)

	#code to get ip address of different L3 interfaces present on all vm's present in the hypervisor
	try:
		ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
	except:
		continue
	
	print("The interface IP addresses:")
	for (name, val) in ifaces.iteritems():
    		if val['addrs']:
        		for ipaddr in val['addrs']:
            			if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4 and ipaddr['addr']!='127.0.0.1':
                			print('IP address:'+ipaddr['addr'])

conn.close()
exit(0)
