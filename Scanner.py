from SymbolTable import SymbolTable

class Scanner:
    def __init__(self,problem):
        self.__symbolTable = SymbolTable(10)
        self.__programInternalForm = {}
        self.__listOfTokens = []
        self.readFromFile("tokens.txt")
        self.__input = ""
        self.readProgram(problem)
        self.__currentKeyPIF = 0
        self.__currentKeyST = 0


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
            if char != "_" and char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                return False
        return True


    def isValidConstant(self,token):
        if token[0] == 0:
            return False
        for char in token:
            if char not in "1234567890":
                return False
        return True


    def clasifyToken(self,t):
        token = t.strip(" ")
        if token == '':
            return
        if (token in self.__listOfTokens):
            self.__programInternalForm[self.__currentKeyPIF] = token
            self.__currentKeyPIF += 1
        elif self.isValidIdentifier(token):
            self.__symbolTable.add(self.__currentKeyST, token)
            self.__currentKeyST += 1
        elif self.isValidConstant(token):
            pass
        else:
            raise Exception("Lexical error found! Invalid token '"+token+"'")


    def isSeparator(self,char):
        return char in ["(", ")", "[", "]", " ", "'", ";", '"', ":"]


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
                elif i == len(self.__input)+1:
                    separatedInput.append(self.__input[lastSeparator+1:i+1])
                else:
                    separatedInput.append(self.__input[lastSeparator+1:i])
                lastSeparator = i
        return separatedInput


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
                    else:
                        allTokens.append(word[lastOperator+1:i])
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
