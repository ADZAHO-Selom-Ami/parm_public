class ManagerDeBranche:
    def __init__(self, source):
        self.dic = {}
        i = 0
        
        file = open(source, "r")
        for line in file:
            line = line.strip()
            if not line:
                pass
            elif line[0] == ".":
                self.dic[line.strip()[:-1]] = i
            elif line[0] != "@":
                i += 1
        file.close()
        

    def getDistanceEntreDeuxLabels(self, labelCible, source):
        cible = self.dic.get(labelCible)
        
        if(not cible):
            raise ValueError
        
        return cible - source - 3
