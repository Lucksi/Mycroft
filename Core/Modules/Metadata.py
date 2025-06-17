# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Formatting
from Core.Utils import Write_File
from Core.Utils import Printer
from Core.Utils import HexString
from Core.Modules.Images import Properties as Prop_I
from Core.Modules import Reader as Decoder
from Core.Modules.Images import Data
from Core.Modules.Media import Extraction
from Core.Modules.Archives import Properties
from Core.Modules.Documents import Content
from Core.Modules.Documents import Metadata as doc_meta
from Core.Modules.Images import Metadata as Im_meta
from Core.Modules import Finder
from time import sleep
import zipfile
import xml.dom.minidom
import xml.etree.ElementTree
import os
import re

class DOCUMENTS:

    @staticmethod
    def File(extension,origfile,name,adv,vrb,out,output,extr,txt_ext,term,comm,date,f_path_name,link_ext):
        accepted =["docx","pptx","odt","odp","ods","xlsx","odg","dotx","potx","docm","xlsm","pptm"]
        if extension == "pdf":
            annotation = []
            link = []
            heights = []
            widths = []
            events = []
            times = []
            instances = []
            agents = []
            parms = []
            changes = []
            images = []
            device = []
            type = []
            height2 = []
            width2 = []
            suspect_keys = []
            permissions = []
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Pdf Metadata")
            reader = open(origfile,"rb")
            max2 = reader.read()
            reader.close()
            if b"adobe:ns:meta/" in max2:
                adobe = "True"
            else:
                adobe = "False"
            if b"photoshop" in max2:
                photoshop = "True"
            else:
                photoshop = "False"
            if b"xmlns:tiff" in max2:
                image = "True"
            else:
                image = "False"
            data = doc_meta.GET.PDF.METADATA(origfile,adobe,photoshop,image,annotation,link,heights,widths,events,times,instances,agents,parms,changes,images,device,height2,width2,suspect_keys,permissions,type)#[0]
            if vrb == 1:
                Printer.GENERATE.Sentence(name,"None","File-Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(HexString.GET.STRING(data[3]),"None","Title: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[0],"None","Pdf-Version: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[15],"None","Encrypted: ",out,output,1,"",vrb)
                if data[15] != "False":
                    Printer.GENERATE.Sentence(data[17],"None","Encryption: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[16],"None","Password-Protected: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[18],"None","Toolkit: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[21],"None","Linearized: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[8],"None","Creator-Tool: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[12],"None","Metadata-Date: ",out,output,1,"",vrb)
                if data[15] == "False":
                    Printer.GENERATE.Sentence(HexString.GET.STRING(data[1]),"None","Pdf-Creator: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(HexString.GET.STRING(data[22]),"None","PDF-Producer: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(HexString.GET.STRING(data[4]),"None","Pdf-Creation-Date: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(HexString.GET.STRING(data[5]),"None","Pdf-Modification-Date: ",out,output,1,"",vrb)
                else:
                    Printer.GENERATE.Sentence(data[1],"None","Pdf-Creator: ",out,output,1,"",vrb)
                if len(permissions):
                    Printer.GENERATE.Sentence(str(permissions).replace("[","").replace("]",""),"None","Permissions: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[9],"None","Document-Id: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[10],"None","Instance-Id: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[11],"None","Layout: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[14],"None","Keywords: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[6],"None","Pages: ",out,output,1,"",vrb)
                if data[15] == "False":
                    Printer.GENERATE.Sentence(HexString.GET.STRING(data[2]),"None","Language: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(HexString.GET.STRING(data[7]),"None","Author: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[19],"None","Company: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[20],"None","Source-Modified: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(data[13],"None","Document-Checksum: ",out,output,1,"",vrb)
                if adv == 1:
                    if len(link):
                        i = 1
                        for links in link:
                            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Uri'n°{}: ".format(i) + Colors.Color.GREEN + Formatting.TEXT.FORMATTED_URL(links))
                            i = i + 1
                    if len(annotation):
                        i = 1
                        for annots in annotation:
                            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Annotation'n°{}: ".format(i) + Colors.Color.GREEN + Formatting.TEXT.FORMATTED(annots))
                            i = i +1
                    if len(heights) and len(widths):
                        i = 1
                        v = 0
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing Image Objects")
                        for height in heights:
                            if "s" in widths[v]:
                                pass
                            else:
                                try:
                                    megapixel = Prop_I.GET.COMMON.Megapixel(int(Formatting.TEXT.FORMATTED(widths[v])),int(Formatting.TEXT.FORMATTED(height)))
                                    p_ratio = Prop_I.GET.COMMON.Pixel_ratio(int(Formatting.TEXT.FORMATTED(widths[v])),int(Formatting.TEXT.FORMATTED(height)))
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Image n°{}: Width: {} Height: {} Megapixel: {} Pixel-Ratio: {}".format(i,Colors.Color.GREEN + Formatting.TEXT.FORMATTED(widths[v]) + Colors.Color.WHITE,Colors.Color.GREEN + Formatting.TEXT.FORMATTED(height) + Colors.Color.WHITE,Colors.Color.GREEN + str(megapixel) + Colors.Color.WHITE,Colors.Color.GREEN + str(p_ratio)))
                                except Exception:
                                    pass
                            i = i +1
                            v = v +1
                    if len(times):
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing file Events")
                        i = 1
                        v = 0
                        p = 0
                        for date in times:
                            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Event'n°{}".format(i))
                            if len(events):
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Action: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(events[v])))
                                    ev = events[v].lstrip().replace('"',"").replace("\n","")
                                except Exception as e:
                                    pass
                            if ev == 'converted' or ev == 'derived':
                                if len(parms):
                                    try:
                                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Parameter: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED_EV(parms[p])))
                                        p = p + 1
                                    except Exception as e:
                                        pass
                            else:
                                if len(times):
                                    try:
                                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Date: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(date)))
                                    except Exception as e:
                                        pass
                                if len(instances):
                                    try:
                                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Instance-Id: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(instances[v])))
                                    except Exception as e:
                                        pass
                                if len(agents):
                                    try:
                                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Software: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(agents[v])))
                                    except Exception as e:
                                        pass
                                if len(changes):
                                    try:
                                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Changes: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED_EV(changes[v])))
                                    except Exception as e:
                                        pass
                            i = i + 1
                            v = v + 1
                    if len(images):
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing file Images")
                        i = 1
                        v = 0
                        for image in images:
                            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Image n°{}".format(i))
                            if len(height2) and len(width2):
                                megapixel = Prop_I.GET.COMMON.Megapixel(int(Formatting.TEXT.FORMATTED(width2[v])),int(Formatting.TEXT.FORMATTED(height2[v])))
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Image-Size: {}x{}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(height2[v]) + Colors.Color.WHITE,Colors.Color.GREEN + Formatting.TEXT.FORMATTED(width2[v])))
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Megapixel: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(str(megapixel))))
                                except Exception as e:
                                    pass
                            if len(images):
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Model: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(image)))
                                except Exception as e:
                                    pass
                            if len(device):
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Model-Version: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(device[v])))
                                except Exception as e:
                                    pass
                            i = i + 1
                            v = v + 1
                    if len(suspect_keys):
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Suspect Keywords Found")
                        descriptions = ["Execute JavaScript code","Execute a specific action at document opening","External file embedded in the document","Embeed flash in a document","Data hidden in Object Stream","Send External Data","URI can sometimes be malicious","Launch an external application or document"]
                        js = 0
                        oa = 0
                        aa = 0
                        ef = 0
                        rme = 0
                        obm = 0
                        gor = 0
                        ur = 0
                        ln = 0
                        for keys in suspect_keys:
                            keys = Formatting.TEXT.FORMATTED(keys).replace(" ","")
                            if keys == "JavaScriptJS":
                                js = js + 1
                            elif keys == "OpenAction":
                                oa = oa + 1
                            elif keys == "AA":
                                aa = aa + 1
                            elif keys == "EmbeddedFile":
                                ef = ef + 1
                            elif keys == "RichMedia":
                                rme = rme + 1
                            elif keys == "ObjectStream":
                                obm = obm + 1
                            elif keys == "SubmitFormGoToR":
                                gor = gor + 1
                            elif keys == "URI":
                                ur = ur + 1
                            elif keys == "Launch":
                                ln = ln + 1
                        if js != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "JavaScript/JS: {} Times Found Description: {}".format(Colors.Color.GREEN + str(js) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[0]))
                        if oa != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "OpenAction: {} Times Found Description: {}".format(Colors.Color.GREEN + str(oa) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[1]))
                        if aa != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "AA: {} Times Found Description: {}".format(Colors.Color.GREEN + str(aa) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[1]))
                        if ef != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "EmbeddedFile: {} Times Found Description: {}".format(Colors.Color.GREEN + str(ef) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[2]))
                        if rme != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "RichMedia: {} Times Found Description: {}".format(Colors.Color.GREEN + str(rme) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[3]))
                        if obm != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "ObjectStream: {} Times Found Description: {}".format(Colors.Color.GREEN + str(obm) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[4]))
                        if gor != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "SubmitForm/GoToR: {} Times Found Description: {}".format(Colors.Color.GREEN + str(gor) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[5]))
                        if ur != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "URI: {} Times Found Description: {}".format(Colors.Color.GREEN + str(ur) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[6]))
                        if ln != 0:
                            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Launch: {} Times Found Description: {}".format(Colors.Color.GREEN + str(ln) + Colors.Color.WHITE,Colors.Color.GREEN + descriptions[7]))
            else:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")

        elif extension in accepted:
            if extension == "docx" or extension == "doc" or extension == "dotx" or extension == "docm":
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Word Document Metadata")
            elif extension == "pptx" or extension == "potx":
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Microsoft Powerpoint Metadata")
            else:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Open Document Metadata")
            images_s = []
            type_images = []
            media_s = []
            type_media = []
            comments = []
            comment_id = []
            created_d = []
            comment_auth_id = []
            num_id = []
            user_t_id = []
            name_l = []
            initials = []
            i = 0
            out3 = output.replace("Metadata.txt","Pictures")
            out2 = output.replace("Metadata.txt","Media")
            os.mkdir(out3)
            os.mkdir(out2)
            d_format = "None"
            try:
                File_m = zipfile.ZipFile(origfile,'r')
            except Exception:
                pass
            try:
                data = doc_meta.GET.OFFICE.METADATA(File_m,extension,"Lib_Office")
                d_format = "Libre_Office"
            except Exception as e:
                try:
                    data = doc_meta.GET.OFFICE.METADATA(File_m,extension,"M_Office")
                    d_format = "Microsoft_Office"
                except Exception as e:
                    print(str(e))

            if comm == 1:
                file_list = File_m.namelist()
                if d_format == "Microsoft_Office":
                    Content.GET.M_OFFICE_COMMENTS(File_m,extension,comments,comment_id,created_d,comment_auth_id,num_id,user_t_id,name_l,initials)
                elif d_format == "Libre_Office": 
                    Content.GET.LIB_OFFICE_COMMENTS(File_m,extension,comments,comment_id,created_d,comment_auth_id,num_id,user_t_id,name_l,initials)
            
            if adv == 1:
                file_list = File_m.namelist()
                if d_format == "Microsoft_Office":
                    Extraction.FILE.MIC_Format(file_list,extension,extr,File_m,out3,images_s,type_images,out2,media_s,type_media)
                else:
                    document2 = xml.etree.ElementTree.fromstring(File_m.read('META-INF/manifest.xml'))
                    Extraction.FILE.LIB_Format(document2,extr,File_m,out3,images_s,type_images,out2,media_s,type_media)
            if vrb == 1:
                try:
                    Printer.GENERATE.Sentence(name,"None","File-Name: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[0],"None","Title: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[1],"None","Description: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(d_format,"None","Document-Format: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[36],"None","Contain-Macros: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[37],"None","Contain-OLEObjects: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[2],"None","Keywords: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[3],"None","Revision: ",out,output,2," Times",vrb)
                    Printer.GENERATE.Sentence(data[4],"None","Revision-Time: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[5],"None","Creator: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[6],"None","Date: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[7],"None","Creation-Date: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[8],"None","Modification-Date: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[9],"None","Last-Modified-By: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[10],"None","Last-Printed: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[11],"None","Language: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[12],"None","Pages: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[13],"None","Paragraphs: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[14],"None","Table-Count: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[15],"None","Image-Count: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[16],"None","Object-Count: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[17],"None","Characters-Count: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[18],"None","Non-Whitespace-Character-Count: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[19],"None","Characters-With-Space: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[20],"None","Template: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[21],"None","Application: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[22],"None","Total-Time: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[23],"None","Doc-Security: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[24],"None","Lines: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[25],"None","Presentation-Format: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[26],"None","Slides: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[27],"None","Hidden-Slides: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[28],"None","Notes: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[29],"None","MMClips: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[30],"None","Shared: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[31],"None","Company: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[32],"None","Words: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[33],"None","App-Version: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[34],"None","Read-Only: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(data[35],"None","Password-Protected: ",out,output,1,"",vrb)
                except Exception as e:
                    print(str(e))
                if len(comments):
                    output = output.replace("Metadata.txt","Comments.txt")
                    Write_File.OUTPUT.HEADER_FILE("Comments",output,date,f_path_name)
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing Extracted Comments")
                    i = 0
                    for comment in comments:
                        Printer.GENERATE.Comment_Sentence(str(i + 1),"None","Comment n°: ",comm,output,1,"",vrb)
                        Printer.GENERATE.Comment_Sentence(comment,"None","Text: ",comm,output,1,"",vrb)
                        if len(comment_id):
                            Printer.GENERATE.Comment_Sentence(comment_id[i],"None","Comment-Id: ",comm,output,1,"",vrb)
                        if len(created_d):
                            Printer.GENERATE.Comment_Sentence(created_d[i],"None","Creation-Date: ",comm,output,1,"",vrb)
                        if len(comment_auth_id):
                            if extension == "xlsx" or extension == "odt" or extension == "odp" or extension == "ods" :
                                param = comment_auth_id[i] + "\n"
                                Printer.GENERATE.Comment_Sentence(param,"None","Author-id: ",comm,output,1,"",vrb)
                            else:
                                Printer.GENERATE.Comment_Sentence(comment_auth_id[i],"None","Author-id: ",comm,output,1,"",vrb)
                        if extension == "docx" or extension == "odt":
                            if len(initials):
                                param = initials[i] + "\n"
                                Printer.GENERATE.Comment_Sentence(param,"None","Author-Initials: ",comm,output,1,"",vrb)
                        else:
                            if len(num_id):
                                index = 0
                                if comment_auth_id[i] in num_id:
                                    pos = index
                                else:
                                    index = index + 1
                                Printer.GENERATE.Comment_Sentence(name_l[pos],"None","Author-Name: ",comm,output,1,"",vrb)
                                Printer.GENERATE.Comment_Sentence(initials[pos],"None","Author-Initials: ",comm,output,1,"",vrb)
                                param = user_t_id[pos] + "\n"
                                Printer.GENERATE.Comment_Sentence(param,"None","Author-User-id: ",comm,output,1,"",vrb)
                        i = i + 1
                    output = output.replace("Comments.txt","Metadata.txt")
                if len(images_s):
                    if vrb == 1:
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing Extracted images")
                        i = 1
                        v = 0
                        for image in images_s:
                            print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Images n° {}: {} Type: {}".format(i,Colors.Color.GREEN + image + Colors.Color.WHITE,Colors.Color.GREEN + type_images[v]))
                            i = i + 1
                            v = v + 1   
                if len(media_s):
                    if vrb == 1:
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing Extracted Media")
                        i = 1
                        v = 0
                        for media in media_s:
                            print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Media n° {}: {} Type: {}".format(i,Colors.Color.GREEN + media + Colors.Color.WHITE,Colors.Color.GREEN + type_media[v]))
                            i = i + 1
                            v = v + 1
            else:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")
            if txt_ext == 1:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting text from file")
                output = output.replace("Metadata.txt","Content.txt")
                try:
                    if extension == "docx" or extension == "xlsx":
                        if extension == "docx":
                            document4 = xml.dom.minidom.parseString(File_m.read('word/document.xml'))
                            result = document4.getElementsByTagName("w:t")
                        else:
                            document4 = xml.dom.minidom.parseString(File_m.read('xl/sharedStrings.xml'))
                            result = document4.getElementsByTagName("t")
                        sleep(3)
                        Content.GET.DOC_TEXT(result,output)
                    elif extension == "pptx":
                        Content.GET.PPTX_TEXT(File_m,output)
                except Exception:
                    document4 = xml.dom.minidom.parseString(File_m.read('content.xml'))
                    result = document4.getElementsByTagName("text:p")
                    Content.GET.DOC_TEXT(result,output)
                if extension == "odt" or extension == "odp" or extension == "odg" or extension == "ods":
                    document4 = xml.dom.minidom.parseString(File_m.read('content.xml'))
                    result = document4.getElementsByTagName("text:span")
                    Content.GET.ODT_TEXT(result,output)
                if len(term):
                    keys_list = ", ".join(term)
                    if len(term) == 1:
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Searching for keyword [{}]".format(Colors.Color.GREEN + keys_list + Colors.Color.WHITE))
                    else:
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Searching for keywords [{}]".format(Colors.Color.GREEN + keys_list + Colors.Color.WHITE))
                    sleep(3)
                    for key in term:
                        found = Finder.OBJECT.FOUND(output,key)[0]
                        lines = Finder.OBJECT.FOUND(output,key)[1]
                        if found != "Not Found":
                            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Keyword: {} found {} times on line: [ {}".format(Colors.Color.GREEN + key + Colors.Color.WHITE,Colors.Color.GREEN + found + Colors.Color.WHITE,Colors.Color.GREEN + lines.replace("[","").replace("]","") ) + Colors.Color.WHITE + " ]")
                        else:
                           print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Keyword: {} Not found".format(Colors.Color.GREEN + key + Colors.Color.WHITE))
                output = output.replace("Content.txt","Metadata.txt")
            if link_ext == 1:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting links from file")
                output = output.replace("Metadata.txt","Urls.txt")
                try:
                    if extension == "docx" or extension == "pptx" or extension == "xlsx":
                        if d_format == "Microsoft_Office":
                            if extension == "docx":
                                document4 = xml.etree.ElementTree.fromstring(File_m.read('word/_rels/document.xml.rels'))
                                sleep(3)
                                Content.GET.DOC_LINKS(document4,output,vrb)
                            elif extension == "pptx":
                                Content.GET.PPTX_LINKS(File_m,output,vrb)
                            elif extension == "xlsx":
                                Content.GET.XLSX_LINKS(File_m,output,vrb)
                        else:
                            document4 = xml.dom.minidom.parseString(File_m.read('content.xml'))
                            result = document4.getElementsByTagName("text:a")
                            Content.GET.ODT_LINKS(result,output,vrb)
                except Exception:
                    pass
                if extension == "odt" or extension == "odp" or extension == "odg" or extension == "ods":
                    try:
                        document4 = xml.dom.minidom.parseString(File_m.read('content.xml'))
                        result = document4.getElementsByTagName("text:a")
                        Content.GET.ODT_LINKS(result,output,vrb)
                    except Exception as e:
                        print(str(e))
        
        elif extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "psd" or extension == "gif" or extension == "jps" or extension == "bmp":
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Image Metadata")
            reader = open(origfile,"rb")
            geoc = "None"
            instances = []
            events = []
            times = []
            agents = []
            changes = []
            device = []
            images = []
            height2 = []
            width2 = []
            reader = open(origfile,"rb")
            max2 = reader.read()
            reader.close()
            max2 = re.sub(b"[^\x20-\x7E]", b"",max2)
            s_p = []
            if b"adobe:ns:meta/" in max2:
                adobe = "True"
            else:
                adobe = "False"
            if b"GIMP" in max2:
                gimp = "True"
            else:
                gimp = "False"
            if b"Photoshop" in max2:
                photoshop = "True"
            else:
                photoshop = "False"
            reader4 = open(origfile,"rb")
            max4 = reader4.readlines()
            j = 0
            for line in max4:
                if b"8BIM" in line.rstrip():
                    Decoder.EXTRACTOR.GET_Metadata("8BIM","8BIM ",j,max4,1,1,True,s_p,line,3,"")
                    break
                j = j +1
            reader4.close()
            meta = Im_meta.GET_METADATA.EXTRACT(adobe,extension,gimp,origfile,device,images,instances,events,times,agents,changes,height2,width2)
            if extension == "png":
                param =  Data.TYPE.PNG.Get_Parameters(origfile)
                width = param[0]
                height = param[1]
                c_byte = param[4]
                c_type = param[5]
                c_method = param[6]
                f_method = param[7]
                e_method = param[8]
                byte_order = param[2]
                pix = param[9]
            elif extension == "bmp":
                param = Data.TYPE.BMP.Get_Parameters(origfile)
                width = param[0]
                height = param[1]
                planes = param[2]
                b_count = param[3]
                comp = param[4]
                x =  param[5]
                y =  param[6]
                pix = param[7]
                c_number = param[8]
                byte_order = param[9]
                imp_color = param[10]
            elif extension == "gif":
                param = Data.TYPE.GIF.Get_Parameters(origfile)
                width = param[0]
                height = param[1]
                b_color = param[4]
                g_type = param[5]
                a_seq = param[6]
                f_method = param[7]
                e_method = param[8]
                c_pal = param[9]
                c_r_d = param[10]
                byte_order = param[2]
                frame = param[11]
                imp1 = param[12]
                pix = param[13]
                c_number = param[14]
                c_n_bytes = param[15]
                duration = param[16] + " seconds"
                b_pix =  param[17]
            elif extension == "jpg" or extension == "jpeg" or extension == "jps":
                param = Data.TYPE.JPEG.Get_Parameters(origfile)
                width = param[0]
                height = param[1]
                byte_order = param[2]
                c_scheme = param[4]
                b_pix = param[5]
                d_pix = param[6]
                x = param[7]
                y = param[8]
                th_w = param[9]
                th_h = param[10]
                pix = param[11]
                c_comp = param[12]
                h_t = param[13]
                meta_order = param[14]
            if extension != "psd":
                megapixel = Prop_I.GET.COMMON.Megapixel(width,height)
            else:
                megapixel = 0
                byte_order = "None"
            if meta[29] != "None" and meta[30] != "None":
                geoc = meta[29] + "," + meta[30]
            Printer.GENERATE.Sentence(name,"None","File-Name: ",out,output,1,"",vrb)
            if extension != "psd":
                Printer.GENERATE.Sentence(str(width),"None","Width: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(height),"None","Height: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(width) +"x" +str(height),"None","Image-Size: ",out,output,1,"",vrb)
            if megapixel != 0:
                Printer.GENERATE.Sentence(str(megapixel),"None","Megapixel: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(byte_order,"None","Byte-Order: ",out,output,1,"",vrb)
            if len(s_p):
                for element in s_p:
                    if "ÿÛ" in element:
                        try:
                            element2 = element.rsplit("(",1)[1].rsplit("ÿÛ",1)[0].replace("\n","").replace("\r","").strip()
                            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Special Instruction: {}".format(Colors.Color.GREEN + element2))
                        except Exception as e:
                            pass
            if extension == "png":
                Printer.GENERATE.Sentence(pix,"None","Pixel-Ratio: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(c_byte),"None","Bit-Depth: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_type,"None","Color-Type: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_method,"None","Compression: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(f_method,"None","Filter: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(e_method,"None","Interlace: ",out,output,1,"",vrb)
            if extension == "bmp":
                Printer.GENERATE.Sentence(pix,"None","Pixel-Ratio: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(b_count),"None","Bit-Depth: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_number,"None","Colors-Available: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(planes,"None","Planes: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(comp,"None","Compression: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(imp_color,"None","Important-Colors: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(x,"None","Pixel-per-Meter X: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(y,"None","Pixel-per-Meter Y: ",out,output,1,"",vrb)
            elif extension == "gif":
                Printer.GENERATE.Sentence(pix,"None","Pixel-Ratio: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(g_type,"None","GIF-Version: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_pal,"None","Color-Map: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_r_d,"None","Color-Resolution-Depth: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_number,"None","Number-of-Colors: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_n_bytes,"None","Colors-Bytes-Lenght: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(b_pix,"None","Bits-Per-Pixel: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(imp1,"None","Color-Order: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(b_color),"None","Background-Color: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(frame),"None","Frame-Number: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(a_seq,"None","Animation-Iteration: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(duration,"None seconds","Duration: ",out,output,1,"",vrb)
            elif extension == "jpg" or extension == "jpeg" or extension == "jps":
                Printer.GENERATE.Sentence(pix,"None","Pixel-Ratio: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(h_t,"None","Huffman-Table: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(meta_order,"None","Metadata-Order: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_scheme,"None","Color-Scheme: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c_comp,"None","Color-Components: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(b_pix,"None","Bits-Per-Sample: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(d_pix,"None","Resolution-Unit: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(x,"None","X-Resolution: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(y,"None","Y-Resolution: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(th_w,"None","Thumbnail-Width: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(th_h,"None","Thumbnail-Height: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[27],"None","Camera-Profile: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[18],"None","ICC-Profile: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[22],"None","Focus-Mode: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[15],"None","Toolkit: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[8],"None","Creator: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[23],"None","Lens-Profile-Name: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[24],"None","Lens-Profile-Filename: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[21],"None","Lens-Model: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[25],"None","Lens-Serial-Number: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[17],"None","Firmware: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[26],"None","Lens-Info (Lens-Range): ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[19],"None","Approximate-Focus-Distance: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[20],"None","Flash-Compensation: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[31],"None","Altitude: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[29],"None","Latitude: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[30],"None","Longitude: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(geoc,"None","Geolocation: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[10],"None","Creator-Tool: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[11],"None","Original-Filename: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[0],"None","Creation-Date: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[12],"None","Modification-Date: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[13],"None","Metadata-Date: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[1],"None","Document-Id: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[2],"None","Instance-Id: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[3],"None","Original-Id: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[14],"None","Color-Mode: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[4],"None","Gimp-Api: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[7],"None","Gimp-Version: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[5],"None","Gimp-Platform: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[6],"None","Timestamp: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[9],"None","Author: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(meta[28],"None","Copyright: ",out,output,1,"",vrb)
            if adv == 1:
                    if len(times):
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing file Events")
                        i = 1
                        v = 0
                        for date in times:
                            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Event'n°{}".format(i))
                            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Action: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(events[v])))
                            if len(times):
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Date: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(date)))
                                except Exception as e:
                                        pass
                            if len(instances):
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Instance-Id: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(instances[v])))
                                except Exception as e:
                                    pass
                            if len(agents):
                                try:
                                    if "rdf:li" in agents[v]:
                                        agents[v] = agents[v].rsplit("rdf",1)[0]
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Software: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED(agents[v])))
                                except Exception as e:
                                    pass
                            if len(changes):
                                try:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Changes: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED_EV(changes[v])))
                                except Exception as e:
                                    pass
                            i = i + 1
                            v = v + 1
            if vrb == 0:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")
        elif extension == "mp4":
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Video Metadata")
            reader = open(origfile,"rb")
            creator = "None"
            extid = "None"
            fbid = "None"
            touchtype = "None"
            sleep(2)
            reader = open(origfile,"rb")
            max2 = reader.read()
            reader.close()
            if b"adobe:ns:meta/" in max2:
                adobe = "True"
            else:
                adobe = "False"
            reader = open(origfile,"rb")
            max1 = reader.readlines()
            i = 0
            for line in max1:
                if adobe == "True":
                    if b"<Attrib:Created>" in line or b"<Attrib:Created> " in line:
                        creator = Decoder.EXTRACTOR.GET_Metadata("<Attrib:Created>","<Attrib:Created> ",i,max1,1,1,False,"",line,6,"")
                    if b"<Attrib:ExtId>" in line or b"<Attrib:ExtId> " in line:
                        extid = Decoder.EXTRACTOR.GET_Metadata("<Attrib:ExtId>","<Attrib:ExtId> ",i,max1,1,1,False,"",line,6,"")
                    if b"<Attrib:FbId>" in line or b"<Attrib:FbId> " in line:
                        fbid = Decoder.EXTRACTOR.GET_Metadata("<Attrib:FbId>","<Attrib:FbId> ",i,max1,1,1,False,"",line,6,"")
                    if b"<Attrib:TouchType>" in line or b"<Attrib:TouchType> " in line:
                        touchtype = Decoder.EXTRACTOR.GET_Metadata("<Attrib:TouchType>","<Attrib:TouchType> ",i,max1,1,1,False,"",line,6,"")
                i = i +1
            Printer.GENERATE.Sentence(name,"None","File-Name: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(creator,"None","Creation-Date: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(extid,"None","Ads Ext-Id: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(fbid,"None","Ads Fb-Id: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(touchtype,"None","Ads Touchtype: ",out,output,1,"",vrb)
        elif extension == "zip" or extension == "apk" or extension == "jar":
            Properties.GET.ZIP_FILE(origfile,output,extr,out,vrb)
        elif extension == "tar.xz" or extension == "tar.gz" or extension == "tar.bz2":
            if "xz" in extension:
                read = "xz"
            elif "gz" in extension:
                read = "gz"
            elif "bz2" in extension:
                read = "bz2"
            Properties.GET.TAR_FILE(origfile,output,extr,out,vrb,read)
        else:
            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Not supported {} files".format(Colors.Color.GREEN + extension + Colors.Color.WHITE))
