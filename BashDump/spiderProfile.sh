#!/bin/bash

 #####                      
#     # #####  # #####  ###### #####  
#       #    # # #    # #      #    # 
 #####  #    # # #    # #####  #    # 
      # #####  # #    # #      #####  
#     # #      # #    # #      #   #  
 #####  #      # #####  ###### #    # 
                                      
######                                       
#     # #####   ####  ###### # #      ###### 
#     # #    # #    # #      # #      #      
######  #    # #    # #####  # #      #####  
#       #####  #    # #      # #      #      
#       #   #  #    # #      # #      #      
#       #    #  ####  #      # ###### ###### 

# USER INPUT

echo "Initiating Spider Profile Construction"
echo
read -p "Filename> " FILENAME
read -p "Name> " NAME
read -p "Sex> " SEX
read -p "Age> " AGE
read -p "Height> " HEIGHT
read -p "Origin> " ORIGIN
read -p "Hair color> " HAIR
read -p "Eye color> " EYE
read -p "Languages> " LANG
read -p "Body structure> " BODY
read -p "Personality type> " PERS
read -p "Characteristics> " CHARS
read -p "Abilities> " ABIL
read -p "JPEG Pic> " PIC

# FILE CONSTRUCTION

jp2a -b --height=30 $PIC >> profile-$FILENAME
echo "|" >> profile-$FILENAME
echo "|__FIELDS_____________VALUES________________________________" >> profile-$FILENAME
echo "|" >> profile-$FILENAME
echo "|>_Name -------------->_$NAME" >> profile-$FILENAME
echo "|>_Sex --------------->_$SEX" >> profile-$FILENAME
echo "|>_Age --------------->_$AGE" >> profile-$FILENAME
echo "|>_Height ------------>_$HEIGHT" >> profile-$FILENAME
echo "|>_Origin ------------>_$ORIGIN" >> profile-$FILENAME
echo "|>_Hair color -------->_$HAIR" >> profile-$FILENAME
echo "|>_Eye color --------->_$EYE" >> profile-$FILENAME
echo "|>_Spoken languages -->_$LANG" >> profile-$FILENAME
echo "|>_Body structure ---->_$BODY" >> profile-$FILENAME
echo "|>_Personality type -->_$PERS" >> profile-$FILENAME
echo "|>_Caharacteristics -->_$CHARS" >> profile-$FILENAME
echo "|>_Abilities --------->_$ABIL" >> profile-$FILENAME
echo "|" >> profile-$FILENAME
echo "|__NOTES____________________________________________________" >> profile-$FILENAME
echo
echo "[*] Put additional notes here"
echo "[*] Write \"notequit\" to interrupt"
while :
do
    read -p "Notes> " NOTES
    if [[ $NOTES = "notequit" ]]
    then
        echo "|____________________________________________________________" >> profile-$FILENAME
        echo >> profile-$FILENAME
        cat profile-$FILENAME
        exit
    else
        echo "|>_$NOTES" >> profile-$FILENAME
    fi
done
