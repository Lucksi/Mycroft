# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Modules.Documents import Properties as Prop_D
from Core.Modules.Documents import Permissions
from Core.Modules import Position
from Core.Modules import Reader as Decoder
import xml.dom.minidom

class GET:

    class PDF:
        
        @staticmethod
        def METADATA(origfile,adobe,photoshop,image,annotation,link,heights,widths,events,times,instances,agents,parms,changes,images,device,height2,width2,suspect_keys,permissions,type):            
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
            toolkit = "None"
            linearized = "False"
            company = "None"
            sour_mod = "None"
            producer = "None"
            i = 0
            for line in max1:
                try:
                    if b"<< " in line:
                        line = line.split(b"<< ",1)[1]
                    if b">>>> " in line:
                        line = line.split(b">>>> ",1)[1]
                    line = line.replace(b">>stream",b"")
                except Exception as e:
                    continue
                if b"%PDF" in line:
                    pdf_version = line.split(b"%PDF-",-1)[1].decode('latin-1').split("/",1)[0].replace(" ","").replace("%âãÏÓ","")
                if b"/Count" in line or b"/Count " in line:
                    pages = Decoder.EXTRACTOR.GET_Metadata("/Count","/Count ",i,max1,1,1,False,"",line,2,"")
                if b"/PageLayout/" in line or b"/PageLayout/ " in line:
                    layout = Decoder.EXTRACTOR.GET_Metadata("/PageLayout/","/PageLayout/  ",i,max1,1,1,False,"",line,2,"")
                if b"/Linearized 1/" in line or b"/Linearized 1/ " in line:
                    linearized = "True"
                    if pages == "None":
                        if b"/N" in line or b"/N " in line:
                            pages = Decoder.EXTRACTOR.GET_Metadata("/N","/N ",i,max1,1,1,False,"",line,1,"")
                if b"/Lang" in line or b"/Lang " in line:
                        lang = Decoder.EXTRACTOR.GET_Metadata("/Lang","/Lang ",i,max1,1,1,False,"",line,1,"")
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
                    Decoder.EXTRACTOR.GET_Metadata("/S /URI /URI","/URI ",i,max1,1,1,True,link,line,9,"")
                    key2 = "URI"
                    suspect_keys.append(key2)
                if b"/Annot /T" in line or b"/Annot /T " in line:
                    Decoder.EXTRACTOR.GET_Metadata("/Annot /T","/Annot /T ",i,max1,1,1,True,annotation,line,1,"")
                if b"/Subtype /" in line or b"/Subtype / " in line:
                    Decoder.EXTRACTOR.GET_Metadata("/Subtype /","/Subtype / ",i,max1,1,1,True,type,line,1,"")
                if b"/Image" in line or b"/Image" in line:
                    if b"/Image\n" in line or b"/Image \n" in line:
                        line1 = max1[i + 1]
                        line2 = max1[i + 2]
                    else:
                        line1 = line
                        line2 = line
                    if b"/Height" in line2 or b"/Height " in line2:
                            Decoder.EXTRACTOR.GET_Metadata("/Height","/Height ",i,max1,1,1,True,heights,line2,1,"")
                    if b"/Width" in line1 or b"/Width " in line1:
                            Decoder.EXTRACTOR.GET_Metadata("/Width","/Width",i,max1,1,1,True,widths,line1,1,"")
                if b"/DocChecksum /" in line or b"/DocChecksum / " in line:
                    doc_ch = Decoder.EXTRACTOR.GET_Metadata("/DocChecksum /","/DocChecksum / ",i,max1,1,1,False,"",line,1,"")
                if b"/Encrypt" in line or b"/Encrypt " in line:
                    line_index = Decoder.EXTRACTOR.GET_Metadata("/Encrypt","/Encrypt ",i,max1,1,1,False,"",line,1,"")
                    index =  Position.FINDER.ENCRYPTION_PDF(line_index,max1)[0]
                    ex_ch = Position.FINDER.ENCRYPTION_PDF(line_index,max1)[1]
                    encrypted = "True"
                    line = max1[index]
                    if line.startswith(b"<</Filter"):
                        pass
                    else:
                        line = line.rsplit(ex_ch,1)[0]
                        line = b"/Filter" + line.rsplit(b"/Filter",1)[1]
                    if b"/Filter/" in line or b"/Filter/ " in line:
                        algo = Decoder.EXTRACTOR.GET_Metadata("/Filter/","/Filter/ ",i,max1,1,1,False,"",line,1,"")
                    else:
                        algo = ""
                    if b"/V" in line or b"/V " in line:
                        version = Decoder.EXTRACTOR.GET_Metadata("/V","/V ",i,max1,1,1,False,"",line,1,"")
                        if ">>" in version:
                           version= " " + version.rsplit(">>",1)[0].lstrip().rstrip()
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
                        if b"Perms" in line:
                            permsission_num = Decoder.EXTRACTOR.GET_Metadata("/P","/P ",i,max1,1,1,False,"",line,8,"/").replace("\n","").lstrip().rstrip()
                        else:
                            permsission_num = Decoder.EXTRACTOR.GET_Metadata("/P","/P ",i,max1,1,1,False,"",line,7,">>").replace("\n","").lstrip().rstrip()
                        Permissions.GET_PERMISSIONS.PDF.GET(permsission_num,revision_b,permissions)
                    try:
                        version = algo + version + ".{} ({})".format(revision_b.replace(" ",""),bit_length.lstrip())
                        """+ version"""
                    except Exception as e:
                        version = "Undefined"
                if adobe == "False":
                    if b"/Title" in line or b"/Title " in line:
                        if title == "None":
                            title = Decoder.EXTRACTOR.GET_Metadata("/Title","/Title ",i,max1,1,1,False,"",line,1,"")
                    if b"/Author" in line or b"/Author " in line:
                        if author == "None":
                            author = Decoder.EXTRACTOR.GET_Metadata("/Author","/Author ",i,max1,1,1,False,"",line,1,"")
                    if b"/Creator" in line or b"/Creator " in line:
                        if creator == "None":
                            creator = Decoder.EXTRACTOR.GET_Metadata("/Creator","/Creator ",i,max1,1,1,False,"",line,1,"")
                    if b"/Producer" in line or b"/Producer " in line:
                        producer = Decoder.EXTRACTOR.GET_Metadata("/Producer","/Producer ",i,max1,1,1,False,"",line,7,"")
                    if b"/CreationDate" in line or b"/CreationDate " in line and creation == "None":
                        creation = Decoder.EXTRACTOR.GET_Metadata("/CreationDate","/CreationDate ",i,max1,1,1,False,"",line,3,"")
                    if b"/Keywords" in line or b"/Keywords " in line:
                        if key == "None":
                            key = Decoder.EXTRACTOR.GET_Metadata("/Keywords","/Keywords ",i,max1,1,1,False,"",line,3,"")
                    if b"/ModDate" in line or b"/ModDate " in line and mod_date == "None":
                        mod_date = Decoder.EXTRACTOR.GET_Metadata("/ModDate","/ModDate ",i,max1,1,1,False,"",line,3,"")
                    if b"/Company" in line or b"/Company " in line and company == "None":
                        company = Decoder.EXTRACTOR.GET_Metadata("/Company","/Company ",i,max1,1,1,False,"",line,1,"")
                    
                if adobe == "True":
                    if b"<pdf:Producer>" in line or b"<pdf:Producer> " in line:
                        creator = Decoder.EXTRACTOR.GET_Metadata("<pdf:Producer>","<pdf:Producer> ",i,max1,1,1,False,"",line,6,"")
                        if "</rdf:Description>" in creator or "</rdf:Description>\n" in creator:
                            creator = creator.replace("</rdf:Description>","")
                    if b"pdf:Producer=" in line or b"pdf:Producer= " in line:
                        creator = Decoder.EXTRACTOR.GET_Metadata("pdf:Producer=","pdf:Producer= ",i,max1,1,1,False,"",line,8,'" ')
                    if b"x:xmptk=" in line or b"x:xmptk= " in line:
                        toolkit = Decoder.EXTRACTOR.GET_Metadata("x:xmptk=","x:xmptk= ",i,max1,1,1,False,"",line,8,'" ')
                    if b"<xmp:CreateDate>" in line or b"<xmp:CreateDate> " in line:
                        creation = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreateDate>","<xmp:CreateDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"xmp:CreateDate=" in line or b"xmp:CreateDate=" in line:
                        creation = Decoder.EXTRACTOR.GET_Metadata("xmp:CreateDate=","xmp:CreateDate= ",i,max1,1,1,False,"",line,8,'" ')
                    if b"<xmp:ModifyDate>" in line or b"<xmp:ModifyDate> " in line:
                        mod_date = Decoder.EXTRACTOR.GET_Metadata("<xmp:ModifyDate>","<xmp:ModifyDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"xmp:ModifyDate=" in line or b"xmp:ModifyDate= " in line:
                        mod_date = Decoder.EXTRACTOR.GET_Metadata("xmp:ModifyDate=","xmp:ModifyDate= ",i,max1,1,1,False,"",line,8,'" ')
                    if b"<pdf:Keywords>" in line or b"<pdf:Keywords> " in line:
                        key = Decoder.EXTRACTOR.GET_Metadata("<pdf:Keywords>","<pdf:Keywords> ",i,max1,1,1,False,"",line,5,"")
                    if title == "None":
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
            parameters = [pdf_version,creator,lang,title,creation,mod_date,pages,author,tool,docId,instId,layout,metadata_d,doc_ch,key,encrypted,pw_protected,version,toolkit,company,sour_mod,linearized,producer]
            return parameters

    class OFFICE:

        @staticmethod
        def METADATA(File_m,extension,type_file):
            creator = "None"
            description = "None"
            title = "None"
            creation = "None"
            mod_date = "None"
            keywords = "None"
            last_mod = "None"
            language = "None"
            last_printed = "None"
            revision = "None"
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
            macro = "None"
            oleobj = "None"
            if type_file == "Lib_Office":
                document = xml.dom.minidom.parseString(File_m.read('meta.xml'))
                document4 = xml.dom.minidom.parseString(File_m.read('meta.xml')).toprettyxml()
                document5 = xml.dom.minidom.parseString(File_m.read('settings.xml')).toprettyxml()
                table = Decoder.EXTRACTOR.ODF_Metadata(document4,"table-count="," ")
                im_count =  Decoder.EXTRACTOR.ODF_Metadata(document4,"image-count="," ")
                pagesn =  Decoder.EXTRACTOR.ODF_Metadata(document4,"page-count="," ")
                paragraph =  Decoder.EXTRACTOR.ODF_Metadata(document4,"paragraph-count="," ")
                words =  Decoder.EXTRACTOR.ODF_Metadata(document4,"word-count="," ")
                char_count = Decoder.EXTRACTOR.ODF_Metadata(document4,"character-count="," ")
                n_c_space = Decoder.EXTRACTOR.ODF_Metadata(document4,"non-whitespace-character-count=","/>")
                if extension == "odp" or extension == "ods" or extension == "odg":
                    obj =  Decoder.EXTRACTOR.ODF_Metadata(document4,"object-count=","/>")
                elif extension == "odt":
                    obj =  Decoder.EXTRACTOR.ODF_Metadata(document4,"object-count="," ")
                date = Decoder.EXTRACTOR.XML_Metadata(document,"dc:date")
                creator = Decoder.EXTRACTOR.XML_Metadata(document,"dc:creator")
                language = Decoder.EXTRACTOR.XML_Metadata(document,"dc:language")
                revision = Decoder.EXTRACTOR.XML_Metadata(document,"meta:editing-cycles")
                revision_t = Decoder.EXTRACTOR.XML_Metadata(document,"meta:editing-duration").replace("D","D-").replace("P","").replace("T","").replace("H","H-").replace("M","M-")
                tool_c = Decoder.EXTRACTOR.XML_Metadata(document,"meta:generator")
                r_only =  Decoder.EXTRACTOR.ODF_Metadata(document5,'<config:config-item config:name="LoadReadonly" config:type="boolean">',"</")
                pw_protected = Decoder.EXTRACTOR.ODF_Metadata(document5,'<config:config-item config:name="RedlineProtectionKey" config:type="base64Binary">',"</")
            elif type_file == "M_Office":
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
                t_time = Prop_D.GET.MSUITE.TIME(t_time)
                sec = Prop_D.GET.MSUITE.SEC_LEVEL(security)
                list = Prop_D.GET.MSUITE.MACROS(File_m,extension,"True")
                macro = list[0]
                oleobj = list[1]
            parameters = [title,description,keywords,revision,revision_t,creator,date,creation,mod_date,last_mod,last_printed,language,pagesn,paragraph,table,im_count,obj,char_count,n_c_space,c_space,template,tool_c,t_time,sec,lines,pres_format,slides,h_slides,notes,mmclips,shared,company,words,app_v,r_only,pw_protected,macro,oleobj]
            return parameters