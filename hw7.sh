#!/bin/bash

rm $1/*~
rm $1/core.*
echo -e "All emacs backup files and core file in the directory" $1 "have been deleted.\n"

ls $1
echo -e "\n"

echo $#
echo -e "This is the the number of postional parameters the script has.\n"
echo $*
echo -e "This is the value of the positional parameters.\n"

cat /home/kstoltzf/.signature
echo -e "This is my signature for alpine.\n"

ps 
