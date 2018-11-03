BY: Srinivas Parasa(sparasa) & Muppidi Harshavardhan Reddy(mreddy2)

This Readme includes details about the Question 2:

-> [1]. (playbook_hw3_q2_1.yaml)
Run the script with sudo.
Make sure that q2-1-1.xml, q2-1-2.xml, q2-1-3.xml, q2-1-4.xml are deleted every time you run from /home/ece792 

-> [2]. (playbook_hw3_q2_2.yaml)
Run the script with sudo.

-> [3]. (playbook_hw3_q2_3.yaml)
Run the script with sudo.
This sensible will be running playbook_app.yaml inside.
This playbook_app.yaml will install Wireshark and iperf in the guest VM's. 

As soon as the Guest VM's are installed, dhclient should be run on both the Guest VM's on eth0 interface. So these Ip's along with username's and password needs to be manually kept inside /etc/ansible/hosts file under the group "Group1".

The above changes will help the ansible to login into the VM's

BONUS QUESTION:
We have done the bonus question as well.
We had implemented for fixed number of interfaces by taking VM name and 2 interfaces from the command prompt. 