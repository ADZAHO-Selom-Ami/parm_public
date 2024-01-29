def traduireRegistre(registre):
    registre = registre.strip()
    if registre[0] != "R":
        raise ValueError
    
    binary = str(format(int(registre[1:]), "b"))
    
    for i in range(3-len(binary)):
        binary = "0" + binary
        
    return binary

def estUnRegistre(registre):
    registre = registre.strip()
    return registre[0] == "R"


def traduireImmediat(immediat, longueur, shift=1):
    immediat = immediat.strip()
    if immediat[0] != "#":
        raise ValueError
    
    binary = format(int(immediat[1:])//shift, "b")
    for i in range(longueur-len(binary)):
        binary = "0" + binary
        
    return binary

def estUnImmediat(immediat):
    immediat = immediat.strip()
    return immediat[0] == "#"



def traduireEnHexadecimal(chaine):
    dic = {
        "0000" : "0",
        "0001" : "1",
        "0010" : "2",
        "0011" : "3",
        "0100" : "4",
        "0101" : "5",
        "0110" : "6",
        "0111" : "7",
        "1000" : "8",
        "1001" : "9",
        "1010" : "a",
        "1011" : "b",
        "1100" : "c",
        "1101" : "d",
        "1110" : "e",
        "1111" : "f"
    }
    
    if(len(chaine) != 16):
        raise ValueError;
    resultat = ""
    for i in range(4):
        resultat += dic.get(chaine[i*4:i*4+4])
    return resultat


def traduireEntierEnBinaireComplement2(n, longueur=8):
    trad = format(abs(n), "b")
    for i in range(longueur-len(trad)):
        trad = "0" + trad
    
    if n >= 0:
        return trad
    
    res = ""
    b = False
    for i in range(len(trad)-1, -1, -1):
        if not b:
            if trad[i] == "1":
                b = True
            res = trad[i] + res
        else:
            if trad[i] == "0":
                res = "1" + res
            if trad[i] == "1":
                res = "0" + res
                
    return res

   
def traduireSymboleEgalite(symbole):
    dic = {
        "EQ" : "0000",
        "NE" : "0001",
        "CS" : "0010",
        "HS" : "0010",
        "CC" : "0011",
        "LO" : "0011",
        "MI" : "0100",
        "PL" : "0101",
        "VS" : "0110",
        "VC" : "0111",
        "HI" : "1000",
        "LS" : "1001",
        "GE" : "1010",
        "LT" : "1011",
        "GT" : "1100",
        "LE" : "1101",
        "AL" : "1110",
    }
    return dic.get(symbole)
     