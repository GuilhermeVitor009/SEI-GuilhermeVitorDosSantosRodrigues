#!/usr/bin/bash

echo "Name = $1";
echo "Age = $2";
echo "Sex = $3";
echo "my first bash program!!!"
GREET="HelooDOG"
echo $GREET

while true; do
	read -p "Do you wish to drink a beer? " yn
	case $yn in
		[Yy]* ) break;;
		[Nn]* ) break;;
		* ) echo "Please answer yes or no.";;
	esac

done

if [$2 -lt 21]; then
	echo "You are too young to take this beer!! "
else
	echo "Enjoy your beer $1 !!"	
fi

long_process &
slow_stuff &
async_job 
