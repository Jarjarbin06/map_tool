#############################
###                       ###
###          MAP          ###
###   ----GetVersion----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

try :
    with open("files\\info\\version.txt", 'r') as file :
        version = file.read()
    file.close()
except FileNotFoundError :
    with open("version.txt", 'r') as file :
        version = file.read()
    file.close()