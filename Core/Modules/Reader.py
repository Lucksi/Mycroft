# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class EXTRACTOR:

    @staticmethod
    def GET_Metadata(Param1,Param2,i,max1,index,position,islist,list,line,style,ext_ch):
        parameter = "None"
        try:
            Param1 = Param1.encode()
            Param2 = Param2.encode()
            Param1_n = Param1.decode() + "\n"
            Param1_n = Param1_n.encode()
            if Param1 in line or Param2 in line:
                if Param1_n in line:
                    try:
                        line = max1[i + index]
                    except Exception as e:
                        pass
                    if style == 3:
                        try:
                            parameter = line.split(b"/",1)[0].decode('latin-1').replace("D:","").split("'",1)[0]
                        except Exception as e:
                            pass
                    else:
                        try:
                            parameter = line.split(b"/",1)[0].decode('latin-1')
                        except Exception as e:
                            pass
                    line = max1[i - index]
                else:
                    if style == 1:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').split("/",1)[0]
                        except Exception as e:
                            pass
                    elif style == 2:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').split("/",1)[0].replace(" ","")
                        except Exception as e:
                            pass
                    elif style == 3:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').split("/",1)[0].replace(" ","").replace("D:","").split("'",1)[0]
                        except Exception as e:
                            pass
                    elif style == 4:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').replace(str(Param1), "")
                        except Exception as e:
                            pass
                    elif style == 5:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').split("/",1)[0].replace(str(Param1), "").replace("<","").replace("T"," ")
                        except Exception as e:
                            pass
                    elif style == 6:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').split("/",1)[0].replace(str(Param1), "").replace("<","")
                        except Exception as e:
                            pass
                    elif style == 7:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1').replace(ext_ch,"")
                        except Exception as e:
                            pass
                    elif style == 8:
                        if ext_ch.encode() in line:
                            ext_ch_2 = ext_ch + "\n"
                            if ext_ch_2.encode() in line:
                                ext_ch = ext_ch + "\n"
                                try:
                                    parameter = line.split(Param1,1)[position].decode('latin-1').split(ext_ch_2 ,1)[0]
                                except Exception as e:
                                    pass
                            else:
                                try:
                                    parameter = line.split(Param1,1)[position].decode('latin-1').split(ext_ch ,1)[0]
                                except Exception as e:
                                    pass
                        else:
                            try:
                                parameter = line.split(Param1,1)[position].decode('latin-1').split("' " ,1)[0]
                            except Exception as e:
                                pass
                    elif style == 9:
                        try:
                            parameter = line.split(Param1,1)[position].decode('latin-1')
                        except Exception as e:
                            pass
            if islist:  
                if parameter in list and list == "link" and list == "annotation":
                    pass
                else:
                    list.append(parameter)
        except:
            parameter = "None"
        return parameter
    
    @staticmethod
    def XML_Metadata(doc,parameter):
        result = "None"
        try:
            result = doc.getElementsByTagName(parameter)[0].childNodes[0].data
        except:
            pass
        return result
    
    @staticmethod
    def ODF_Metadata(document,param,separator):
        parameter = "None"
        try:
            parameter = document.split(param,1)[1].split(separator,1)[0].replace('"',"")
            if "/>" in parameter:
                parameter = document.split("/>",1)[0].replace('"',"")
        except:
            pass
        return parameter
    
    @staticmethod
    def GIMP_Metadata(Param1,Param2,line):
        parameter = "None"
        try:
            line = line.decode("latin-1")
            parameter = line.replace(Param1.lstrip(),"").replace('"',"").lstrip()
        except:
            pass
        return parameter