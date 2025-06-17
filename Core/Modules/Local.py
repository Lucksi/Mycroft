# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import time
from time import sleep
from stat import *
import datetime
from Core.Utils import Colors
from Core.Utils import Write_File
import mimetypes

class GET_DATA:
    
    @staticmethod
    def Type(filename):
        filetype = ""
        if filename.endswith('.txt'):
            filetype = "Text File"
        elif filename.endswith(".cmd"):
            filetype = "Windows Command Prompt File"
        elif filename.endswith(".py"):
            filetype = "Python File"
        elif filename.endswith(".js"):
            filetype = "Javascript File"
        elif filename.endswith(".sh"):
            filetype = "Shell-Script/Bash File"
        elif filename.endswith(".ps1"):
            filetype = "Windows Powershell File"
        elif filename.endswith(".cpp"):
            filetype = "C++ File"
        elif filename.endswith(".c"):
            filetype = "C File"
        elif filename.endswith(".c#"):
            filetype = "C# File"
        elif filename.endswith(".bat"):
            filetype = "Windows Batch File"
        elif filename.endswith(".doc") or filename.endswith(".docx"):
            filetype = "Microsoft Word Document"
        elif filename.endswith(".pptx"):
            filetype = "Microsoft PowerPoint Open XML Presentation"
        elif filename.endswith(".xls") or filename.endswith(".xlsx"):
            filetype = "Microsoft Excel Spreadsheet"
        elif filename.endswith(".odt"):
            filetype = "Open Document Text"
        elif filename.endswith(".odp"):
            filetype = "Open Document Presentation"
        elif filename.endswith(".ods"):
            filetype = "Open Document Spreadsheet"
        elif filename.endswith(".pdf"):
            filetype = "Pdf File"
        elif filename.endswith(".iso"):
            filetype = "Disk-Image File"
        elif filename.endswith(".jpg"):
            filetype = "Image/Jpg File (JPG)"
        elif filename.endswith(".jpeg"):
            filetype = "Image/Jpeg File (JPEG)"
        elif filename.endswith(".png"):
            filetype = "Image/Png File (PNG)"
        elif filename.endswith(".psd"):
            filetype = "Photoshop Image"
        elif filename.endswith(".gif"):
            filetype = "Graphics Interchange Format Image"
        elif filename.endswith(".exe"):
            filetype = "Windows Executable File"
        elif filename.endswith(".elf"):
            filetype = "Linux Executable and Linkable File"
        elif filename.endswith(".dll"):
            filetype = "Dynamic-Link Library"
        elif filename.endswith(".so"):
            filetype = "Shared Library"
        elif filename.endswith(".a"):
            filetype = "Static Library"
        elif filename.endswith(".zip"):
            filetype = "Zip Archive"
        elif filename.endswith(".a"):
            filetype = "Rar Archive"
        elif filename.endswith(".jar"):
            filetype = "Java Archive"
        elif filename.endswith(".apk"):
            filetype = "Android Package"
        elif filename.endswith(".gz"):
            filetype = "GNU Zip Archive"
        elif filename.endswith(".tar"):
            filetype = "Tape File Archive"
        elif filename.endswith(".rtf"):
            filetype = "Rich Text Format File"
        elif filename.endswith(".php"):
            filetype = "Php File"
        elif filename.endswith(".uue"):
            filetype = "Uuencoded File"
        elif filename.endswith(".ace"):
            filetype = "A Compact ENDF Archive"
        elif filename.endswith(".7z"):
            filetype = "7Zip Archive"
        elif filename.endswith(".z"):
            filetype = "Unix Compressed File"
        elif filename.endswith(".img"):
            filetype = "Raw Image File"
        elif filename.endswith(".ppam"):
            filetype = "PowerPoint Macro-Enabled Add-Ins"
        elif filename.endswith(".vbs"):
            filetype = "Visual Basic Script"
        return filetype
    
    @staticmethod
    def CountLines(filename):
        linec = 0
        wordsc = 0
        charact = 0
        if filename.endswith('.txt') or filename.endswith(".cmd") or filename.endswith(".py") or filename.endswith(".sh") or filename.endswith(".json") or filename.endswith(".sh"): #or filename.endswith(".docx") or filename.endswith(".doc"):
            try:
                f = open(filename,"r")
            except Exception:
                f = open(filename,"rb")
        else:
            f = open(filename,"rb")
        try:
            for line in f:
                try:
                    linec = linec + 1
                except Exception:
                    linec = linec + 1
                if filename.endswith('.txt') or filename.endswith(".cmd") or filename.endswith(".py") or filename.endswith(".sh"): #or filename.endswith(".docx") or filename.endswith(".doc"):
                    try:
                        for words in line:
                            charact = charact + 1
                            if " " in words or "." in words or "," in words or ":" in words or "\n" in words:
                                wordsc = wordsc + 1
                    except Exception:
                        pass
        except Exception:
            pass
        return linec,wordsc,charact
    
    @staticmethod
    def Parameters(name,origfile,vrb,out,output):#,f_name):
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Getting Local Information...")
        sleep(2)
        lines = GET_DATA.CountLines(origfile)[0]
        words = GET_DATA.CountLines(origfile)[1]
        chars = GET_DATA.CountLines(origfile)[2]
        size = os.path.getsize(origfile)
        if name.endswith(".tar.xz"):
            extension = "tar.xz"
        elif name.endswith(".tar.gz"):
            extension = "tar.gz"
        elif name.endswith(".tar.bz2"):
            extension = "tar.bz2"
        else:
            extension = os.path.splitext(origfile)[1].replace(".","")
        modify = os.path.getmtime(origfile)
        creation = os.path.getctime(origfile)
        modify1 = time.ctime(modify)
        modify2 = datetime.datetime.strptime(modify1,'%a %b %d %H:%M:%S %Y')
        creation1 = time.ctime(creation)
        creation2 = datetime.datetime.strptime(creation1,'%a %b %d %H:%M:%S %Y')
        stats = os.stat(origfile)
        last_access1 = time.ctime(stats.st_atime)
        user_id = stats.st_uid
        last_access2 = datetime.datetime.strptime(last_access1,'%a %b %d %H:%M:%S %Y')
        permissions = ""
        mime_type, encode = mimetypes.guess_type(origfile)
        info = [extension,str(mime_type),str(size)]
        if os.access(origfile, os.R_OK):
            permissions =  permissions + "r"
        else:
            pass
            
        if os.access(origfile, os.W_OK):
            if "r" in permissions:
                permissions =  permissions + "-w"
            else:
                permissions =  permissions + "w"

        else:
            pass
            
        if os.access(origfile, os.X_OK):
            if "r" in permissions or "w":
                permissions =  permissions + "-x"
            else:
                permissions =  permissions + "x"
        else:
            pass
        filetype = GET_DATA.Type(origfile)
        if out == 1:
            f = open(output,"a")
            f.write("-----------------------------------------------------------------------------------------------------------------------------------------------------")
            f.write("\nLocal file details:\n\n")
            Write_File.OUTPUT.LINE(name,f,"File-Name: ")
            Write_File.OUTPUT.LINE(origfile,f,"File-Location: ")
            Write_File.OUTPUT.LINE(str(size),f,"File-Size: ")
            if filetype != "":
                Write_File.OUTPUT.LINE(filetype,f,"File-Type: ")
            Write_File.OUTPUT.LINE(extension,f,"Extension: ")
            Write_File.OUTPUT.LINE(str(user_id),f,"Owner-Id: ")
            Write_File.OUTPUT.LINE(str(mime_type),f,"Mime-Type: ")
            Write_File.OUTPUT.LINE(permissions,f,"User-Permissions: ")
            Write_File.OUTPUT.LINE(creation2.strftime('%Y/%m/%d %H:%M:%S'),f,"Creation: ")
            Write_File.OUTPUT.LINE(modify2.strftime('%Y/%m/%d %H:%M:%S'),f,"Modified: ")
            Write_File.OUTPUT.LINE(last_access2.strftime('%Y/%m/%d %H:%M:%S'),f,"Last-Access: ")
            Write_File.OUTPUT.LINE(str(lines),f,"Lines: ")
            if chars > 0 and words > 0:
                Write_File.OUTPUT.LINE(str(chars),f,"Characters: ")
                Write_File.OUTPUT.LINE(str(words),f,"Words: ")
            f.write("-----------------------------------------------------------------------------------------------------------------------------------------------------")
            f.close()
        if vrb == 1:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Name: {}".format(Colors.Color.GREEN + name))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Location: {}".format(Colors.Color.GREEN + origfile))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Size: {} Bytes".format(Colors.Color.GREEN + str(size)))
            if filetype != "":
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Type: {}".format(Colors.Color.GREEN + filetype))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Extension: {}".format(Colors.Color.GREEN + extension))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Owner-Id: {}".format(Colors.Color.GREEN + str(user_id)))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Mime-Type: {}".format(Colors.Color.GREEN + str(mime_type)))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "User-Permissions: {}".format(Colors.Color.GREEN + permissions))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Creation: {}".format(Colors.Color.GREEN + creation2.strftime('%Y/%m/%d %H:%M:%S')))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Modified: {}".format(Colors.Color.GREEN + modify2.strftime('%Y/%m/%d %H:%M:%S')))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Last-Opened: {}".format(Colors.Color.GREEN + last_access2.strftime('%Y/%m/%d %H:%M:%S')))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Lines: {}".format(Colors.Color.GREEN + str(lines)))
            if chars > 0 and words > 0:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Characters: {}".format(Colors.Color.GREEN + str(chars)))
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Words: {}".format(Colors.Color.GREEN + str(words)))
        else:
            print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")
        return extension, info