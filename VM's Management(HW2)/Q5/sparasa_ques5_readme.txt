BY: Srinivas Parasa(sparasa) & Muppidi Harshavardhan Reddy(mreddy2)

This Readme includes details about the Question5 ( Python Libvirt API) 

-->We have 3 python scripts for this part of the question named:
	hostinfo.py
	guestinfo.py
	q5.py

-> hostinfo.py and guestinfo.py files are for the part 1&2 of the question 5 which gives the host information and guest information respectively. 

->q5.py is the combined code for both the Part 3 and as well as the Bonus question. 

Cases:
[1] For question [3.a] User input only either CPU or MEM
    It will print all VM's CPU or Memory Utilization in ascending order based on the user                     
    input being either CPU or MEM 
	Output Format: Hostname, Utilization(Not %  

[2] For question [3.b] User Input <CPU/MEM> <Theshold>
    Note:Threshold has to be in percentage 
    It will print and as well log into a file called "alert_file.csv" an alert when it crosses the threshold utilization given by the user input.

[3] For Bonus Question User Input <SYS/MEM> <Polling Size> <Window Size>
    [NOTE] Polling Size and Window Size are integer values. //This function call will run with the window interval until you explicitly stop it.
    In case of --->CPU Moving average of time taken by the VM within the polling window.
    In case of --->MEM Moving average of used memory by the VM within the polling window.
    We have considered the polling size as granularity.
    Memory given is in Bytes and the CPU is in seconds, so for a polling size of 5 the moving average for every VM will be in the range of 0-5seconds.
    We tested this by running stress on centos which clarified this assumption.
