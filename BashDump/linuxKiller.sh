#!/bin/bash

#                              #    #                               
#       # #    # #    # #    # #   #  # #      #      ###### #####  
#       # ##   # #    #  #  #  #  #   # #      #      #      #    # 
#       # # #  # #    #   ##   ###    # #      #      #####  #    # 
#       # #  # # #    #   ##   #  #   # #      #      #      #####  
#       # #   ## #    #  #  #  #   #  # #      #      #      #   #  
####### # #    #  ####  #    # #    # # ###### ###### ###### #    # 
#============================================= By Zero Davila 2016
#Wiping the entire diskEdit
#This will overwrite all partitions, master boot records, and data. Use the sudo command as well (sudo dd...)
#   Filling the disk with all zeros (This may take a while, as it is making every bit of data 0) :
#   dd if=/dev/zero of=/dev/sdX bs=1M *replace X with the target drive letter.
#   If you are wiping your hard drive for security, you should populate it with random data rather than zeros (This is going to take even longer than the first example.) :
#   dd if=/dev/urandom of=/dev/sdX bs=1M *replace X with the target drive letter.
#The reason one should fill with urandom in case of required security is explained here: [1]
#Important Note: You need to replace sda with the device name you want to overwrite. sda is usually the first hard drive, the second drive would be sdb and so on. Use for example gparted to find the correct drive. If you replace the device name, you can also wipe USB sticks and other peripherals.
#Wiping the Master boot record (MBR)Edit
#If you messed up your master boot record (MBR) you can wipe it using this command :
#   dd if=/dev/zero of=/dev/hdX bs=446 count=1 *replace X with the target drive letter.
#Wiping partitionsEdit
#You can wipe a partition using the same method than for the whole disk. Just replace the device identifier. i
#If /dev/sda is the whole disk, then (on Linux, because the naming scheme vary from one Linux to another) 
#/dev/sda3 is the third partition on the disk.
#   Filling the second partition on the /dev/sda disk with all zeros :
#   dd if=/dev/zero of=/dev/sdX2 bs=1M *replace X with the target drive letter.
#   Filling the third partition with random data :
#   dd if=/dev/urandom of=/dev/sdX3 bs=1M *replace X with the target drive letter.

echo """
                                   
                            .,:clooll:,.
                        ;dKWMMMMMMMMMMMMWKx:
                      :XMMMMMMMMMMMMMMMMMMMMX:
                     oMMMMMMMMMMMMMMMMMMMMMMMMl
                    .WlXMMMMMMMMMMMMMMMMMMMMXcN.
                    ,N 0MMMMMMMMMMMMMMMMMMMMX K;
                    .N;cMMMMMMMMMMMMMMMMMMMMo,W.
                     :k.MXkdlcckMMMMk:clokXM,dc
                      .'X.     .NMMW.      K:
             ,x'       oM:    .OMMMM0.    :Wx       .x,
             OMWl      dMWk:;dNWoc:oWNd::xWMk      :WMO
           ,KMMMMNkc'  .dKWMMMMd ;' oMMMMW0d.  .:dXMMMM0'
           .''..;oONMNkc' .;xWMd.xo.oMMk;. .:xXMWKd:'',;.
                    .cxXMc'l,cNWWWWWNXo'c,:MNkl'
                        ...loccllooccccll'..
                          .Kcccllodlccl:X.
                     .,oON:oWN0kkOOkk0NWo,NOo,.
              .dxddkKWMKx:. .oOXWWWWXOo. .:xXMWKxoooo.
               .OMMMk:.                      .c0MMM0,
                .WX,                            ;XM'
                 '                               .,
#                              #    #                               
#       # #    # #    # #    # #   #  # #      #      ###### #####  
#       # ##   # #    #  #  #  #  #   # #      #      #      #    # 
#       # # #  # #    #   ##   ###    # #      #      #####  #    # 
#       # #  # # #    #   ##   #  #   # #      #      #      #####  
#       # #   ## #    #  #  #  #   #  # #      #      #      #   #  
####### # #    #  ####  #    # #    # # ###### ###### ###### #    # 
#============================================= By Zero Davila 2016
"""

echo "[1] Zero fill Hard Drive"
echo "[2] Random data fill HD *4SECURITY*"
echo "[3] Wipe Master Boot Record"
echo "[4] Wipe specific partition"
echo "[5] Zero fill specific partition"
echo "[6] Random data fill partition *4SEC*"

read -p "[ ! ]> " INPUT

if [[ $INPUT -eq 1 ]]
then
    echo "[*] You have chosen to Zero Fill a Hard Drive!"
    echo "[*] This will take some time..."
    echo "[*] The command about to be executed is :"
    echo "[!] dd if=/dev/zero of=/dev/sdX bs=1M"
    echo "[*] Replace X with the target drive letter."
    echo "[*] \'a\' is the first HD, \'b\' is the second, etc."
    echo "[*] If unsure, or if you only have one hard drive, insert the letter \'a\'"
    read -p "ZeroFillHD> " TARGET1
    sudo dd if=/dev/zero of=/dev/sd$TARGET1 bs=1M
fi

if [[ $INPUT -eq 2 ]]
then
    echo "[*] You have chosen to Random Data Fill a Hard Drive!"
    echo "[*] This is used for security purposes and will take some time..."
    echo "[*] The command about to be executed is :"
    echo "[!] dd if=/dev/urandom of=/dev/sdX bs=1M"
    echo "[*] Replace X with the target drive letter."
    echo "[*] \'a\' is the first HD, \'b\' is the second, etc."
    echo "[*] If unsure, or if you only have one hard drive, insert the letter \'a\'"
    read -p "RandFillHD> " TARGET2
    sudo dd if=/dev/urandom of=/dev/sd$TARGET2 bs=1M
fi

if [[ $INPUT -eq 3 ]]
then
    echo "[*] You have chosen to Wipe the Master Boot Record!"
    echo "[*] The command about to be executed is :"
    echo "[!] dd if=/dev/zero of=/dev/hdX bs=446 count=1"
    echo "[*] Replace X with the target drive letter."
    echo "[*] \'a\' is the first HD, \'b\' is the second, etc."
    echo "[*] If unsure, or if you only have one hard drive, insert the letter \'a\'"
    read -p "WipeMBR> " TARGET3
    sudo dd if=/dev/zero of=/dev/hd$TARGET3 bs=446 count=1
fi

if [[ $INPUT -eq 4 ]]
then
    echo "[*] You have chosen to Wipe a Specific Partition!"
    echo "[*] The command about to be executed is :"
    echo "[!] dd if=/dev/zero of=/dev/sdXY bs=446 count=1"
    echo "[*] Replace X with the target drive letter, Y with partition number"
    echo "[*] \'a\' is the first HD, \'b\' is the second, etc."
    echo "[*] \'1\' is the first partition, \'2\' the second, etc."
    echo "[*] If unsure, or if you only have one hard drive, insert the letter \'a\'"
    echo "[*] If unsure, or if you only have one disk partition, insert the number \'1\'"
    read -p "TargetDrive> " TARGET4
    read -p "TargetPartition> " TARGET5
    sudo dd if=/dev/zero of=/dev/sd$TARGET4$TARGET5 bs=446 count=1
fi

if [[ $INPUT -eq 5 ]]
then
    echo "[*] You have chosen to Zero Fill a Partition!"
    echo "[*] This will take some time..."
    echo "[*] The command about to be executed is :"
    echo "[!] dd if=/dev/zero of=/dev/sdXY bs=1M"
    echo "[*] Replace X with the target drive letter, Y with partition number"
    echo "[*] \'a\' is the first HD, \'b\' is the second, etc."
    echo "[*] \'1\' is the first partition, \'2\' the second, etc."
    echo "[*] If unsure, or if you only have one hard drive, insert the letter \'a\'"
    echo "[*] If unsure, or if you only have one disk partition, insert the number \'1\'"
    read -p "TargetDrive> " TARGET6
    read -p "TargetPartition> " TARGET7
    sudo dd if=/dev/zero of=/dev/sd$TARGET6$TARGET7 bs=1M
fi

if [[ $INPUT -eq 6 ]]
then
    echo "[*] You have chosen to Random Data Fill a Partition!"
    echo "[*] This is used for security purposes and will take some time..."
    echo "[*] The command about to be executed is :"
    echo "[!] dd if=/dev/urandom of=/dev/sdXY bs=1M"
    echo "[*] Replace X with the target drive letter, Y with partition number"
    echo "[*] \'a\' is the first HD, \'b\' is the second, etc."
    echo "[*] \'1\' is the first partition, \'2\' the second, etc."
    echo "[*] If unsure, or if you only have one hard drive, insert the letter \'a\'"
    echo "[*] If unsure, or if you only have one disk partition, insert the number \'1\'"
    read -p "TargetDrive> " TARGET8
    read -p "TargetPartition> " TARGET9
    sudo dd if=/dev/urandom of=/dev/sd$TARGET8$TARGET9 bs=1M
fi

