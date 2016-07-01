#!/bin/bash
echo "Start get link"
cat allproduct.csv | while read line
do 
         python searchproduct.py  ${line// /_}
 wait
done
echo "Finished get link"
