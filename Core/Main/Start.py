# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import shutil
import datetime
import zipfile
from Core.Modules import Local
from Core.Modules import Metadata
from Core.Modules import Hashes
from Core.Utils import Database
from Core.Modules import Checksum
from Core.Utils import Write_File
from Core.Utils import Colors


class MAIN:

    @staticmethod
    def GET_DATA(name,adv,vrb,out,extr,folder,inp_folder,f_name,txt_ext,term,comm,link_ext):
        extension = name.split(".",1)[1]
        if f_name == "":
            f_name = name
            n = 0
        else:
            f_name = f_name.rstrip()
            n = 1
        if inp_folder == 0:
            filename = name
            c = name.count("/")
            if n == 0:
                f_name = f_name.replace("/","_",c-1).split("/",1)[1]
                origfilename = filename.replace("/","_",c-1).split("/",1)[1]
            else:
                f_name = f_name
                origfilename = name
        else:
            filename = "Files/{}".format(name)
            origfilename = name
        extension = extension.replace(" ","")
        if folder == "":
            outfolder = "Output/{}".format(f_name.replace(" ","_"))
            outfolder2 = str(os.getcwd()) + "/Output/{}".format(f_name.replace(" ","_"))
        else:
            outfolder = folder + "/{}".format(f_name.replace(" ","_")).rstrip()
            outfolder2 = outfolder
        if os.path.isfile(filename):
            if os.path.isdir(outfolder):
                shutil.rmtree(outfolder)
            os.mkdir(outfolder)
            output = outfolder + "/{}.txt".format("Local_data")
            date = datetime.datetime.now()
            if out == 1:
                Write_File.OUTPUT.HEADER_FILE("Information",output,date,name)
            if os.path.exists(filename):
                parms = Local.GET_DATA.Parameters(origfilename,filename,vrb,out,output)[1]
                extension = parms[0]
                extension = extension.replace(" ","")
                hashes = Hashes.GET_HASHES.Converter(filename,vrb,out,output)[3]
                md5 =  hashes[0]
                sha1 = hashes[1]
                sha256 = hashes[2]
                sha384 = hashes[3]
                sha512 = hashes[4]
                Checksum.GET.CHECKSUM(filename,vrb,out,output)
                Database.DATABASE.EXIST(md5,sha1,sha256,sha384,sha512,date,parms[2],origfilename,parms[1],extension)
                output = outfolder + "/{}.txt".format("Metadata")
                if out == 1:
                   Write_File.OUTPUT.HEADER_FILE("Metadata",output,date,name)
                Metadata.DOCUMENTS.File(extension,filename,origfilename,adv,vrb,out,output,extr,txt_ext,term,comm,date,name,link_ext)
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Output Saved on: {}".format(Colors.Color.GREEN + outfolder2))
            else:
                print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "File not Found")
        else:
            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Not a File" + str(filename))
