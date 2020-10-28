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
        self.__st = [None] * length
        self.__length= length

    def hash(self,key):
        length = len(self.__st)
        return key % length

    def __str__(self):
        s="";
        for symbol in self.__st:
            s+=str(symbol)+"\n"
        return s

    def ascii(self, elem):
        s = 0
        elem.strip("\"")
        for i in range(0, len(elem)):
            s = s + ord(elem[i])
        return s

    def add(self,value):
        if isinstance(value, str):
            key = self.ascii(value)
        else:
            key = value
        index = self.hash(key)
        node = self.__st[index]
        if node is None:
            self.__st[index] = Node(value)
            return index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(value)


    def findValue(self, value):
        if isinstance(value, str):
            key = self.ascii(value)
        else:
            key = value
        index = self.hash(key)
        if self.__st[index] is None:
            return -1
        else:
            node = self.__st[index]
            while node is not None:
                if node.getValue() == value:
                    return index
                node = node.next



def test():
    st = SymbolTable(5)

    st.add("a")
    st.add("b")
    st.add("c")
    st.add("d")

    print("Symbol table: \n")
    print(st)

    print("checking for value 'c':")
    print(st.findValue("c"))
    print("checking for value 'a':")
    print(st.findValue("a"))
    print("checking for value 'r':")
    print(st.findValue("r"))
    print("checking for value 'b':")
    print(st.findValue("b"))


test()
