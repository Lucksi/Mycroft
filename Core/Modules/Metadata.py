# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Formatting
from Core.Utils import Write_File
from Core.Utils import Printer
from Core.Modules import Reader as Decoder
from Core.Modules.Images import Dimension
from Core.Modules.Media import Extraction
from Core.Modules.Archives import Properties
from Core.Modules.Documents import Content
from Core.Modules.Documents import Permissions
from Core.Modules import Position
from Core.Modules import Finder
from time import sleep
import zipfile
import xml.dom.minidom
import xml.etree.ElementTree
import os

class DOCUMENTS:

    @staticmethod
    def File(extension,origfile,name,adv,vrb,out,output,extr,txt_ext,term):
        if extension == "pdf":
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Pdf Metadata")
            sleep(2)
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
            reader = open(origfile,"rb")
            max1 = reader.readlines()
            pdf_version = "None"
            creator = "None"
            lang = "None"
            title = "None"
            creation = "None"
            mod_date = "None"
            pages = "None"
            author = "None"
            tool = "None"
            docId = "None"
            instId = "None"
            layout = "None"
            metadata_d = "None"
            doc_ch = "None"
            key = "None"
            encrypted = "False"
            pw_protected = "None"
            version = "None"
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
            permissions_l = []
            company = "None"
            sour_mod = "None"
            i = 0
            for line in max1:
                try:
                    if b"<< " in line:
                        line = line.split(b"<< ",1)[1]
                except Exception as e:
                    continue
                if b"%PDF" in line:
                    pdf_version = line.split(b"%PDF-",-1)[1].decode('latin-1').split("/",1)[0].replace(" ","").replace("%âãÏÓ","")
                if b"/Count" in line or b"/Count " in line:
                    pages = Decoder.EXTRACTOR.GET_Metadata("/Count","/Count ",i,max1,1,1,False,"",line,2,"")
                if b"/PageLayout/" in line or b"/PageLayout/ " in line:
                    layout = Decoder.EXTRACTOR.GET_Metadata("/PageLayout/","/PageLayout/  ",i,max1,1,1,False,"",line,2,"")
                if b"/OpenAction" in line or b"/OpenAction " in line:
                    key2 = "OpenAction"
                    suspect_keys.append(key2)
                if b"/AA " in line:
                    key2 = "/AA"
                    suspect_keys.append(key2)
                if b"/JavaScript" in line or b"/JavaScript " in line:
                    key2 = "JavaScript/JS"
                    suspect_keys.append(key2)
                if b"/Launch" in line or b"/Launch " in line:
                    key2 = "Launch"
                    suspect_keys.append(key2)
                if b"/JS" in line or b"/JS " in line:
                    key2 = "JavaScript/JS"
                    suspect_keys.append(key2)
                if b"/RichMedia" in line or b"/RichMedia " in line:
                    key2 = "RichMedia"
                    suspect_keys.append(key2)
                if b"/EmbeddedFile" in line or b"/EmbeddedFile " in line:
                    key2 = "EmbeddedFile"
                    suspect_keys.append(key2)
                if b"/ObjStm" in line or b"/ObjStm " in line:
                    key2 = "ObjectStream"
                    suspect_keys.append(key2)
                if b"/SubmitForm" in line or b"/SubmitForm " in line or b"/GoToR" in line or b"/GoToR " in line:
                    key2 = "SubmitForm/GoToR"
                    suspect_keys.append(key2)
                if b"/S /URI /URI" in line or b"/URI " in line:
                    if b"/S /URI /URI" in line:
                        Decoder.EXTRACTOR.GET_Metadata("/S /URI /URI","/URI ",i,max1,1,1,True,link,line,9,"")
                    elif b"/URI " in line:
                        Decoder.EXTRACTOR.GET_Metadata("/URI ","/URI ",i,max1,1,1,True,link,line,9,"")
                    key2 = "URI"
                    suspect_keys.append(key2)
                if b"/DocChecksum /" in line or b"/DocChecksum / " in line:
                    doc_ch = Decoder.EXTRACTOR.GET_Metadata("/DocChecksum /","/DocChecksum / ",i,max1,1,1,False,"",line,1,"")
                if b"/Encrypt" in line or b"/Encrypt " in line:
                    line_index = Decoder.EXTRACTOR.GET_Metadata("/Encrypt","/Encrypt ",i,max1,1,1,False,"",line,1,"")
                    index =  Position.FINDER.ENCRYPTION_PDF(line_index,max1)
                    encrypted = "True"
                    line = max1[index]
                    if b"/Filter/" in line or b"/Filter/ " in line:
                        algo = Decoder.EXTRACTOR.GET_Metadata("/Filter/","/Filter/ ",i,max1,1,1,False,"",line,1,"")
                    else:
                        algo = ""
                    if b"/V" in line or b"/V " in line:
                        version = Decoder.EXTRACTOR.GET_Metadata("/V","/V ",i,max1,1,1,False,"",line,1,"")
                    else:
                        version = ""
                    if b"/Length" in line or b"/Length " in line:
                        bit_length = Decoder.EXTRACTOR.GET_Metadata("/Length","/Length ",i,max1,1,1,False,"",line,1,"") + " Bits"
                    else:
                        bit_length = ""
                    if b"/R" in line or b"/R " in line:
                        revision_b = Decoder.EXTRACTOR.GET_Metadata("/R","/R ",i,max1,1,1,False,"",line,1,"")
                    else:
                        revision_b = ""
                    if b"/P" in line or b"/P " in line:
                        permsission_num = Decoder.EXTRACTOR.GET_Metadata("/P","/P ",i,max1,1,1,False,"",line,7,">>").replace("\n","")
                        Permissions.GET_PERMISSIONS.PDF.GET(permsission_num,revision_b,permissions_l)
                    try:
                        version = algo + version + ".{} ({})".format(revision_b.replace(" ",""),bit_length.lstrip())
                    except Exception as e:
                        version = "Undefined"
                if adobe == "False":
                    if b"/Title" in line or b"/Title " in line:
                        title = Decoder.EXTRACTOR.GET_Metadata("/Title","/Title ",i,max1,1,1,False,"",line,1,"")
                    if b"/Author" in line or b"/Author " in line:
                        author = Decoder.EXTRACTOR.GET_Metadata("/Author","/Author ",i,max1,1,1,False,"",line,1,"")
                    if b"/Lang" in line or b"/Lang " in line:
                        lang = Decoder.EXTRACTOR.GET_Metadata("/Lang","/Lang ",i,max1,1,1,False,"",line,1,"")
                    if b"/Producer" in line or b"/Producer " in line:
                        creator = Decoder.EXTRACTOR.GET_Metadata("/Producer","/Producer ",i,max1,1,1,False,"",line,7,"")
                    if b"/Annot /T" in line or b"/Annot /T " in line:
                        Decoder.EXTRACTOR.GET_Metadata("/Annot /T","/Annot /T ",i,max1,1,1,True,annotation,line,1,"")
                    if b"/Subtype /" in line or b"/Subtype / " in line:
                        Decoder.EXTRACTOR.GET_Metadata("/Subtype /","/Subtype / ",i,max1,1,1,True,type,line,1,"")
                    if b"/Height" in line or b"/Height " in line:
                        Decoder.EXTRACTOR.GET_Metadata("/Height","/Height ",i,max1,1,1,True,heights,line,1,"")
                    if b"/Width" in line or b"/Width " in line:
                        Decoder.EXTRACTOR.GET_Metadata("/Width","/Width",i,max1,1,1,True,widths,line,1,"")
                    if b"/Subtype/" in line or b"/Subtype/ " in line:
                        Decoder.EXTRACTOR.GET_Metadata("/Subtype/","/Subtype/ ",i,max1,1,1,True,type,line,1,"")
                    if b"/CreationDate" in line or b"/CreationDate " in line:
                        creation = Decoder.EXTRACTOR.GET_Metadata("/CreationDate","/CreationDate ",i,max1,1,1,False,"",line,3,"")
                    if b"/Keywords" in line or b"/Keywords " in line:
                        key = Decoder.EXTRACTOR.GET_Metadata("/Keywords","/Keywords ",i,max1,1,1,False,"",line,3,"")
                    if b"/ModDate" in line or b"/ModDate " in line:
                        mod_date = Decoder.EXTRACTOR.GET_Metadata("/ModDate","/ModDate ",i,max1,1,1,False,"",line,3,"")
                    if b"/Company" in line or b"/Company " in line:
                        author = Decoder.EXTRACTOR.GET_Metadata("/Company","/Company ",i,max1,1,1,False,"",line,1,"")
                else:
                    if b"<pdf:Producer>" in line or b"<pdf:Producer> " in line:
                        creator = Decoder.EXTRACTOR.GET_Metadata("<pdf:Producer>","<pdf:Producer> ",i,max1,1,1,False,"",line,6,"")
                        if "</rdf:Description>" in creator or "</rdf:Description>\n" in creator:
                            creator = creator.replace("</rdf:Description>","")
                    if b"<xmp:CreateDate>" in line or b"<xmp:CreateDate> " in line:
                        creation = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreateDate>","<xmp:CreateDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmp:ModifyDate>" in line or b"<xmp:ModifyDate> " in line:
                        mod_date = Decoder.EXTRACTOR.GET_Metadata("<xmp:ModifyDate>","<xmp:ModifyDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"<pdf:Keywords>" in line or b"<pdf:Keywords> " in line:
                        key = Decoder.EXTRACTOR.GET_Metadata("<pdf:Keywords>","<pdf:Keywords> ",i,max1,1,1,False,"",line,5,"")
                    if b'<dc:title><rdf:Alt><rdf:li xml:lang="x-default">' in line or b"<dc:title>\n" in line:
                        if b"<dc:title>\n" in line:
                            line = max1[i + 2]
                            try:
                                title = line.split(b'<rdf:li xml:lang="x-default">',1)[1].decode('latin-1').replace('</rdf:li>', "").replace("<","")
                            except Exception as e:
                                pass
                            line = max1[i - 2]
                        else:
                            title = line.split(b'<dc:title><rdf:Alt><rdf:li xml:lang="x-default">',1)[1].decode('latin-1').split("/",1)[0].replace("<","")
                    if b"<dc:creator><rdf:Seq><rdf:li>" in line or b"<dc:creator>\n" in line:
                        if b"<dc:creator>\n" in line:
                            line = max1[i + 2]
                            try:
                                author = line.split(b"<rdf:li>",1)[1].decode('latin-1').replace("</rdf:li>", "").replace("<","")
                            except Exception as e:
                                pass
                            line = max1[i - 2]
                        else:
                            author = line.split(b"dc:creator><rdf:Seq><rdf:li>",1)[1].decode('latin-1').split("/",1)[0].replace("<","")
                    if b"<xmp:CreatorTool>" in line or b"<xmp:CreatorTool> " in line:
                        tool = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreatorTool>","<xmp:CreatorTool>  ",i,max1,1,1,False,"",line,6,"")
                    if b"<xmp:MetadataDate>" in line or b"<xmp:MetadataDate> " in line:
                        metadata_d = Decoder.EXTRACTOR.GET_Metadata("<xmp:MetadataDate>","<xmp:MetadataDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmpMM:DocumentID>" in line or b"<xmpMM:DocumentID> " in line:
                        docId = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:DocumentID>","<xmpMM:DocumentID> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmpMM:InstanceID>" in line or b"<xmpMM:InstanceID> " in line:
                        instId = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:InstanceID>","<xmpMM:InstanceID> ",i,max1,1,1,False,"",line,5,"")
                    if b"<pdfx:Company>" in line or b"<pdfx:Company> " in line:
                        company = Decoder.EXTRACTOR.GET_Metadata("<pdfx:Company>","<pdfx:Company> ",i,max1,1,1,False,"",line,5,"")
                        if company == "" or company == " ":
                            company == "None"
                    if b"<pdfx:SourceModified>" in line or b"<pdfx:SourceModified> " in line:
                        if b"<pdfx:SourceModified>\n" in line:
                            line = max1[i + 1]
                            sour_mod = line.split(b"/",1)[0]
                            line = max1[i - 1]
                        else:
                            sour_mod = line.split(b"<pdfx:SourceModified>",1)[1].split("/",1)[0].replace("</pdfx:SourceModified>", "").replace("<","")
                        print(sour_mod)
                        if sour_mod == "" or sour_mod == " ":
                            sour_mod == "None"
                    if b"<stEvt:action>" in line or b"<stEvt:action> " in line:
                        Decoder.EXTRACTOR.GET_Metadata("<stEvt:action>","<stEvt:action> ",i,max1,1,1,True,events,line,5,"")
                    if b"<stEvt:when>" in line or b"<stEvt:when> " in line:
                        Decoder.EXTRACTOR.GET_Metadata("<stEvt:when>","<stEvt:when> ",i,max1,1,1,True,times,line,5,"")
                    if b"<stEvt:instanceID>" in line or b"<stEvt:instanceID> " in line:
                        Decoder.EXTRACTOR.GET_Metadata("<stEvt:instanceID>","<stEvt:instanceID> ",i,max1,1,1,True,instances,line,5,"")
                    if b"<stEvt:softwareAgent>" in line or b"<stEvt:softwareAgent> " in line:
                        Decoder.EXTRACTOR.GET_Metadata("<stEvt:softwareAgent>","<stEvt:softwareAgent> ",i,max1,1,1,True,agents,line,5," ")
                    if b"<stEvt:changed>" in line or b"<stEvt:changed> " in line:
                        Decoder.EXTRACTOR.GET_Metadata("<stEvt:changed>","<stEvt:changed> ",i,max1,1,1,True,changes,line,7,"/stEvt:changed")
                    if image == "True":
                        if b"tiff:ImageWidth=" in line or b"tiff:ImageWidth= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:ImageWidth=","tiff:ImageWidth= ",i,max1,1,1,True,width2,line,8," ")
                        if b"tiff:ImageLength=" in line or b"tiff:ImageLength= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:ImageLength=","tiff:ImageLength= ",i,max1,1,1,True,height2,line,8," ")
                        if b"tiff:Make=" in line or b"tiff:Make= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:Make=","tiff:Make= ",i,max1,1,1,True,device,line,8,'" ')
                        if b"tiff:Model=" in line or b"tiff:Model= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:Model=","tiff:Model= ",i,max1,1,1,True,images,line,8,'" ')
                    if photoshop == "True":
                        if b"stEvt:action=" in line or b"stEvt:action= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:action=","stEvt:action= ",i,max1,1,1,True,events,line,8," ")
                        if b"stEvt:when=" in line or b"stEvt:when= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:when=","stEvt:when= ",i,max1,1,1,True,times,line,8," ")
                        if b"stEvt:instanceID=" in line or b"stEvt:instanceID= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:instanceID=","stEvt:instanceID= ",i,max1,1,1,True,instances,line,8," ")
                        if b"stEvt:parameters=" in line or b"stEvt:parameters= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:parameters=","stEvt:parameters= ",i,max1,1,1,True,parms,line,8,'/>')
                        if b"stEvt:softwareAgent=" in line or b"stEvt:softwareAgent= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:softwareAgent=","stEvt:softwareAgent= ",i,max1,1,1,True,agents,line,8,'" ')
                        if b"stEvt:changed=" in line or b"stEvt:changed= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:changed=","stEvt:changed= ",i,max1,1,1,True,changes,line,8," ")
                i = i +1
            reader.close()
            if vrb == 1:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Name: {}".format(Colors.Color.GREEN + name))
                Printer.GENERATE.Sentence(title,"None","Title: ")
                Printer.GENERATE.Sentence(pdf_version,"None","Pdf-Version: ")
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Encrypted: " + Colors.Color.GREEN + Formatting.TEXT.FORMATTED(encrypted))
                if encrypted != "False":
                    Printer.GENERATE.Sentence(version,"None","Encryption: ")
                Printer.GENERATE.Sentence(pw_protected,"None","Password-Protected: ")
                Printer.GENERATE.Sentence(tool,"None","Creator-Tool: ")
                Printer.GENERATE.Sentence(metadata_d,"None","Metadata-Date: ")
                Printer.GENERATE.Sentence(creator,"None","Pdf-Creator: ")
                if encrypted == "False":
                    Printer.GENERATE.Sentence(creation,"None","Pdf-Creation-Date: ")
                    Printer.GENERATE.Sentence(mod_date,"None","Pdf-Modification-Date: ")
                if len(permissions_l):
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Permissions: " + Colors.Color.GREEN + str(permissions_l).replace("[","").replace("]",""))
                Printer.GENERATE.Sentence(docId,"None","Document-Id: ")
                Printer.GENERATE.Sentence(instId,"None","Instance-Id: ")
                Printer.GENERATE.Sentence(layout,"None","Layout: ")
                Printer.GENERATE.Sentence(key,"None","Keywords: ")
                Printer.GENERATE.Sentence(pages,"None","Pages: ")
                if encrypted == "False":
                    Printer.GENERATE.Sentence(lang,"None","Language: ")
                Printer.GENERATE.Sentence(author,"None","Author: ")
                Printer.GENERATE.Sentence(company,"None","Company: ")
                Printer.GENERATE.Sentence(sour_mod,"None","Source-Modified: ")
                Printer.GENERATE.Sentence(doc_ch,"None","Document-Checksum: ")
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
                    if len(heights):
                        i = 1
                        v = 0
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing file Objects")
                        for height in heights:
                            if len(type):
                                types = Formatting.TEXT.FORMATTED(type[v]).replace(" ","")
                                if types == "Image":
                                    if "s" in widths[v]:
                                        pass
                                    else:
                                        megapixel = Dimension.IMAGE.Megapixel(int(Formatting.TEXT.FORMATTED(widths[v])),int(Formatting.TEXT.FORMATTED(height)))
                                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Object'n°{}: Type: {} Height: {} Width: {} Megapixel: {}".format(i,Colors.Color.GREEN + Formatting.TEXT.FORMATTED(type[v]) + Colors.Color.WHITE,Colors.Color.GREEN + Formatting.TEXT.FORMATTED(height) + Colors.Color.WHITE,Colors.Color.GREEN + Formatting.TEXT.FORMATTED(widths[v]) + Colors.Color.WHITE,Colors.Color.GREEN + str(megapixel)))
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
                                megapixel = Dimension.IMAGE.Megapixel(int(Formatting.TEXT.FORMATTED(width2[v])),int(Formatting.TEXT.FORMATTED(height2[v])))
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
            
            if out == 1:
                f = open(output,"a")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(name),f,"File-name: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(title),f,"Title: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(pdf_version),f,"Pdf-Version: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(tool),f,"Creator-Tool: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(metadata_d),f,"Metadata-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creator),f,"Pdf-Creator: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creation),f,"Pdf-Creation-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(mod_date),f,"Pdf-Modification-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(docId),f,"Document-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(instId),f,"Instance-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(layout),f,"Layout: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(key),f,"Keywords: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(pages),f,"Pages: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(lang),f,"Language: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(author),f,"Author: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(company),f,"Company: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(sour_mod),f,"Source-Modified: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(doc_ch),f,"Document-Checksum: ")
                f.close()

        elif extension == "docx" or extension == "pptx" or extension == "odt" or extension == "odp" or extension == "ods" or extension == "xlsx":
            if extension == "docx" or extension == "doc":
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Word Document Metadata")
            elif extension == "pptx":
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Microsoft Powerpoint Metadata")
            else:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Open Document Metadata")
            reader = open(origfile,"rb")
            creator = "None"
            description = "None"
            title = "None"
            creation = "None"
            mod_date = "None"
            keywords = "None"
            last_mod = "None"
            author = "None"
            language = "None"
            last_printed = "None"
            date = "None"
            revision_t = "None"
            pagesn = "None"
            security = "None"
            sec = "None"
            template = "None"
            words = "None"
            lines = "None"
            paragraph = "None"
            t_time = "None"
            shared = "None"
            tool_c = "None"
            company = "None"
            c_space = "None"
            table = "None"
            im_count = "None"
            n_c_space = "None"
            obj = "None"
            char_count = "None"
            app_v = "None"
            pres_format = "None"
            slides = "None"
            notes = "None"
            h_slides = "None"
            mmclips = "None"
            r_only = "False"
            pw_protected = "None"
            images_s = []
            type_images = []
            media_s = []
            type_media = []
            i = 0
            out3 = output.replace("Metadata.txt","Pictures")
            out2 = output.replace("Metadata.txt","Media")
            os.mkdir(out3)
            os.mkdir(out2)
            File_m = zipfile.ZipFile(origfile,'r')
            if extension == "odt" or extension == "odp" or extension == "ods":
                document = xml.dom.minidom.parseString(File_m.read('meta.xml'))
                document2 = xml.etree.ElementTree.fromstring(File_m.read('META-INF/manifest.xml'))
                document4 = xml.dom.minidom.parseString(File_m.read('meta.xml')).toprettyxml()
                document5 = xml.dom.minidom.parseString(File_m.read('settings.xml')).toprettyxml()
                table = Decoder.EXTRACTOR.ODF_Metadata(document4,"table-count="," ")
                im_count =  Decoder.EXTRACTOR.ODF_Metadata(document4,"image-count="," ")
                pagesn =  Decoder.EXTRACTOR.ODF_Metadata(document4,"page-count="," ")
                paragraph =  Decoder.EXTRACTOR.ODF_Metadata(document4,"paragraph-count="," ")
                words =  Decoder.EXTRACTOR.ODF_Metadata(document4,"word-count="," ")
                char_count = Decoder.EXTRACTOR.ODF_Metadata(document4,"character-count="," ")
                n_c_space = Decoder.EXTRACTOR.ODF_Metadata(document4,"non-whitespace-character-count=","/>")
                if extension == "odp" or extension == "ods":
                    obj =  Decoder.EXTRACTOR.ODF_Metadata(document4,"object-count=","/>")
                elif extension == "odt":
                    obj =  Decoder.EXTRACTOR.ODF_Metadata(document4,"object-count="," ")
                date = Decoder.EXTRACTOR.XML_Metadata(document,"dc:date")
                revision = Decoder.EXTRACTOR.XML_Metadata(document,"meta:editing-cycles")
                revision_t = Decoder.EXTRACTOR.XML_Metadata(document,"meta:editing-duration").replace("D","D-").replace("P","").replace("T","").replace("H","H-").replace("M","M-")
                creator = Decoder.EXTRACTOR.XML_Metadata(document,"meta:generator")
                r_only =  Decoder.EXTRACTOR.ODF_Metadata(document5,'<config:config-item config:name="LoadReadonly" config:type="boolean">',"</")
                pw_protected = Decoder.EXTRACTOR.ODF_Metadata(document5,'<config:config-item config:name="RedlineProtectionKey" config:type="base64Binary">',"</")
                if adv == 1:
                    Extraction.FILE.LIB_Format(document2,extr,File_m,out3,images_s,type_images,out2,media_s,type_media)
            else:
                document = xml.dom.minidom.parseString(File_m.read('docProps/core.xml'))
                document2 = xml.dom.minidom.parseString(File_m.read('docProps/app.xml'))
                title = Decoder.EXTRACTOR.XML_Metadata(document,"dc:title")
                description = Decoder.EXTRACTOR.XML_Metadata(document,"dc:description")
                creator = Decoder.EXTRACTOR.XML_Metadata(document,"dc:creator")
                last_mod = Decoder.EXTRACTOR.XML_Metadata(document,"cp:lastModifiedBy")
                creation = Decoder.EXTRACTOR.XML_Metadata(document,"dcterms:created")
                mod_date = Decoder.EXTRACTOR.XML_Metadata(document,"dcterms:modified")
                revision = Decoder.EXTRACTOR.XML_Metadata(document,"cp:revision")
                keywords = Decoder.EXTRACTOR.XML_Metadata(document,"cp:keywords")
                language = Decoder.EXTRACTOR.XML_Metadata(document,"dc:language")
                last_printed = Decoder.EXTRACTOR.XML_Metadata(document,"cp:lastPrinted")
                pagesn = Decoder.EXTRACTOR.XML_Metadata(document2,"Pages")
                paragraph = Decoder.EXTRACTOR.XML_Metadata(document2,"Paragraphs")
                template = Decoder.EXTRACTOR.XML_Metadata(document2,"Template")
                tool_c = Decoder.EXTRACTOR.XML_Metadata(document2,"Application")
                lines = Decoder.EXTRACTOR.XML_Metadata(document2,"Lines")
                security = Decoder.EXTRACTOR.XML_Metadata(document2,"DocSecurity")
                t_time = Decoder.EXTRACTOR.XML_Metadata(document2,"TotalTime")
                shared = Decoder.EXTRACTOR.XML_Metadata(document2,"SharedDoc")
                company = Decoder.EXTRACTOR.XML_Metadata(document2,"Company")
                c_space = Decoder.EXTRACTOR.XML_Metadata(document2,"CharactersWithSpaces")
                words = Decoder.EXTRACTOR.XML_Metadata(document2,"Words")
                pres_format = Decoder.EXTRACTOR.XML_Metadata(document2,"PresentationFormat")
                slides = Decoder.EXTRACTOR.XML_Metadata(document2,"Slides")
                notes = Decoder.EXTRACTOR.XML_Metadata(document2,"Notes")
                h_slides = Decoder.EXTRACTOR.XML_Metadata(document2,"HiddenSlides")
                mmclips = Decoder.EXTRACTOR.XML_Metadata(document2,"MMClips")
                app_v = Decoder.EXTRACTOR.XML_Metadata(document2,"AppVersion")
                
                if adv == 1:
                    file_list = File_m.namelist()
                    Extraction.FILE.MIC_Format(file_list,extension,extr,File_m,out3,images_s,type_images,out2,media_s,type_media)
             
            if vrb == 1:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Name: {}".format(Colors.Color.GREEN + name))
                Printer.GENERATE.Sentence(title,"None","Title: ")
                Printer.GENERATE.Sentence(description,"None","Description: ")
                Printer.GENERATE.Sentence(keywords,"None","Keywords: ")
                Printer.GENERATE.Sentence(revision,"None","Revision: ")
                Printer.GENERATE.Sentence(revision_t,"None","Revision-Time: ")
                Printer.GENERATE.Sentence(creator,"None","Creator: ")
                Printer.GENERATE.Sentence(date,"None","Date: ")
                Printer.GENERATE.Sentence(creation,"None","Creation-Date: ")
                Printer.GENERATE.Sentence(last_mod,"None","Last-Modified-By: ")
                Printer.GENERATE.Sentence(mod_date,"None","Modification-Date: ")
                Printer.GENERATE.Sentence(last_printed,"None","Last-Printed: ")
                Printer.GENERATE.Sentence(language,"None","Language: ")
                Printer.GENERATE.Sentence(pagesn,"None","Pages: ")
                Printer.GENERATE.Sentence(paragraph,"None","Paragraphs: ")
                Printer.GENERATE.Sentence(table,"None","Table-Count: ")
                Printer.GENERATE.Sentence(im_count,"None","Image-Count: ")
                Printer.GENERATE.Sentence(obj,"None","Object-Count: ")
                Printer.GENERATE.Sentence(char_count,"None","Characters-Count: ")
                Printer.GENERATE.Sentence(n_c_space,"None","Non-Whitespace-Character-Count: ")
                Printer.GENERATE.Sentence(template,"None","Template: ")
                Printer.GENERATE.Sentence(tool_c,"None","Application: ")
                if t_time != "None":
                    t_time2 = int(t_time)/60
                    if t_time2 < 1:
                        t_time = t_time + " Minutes"
                    elif t_time2 < 24:
                        t_time = str(t_time2) + " Hours"
                    else:
                        t_time2 = round(t_time2 / 23.878,2)
                        t_time = str(t_time2) + " Days"
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total-Time: " + Colors.Color.GREEN + t_time)
                Printer.GENERATE.Sentence(lines,"None","Lines: ")
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
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Doc-Security: " + Colors.Color.GREEN + sec)
                Printer.GENERATE.Sentence(pres_format,"None","Presentation-Format: ")
                Printer.GENERATE.Sentence(slides,"None","Slides: ")
                Printer.GENERATE.Sentence(h_slides,"None","Hidden-Slides: ")
                Printer.GENERATE.Sentence(notes,"None","Notes: ")
                Printer.GENERATE.Sentence(mmclips,"None","MMClips: ")
                Printer.GENERATE.Sentence(shared,"None","Shared: ")
                Printer.GENERATE.Sentence(company,"None","Company: ")
                Printer.GENERATE.Sentence(words,"None","Words: ")
                Printer.GENERATE.Sentence(c_space,"None","Characters-With-Space: ")
                Printer.GENERATE.Sentence(app_v,"None","App-Version: ")
                Printer.GENERATE.Sentence(r_only,"None","Read-Only: ")
                Printer.GENERATE.Sentence(pw_protected,"None","Password-Protected: ")
                if len(images_s):
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing Extracted images")
                    i = 1
                    v = 0
                    for image in images_s:
                        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Images n° {}: {} Type: {}".format(i,Colors.Color.GREEN + image + Colors.Color.WHITE,Colors.Color.GREEN + type_images[v]))
                        i = i + 1
                        v = v + 1
                if len(media_s):
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Printing Extracted Media")
                    i = 1
                    v = 0
                    for media in media_s:
                        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Media n° {}: {} Type: {}".format(i,Colors.Color.GREEN + media + Colors.Color.WHITE,Colors.Color.GREEN + type_media[v]))
                        i = i + 1
                        v = v + 1
            else:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")
                
            if out == 1:
                f = open(output,"a")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(name),f,"File-name: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(title),f,"Title: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(description),f,"Description: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(keywords),f,"Keywords: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(revision),f,"Revision: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(revision_t),f,"Revision-Time: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creator),f,"Creator: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(date),f,"Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creation),f,"Creation-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(last_mod),f,"Last-Modified-By: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(mod_date),f,"Modification-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(last_printed),f,"Last-Printed: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(language),f,"Language: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(pagesn),f,"Pages: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(paragraph),f,"Paragraphs: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(table),f,"Table-Count: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(im_count),f,"Image-Count: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(obj),f,"Object-Count: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(char_count),f,"Characters-Count: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(n_c_space),f,"Non-Whitespace-Character-Count: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(template),f,"Template: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(tool_c),f,"Application: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(t_time),f,"Total-Time: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(lines),f,"Lines: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(sec),f,"Doc-Security: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(pres_format),f,"Presentation-Format: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(slides),f,"Slides: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(h_slides),f,"Hidden-Slides: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(notes),f,"Notes: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(mmclips),f,"MMClips: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(shared),f,"Shared: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(company),f,"Company: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(words),f,"Words: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(c_space),f,"Characters-With-Space: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(app_v),f,"App-Version: ")
                f.close()
            
            if txt_ext == 1:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting text from file")
                output = output.replace("Metadata.txt","Content.txt")
                if extension == "docx":
                    document4 = xml.dom.minidom.parseString(File_m.read('word/document.xml'))
                    result = document4.getElementsByTagName("w:t")
                    sleep(3)
                    Content.GET.DOC_TEXT(result,output)
                elif extension == "odt" or extension == "odp":
                    document4 = xml.dom.minidom.parseString(File_m.read('content.xml'))
                    if extension == "odt" or extension == "odp":
                        result = document4.getElementsByTagName("text:span")
                        Content.GET.DOC_TEXT(result,output)
                elif extension == "pptx":
                    Content.GET.PPTX_TEXT(File_m,output)
                if term != "":
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Searching for {}".format(Colors.Color.GREEN + term + Colors.Color.WHITE))
                    sleep(3)
                    found = Finder.OBJECT.FOUND(output,term)[0]
                    lines = Finder.OBJECT.FOUND(output,term)[1]
                    if found != "Not Found":
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Term: {} found {} times on line: {}".format(Colors.Color.GREEN + term + Colors.Color.WHITE,Colors.Color.GREEN + found + Colors.Color.WHITE,Colors.Color.GREEN + lines.replace("[","").replace("]","") ))
                    else:
                        print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Term: {} Not found".format(Colors.Color.GREEN + term + Colors.Color.WHITE))
        
        elif extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "psd" or extension == "gif":
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Image Metadata")
            reader = open(origfile,"rb")
            width = Dimension.IMAGE.Size(extension,origfile)[0]
            height = Dimension.IMAGE.Size(extension,origfile)[1]
            byte_order = Dimension.IMAGE.Size(extension,origfile)[2]
            megapixel = Dimension.IMAGE.Size(extension,origfile)[3]
            creation = "None"
            docid = "None"
            instid = "None"
            odid = "None"
            api = "None"
            platform = "None"
            timestamp = "None"
            version = "None"
            creator = "None"
            author = "None" 
            tool = "None"
            mod_date = "None"
            metadata_d = "None"
            col_mode = "None"
            sleep(2)
            instances = []
            events = []
            times = []
            agents = []
            changes = []
            reader = open(origfile,"rb")
            max2 = reader.read()
            reader.close()
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
                tool = "Photoshop"
            else:
                photoshop = "False"
            reader = open(origfile,"rb")
            max1 = reader.readlines()
            i = 0
            for line in max1:
                if adobe == "False":
                    try:
                        if b"^" in line and extension != "gif":
                            line = max1[0]
                            creation = line.split(b"^",1)[1].split(b"\x00\x00\x02\xa0",1)[0].decode("latin-1")
                    except Exception as e:
                        creation = "None"
                    if b"Exif_JPEG_420" in line:
                        creator = line.split(b"Exif_JPEG_420",1)[1].split(b"Software",1)[0].decode("latin-1")
                    if b"Software Version" in line:
                        version = line.split(b"Software Version",1)[1].split(b" ",1)[1].decode("latin-1")
                else:
                    if gimp == "True":
                        if b"xmpMM:DocumentID=" in line or b"xmpMM:DocumentID= " in line:
                            docid = Decoder.EXTRACTOR.GIMP_Metadata("xmpMM:DocumentID=","xmpMM:DocumentID= ",line)
                        if b"xmpMM:InstanceID=" in line or b"xmpMM:InstanceID= " in line:
                            instid = Decoder.EXTRACTOR.GIMP_Metadata("xmpMM:InstanceID=","xmpMM:InstanceID= ",line)
                        if b"xmpMM:OriginalDocumentID=" in line or b"xmpMM:OriginalDocumentID= " in line:
                            odid = Decoder.EXTRACTOR.GIMP_Metadata("xmpMM:OriginalDocumentID=","xmpMM:OriginalDocumentID= ",line)
                        if b"GIMP:API=" in line or b"GIMP:API= " in line:
                            api = Decoder.EXTRACTOR.GIMP_Metadata("GIMP:API=","GIMP:API= ",line)
                        if b"GIMP:Platform=" in line or b"GIMP:Platform= " in line:
                            platform = Decoder.EXTRACTOR.GIMP_Metadata("GIMP:Platform=","GIMP:Platform= ",line)
                        if b"GIMP:TimeStamp=" in line or b"GIMP:TimeStamp= " in line:
                            timestamp = Decoder.EXTRACTOR.GIMP_Metadata("GIMP:TimeStamp=","GIMP:TimeStamp= ",line)
                        if b"GIMP:Version=" in line or b"GIMP:Version= " in line:
                            version = Decoder.EXTRACTOR.GIMP_Metadata("GIMP:Version=","GIMP:Version= ",line)
                        if b"xmp:CreatorTool=" in line or b"xmp:CreatorTool= " in line:
                            creator = Decoder.EXTRACTOR.GIMP_Metadata("xmp:CreatorTool=","xmp:CreatorTool= ",line)
                        if b"<dc:creator><rdf:Seq><rdf:li>" in line or b"<dc:creator>\n" in line:
                            if b"<dc:creator>\n" in line:
                                line = max1[i + 2]
                                author = line.split(b"<rdf:li>",1)[1].decode('latin-1').replace("</rdf:li>", "").replace("<","")
                                line = max1[i - 2]
                            else:
                                author = line.split(b"dc:creator><rdf:Seq><rdf:li>",1)[1].decode('latin-1').split("/",1)[0].replace("<","")
                        if b"stEvt:action=" in line or b"stEvt:action= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:action=","stEvt:action= ",i,max1,1,1,True,events,line,8," ")
                        if b"stEvt:when=" in line or b"stEvt:when= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:when=","stEvt:when= ",i,max1,1,1,True,times,line,8," ")
                        if b"stEvt:instanceID=" in line or b"stEvt:instanceID= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:instanceID=","stEvt:instanceID= ",i,max1,1,1,True,instances,line,8," ")
                        if b"stEvt:softwareAgent=" in line or b"stEvt:softwareAgent= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:softwareAgent=","stEvt:softwareAgent= ",i,max1,1,1,True,agents,line,8," ")
                        if b"stEvt:changed=" in line or b"stEvt:changed= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("stEvt:changed=","stEvt:changed= ",i,max1,1,1,True,changes,line,7," ")
                    if photoshop == "True":
                        if extension == "psd":
                            if b"<xmp:CreatorTool>" in line or b"/ModDate " in line:
                                tool = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreatorTool>","<xmp:CreatorTool>  ",i,max1,1,1,False,"",line,6,"")
                            if b"<xmp:MetadataDate>" in line or b"/ModDate " in line:
                                metadata_d = Decoder.EXTRACTOR.GET_Metadata("<xmp:MetadataDate>","<xmp:MetadataDate> ",i,max1,1,1,False,"",line,5,"")
                            if b"<xmpMM:DocumentID>" in line or b"/ModDate " in line:
                                docid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:DocumentID>","<xmpMM:DocumentID> ",i,max1,1,1,False,"",line,5,"")
                            if b"<xmpMM:InstanceID>" in line or b"/ModDate " in line:
                                instid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:InstanceID>","<xmpMM:InstanceID> ",i,max1,1,1,False,"",line,5,"")
                            if b"<xmp:CreateDate>" in line or b"<xmp:CreateDate> " in line:
                                creation = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreateDate>","<xmp:CreateDate> ",i,max1,1,1,False,"",line,5,"")
                            if b"<xmp:ModifyDate>" in line or b"/ModDate " in line:
                                mod_date = Decoder.EXTRACTOR.GET_Metadata("<xmp:ModifyDate>","<xmp:ModifyDate> ",i,max1,1,1,False,"",line,5,"")
                            if b"<xmpMM:OriginalDocumentID>" in line or b"<xmpMM:OriginalDocumentID> " in line:
                                odid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:OriginalDocumentID>","<xmpMM:OriginalDocumentID> ",i,max1,1,1,False,"",line,5,"")
                            if b"<photoshop:ColorMode>" in line or b"<photoshop:ColorMode> " in line:
                                col_mode = Decoder.EXTRACTOR.GET_Metadata("<photoshop:ColorMode>","<photoshop:ColorMode> ",i,max1,1,1,False,"",line,5," ")
                            if b"<stEvt:action>" in line or b"<stEvt:action> " in line:
                                Decoder.EXTRACTOR.GET_Metadata("<stEvt:action>","<stEvt:action> ",i,max1,1,1,True,events,line,5,"")
                            if b"<stEvt:when>" in line or b"<stEvt:when> " in line:
                                Decoder.EXTRACTOR.GET_Metadata("<stEvt:when>","<stEvt:when> ",i,max1,1,1,True,times,line,5,"")
                            if b"<stEvt:instanceID>" in line or b"<stEvt:instanceID> " in line:
                                Decoder.EXTRACTOR.GET_Metadata("<stEvt:instanceID>","<stEvt:instanceID> ",i,max1,1,1,True,instances,line,5,"")
                            if b"<stEvt:softwareAgent>" in line or b"<stEvt:softwareAgent> " in line:
                                Decoder.EXTRACTOR.GET_Metadata("<stEvt:softwareAgent>","<stEvt:softwareAgent> ",i,max1,1,1,True,agents,line,5,"")
                            if b"<stEvt:changed>" in line or b"<stEvt:changed> " in line:
                                Decoder.EXTRACTOR.GET_Metadata("<stEvt:changed>","<stEvt:changed> ",i,max1,1,1,True,changes,line,7,"/stEvt:changed")
                        else:
                            if b"xmp:CreatorTool=" in line or b"xmp:CreatorTool= " in line:
                                tool = Decoder.EXTRACTOR.GET_Metadata("xmp:CreatorTool=","xmp:CreatorTool=  ",i,max1,1,1,False,"",line,8,'" ')
                            if b"xmp:CreateDate=" in line or b"xmp:CreateDate= " in line:
                                creation = Decoder.EXTRACTOR.GET_Metadata("xmp:CreateDate=","xmp:CreateDate=  ",i,max1,1,1,False,"",line,8," ")
                            if b"xmp:MetadataDate=" in line or b"xmp:MetadataDate= " in line:
                                metadata_d = Decoder.EXTRACTOR.GET_Metadata("xmp:MetadataDate=","xmp:MetadataDate  ",i,max1,1,1,False,"",line,8," ")
                            if b"xmp:ModifyDate=" in line or b"xmp:ModifyDate= " in line:
                                mod_date = Decoder.EXTRACTOR.GET_Metadata("xmp:ModifyDate=","xmp:ModifyDate=  ",i,max1,1,1,False,"",line,8," ")
                            if b"xmpMM:InstanceID=" in line or b"xmpMM:InstanceID= " in line:
                                instid = Decoder.EXTRACTOR.GET_Metadata("xmpMM:InstanceID=","xmpMM:InstanceID= ",i,max1,1,1,False,"",line,8," ")
                            if b"xmpMM:DocumentID=" in line or b"xmpMM:DocumentID= " in line:
                                docid = Decoder.EXTRACTOR.GET_Metadata("xmpMM:DocumentID=","xmpMM:DocumentID= ",i,max1,1,1,False,"",line,8," ")
                            if b"xmpMM:OriginalDocumentID=" in line or b"xmpMM:OriginalDocumentID= " in line:
                                odid = Decoder.EXTRACTOR.GET_Metadata("xmpMM:OriginalDocumentID=","xmpMM:OriginalDocumentID= ",i,max1,1,1,False,"",line,8," ")
                            if b"photoshop:ColorMode=" in line or b"photoshop:ColorMode= " in line:
                                col_mode = Decoder.EXTRACTOR.GET_Metadata("photoshop:ColorMode=","photoshop:ColorMode= ",i,max1,1,1,False,"",line,8," ")
                            if b"stEvt:action=" in line or b"stEvt:action= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:action=","stEvt:action= ",i,max1,1,1,True,events,line,8," ")
                            if b"stEvt:when=" in line or b"stEvt:when= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:when=","stEvt:when= ",i,max1,1,1,True,times,line,8," ")
                            if b"stEvt:instanceID=" in line or b"stEvt:instanceID= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:instanceID=","stEvt:instanceID= ",i,max1,1,1,True,instances,line,8," ")
                            if b"stEvt:softwareAgent=" in line or b"stEvt:softwareAgent= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:softwareAgent=","stEvt:softwareAgent= ",i,max1,1,1,True,agents,line,8,'" ')
                            if b"stEvt:changed=" in line or b"stEvt:changed= " in line:
                                Decoder.EXTRACTOR.GET_Metadata("stEvt:changed=","stEvt:changed= ",i,max1,1,1,True,changes,line,8," ")
                i = i +1
            reader.close()
            if vrb == 1:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Name: {}".format(Colors.Color.GREEN + name))
                if megapixel != 0:
                    print(Colors.Color.YELLOW + "[v]" +  Colors.Color.WHITE + "Image-Size: {}x{}".format(Colors.Color.GREEN + str(width) + Colors.Color.WHITE, Colors.Color.GREEN + str(height)))
                    print(Colors.Color.YELLOW + "[v]" +  Colors.Color.WHITE + "Megapixel: {}".format(Colors.Color.GREEN + str(megapixel)))
                Printer.GENERATE.Sentence(byte_order,"None","Byte-Order: ")
                Printer.GENERATE.Sentence(creator,"None","Creator: ")
                Printer.GENERATE.Sentence(tool,"None","Creator-Tool: ")
                Printer.GENERATE.Sentence(creation,"None","Creation-Date: ")
                Printer.GENERATE.Sentence(mod_date,"None","Modification-Date: ")
                Printer.GENERATE.Sentence(metadata_d,"None","Metadata-Date: ")
                Printer.GENERATE.Sentence(docid,"None","Document-Id: ")
                Printer.GENERATE.Sentence(instid,"None","Instance-Id: ")
                Printer.GENERATE.Sentence(odid,"None","Original-Id: ")
                Printer.GENERATE.Sentence(col_mode,"None","Color-Mode: ")
                Printer.GENERATE.Sentence(api,"None","Gimp-Api: ")
                Printer.GENERATE.Sentence(version,"None","Gimp-Version: ")
                Printer.GENERATE.Sentence(platform,"None","Gimp-Platform: ")
                Printer.GENERATE.Sentence(timestamp,"None","Timestamp: ")
                Printer.GENERATE.Sentence(author,"None","Author: ")
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
            else:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")
            if out == 1:
                f = open(output,"a")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(name),f,"File-name: ")
                if megapixel != 0:
                    Write_File.OUTPUT.D_LINE(str(width),str(height),f,"Image-Size: {}x{}\n")
                    Write_File.OUTPUT.LINE(str(megapixel),f,"Megapixel: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(byte_order),f,"Byte-Order: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creator),f,"Creator: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(tool),f,"Creator-Tool: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creation),f,"Creation-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(mod_date),f,"Modification-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(metadata_d),f,"Metadata-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(docid),f,"Document-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(instid),f,"Instance-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(odid),f,"Original-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(col_mode),f,"Color-Mode: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(api),f,"Gimp-Api: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(version),f,"Gimp-Version: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(platform),f,"Gimp-Platform: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(timestamp),f,"Timestamp: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(author),f,"Author: ")
                f.close()
        
        elif extension == "mp4":
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Video Metadata")
            reader = open(origfile,"rb")
            creation = "None"
            extid = "None"
            fbid = "None"
            touchtype = "None"
            author = "None"
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
            if vrb == 1:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File-Name: {}".format(Colors.Color.GREEN + name))
                Printer.GENERATE.Sentence(creator,"None","Creation-Date: ")
                Printer.GENERATE.Sentence(extid,"None","Ads Ext-Id: ")
                Printer.GENERATE.Sentence(fbid,"None","Ads Fb-Id: ")
                Printer.GENERATE.Sentence(touchtype,"None","Ads Touchtype: ")
            else:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")
            
            if out == 1:
                f = open(output,"a")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(name),f,"File-name: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(creator),f,"Creation-Date: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(extid),f,"Ext-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(fbid),f,"Fb-Id: ")
                Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(touchtype),f,"Touchtype: ")
                f.close()
        elif extension == "zip" or extension == "apk" or extension == "jar":
            Properties.GET.ZIP_FILE(origfile,output,extr,out,vrb)
        else:
            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Not supported {} files".format(Colors.Color.GREEN + extension + Colors.Color.WHITE))
