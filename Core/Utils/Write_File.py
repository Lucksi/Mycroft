# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class OUTPUT:

    @staticmethod
    def HEADER_FILE(topic,file,date,name):
        f = open(file,"w")
        f.write("-------------------------------------------\n")
        f.write("| Scanned with Mycroft                    |\n")
        f.write("| Link: https://github.com/Lucksi/Mycroft |\n")
        f.write("| Date: {}        |\n".format(date))
        f.write("-------------------------------------------")
        f.write("\n\nExtracting {} from file: {}\n\n".format(topic,name))
        f.close()

    @staticmethod
    def LINE(value,byte,string):
        if value != "None": 
            if "Size: " in string:
                byte.write(string + value + " Bytes\n")
            else:
                byte.write(string + value + "\n")
    
    @staticmethod
    def D_LINE(value,value2,byte,string):
        if value != "None" and value2 != "None": 
           byte.write(string.format(value,value2))