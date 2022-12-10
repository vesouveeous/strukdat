class object:

    def __init__(self, nama, kondisi):
        self.namabarang = nama
        self.kondisibarang = kondisi


class Node:

    '''Node class with two fields'''

    def __init__(self, data):
        self.data = data
        self.next_ptr = None


class Stack:

    '''This class will implement the functionality of Stack'''

    def __init__(self):
        self.top = None

    def Push(self, item):
        '''This will add an item to the stack'''

        node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next_ptr = self.top
            self.top = node

    # def Pop(self):
    #     '''This will remove and return the last inserted item from the stack'''

    #     if self.top is None:
    #         return None
    #     else:
    #         temp = self.top.data
    #         temp1 = self.top.next_ptr
    #         self.top.next_ptr = None
    #         self.top = temp1
    #         return temp

    def getTop(self):
        '''Returns the top node'''

        return self.top.data

    def verifying(self):
        print ('barang', self.top.data.namabarang)
        verifikasi = input('kondisi barang: (baik/rusak) ')
        if verifikasi == 'baik':
            if self.top is None:
                return None
            else:
                temp = self.top.data
                temp1 = self.top.next_ptr
                self.top.next_ptr = None
                self.top = temp1
                return temp
        elif verifikasi == 'rusak':
            print('pending')
        else:
            print('input salah')

    def printStack(self):
        '''This will print the stack'''

# ........print(self.top.data.namabarang)

        currentNode = self.top
        while currentNode is not None:
            print ('nama: ', currentNode.data.namabarang, 'kondisi: ',
                   currentNode.data.kondisibarang)
            currentNode = currentNode.next_ptr


# masukstack = Stack()
# print('sebelum')
# masukstack.printStack
# nama = 'kecap'
# kondisi = 'baik'
# masukobject = object(nama,kondisi)
# masukstack.Push(5)
# masukstack.Push(6)
# print('sesudah')
# masukstack.printStack

masukstack = Stack()
while True:
    print('''
1.tambah 
2.lihat 
3.hapus''')
    userinput = input('\nmasukkan angka: ')
    if userinput == '1':
        namabarang = input('nama barang: ')
        kondisibarang = input('kondisi barang: ')
        sementaradict = object(namabarang, kondisibarang)
        masukstack.Push(sementaradict)
    elif userinput == '2':
        masukstack.printStack()
    elif userinput == '3':
        masukstack.verifying()
