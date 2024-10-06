# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from time import sleep
import xml.dom.minidom
import xml.etree.ElementTree

class GET:

    @staticmethod
    def DOC_TEXT(index,output):
        f = open(output,"a")
        s_string = 0
        for element in index:
            try:
                content = element.childNodes[0].data
                f.write(str(content))
                s_string = s_string + 1
            except Exception as e:
               pass
        if s_string > 0:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        f.close()

    @staticmethod
    def ODT_TEXT(index,output):
        f = open(output,"a")
        s_string = 0
        for element in index:
            try:
                content = element.childNodes[0].data
                f.write(str(content))
                s_string = s_string + 1
            except Exception as e:
                pass
        if s_string > 0:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        f.close()
    
    @staticmethod
    def PPTX_TEXT(index,output):
        list = index.namelist()
        f = open(output,"w")
        f.write("Getting-Slides")
        for element in list:
            if "ppt/slides/slide" in element:
                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Slide found: {}".format(Colors.Color.GREEN + element.replace("ppt/slides/","")))
                sleep(3)
                f = open(output,"a")
                f.write("\n\n" + element.replace("ppt/slides/","") + "\n")
                document4 = xml.dom.minidom.parseString(index.read(element))
                string = document4.getElementsByTagName("a:t")
                try:
                    for text in string:
                        content = text.childNodes[0].data
                        f.write(str(content))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Content Stored Successfully")
                except Exception as e:
                        print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "Something Went Wrong: " + Colors.Color.GREEN + str(e) + "\n")
            else:
                pass
        f.close()