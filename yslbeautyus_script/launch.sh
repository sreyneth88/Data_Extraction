#!/bin/bash
echo "Start get link menu"

        python getLinkMenu.py $line
        #get one csv file ysl_link_menu.csv

echo "successful get link menu" 
wait 20
echo "Start get link product"
cat ysl_link_menu.csv | while read line
do 
        python getLinkPro.py $line
        #get one csv file ysl_link_product.csv
 wait
done
echo "successful get link product" 
wait 20
echo "Start get data in product detail"
cat ysl_link_product.csv | while read line
do 
        python getDetail.py $line
        #get one json file ysl_product.json
  wait
done
echo "successful get data" 