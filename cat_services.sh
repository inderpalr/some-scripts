#!/bin/bash 
#THIS SCRIPT WILL ECHO OUT ALL UNCOMMENTED LINES FROM SERVICES.EXT
#NEED TO BE STATIC AS WE WILL PULL SERVICES FROM SERVICES.TXT

CONTENTS=$(<services.txt)
SERVICES=$(echo "$CONTENTS" | grep -v '#')

#LOOP THROUGH SERVICES CERTAIN COMMAND

for i in $SERVICES 
do
 STATUS=$(echo $(systemctl status $i | grep Active | awk '{print $2}'))
 if [ $STATUS = inactive ];
  then
  echo $(notify-send -u critical 'This is from the script check your service.'$i )
  #else
  #echo "All services are running good!! :)"	  
 fi  
done
