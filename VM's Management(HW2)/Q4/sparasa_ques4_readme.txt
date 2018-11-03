BY: Srinivas Parasa(sparasa) & Muppidi Harshavardhan Reddy(mreddy2)

This Readme includes details about the question4 with respect to the Ansible Scripts.

[4.1] 
-->We have 2 playbook files for this part of the question named:
	playbook_network.yaml
	playbool_vm.yaml 

-> The first playbook "playbook_network.yaml" defines a new network with a sparasa_NETWORK3.xml file. 
Then it starts the network and also creates a bridge in this playbook. 

-> Then we run the other playbook to create the VM's "playbook_vm.yaml" 
This playbook creates 2 VM's with the network same as created in the above playbook which is sparasa_NETWORK3. 

->Now for the VM's to have IP addresses we manually create a nat bridge and attach it to both VM's, so that we can ssh with the IP addresses for the following next question 4.2.

[4.2] 
-->We have playbook_log.yaml and playbook_cron.yaml for this part of the question.

->Firstly have the both files in the same directory and we run the playbook_cron.yaml file which inturn runs the playbook_log.yaml file with 1minute granularity.

-> The cron playbook runs only in the localhost(hypervisor) while the log playbook runs on 
everyone that is the host and the 2 VM's. This is supported by configuring the ssh keygens at all the VM's and ensuring ssh's go through without hassle.
Please note: Our SSH process works internally using keygen which we configured. 
This is our Host File:
----------------------------------------------------------------------------
192.168.124.5 ansible_user=ece792 ansible_ssh_pass=linux123
192.168.132.68
192.168.132.118
----------------------------------------------------------------------------
-> Now at the VM's and both the hosts, from the uptime result we take the part we need to log from the command line output and log it back at the host inside the var/customlogs/logs folder. 

