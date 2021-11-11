class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class Single_LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self):
        no = int(input("Enter no of nodes to be inserted "))
        for i in range(no):
            data = eval(input("Enter data to be inserted "))
            self.insert_at_end(data)

    def insert_at_end(self, data):
        temp = Node(data)
        p = self.head
        if not p:
            self.head = temp
            return
        while p.link:
            p = p.link
        p.link = temp

    def display_list(self):
        if not self.head:
            print("Empty List")
            return
        p = self.head
        print("The list is ")
        while p:
            print(p.data, end = ' ')
            p = p.link
        print()

    def count_nodes(self):
        if not self.head:
            print("Empty List")
            return
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.link
        print("Number of nodes are ", count)

    def search(self, x):
        pos = 1
        p = self.head
        while p:
            if p.data == x:
                print(x ,"is found at position ",pos)
                break
            p = p.link
            pos +=1
        else:
            print(x,"is not found")

    def insert_at_begining(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
        else:
            temp.link = self.head
            self.head = temp

    def insert(self,pos,data):
        temp = Node(data)
        if pos ==1:
            self.insert_at_begining(data)
            return
        i = 1
        p = self.head
        while i<pos-1 and p:
            i += 1
            p = p.link
        if not p:
            print("you can insert at pos ",i)
        else:
            temp.link = p.link
            p.link = temp



