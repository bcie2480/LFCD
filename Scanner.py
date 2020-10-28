from SymbolTable import SymbolTable

class Scanner:
    def __init__(self,problem):
        self.__symbolTable = SymbolTable(10)
        self.__programInternalForm = []
        self.__listOfTokens = []
        self.readFromFile("tokens.txt")
        self.__input = ""
        self.readProgram(problem)


    def readFromFile(self,fileName):
        f = open(fileName, "r")
        for token in f:
            self.__listOfTokens.append(token[:-1])
        f.close()


    def readProgram(self,fileName):
        f = open(fileName, "r")
        for instruction in f:
            self.__input+= " " + instruction[:-1]
        f.close()


    def printInput(self):
        print(self.__input)


    def isValidIdentifier(self,token):
        if token[0] not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            return False
        for char in token[1:]:
            if char != "_" and char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_":
                return False
        return True


    def isValidConstantInt(self,token):
        if token[0] == "0":
            return False
        for char in token:
            if char not in "1234567890":
                return False
        return True

    def isValidConstantString(self,token):
        if token[0] != "'":
            return False
        if token[-1] != "'":
            return False
        for char in token[1:-1]:
            if char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_":
                return False
        return True


    def clasifyToken(self,t):
        token = t.strip(" ")
        if token == '':
            return
        if (token in self.__listOfTokens):
            self.__programInternalForm.append([token,-1])
        elif self.isValidIdentifier(token):
            id = self.__symbolTable.findValue(token)
            if id == -1:
                self.__symbolTable.add(token)
                self.__programInternalForm.append(["id", id])
            else:
                self.__programInternalForm.append(["id", id])
        elif self.isValidConstantInt(token):
            self.__programInternalForm.append(["const",token])
        elif self.isValidConstantString(token):
            self.__programInternalForm.append(["const", token])
        else:
            raise Exception("Lexical error found! Invalid token '"+token+"'")


    def isSeparator(self,char):
        return char in ["(", ")", "[", "]", " ", ";", '"', ":","\n"]


    def isOperator(self,char):
        return char in ["+", "-", "*", "/", "%", "<=", ">=", "==", "=", "<", ">", "and", "or", "not"]


    def splitInputSeparators(self):
        #split for all delimiters
        separatedInput = []
        lastSeparator = 0
        for i in range(0,len(self.__input)):
            if self.isSeparator(self.__input[i]):
                if lastSeparator == 0:
                    separatedInput.append(self.__input[lastSeparator:i])
                    separatedInput.append(self.__input[i])
                elif i == len(self.__input)+1:
                    separatedInput.append(self.__input[lastSeparator])
                    separatedInput.append(self.__input[lastSeparator+1:i+1])
                else:
                    separatedInput.append(self.__input[lastSeparator+1:i])
                    separatedInput.append(self.__input[i])
                lastSeparator = i
        return separatedInput
        '''
        separatedInput = re.split(";|:| |\(|\)|\[|\]",self.__input)
        return separatedInput'''



    def splitInputOperators(self):
        #split for all operators to get constants and identifiers
        separatedInput = self.splitInputSeparators()
        allTokens=[]
        for word in separatedInput:
            lastOperator = 0
            for i in range(0,len(word)):
                if self.isOperator(word[i]):
                    if lastOperator == 0:
                        allTokens.append(word[lastOperator:i])
                        allTokens.append(word[i])
                    else:
                        allTokens.append(word[lastOperator+1:i])
                        allTokens.append(word[i])
                    lastOperator = i
            if lastOperator == 0:
                allTokens.append(word)
            else:
                allTokens.append(word[lastOperator+1:i+1])
        return allTokens


    def scan(self):
        tokensInProgram = self.splitInputOperators()
        for token in tokensInProgram:
            self.clasifyToken(token)
        print("\nThe program has been scanned!\n")
        self.printOutput()


    def printTokens(self):
        print(self.__listOfTokens)


    def printOutput(self):
        print("Symbol Table: ")
        print(self.__symbolTable)
        print("PIF: ")
        print(self.__programInternalForm)


def test():
    s = Scanner("p1.txt")
    s.scan()


test()
