from ManagerDeBranche import ManagerDeBranche



def traduireRegistre(registre):
    if registre[0] != "r":
        raise ValueError
    
    binary = str(format(int(registre[1:]), "b"))
    
    for i in range(3-len(binary)):
        binary = "0" + binary
        
    return binary

def estUnRegistre(registre):
    return registre[0] == "r"


def traduireImmediat(immediat, longueur, shift=1):
    immediat = immediat.strip()
    if immediat[0] != "#":
        raise ValueError
    
    binary = format(int(immediat[1:])//shift, "b")
    for i in range(longueur-len(binary)):
        binary = "0" + binary
        
    return binary

def estUnImmediat(immediat):
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
    return resultat;


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
    return dic.get(symbole.upper())
        
         
def traduireInstruction(instruction, managerBranche, numInstruction):
    instruction = instruction.replace(",", " ")
    tab = instruction.split(" ")
    tab = [instruction for instruction in tab if instruction != ""]
    
    
    resultat = ""
    
    if tab[0].upper() == "LSLS":
        if(len(tab) == 4):
            binaire = "00000" + traduireImmediat(tab[3], 5) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
        else:
            binaire = "0100000010" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "LSRS":
        if(len(tab) == 4):
            binaire = "00001" + traduireImmediat(tab[3], 5) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
        else:
            binaire = "0100000011" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "ASRS":
        if(len(tab) == 4):
            binaire = "00010" + traduireImmediat(tab[3], 5) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
        else:
            binaire = "0100000100" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "ADDS":
        if(len(tab) == 4):
            if(estUnRegistre(tab[3])):
                binaire = "0001100" + traduireRegistre(tab[3]) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
                resultat = traduireEnHexadecimal(binaire)
            else:
                binaire = "0001110" + traduireImmediat(tab[3], 3) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
                resultat = traduireEnHexadecimal(binaire)
        else:
            binaire = "00110" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
            resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "SUBS":
        if(len(tab) == 4):
            if(estUnRegistre(tab[3])):
                binaire = "0001101" + traduireRegistre(tab[3]) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
                resultat = traduireEnHexadecimal(binaire)
            else:
                binaire = "0001111" + traduireImmediat(tab[3], 3) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
                resultat = traduireEnHexadecimal(binaire)
        else:
            binaire = "00111" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
            resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "MOVS":
        binaire = "00100" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "CMP":
        if(estUnRegistre(tab[2])):
            binaire = "0100001010" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            resultat = traduireEnHexadecimal(binaire)
        else:
            binaire = "00101" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
            resultat = traduireEnHexadecimal(binaire)
     
     
    elif tab[0].upper() == "ANDS":
        binaire = "0100000000" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "EORS":
        binaire = "0100000001" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "ADCS":
        binaire = "0100000101" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "SBCS":
        binaire = "0100000110" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "RORS":
        binaire = "0100000111" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
        
    elif tab[0].upper() == "TST":
        binaire = "0100001000" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "RSBS":
        binaire = "0100001001" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)

    
    elif tab[0].upper() == "CMN":
        binaire = "0100001011" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "ORRS":
        binaire = "0100001100" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "MULS":
        binaire = "0100001101" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "BICS":
        binaire = "0100001110" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "MVNS":
        binaire = "0100001111" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        resultat = traduireEnHexadecimal(binaire)
        
        
    elif tab[0].upper() == "STR":
        offset = tab[-1][:-1]
        if "S" in offset.upper():
            offset = "#0"
        binaire = "10010" + traduireRegistre(tab[1]) + traduireImmediat(offset, 8, 4)
        resultat = traduireEnHexadecimal(binaire)
    
    
    elif tab[0].upper() == "LDR":
        offset = tab[-1][:-1]
        binaire = "10011" + traduireRegistre(tab[1]) + traduireImmediat(offset, 8, 4)
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "ADD":
        binaire = "101100000" + traduireImmediat(tab[2], 7, 4)
        resultat = traduireEnHexadecimal(binaire)
        
    
    elif tab[0].upper() == "SUB":
        binaire = "101100001" + traduireImmediat(tab[2], 7, 4)
        resultat = traduireEnHexadecimal(binaire)
        

    elif tab[0][0].upper() == "B":
        if tab[0].upper() == "B":
            distance = managerBranche.getDistanceEntreDeuxLabels(tab[1], numInstruction)
            binaire = "11100" + traduireEntierEnBinaireComplement2(distance, 11)
            resultat = traduireEnHexadecimal(binaire)
        else:
            distance = managerBranche.getDistanceEntreDeuxLabels(tab[1], numInstruction)
            binaire = "1101" + traduireSymboleEgalite(tab[0][1:]) + traduireEntierEnBinaireComplement2(distance)
            resultat = traduireEnHexadecimal(binaire)
    
    else:
        raise NotImplementedError
        
    return resultat


source = input("Chemin source: ")
cible = input("Chemin cible: ")

try:
    fichierCible = open(cible, "x")
except:
    fichierCible = open(cible, "w")

managerBranche = ManagerDeBranche(source)

file = open(source, "r")
fichierCible.write("v2.0 raw\n")
i = 0
for line in file:
    line = line.strip()
    if line and line[0] != "." and line[0] != "@":
        print(line + " -> " + traduireInstruction(line, managerBranche, i))
        fichierCible.write(traduireInstruction(line, managerBranche, i) + " ")
        i += 1
        
print("SUCCESS")