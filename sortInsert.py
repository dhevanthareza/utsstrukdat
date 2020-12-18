# SINGLE LINKED LIST (Sort Insert)
# =======================================================================
# Dhevan Muhamad Anthareza
# A11.2019.12293
 
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
    def sortInsert(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            if(current_node.data > data):
                self.head = new_node
                self.head.next_node = current_node
                return
            while current_node.next_node is not None and current_node.next_node.data < data:
                current_node = current_node.next_node
            bigger_node = current_node.next_node
            current_node.next_node = new_node
            current_node.next_node.next_node = bigger_node
            if(bigger_node is None): 
                self.tail = new_node
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
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Tambah Secara Urut")
            print("2. Tampil Data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("clear")
                obj = int(input("Masukan data yang ingin anda tambahkan: "))
                self.sortInsert(obj)
            elif(pilihan=="2"):
                os.system("clear")
                self.showData()
                x = input("")
            else:
                pilih="n"
 
if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()
