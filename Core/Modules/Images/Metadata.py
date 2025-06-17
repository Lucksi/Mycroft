# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Modules import Reader as Decoder
from Core.Utils import Conversion


class GET_METADATA:
  
    @staticmethod
    def EXTRACT(adobe,extension,gimp,origfile,device,images,instances,events,times,agents,changes,height2,width2):
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
        o_f_n = "None"
        mod_date = "None"
        metadata_d = "None"
        col_mode = "None"
        toolkit = "None"
        icc_prof = "None"
        flash_s = "None"
        firmware = "None"
        a_f_d = "None"
        a_f_d_c = "None"
        a_f_l_c = "None"
        lens_mod = "None"
        focus_m = "None"
        lens_p_n = "None"
        lens_p_f = "None"
        lens_s_n = "None"
        lens_info = "None"
        cam_p = "None"
        copy = "None"
        lat = "None"
        lon = "None"
        alt = "None"
        geoc = "None"
        results = []
        i = 0
        reader = open(origfile,"rb")
        max1 = reader.readlines()
        for line in max1:
                if adobe == "False":
                    try:
                        if b"^" in line and extension != "gif" and extension != "bmp":
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
                    if b"<xmp:CreatorTool>" in line or b"<xmp:CreatorTool> "in line:
                            tool = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreatorTool>","<xmp:CreatorTool>  ",i,max1,1,1,False,"",line,6,"")
                    if b"x:xmptk=" in line or b"x:xmptk= " in line:
                            toolkit = Decoder.EXTRACTOR.GET_Metadata("x:xmptk=","x:xmptk= ",i,max1,1,1,False,"",line,8,'" ')
                    if b"<xmp:MetadataDate>" in line or b"<xmp:MetadataDate> " in line:
                            metadata_d = Decoder.EXTRACTOR.GET_Metadata("<xmp:MetadataDate>","<xmp:MetadataDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmpMM:DocumentID>" in line or b"<xmpMM:DocumentID> " in line:
                            docid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:DocumentID>","<xmpMM:DocumentID> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmpMM:InstanceID>" in line or b"<xmpMM:InstanceID> " in line:
                            instid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:InstanceID>","<xmpMM:InstanceID> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmp:Instructions>" in line or b"<xmp:Instructions> " in line:
                            instid = Decoder.EXTRACTOR.GET_Metadata("<xmp:Instructions>","<xmp:Instructions> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmp:CreateDate>" in line or b"<xmp:CreateDate> " in line:
                            creation = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreateDate>","<xmp:CreateDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmp:ModifyDate>" in line or b"<xmp:ModifyDate> " in line:
                            mod_date = Decoder.EXTRACTOR.GET_Metadata("<xmp:ModifyDate>","<xmp:ModifyDate> ",i,max1,1,1,False,"",line,5,"")
                    if b"<xmpMM:OriginalDocumentID>" in line or b"<xmpMM:OriginalDocumentID> " in line:
                            odid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:OriginalDocumentID>","<xmpMM:OriginalDocumentID> ",i,max1,1,1,False,"",line,5,"")
                    if b"<aux:Lens>" in line or b"<aux:Lens> " in line:
                            lens_mod = Decoder.EXTRACTOR.GET_Metadata("<aux:Lens>","<aux:Lens> ",i,max1,1,1,False,"",line,5,'" ')
                    if b"<aux:LensInfo>" in line or b"<aux:LensInfo> " in line:
                            lens_info = Decoder.EXTRACTOR.GET_Metadata("<aux:LensInfo>","<aux:LensInfo> ",i,max1,1,1,False,"",line,5,'" ')
                    if b"<aux:LensSerialNumber>" in line or b"<aux:LensSerialNumber> " in line:
                            lens_s_n = Decoder.EXTRACTOR.GET_Metadata("<aux:LensSerialNumber>","<aux:LensSerialNumber> ",i,max1,1,1,False,"",line,5,'" ')
                    if b"<aux:ApproximateFocusDistance>" in line or b"<aux:ApproximateFocusDistance> " in line:
                            a_f_d = Decoder.EXTRACTOR.GET_Metadata("<aux:ApproximateFocusDistance>","<aux:ApproximateFocusDistance> ",i,max1,1,1,False,"",line,5,'" ')
                            a_f_d_c = Conversion.GET.IMAGE.DISTANCE(a_f_d)
                    if b"<aux:Firmware>" in line or b"<aux:Firmware> " in line:
                            firmware =  Decoder.EXTRACTOR.GET_Metadata("<aux:Firmware>","<aux:Firmware> ",i,max1,1,1,False,"",line,5,'" ')
                    if b"<aux:FlashCompensation>" in line or b"<aux:FlashCompensation> " in line:
                            a_f_l_c = Decoder.EXTRACTOR.GET_Metadata("<aux:FlashCompensation>","<aux:FlashCompensation> ",i,max1,1,1,False,"",line,5,'" ')
                    if b"<exif:GPSAltitude>" in line or b"<exif:GPSAltitude> " in line:
                            alt = Decoder.EXTRACTOR.GET_Metadata("<exif:GPSAltitude>","<exif:GPSAltitude> ",i,max1,1,1,False,"",line,5," ")
                            alt = Conversion.GET.IMAGE.SEA_LEVEL(alt)
                    if b"<exif:GPSLatitude>" in line or b"<exif:GPSLatitude> " in line:
                            lat = Decoder.EXTRACTOR.GET_Metadata("<exif:GPSLatitude>","<exif:GPSLatitude> ",i,max1,1,1,False,"",line,5," ")
                    if b"<exif:GPSLongitude>" in line or b"exif:GPSLongitude= " in line:
                            lon = Decoder.EXTRACTOR.GET_Metadata("<exif:GPSLongitude>","<exif:GPSLongitude> ",i,max1,1,1,False,"",line,5," ")
                    if b"<photoshop:ColorMode>" in line or b"<photoshop:ColorMode> " in line:
                            col_mode = Decoder.EXTRACTOR.GET_Metadata("<photoshop:ColorMode>","<photoshop:ColorMode> ",i,max1,1,1,False,"",line,5," ")
                    if b"<photoshop:ICCProfile>" in line or b"<photoshop:ICCProfile> " in line:
                            icc_prof = Decoder.EXTRACTOR.GET_Metadata("<photoshop:ICCProfile>","<photoshop:ICCProfile> ",i,max1,1,1,False,"",line,5," ")
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
                    if b'<dc:rights><rdf:Alt><rdf:li xml:lang="x-default">' in line or b"<dc:rights>\n" in line:
                        if b"<dc:rights>\n" in line:
                            line = max1[i + 2]
                            try:
                                copy = line.split(b'<rdf:li xml:lang="x-default">',1)[1].decode('latin-1').replace("</rdf:li>", "").replace("<","")
                            except Exception as e:
                                pass
                            line = max1[i - 2]
                        else:
                            copy = line.split(b'dc:rights><rdf:Alt><rdf:li xml:lang="x-default">',1)[1].decode('latin-1').split("/",1)[0].replace("<","")
                        #print(copy)
                    if extension == "psd":
                        if b"<xmp:CreatorTool>" in line or b"<xmp:CreatorTool> "in line:
                            tool = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreatorTool>","<xmp:CreatorTool>  ",i,max1,1,1,False,"",line,6,"")
                        if b"x:xmptk=" in line or b"x:xmptk= " in line:
                            toolkit = Decoder.EXTRACTOR.GET_Metadata("x:xmptk=","x:xmptk= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"<xmp:MetadataDate>" in line or b"<xmp:MetadataDate> " in line:
                            metadata_d = Decoder.EXTRACTOR.GET_Metadata("<xmp:MetadataDate>","<xmp:MetadataDate> ",i,max1,1,1,False,"",line,5,"")
                        if b"<xmpMM:DocumentID>" in line or b"<xmpMM:DocumentID> " in line:
                            docid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:DocumentID>","<xmpMM:DocumentID> ",i,max1,1,1,False,"",line,5,"")
                        if b"<xmpMM:InstanceID>" in line or b"<xmpMM:InstanceID> " in line:
                            instid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:InstanceID>","<xmpMM:InstanceID> ",i,max1,1,1,False,"",line,5,"")
                        if b"<xmp:Instructions>" in line or b"<xmp:Instructions> " in line:
                            instid = Decoder.EXTRACTOR.GET_Metadata("<xmp:Instructions>","<xmp:Instructions> ",i,max1,1,1,False,"",line,5,"")
                        if b"<xmp:CreateDate>" in line or b"<xmp:CreateDate> " in line:
                            creation = Decoder.EXTRACTOR.GET_Metadata("<xmp:CreateDate>","<xmp:CreateDate> ",i,max1,1,1,False,"",line,5,"")
                        if b"<xmp:ModifyDate>" in line or b"<xmp:ModifyDate> " in line:
                            mod_date = Decoder.EXTRACTOR.GET_Metadata("<xmp:ModifyDate>","<xmp:ModifyDate> ",i,max1,1,1,False,"",line,5,"")
                        if b"<xmpMM:OriginalDocumentID>" in line or b"<xmpMM:OriginalDocumentID> " in line:
                            odid = Decoder.EXTRACTOR.GET_Metadata("<xmpMM:OriginalDocumentID>","<xmpMM:OriginalDocumentID> ",i,max1,1,1,False,"",line,5,"")
                        if b"<photoshop:ColorMode>" in line or b"<photoshop:ColorMode> " in line:
                            col_mode = Decoder.EXTRACTOR.GET_Metadata("<photoshop:ColorMode>","<photoshop:ColorMode> ",i,max1,1,1,False,"",line,5,"")
                        if b"<photoshop:ICCProfile>" in line or b"<photoshop:ICCProfile> " in line:
                            icc_prof = Decoder.EXTRACTOR.GET_Metadata("<photoshop:ICCProfile>","<photoshop:ICCProfile> ",i,max1,1,1,False,"",line,5,"")
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
                        line = line.replace(b">",b"")
                        if b"x:xmptk=" in line or b"x:xmptk= " in line:
                            toolkit = Decoder.EXTRACTOR.GET_Metadata("x:xmptk=","x:xmptk=  ",i,max1,1,1,False,"",line,8,'" ')
                        if b"xmp:CreatorTool=" in line or b"xmp:CreatorTool= " in line:
                            tool = Decoder.EXTRACTOR.GET_Metadata("xmp:CreatorTool=","xmp:CreatorTool=  ",i,max1,1,1,False,"",line,8,'" ')
                        if b"xmp:CreateDate=" in line or b"xmp:CreateDate= " in line:
                            creation = Decoder.EXTRACTOR.GET_Metadata("xmp:CreateDate=","xmp:CreateDate=  ",i,max1,1,1,False,"",line,8," ")
                        if b"xmp:MetadataDate=" in line or b"xmp:MetadataDate= " in line:
                            metadata_d = Decoder.EXTRACTOR.GET_Metadata("xmp:MetadataDate=","xmp:MetadataDate  ",i,max1,1,1,False,"",line,8," ")
                        if b"xmp:ModifyDate=" in line or b"xmp:ModifyDate= " in line:
                            mod_date = Decoder.EXTRACTOR.GET_Metadata("xmp:ModifyDate=","xmp:ModifyDate=  ",i,max1,1,1,False,"",line,8," ")
                        if b"xmp:Instructions" in line or b"xmp:Instructions " in line:
                            instid = Decoder.EXTRACTOR.GET_Metadata("xmp:Instructions","xmp:Instructions ",i,max1,1,1,False,"",line,8,"")
                        if b"xmpMM:InstanceID=" in line or b"xmpMM:InstanceID= " in line:
                            instid = Decoder.EXTRACTOR.GET_Metadata("xmpMM:InstanceID=","xmpMM:InstanceID= ",i,max1,1,1,False,"",line,8," ")
                        if b"xmpMM:DocumentID=" in line or b"xmpMM:DocumentID= " in line:
                            docid = Decoder.EXTRACTOR.GET_Metadata("xmpMM:DocumentID=","xmpMM:DocumentID= ",i,max1,1,1,False,"",line,8," ")
                        if b"xmpMM:OriginalDocumentID=" in line or b"xmpMM:OriginalDocumentID= " in line:
                            odid = Decoder.EXTRACTOR.GET_Metadata("xmpMM:OriginalDocumentID=","xmpMM:OriginalDocumentID= ",i,max1,1,1,False,"",line,8," ")
                        if b"xmpMM:PreservedFileName=" in line or b"xmpMM:PreservedFileName= " in line:
                            o_f_n = Decoder.EXTRACTOR.GET_Metadata("xmpMM:PreservedFileName=","xmpMM:PreservedFileName= ",i,max1,1,1,False,"",line,8," ")
                        if b"photoshop:ColorMode=" in line or b"photoshop:ColorMode= " in line:
                            col_mode = Decoder.EXTRACTOR.GET_Metadata("photoshop:ColorMode=","photoshop:ColorMode= ",i,max1,1,1,False,"",line,8," ")
                        if b"photoshop:ICCProfile=" in line or b"photoshop:ICCProfile= " in line:
                            icc_prof = Decoder.EXTRACTOR.GET_Metadata("photoshop:ICCProfile=","photoshop:ICCProfile= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"crs:CameraProfile=" in line or b"crs:CameraProfie= " in line:
                            cam_p = Decoder.EXTRACTOR.GET_Metadata("crs:CameraProfile=","crs:CameraProfile= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"crs:LensProfileName=" in line or b"crs:LensProfileName= " in line:
                            lens_p_n = Decoder.EXTRACTOR.GET_Metadata("crs:LensProfileName=","crs:LensProfileName= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"crs:LensProfileFilename=" in line or b"crs:LensProfileFilename= " in line:
                            lens_p_f = Decoder.EXTRACTOR.GET_Metadata("crs:LensProfileFilename=","crs:LensProfileFilename= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"exifEX:LensModel=" in line or b"exifEX:LensModel= " in line:
                            lens_mod = Decoder.EXTRACTOR.GET_Metadata("exifEX:LensModel=","exifEX:LensModel= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"aux:Lens=" in line or b"aux:Lens= " in line:
                            lens_mod = Decoder.EXTRACTOR.GET_Metadata("aux:Lens=","aux:Lens= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"aux:LensInfo=" in line or b"aux:LensInfo= " in line:
                            lens_info = Decoder.EXTRACTOR.GET_Metadata("aux:LensInfo=","aux:LensInfo= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"aux:LensSerialNumber=" in line or b"aux:LensSerialNumber= " in line:
                            lens_s_n = Decoder.EXTRACTOR.GET_Metadata("aux:LensSerialNumber=","aux:LensSerialNumber= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"aux:ApproximateFocusDistance=" in line or b"aux:ApproximateFocusDistance= " in line:
                            a_f_d = Decoder.EXTRACTOR.GET_Metadata("aux:ApproximateFocusDistance=","aux:ApproximateFocusDistance= ",i,max1,1,1,False,"",line,8,'" ')
                            a_f_d_c = Conversion.GET.IMAGE.DISTANCE(a_f_d)
                        if b"aux:Firmware=" in line or b"aux:Firmware=" in line:
                            firmware =  Decoder.EXTRACTOR.GET_Metadata("aux:Firmware=","aux:Firmware= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"aux:FlashCompensation=" in line or b"aux:FlashCompensation= " in line:
                            a_f_l_c = Decoder.EXTRACTOR.GET_Metadata("aux:FlashCompensation=","aux:FlashCompensation= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"exif:GPSAltitude=" in line or b"exif:GPSAltitude= " in line:
                            alt = Decoder.EXTRACTOR.GET_Metadata("exif:GPSAltitude=","exif:GPSAltitude= ",i,max1,1,1,False,"",line,8,'" ')
                            alt = Conversion.GET.IMAGE.SEA_LEVEL(alt)
                        if b"exif:GPSLatitude=" in line or b"exif:GPSLatitude= " in line:
                            lat = Decoder.EXTRACTOR.GET_Metadata("exif:GPSLatitude=","exif:GPSLatitude= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"exif:GPSLongitude=" in line or b"exif:GPSLongitude= " in line:
                            lon = Decoder.EXTRACTOR.GET_Metadata("exif:GPSLongitude=","exif:GPSLongitude= ",i,max1,1,1,False,"",line,8,'" ')
                        if b"tiff:ImageWidth=" in line or b"tiff:ImageWidth= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:ImageWidth=","tiff:ImageWidth= ",i,max1,1,1,True,width2,line,8," ")
                        if b"tiff:ImageLength=" in line or b"tiff:ImageLength= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:ImageLength=","tiff:ImageLength= ",i,max1,1,1,True,height2,line,8," ")
                        if b"tiff:Make=" in line or b"tiff:Make= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:Make=","tiff:Make= ",i,max1,1,1,True,device,line,8,'" ')
                        if b"tiff:Model=" in line or b"tiff:Model= " in line:
                            Decoder.EXTRACTOR.GET_Metadata("tiff:Model=","tiff:Model= ",i,max1,1,1,True,images,line,8,'" ')
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
        results = [creation,docid,instid,odid,api,platform,timestamp,version,creator,author,tool,o_f_n,mod_date,metadata_d,col_mode,toolkit,flash_s,firmware,icc_prof,a_f_d_c,a_f_l_c,lens_mod,focus_m,lens_p_n,lens_p_f,lens_s_n,lens_info,cam_p,copy,lat,lon,alt]
        return results