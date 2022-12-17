class stack: #membuat class dengan objek stack
    def __init__(self): #membuat fungsi init
        s = int(input("masukkan kapasitas container(kg): ")) #input s untuk memasukkan ukuran stack
        self.size = s #variabel untuk size stack/container
        self.current_size = 0 #variabel untuk current size stack
        self.data = []; #variabel untuk isi stack
        print("container dengan kapasitas", s, "telah diatur")

    # def setsize(self, n): #fungsi setsize
    #     self.size = n #variabel self.size = n

    def getsize(self): #fungsi getsize
        return self.size #mengembalikan nilai self.size

    # def setcurrentsize(self, n): #fungsi setcurrentsize
    #     self.current_size = n # variabel self.current_size = n

    def getcurrentsize(self):
        return self.current_size #mengembalikan nilai self.current_size

    def isempty(self): #fungsi isempty
        if self.getcurrentsize() == 0: #jika self.getcurrentsize itu 0
            return True #jika iya maka return true
        else:
            return False #jika tidak retun false

    def isfull(self):
        if self.getcurrentsize() >= self.getsize():
            return True
        else:
            return False

    def push(self):
        if not self.isfull(): #jika isfull bernilai false
            kode = input('kode barang: ')
            berat = int(input('berat barang (kg): '))
            if self.size >= self.current_size + berat:
                self.data.append({
                    'kode':kode,
                    'berat':berat,
                }) #menambahkan isi ke stack
                self.current_size += berat
                print("\n=================================================")
                print("data berhasil dimasukkan ke dalam stack |")
                print("\n===============================================")
            else:
                print("barang melebihi kapasitas")
            # self.setcurrentsize(self.getcurrentsize() + berat) #menambah berat barang ke self.current_size
            

        else:
            print("\n=================================================")
            print("stack penuh, data tidak dapat di push (OVERFLOW)   |")
            print("\n===============================================")

    def pop(self):
        if not self.isempty(): #jika fungsi isempty bernilai false
            self.current_size -= self.data[-1]['berat'] #mengurangi 1 dari self.current_size
            print("\n=================================================")
            print("kode barang: ", self.data[-1]['kode'], '\nberat: ', self.data[-1]['berat'], "kg \nberhasil dikeluarkan dari stack   |")
            print("\n===============================================")
            self.data.pop() #menghapus isi stack yang terakhir di input

        else: #jika fungsi isempty bernilai true
            print("\n=================================================")
            print("stack kosong, tidak ada data yang dapat di pop (UNDERFLOW)   |")
            print("\n===============================================")

    def print(self):
            print("\n=================================================")
            print("|\t\t LIST DATA BARANG \t\t|")
            print("=================================================")
            # for i in range (self.getcurrentsize()-1, -1, -1):
            # if self.getcurrentsize == 0:
            if self.current_size == 0:
                # if i == self.getcurrentsize():
                print('TIDAK ADA BARANG')
            else: 
                # for i in range (self.getcurrentsize()-1, -1, -1):
                for i in range(len(self.data)):
                    print('|\t', 'kode: ', self.data[i]['kode'], 'berat: ', self.data[i]['berat'], 'kg' , '\t|')
            print ("================================================")
                

    def menu(self):
        print("------------------------------------------")
        print("            Data Barang Terbaru           ")
        print("------------------------------------------")
        print("1. Melihat Data Barang                    ")
        print("2. Menambah Data Barang                   ")
        print("3. Menghapus Data Barang                  ")
        print("4. Keluar dari Program                    ")
        print("------------------------------------------")

        pilih = input("\nMasukkan Menu yang ingin diinginkan: ")

        if pilih == '1':
            self.print()
            input ("\nTekan [Enter] Untuk Kembali Ke Menu....")
            self.menu()
        
        elif pilih == '2':
            self.push()
            input ("\nTekan [Enter] Untuk Kembali Ke Menu....")
            self.menu()
        
        elif pilih == '3':
            self.pop()
            input ("\nTekan [Enter] Untuk Kembali Ke Menu....")
            self.menu()

        elif pilih == '4':
            exit()

        else:
            print("Pilih menu 1, 2, 3, atau 4")
        
        input("Tekan enter untuk melanjutkan")

my = stack()
my.menu()