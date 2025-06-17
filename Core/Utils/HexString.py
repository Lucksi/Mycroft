# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import codecs

class GET:

    staticmethod
    def CHECK(string):
        is_hex = False
        try:
            int(string,16)
            is_hex = True
        except Exception as e:
            is_hex = False
        return is_hex

    @staticmethod
    def STRING(string):
        string = string.replace(">>","").replace("\n","").replace("(","").replace(")","").replace(">","").replace("<","").replace('"',"").replace("/","").replace("þÿ","").rstrip().lstrip()
        type = GET.CHECK(string)
        if type == True:
            try:
                c_string = codecs.decode(string,"hex").decode("latin-1").replace("þÿ","")
            except Exception as e:
                c_string = string
        else:
            c_string = string
        return c_string