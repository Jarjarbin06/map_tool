#############################
###                       ###
###          MAP          ###
### ----UpdateVersion---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

with open("version.txt", 'r') as file :
    version = file.read()
file.close()

print(f"{version}", end = "")

version = version.split(".")

version[2] = int(version[2]) + 1

if int(version[2]) > 9 :
    version[2] = 0
    version[1] = int(version[1]) + 1

if int(version[1]) > 9 :
    version[1] = 0
    version[0] = int(version[0]) + 1

version = f"{version[0]}.{version[1]}.{version[2]}"

with open("version.txt", 'w') as file :
    file.writelines(version)
file.close()

print(f" -> {version}")