from ManagerDeBranche import ManagerDeBranche



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
        
         
def traduireInstruction(instruction, managerBranche, numInstruction):
    instruction = instruction.replace(",", " ")
    instruction = instruction.replace("\t", " ")
    instruction = instruction.upper()
    tab = instruction.split(" ")
    tab = [instruction for instruction in tab if instruction != ""]
    print(tab)
    
    binaire = ""
    
    if tab[0] == "LSLS":
        if(len(tab) == 4):
            binaire = "00000" + traduireImmediat(tab[3], 5) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        else:
            binaire = "0100000010" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
    
    
    elif tab[0] == "LSRS":
        if(len(tab) == 4):
            binaire = "00001" + traduireImmediat(tab[3], 5) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        else:
            binaire = "0100000011" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
    
    
    elif tab[0] == "ASRS":
        if(len(tab) == 4):
            binaire = "00010" + traduireImmediat(tab[3], 5) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        else:
            binaire = "0100000100" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
    
    
    elif tab[0] == "ADDS":
        if(len(tab) == 4):
            if(estUnRegistre(tab[3])):
                binaire = "0001100" + traduireRegistre(tab[3]) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            else:
                binaire = "0001110" + traduireImmediat(tab[3], 3) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        else:
            binaire = "00110" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
    
    
    elif tab[0] == "SUBS":
        if(len(tab) == 4):
            if(estUnRegistre(tab[3])):
                binaire = "0001101" + traduireRegistre(tab[3]) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
            else:
                binaire = "0001111" + traduireImmediat(tab[3], 3) + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        else:
            binaire = "00111" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
    
    
    elif tab[0] == "MOVS":
        binaire = "00100" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
        
    
    elif tab[0] == "CMP":
        if(estUnRegistre(tab[2])):
            binaire = "0100001010" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        else:
            binaire = "00101" + traduireRegistre(tab[1]) + traduireImmediat(tab[2], 8)
     
     
    elif tab[0] == "ANDS":
        binaire = "0100000000" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "EORS":
        binaire = "0100000001" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
    
    
    elif tab[0] == "ADCS":
        binaire = "0100000101" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "SBCS":
        binaire = "0100000110" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "RORS":
        binaire = "0100000111" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
        
    elif tab[0] == "TST":
        binaire = "0100001000" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "RSBS":
        binaire = "0100001001" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])

    
    elif tab[0] == "CMN":
        binaire = "0100001011" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "ORRS":
        binaire = "0100001100" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "MULS":
        binaire = "0100001101" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
    
    elif tab[0] == "BICS":
        binaire = "0100001110" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
    
    
    elif tab[0] == "MVNS":
        binaire = "0100001111" + traduireRegistre(tab[2]) + traduireRegistre(tab[1])
        
        
    elif tab[0] == "STR":
        offset = tab[-1][:-1]
        if "S" in offset:
            offset = "#0"
        binaire = "10010" + traduireRegistre(tab[1]) + traduireImmediat(offset, 8, 4)
    
    
    elif tab[0] == "LDR":
        offset = tab[-1][:-1]
        binaire = "10011" + traduireRegistre(tab[1]) + traduireImmediat(offset, 8, 4)
        
    
    elif tab[0] == "ADD":
        binaire = "101100000" + traduireImmediat(tab[2], 7, 4)
        
    
    elif tab[0] == "SUB":
        binaire = "101100001" + traduireImmediat(tab[2], 7, 4)
        

    elif tab[0][0] == "B":
        if tab[0] == "B":
            distance = managerBranche.getDistanceEntreDeuxLabels(tab[1], numInstruction)
            binaire = "11100" + traduireEntierEnBinaireComplement2(distance, 11)
        else:
            distance = managerBranche.getDistanceEntreDeuxLabels(tab[1], numInstruction)
            binaire = "1101" + traduireSymboleEgalite(tab[0][1:]) + traduireEntierEnBinaireComplement2(distance)
    
    else:
        raise NotImplementedError
        
    return traduireEnHexadecimal(binaire)


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
    print(line)
    if line and line[0] != "." and line[0] != "@" and line != "run:":
        print(line + " -> " + traduireInstruction(line, managerBranche, i))
        fichierCible.write(traduireInstruction(line, managerBranche, i) + " ")
        i += 1
        
print("SUCCESS")