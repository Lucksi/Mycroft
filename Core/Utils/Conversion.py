# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class GET:

    class IMAGE:

        @staticmethod
        def DISTANCE(string):
            m = 0
            m2 = "None"
            n1 = string.rsplit("/",1)[0]
            n2 = string.rsplit("/",1)[1]
            n1 = int(n1.replace('"',""))
            n2 = int(n2.replace('"',""))
            if n1 == 4294967295:
                m2 = "Infinity"
            else:
                m = n1/n2
            if m == 0:
                pass
            else:
                m2 = str(m) + " Meters"
            return m2
        
        @staticmethod
        def SEA_LEVEL(string):
            if string == "0":
                level = "0 (Above Sea-Level)"
            elif string == "1":
                level = "1 (Below Sea-Level)"
            else:
                level = "None"
            return level