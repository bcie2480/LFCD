class Node():
    def __init__(self,val):
        self.__value = val
        self.next = None

    def __str__(self):
        return "value:" +str(self.__value) + " next: " +str(self.next)

    def getValue(self):
        return self.__value



class SymbolTable():
    def  __init__(self,length):
        #initializing all the values from st with none
        self.__st = [None] * length
        self.__length= length

    def hash(self,key):
        length = len(self.__st)
        return hash(key) % length

    def __str__(self):
        s="";
        for symbol in self.__st:
            s+=str(symbol)+"\n"
        return s

    def add(self, key, value):
        if self.findValue(value):
            return
        elem = self.__st[self.hash(key)]

        if elem == None:
            elem = Node(value)
            self.__st[self.hash(key)] = elem
            return

        node = Node(value)
        node.next = elem
        self.__st[self.hash(key)] = node
        return

    def findValue(self, value):
        for key in range(0,self.__length):
            index = self.hash(key)
            if self.__st[index]==None:
                continue
            else:
                node = self.__st[index]
                while node != None:
                    if node.getValue() == value:
                        return True
                    node = node.next
        return False



def test():
    st = SymbolTable(5)

    st.add(1,"a")
    st.add(6,"b")
    st.add(2,"c")
    st.add(3,"d")

    print("Symbol table: \n")
    print(st)

    print("checking for value 'c':")
    print(st.findValue("c"))
    print("checking for value 'a':")
    print(st.findValue("a"))
    print("checking for value 'r':")
    print(st.findValue("r"))

#test()
