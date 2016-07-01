#!/bin/bash
echo "Start Get Link Menu"

    python getLinkMenu.py  $line
    # get one csv file linkmenu.csv

echo "Finished get link menu"
wait 20
echo "Start Get Link of Product"

    python getLinkPro.py  $line
    #get one csv file linkprodetail.csv

echo "Finished get link product"
wait 20
echo "Start get data in product detals"

	python getProDetail.py  $link
	#get one json file ProductDetail.json

echo "Finished get data"
