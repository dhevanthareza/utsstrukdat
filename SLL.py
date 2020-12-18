#SINGLE LINKED LIST
#=======================================================================
 
 
import os
 
# Membuat class untuk node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
   
    # Mengambil data dari node
    def get_data(self):
        return self.data
   
    # Mengambil node berikutnya
    def get_next(self):
        return self.next_node
   
    # Menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next
       
# Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail= tail
   
    # Menambah node baru
    def tambahdepan(self, data):
        # Inisialisasi node baru
        new_node = Node(data)
        # jika head masih kosong
        if (self.head is None):
            self.head=new_node
            self.tail=new_node
        else :
            new_node.set_next(self.head)
            self.head=new_node
            
    def tambahbelakang(self, data):
        # Inisialisasi node baru
        new_node = Node(data)
        # jika head masih kosong
        if (self.head is None):
            self.head=new_node
            self.tail=new_node
        else :
            self.tail.next_node=new_node
            self.tail=new_node
            
  # Mencari sebuah data pada list
    def cari(self, data):
        # Membuat pointer baru menunjuk ke node yang ditunjuk oleh HEAD
        current = self.head
        found = False
        # Perulangan mencari node yang dicari
        while current and found is False:
            if current.get_data() == data:
                found = True
                print(current.data)
            else:
                current = current.get_next()
               
        return found

 # Menambah sebuah data ditengah pada list
    def tambahtengah(self, data):
        # Membuat pointer baru menunjuk ke node yang ditunjuk oleh HEAD
        current = self.head
        found = False
        # Perulangan mencari node yang dicari
        while current and found is False:
            if current.get_data() == data:
                found = True
                obj1 = str(input("Masukan data yang ingin anda Tambahkan: "))
                new_node = Node(obj1)
                new_node.next_node = current.next_node
                current.next_node = new_node
            else:
                current = current.get_next()
               
        return found

    # Menampilkan isi dari list
    def showData(self):
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        current_node = self.head
        if (self.head is None):
            print("Data masih Kosong")
        else:    
            while current_node is not None:
                print (current_node.data),
                print ("   ->"),
                current_node = current_node.next_node

   # Menghapus Data didepan dari list
    def deletedidepan(self):
        if (self.head is None):
            print("Data Tidak Ada")
        else:    
            self.head = self.head.next_node

    # Menghapus data belakang dari list
    def deletedibelakang(self):
        current_node = self.head
        if (self.head is None):
            print("Data masih Kosong")
        else:    
            while current_node.next_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node=self.tail.next_node
            self.tail=current_node
 
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Tambah Depan")
            print("2. Tambah Belakang")
            print("3. Mencari Data")
            print("4. Tambah Data di Tengah")
            print("5. Hapus Data didepan")
            print("6. Hapus Data dibelakang")
            print("8. Tampil Data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda tambahkan: "))
                self.tambahdepan(obj)
            elif(pilihan=="2"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda tambahkan: "))
                self.tambahbelakang(obj)
            elif(pilihan=="3"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda Cari: "))
                self.cari(obj)
            elif(pilihan=="4"):
                os.system("clear")
                obj = str(input("Tambah Data Setelah : "))
                self.tambahtengah(obj)
            elif(pilihan=="5"):
                os.system("clear")
                self.deletedidepan()
            elif(pilihan=="6"):
                os.system("clear")
                self.deletedibelakang()
            elif(pilihan=="8"):
                os.system("clear")
                self.showData()
                x = input("")
            else:
                pilih="n"
 
if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()
