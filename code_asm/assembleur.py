from ManagerDeBranche import ManagerDeBranche
from outils import *

   
         
def traduireInstruction(instruction, managerBranche=None, numInstruction=0):
    instruction = instruction.replace(",", " ")
    instruction = instruction.replace("\t", " ")
    instruction = instruction.upper()
    tab = instruction.split(" ")
    tab = [instruction for instruction in tab if instruction != ""]
    
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


if __name__ == "__main__":
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
        if line and line[0] != "." and line[0] != "@" and line != "run:":
            print(line + " -> " + traduireInstruction(line, managerBranche, i))
            fichierCible.write(traduireInstruction(line, managerBranche, i) + " ")
            i += 1
            
    print("SUCCESS")