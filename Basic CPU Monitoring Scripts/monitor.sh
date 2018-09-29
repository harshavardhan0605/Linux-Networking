#!/bin/bash
loop=`expr $2 / $1`

while [ $loop -gt 0 ]
do
cpu_load=$(uptime | awk -F'[a-z]:' '{split($1,a," "); print a[1] "," $2}');
echo $cpu_load;
echo $cpu_load >> cpu_load.csv;
A=$(awk -F, '{print $2}' <<< $cpu_load)
B=$(awk -F, '{print $3}' <<< $cpu_load)
C=$(awk -F, '{print $4}' <<< $cpu_load)

#check for 1min average
if [ $(bc <<< "$A > $3") -eq 1 ];
then
echo "HIGH CPU Usage"
log1=$(awk -F, '{split($1,a," "); print a[1] ",HIGH CPU Usage,"} {print $2}' <<< $cpu_load)
echo $log1 >> alert.csv;
fi

#check for 5min average
if [ $(bc <<< "$B > $4") -eq 1 ];
then
if [ $(bc <<< "$A > $B") -eq 1 ] || [ $(bc <<< "$A > $C") -eq 1 ]
then
echo "Very HIGH CPU Usage"
log2=$(awk -F, '{split($1,a," "); print a[1] ",Very HIGH CPU Usage,"} {print $3}' <<< $cpu_load)
echo $log2 >> alert.csv;
fi
fi
sleep $1
let "loop--"
done