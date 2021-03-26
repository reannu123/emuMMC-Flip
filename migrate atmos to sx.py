import os
import shutil

#Atmosphere to SX OS
shutil.move("boot.dat","ATMOS/boot.dat")
shutil.move("boot.ini","ATMOS/boot.ini")

shutil.move("./EMUMMC/SD00/emmc/BOOT0","./sxos/emunand/boot0.bin")
shutil.move("./EMUMMC/SD00/emmc/BOOT1","./sxos/emunand/boot1.bin")


for i in range (8):
    shutil.move("./EMUMMC/SD00/emmc/0"+ str(i),"./sxos/emunand/full.0"+ str(i) +".bin")


shutil.move("SX/boot.dat","boot.dat")