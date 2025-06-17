# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0


class GET:

    class MSUITE:

        @staticmethod
        def MACROS(file_list,extension,m_format):
            try:
                macro = "False"
                ole = "False"
                if extension == "docm" or extension == "docx" or extension == "doc":
                    fold = "word/_rels"
                    fold2 = "word/"
                elif extension =="xlsm" or extension == "xlsx" or extension == "xls":
                    fold = "xls/_rels"
                    fold2 = "xls"
                elif extension =="pptm" or extension == "pptx" or extension == "ppt" or extension == "ppam":
                    fold = "ppt/_rels"
                    fold2 = "ppt"
                if m_format == "True":
                    list = file_list.namelist()
                    check = fold + "/VBA"
                    check2 = fold + "/vba"
                    check3 = check2.capitalize()
                    check4 = fold2 + "/VBA"
                    check5 = fold2 + "/vba"
                    check6 = check5.capitalize()
                    macro = "False"
                    for element in list:
                        if check in element or check2 in element or check3 in element or check4 in element or check5 in element or check6 in element:
                            macro = "True"
                        if "vba" in element and element.endswith(".bin"):
                            macro = "True" 
                        if "ole" in element and element.endswith(".bin"):# and ".xml" not in element:
                            ole = "True"
                list = [macro,ole]
            except Exception:
                list = ["None","None"]
            return list

        @staticmethod
        def SEC_LEVEL(security):
            sec = "None"
            if security != "None":
                if security == "0":
                    sec = "Undefined"
                elif security == "1":
                    sec = "Password-Protected"
                elif security == "2":
                    sec = "Recommended to view it read only"
                elif security == "4":
                    sec = "Enforced to view it read only"
                elif security == "8":
                    sec = "Locked for annotation"
                else:
                    sec = "Unknown"
            return sec
        
        @staticmethod
        def TIME(t_time):
            if t_time != "None":
                t_time2 = int(t_time)/60
                if t_time2 < 1:
                    t_time = t_time + " Minutes"
                elif t_time2 < 24:
                    t_time = str(t_time2) + " Hours"
                else:
                    t_time2 = round(t_time2 / 23.878,2)
                    t_time = str(t_time2) + " Days"
            return t_time
