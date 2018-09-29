BY: Muppidi Harshavardhan Reddy(mreddy2) && Srinivas Parasa (sparasa)

This Readme includes details regarding how to run the scripts and the implementations. 
PLEASE NOTE: Have the script files(monitor.sh and clear.sh) in your home directory for easier management. 
If not you would need to specify the log files path in the clear.sh file and also accordingly change path for your cronjob command. 

Assuming the home directory here to be /home/ece792

[1] Monitoring Script: (File Name: monitor.sh)

This script needs 4 different arguments:
1. Required Seconds granularity for CPU Load Averages to be logged.(in seconds)
2. Total duration for the logging to be done(in seconds)
3. The Alert Threshold limit for last 1 Min CPU Usage 
4. The Alert Threshold limit for last 5 Min CPU Usage

These values are given as command line arguments.An example for running this script would be:
./monitor.sh 5 100 0.05 0.25
Log CPU Load Averages for every 5 seconds for a total duration of 100seconds with the 1min Threshold of 0.05 and 5min Threshold of 0.25.

The CPU Load Averages are logged in file name: cpu_load.csv
The Alerts are logged in file name: alert.csv

Please make sure the script files are in home directory for easier path management. 

Based on the 4 inputs the script logs into the files as per the below format:
cpu_load.csv : timestamp, 1 min load average, 5 min load average, 15 min load average
Alert.csv    : timestamp, alert String, CPU load Average

In the Alert.csv, the respective CPU Load average is logged. 
For ex: if it's a alert with respect to the last 1 min Average it logs the CPU Load Average of that particular Last 1min only and not the others(5min or 15mins).

Apart from logging whenever there is an alert it shows an alert message 
For Last 1min CPU Load Averages: HIGH CPU Usage
For Last 5min CPU Load Averages: Very HIGH CPU Usage



[2] Log Cleaning Script (File Name: clear.sh)

This script cleans the log files. For it to clear the log files every hour we are using cronjobs.

-> crontab -e
-> To the file Add the command "0 * * * * /home/ece792/clear.sh" (assuming the path of the scripts to be in home directory) 


This Cronjob runs the clear.sh script every hour which clears the log files.




The Graph showing one minute load average taken every 10 seconds over 10 minutes duration is attached with the submission with the timestamps along the X-Axis and the Load Averages along the Y-Axis. (The System was stressed before capturing the information)

 

