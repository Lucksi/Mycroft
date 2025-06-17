# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class OBJECT:
    
    @staticmethod
    def FOUND(text,term):
        terms = []
        if term.startswith('"'):
            term = term.replace('"',"")
            terms = [term]
        else:
            term1 = term.upper()
            term2 = term.lower()
            term3 = term.capitalize()
            term4 = term[0].lower() + term[1:]
            if term == term1:
                terms =[term,term2,term3,term4]
            elif term == term2:
                terms = [term,term1,term3,term4]
            elif term == term3:
                terms = [term,term1,term2,term4]
            elif term == term4:
                terms = [term,term1,term2,term3]
            else:
                terms = [term,term1,term2,term3,term4]
        line_c = 0
        f_lines = []
        t_term = 0
        f = open(text,"r")
        reader = f.readlines()
        for line in reader:
            line_c = line_c + 1
            for element in terms:
                t_term = t_term + line.count(element)
                if element in line:
                    if line_c in f_lines:
                        pass
                    else:
                        f_lines.append(line_c)
        if t_term > 0:
            is_found = str(t_term)
        else:
            is_found = "Not Found"
        return is_found,str(f_lines)