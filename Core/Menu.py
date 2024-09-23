# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Main import Start
from Core.Utils import Banner
from Core.Modules import List

class MAIN:

    @staticmethod
    def Options():
        print(Colors.Color.ORANGE + "-------------------------------------------------------------------------------------")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--internal:" + Colors.Color.WHITE + " Scan files from 'Files' internal folder ex: " + Colors.Color.GREEN + "'test.docx --internal'" + Colors.Color.ORANGE + "     |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--output:" + Colors.Color.WHITE + " Insert path to a custom output folder ex: " + Colors.Color.GREEN + "'--output /home/test/Desktop'"  + Colors.Color.ORANGE + "  |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--ext_d:" + Colors.Color.WHITE + " List Files of an external directory ex: " + Colors.Color.GREEN + "'list --ext_d /home/test/Desktop'" + Colors.Color.ORANGE + " |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--folder_name:" + Colors.Color.WHITE + " Change the name of the output directory ex: " + Colors.Color.GREEN + "'--folder_name Test'" + Colors.Color.ORANGE + "    |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--advanced:" + Colors.Color.WHITE + " Extract advanced information from metadata ex: " + Colors.Color.GREEN +"'test.docx --advanced'" + Colors.Color.ORANGE + "  |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--verbose:" + Colors.Color.WHITE + " Disable screen output ex: "+ Colors.Color.GREEN + "'test.docx --verbose'"  + Colors.Color.ORANGE + "                         | ")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--noOutput:" + Colors.Color.WHITE + " Disable file output ex: " + Colors.Color.GREEN + "'test.docx --noOutput'" + Colors.Color.ORANGE + "                         |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--extraction:" + Colors.Color.WHITE + " Extract media from documents ex: " + Colors.Color.GREEN + "'test.docx --extraction'" + Colors.Color.ORANGE + "            |")
        print(Colors.Color.ORANGE + "-------------------------------------------------------------------------------------")
    
    @staticmethod
    def Static():
        Banner.GET_BANNER.Banner(1)
        while True:
            string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert file name\n\n" + Colors.Color.ORANGE + "[Mycroft]" + Colors.Color.WHITE + "-->"))
            while string == "" or string == " ":
                string = str(input(Colors.Color.WHITE + "\nInsert file name\n\n" + Colors.Color.ORANGE + "[Mycroft]" + Colors.Color.WHITE + "-->"))
            if string == "clear" or string == "Clear":
                Banner.GET_BANNER.Banner(1)
            elif "list" in string or "List" in string:
                if " --ext_d" in string or "--ext_d" in string:
                    string = string.replace(" --ext_d","--ext_d")
                    list_folder = string.split("--ext_d",1)[1].split(" ",1)[1].lstrip()
                    string = string.replace(" --ext_d","--ext_d").replace("--ext_d","")
                else:
                    list_folder = ""
                List.GET.Files(list_folder)
            elif string == "help" or string == "Help":
                MAIN.Options()
            elif string == "exit" or string == "Exit":
                print(Colors.Color.WHITE + "\nQuitting the programm\n")
                break
            else:
                if " --verbose" in string or "--verbose" in string:
                    string = string.replace(" --verbose","--verbose").replace("--verbose","")
                    vrb = 0
                else:
                    vrb = 1
                if " --advanced" in string or "--advanced" in string:
                    string = string.replace(" --advanced","--advanced").replace("--advanced","")
                    adv = 1
                else:
                    adv = 0
                if " --extraction" in string or "--extraction" in string:
                    string = string.replace(" --extraction","--extraction").replace("--extraction","")
                    extr = 1
                else:
                    extr = 0
                if " --noOutput" in string or "--noOutput" in string:
                    string = string.replace(" --noOutput","--noOutput").replace("--noOutput","")
                    out = 0
                else:
                    out = 1
                if " --output" in string or "--output" in string:
                    string = string.replace(" --output","--output")
                    folder = string.split("--output",1)[1].split(" ",1)[1].split(" ",1)[0]
                    string = string.replace(" --output","--output").replace("--output","")
                    string = string.replace(" {}".format(folder),"")
                else:
                    folder = ""
                if " --folder_name" in string or "--folder_name" in string:
                    string = string.replace(" --folder_name","--folder_name")
                    folder_n = string.split("--folder_name",1)[1].split(" ",1)[1].split(" ",1)[0]
                    string = string.replace(" --folder_name","--folder_name").replace("--folder_name","")
                    string = string.replace("{}".format(folder_n),"")
                else:
                    folder_n = ""
                if " --internal" in string or "--internal" in string:
                    string = string.replace(" --internal","--internal").replace("--internal","")
                    int_f = 1
                else:
                    int_f = 0
                Start.MAIN.GET_DATA(string.lstrip().rstrip(),adv,vrb,out,extr,folder,int_f,folder_n)