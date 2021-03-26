import os
import shutil

#SX OS to Atmosphere
shutil.move("boot.dat","SX/boot.dat")

shutil.move("./sxos/emunand/boot0.bin","./EMUMMC/SD00/emmc/BOOT0")
shutil.move("./sxos/emunand/boot1.bin","./EMUMMC/SD00/emmc/BOOT1")


for i in range (8):
    shutil.move("./sxos/emunand/full.0"+ str(i) +".bin","./EMUMMC/SD00/emmc/0"+ str(i))


shutil.move("ATMOS/boot.dat","boot.dat")
shutil.move("ATMOS/boot.ini","boot.ini")