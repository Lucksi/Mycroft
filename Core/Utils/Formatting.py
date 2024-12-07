# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class TEXT:
    
    @staticmethod
    def FORMATTED(string):
        string = string.replace(">>","").replace("\n","").replace("(","").replace(")","").replace(">","").replace("<","").replace('"',"").replace("/","").lstrip().rstrip()
        return string
    
    @staticmethod
    def FORMATTED_URL(string):
        string = string.replace(">>","").replace("\n","").replace("(","").replace(")","").replace(">","").replace("<","").replace('"',"").lstrip().rstrip()
        return string
    
    @staticmethod
    def FORMATTED_EV(string):
        string = string.replace(">>","").replace("\n","").replace("(","").replace(")","").replace(">","").replace("<","").replace('"',"").lstrip().rstrip()
        return string
    
    @staticmethod
    def FORMATTED_ZIP(string):
        string = string.replace(", ","/",3).replace(", ",":",2).replace("(","").replace(")","").lstrip().rstrip()
        return string