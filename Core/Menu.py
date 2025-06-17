# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Main import Start
from Core.Utils import Banner
from Core.Utils import Database
from Core.Modules import List

class MAIN:

    @staticmethod
    def Options():
        print(Colors.Color.ORANGE + "----------------------------------------------------------------------------------------------------------------------------")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--internal:" + Colors.Color.WHITE + " Scan files from 'Files' internal folder ex: " + Colors.Color.GREEN + "'test.docx --internal'" + Colors.Color.ORANGE + "                                            |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--output:" + Colors.Color.WHITE + " Insert path to a custom output folder ex: " + Colors.Color.GREEN + "'--output /home/test/Desktop'"  + Colors.Color.ORANGE + "                                         |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--ext_d:" + Colors.Color.WHITE + " List Files of an external directory ex: " + Colors.Color.GREEN + "'list --ext_d /home/test/Desktop'" + Colors.Color.ORANGE + "                                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--folder_name:" + Colors.Color.WHITE + " Change the name of the output directory ex: " + Colors.Color.GREEN + "'--folder_name Test'" + Colors.Color.ORANGE + "                                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--advanced:" + Colors.Color.WHITE + " Extract advanced information (ex: media,comments) ex: " + Colors.Color.GREEN +"'test.docx --advanced'" + Colors.Color.ORANGE + "                                  |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--comments:" + Colors.Color.WHITE + " Save and print File Comments ex: " + Colors.Color.GREEN +"'test.docx --comments'" + Colors.Color.ORANGE + "                                                       |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--text:" + Colors.Color.WHITE + " Extract file text-content from document ex: " + Colors.Color.GREEN +"'test.docx --text'" + Colors.Color.ORANGE + "                                                    |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--urls:" + Colors.Color.WHITE + " Extract urls from document ex: " + Colors.Color.GREEN +"'test.docx --urls'" + Colors.Color.ORANGE + "                                                                 |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--search:" + Colors.Color.WHITE + " Search for a specific keyword in the document ex: "+ Colors.Color.GREEN + "'test.docx --text --search test'"  + Colors.Color.ORANGE + "                              |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--db_search:" + Colors.Color.WHITE + " Search for a specific file in the database by (id,md5,sha1,sha256,sha512 or name) ex: "+ Colors.Color.GREEN + "'--db_search test.txt'"  + Colors.Color.ORANGE + " |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--adv_db_search:" + Colors.Color.WHITE + " Create Custom search Query's ex: "+ Colors.Color.GREEN + '--adv_db_search name="test" AND extension = "txt"'  + Colors.Color.ORANGE + "                       |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--noVerbose:" + Colors.Color.WHITE + " Disable screen output ex: "+ Colors.Color.GREEN + "'test.docx --noVerbose'"  + Colors.Color.ORANGE + "                                                            |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--noOutput:" + Colors.Color.WHITE + " Disable file output ex: " + Colors.Color.GREEN + "'test.docx --noOutput'" + Colors.Color.ORANGE + "                                                                |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--media:" + Colors.Color.WHITE + " Extract media from documents ex: " + Colors.Color.GREEN +"'test.docx --advanced --media'" + Colors.Color.ORANGE + "                                                             |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + "--extraction:" + Colors.Color.WHITE + " Extract files from archives ex: " + Colors.Color.GREEN +"'test.zip --extraction'" + Colors.Color.ORANGE + "                                                     |")
        print(Colors.Color.ORANGE + "----------------------------------------------------------------------------------------------------------------------------")

    
    @staticmethod
    def Supported():
        print(Colors.Color.ORANGE + "---------------------------------------------------------------------------------------------")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " All Files:" + Colors.Color.WHITE + " Get local file information, hashes, checksums" + Colors.Color.ORANGE + "                                  |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Pdf:" + Colors.Color.WHITE + "  Extract metadata,file events,encryption algorithm and malicious keywords check" + Colors.Color.ORANGE + "      |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Docx:" + Colors.Color.WHITE + " Extract metadata,media,comments,text and search for keywords" + Colors.Color.ORANGE + "                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Pptx:" + Colors.Color.WHITE + " Extract metadata,media,comments,text and search for keywords "+ Colors.Color.ORANGE + "                       |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Odt:" + Colors.Color.WHITE + "  Extract metadata,media,comments,text and search for keywords" + Colors.Color.ORANGE + "                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Odp:" + Colors.Color.WHITE + "  Extract metadata,media,comments,text and search for keywords" + Colors.Color.ORANGE + "                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Xlsx:" + Colors.Color.WHITE + " Extract metadata,media,comments,text and search for keywords" + Colors.Color.ORANGE + "                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Ods:" + Colors.Color.WHITE + "  Extract metadata,media,comments,text and search for keywords" + Colors.Color.ORANGE + "                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Bmp:" + Colors.Color.WHITE + "  Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Jpg:" + Colors.Color.WHITE + "  Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Jpeg:" + Colors.Color.WHITE + " Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Jps:" + Colors.Color.WHITE + "  Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Gif:" + Colors.Color.WHITE + "  Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Png:" + Colors.Color.WHITE + "  Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Psd:" + Colors.Color.WHITE + "  Extract metadata,file events,get image details and pixel " + Colors.Color.ORANGE + "                           |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Zip:" + Colors.Color.WHITE + "  Extract metadata and files "+ Colors.Color.ORANGE + "                                                         | ")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Apk:" + Colors.Color.WHITE + "  Extract metadata and files "+ Colors.Color.ORANGE + "                                                         | ")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Jar:" + Colors.Color.WHITE + "  Extract metadata and files "+ Colors.Color.ORANGE + "                                                         | ")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Tar.xz:" + Colors.Color.WHITE + "  Extract metadata and files "+ Colors.Color.ORANGE + "                                                      | ")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Tar.gz:" + Colors.Color.WHITE + "  Extract metadata and files "+ Colors.Color.ORANGE + "                                                      | ")
        print(Colors.Color.ORANGE + "|" + Colors.Color.GREEN + " Tar.bz2:" + Colors.Color.WHITE + " Extract metadata and files "+ Colors.Color.ORANGE + "                                                      | ")
        print(Colors.Color.ORANGE + "---------------------------------------------------------------------------------------------")
    
    @staticmethod
    def Static():
        Banner.GET_BANNER.Banner(1)
        while True:
            string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert file name\n\n" + Colors.Color.ORANGE + "[Mycroft]" + Colors.Color.WHITE + "-->"))
            while string == "" or string == " ":
                string = str(input(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "\nInsert file name\n\n" + Colors.Color.ORANGE + "[Mycroft]" + Colors.Color.WHITE + "-->"))
            if string == "clear" or string == "Clear":
                Banner.GET_BANNER.Banner(1)
            elif "--db_search" in string or " --db_search" in string:
                string = string.replace("--db_search"," --db_search")
                param = string.split("--db_search",1)[1].split(" ",1)[1].lstrip()
                string = string.replace(" --db_search","--db_search").replace("--db_search","")
                Database.DATABASE.SEARCH(param,0)
            elif "--adv_db_search" in string or " --adv_db_search" in string:
                string = string.replace("--adv_db_search"," --adv_db_search")
                param = string.split("--adv_db_search",1)[1].split(" ",1)[1].lstrip()
                string = string.replace(" --adv_db_search","--adv_db_search").replace("--adv_db_search","")
                Database.DATABASE.ADV_SEARCH(param,1)
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
            elif string == "reset" or string == "Reset":
                Database.DATABASE.RESET()
            elif string == "supported" or string == "Supported":
                MAIN.Supported()
            elif string == "exit" or string == "Exit":
                print(Colors.Color.WHITE + "\nQuitting the programm\n")
                break
            else:
                if " --noVerbose" in string or "--noVerbose" in string:
                    string = string.replace(" --noVerbose","--noVerbose").replace("--noVerbose","")
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
                if " --media" in string or "--media" in string:
                    string = string.replace(" --media","--media").replace("--media","")
                    extr = 1
                else:
                    extr = 0
                if " --comments" in string or "--comments" in string:
                    string = string.replace(" --comments","--comments").replace("--comments","")
                    comm = 1
                else:
                    comm = 0
                if " --text" in string or "--text" in string:
                    string = string.replace(" --text","--text").replace("--text","")
                    txt_ext = 1
                else:
                    txt_ext = 0
                if " --urls" in string or "--urls" in string:
                    string = string.replace(" --urls","--urls").replace("--urls","")
                    link_ext = 1
                else:
                    link_ext = 0
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
                if " --search" in string or "--search" in string:
                    string = string.replace(" --search","--search")
                    term = string.split("--search",1)[1].split(" ",1)[1] + "separator_char".split("separator_char",1)[0]
                    terms = term.split(",")
                    string = string.replace(" --search","--search").replace("--search","")
                    string = string.rsplit("{}".format(term),1)[0]
                else:
                    terms = []
                try:
                    Start.MAIN.GET_DATA(string.lstrip().rstrip(),adv,vrb,out,extr,folder,int_f,folder_n,txt_ext,terms,comm,link_ext)
                except Exception as e:
                    print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "An Error occurred : {}".format(str(e)))
