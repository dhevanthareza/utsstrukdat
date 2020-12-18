import os 
# Membuat class untuk node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.matkul = data['matkul']
        self.nilai = data['nilai']
        self.tanggal = data['tanggal']
        self.next_node = next_node
       
# Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail= tail
            
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

    # Menampilkan isi dari list
    def showData(self):
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        current_node = self.head
        if (self.head is None):
            print("Data masih Kosong")
        else:    
            while current_node is not None:
                print ("Matkul: {}, Nilai: {}, Tanggal: {}".format(current_node.matkul, current_node.nilai, current_node.tanggal))
                print ("   -> ")
                current_node = current_node.next_node
 
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("|  Menu aplikasi pendataan nilai uts  |")
            print("===============================")
            print("1. Tambah Belakang")
            print("2. Tampil Data")
            print("3. Hapus Data ditengah")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("clear")
                matkul = str(input("Masukan Mata kuliah yang ingin anda tambahkan: "))
                nilai = str(input("Masukan nilai dari Mata kuliah tersebut (0-4): "))
                tanggal = str(input("Masukan tanggal UTS (DD/MM/YYYY): "))
                data = {
                  "matkul": matkul,
                  "nilai": nilai,
                  "tanggal": tanggal
                }
                self.tambahbelakang(data)
            elif(pilihan=="2"):
                os.system("clear")
                self.showData()
                x = input("")
            elif(pilihan=="3"):
                os.system("clear")
                self.hapusTengah()
            else:
                pilih="n"
    def hapusTengah(self):
        matkul = input("Masukan matkul yang ingin dihapus = ")
        current_node = self.head
        if(self.head is None):
            print("Data masih kosong")
        elif(current_node.matkul == matkul):
          self.head = current_node.next_node
        elif(self.tail.matkul == matkul):
          while current_node.next_node.next_node is not None:
            current_node = current_node.next_node
          current_node.next_node=None
          self.tail=current_node
        else:
            while current_node.next_node.matkul != matkul and current_node.next_node is not None:
                current_node = current_node.next_node
            if(current_node.next_node is not None):
                current_node.next_node = current_node.next_node.next_node
 
if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()
