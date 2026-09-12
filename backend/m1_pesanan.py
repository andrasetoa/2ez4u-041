class Pesanan:
    def __init__(self, oid, pelanggan, resto, menu, harga, prioritas, t_masuk_detik, t_selesai_detik, status):
        self.oid = oid
        self.pelanggan = pelanggan
        self.resto = resto
        self.menu = menu
        self.harga = harga
        self.prioritas = prioritas
        self.t_masuk_detik = t_masuk_detik
        self.t_selesai_detik = t_selesai_detik
        self.status = status
        
class Array:
    def __init__(self):
        self.data = []
        
    def append(self, item):
        pass
        self.data.append(item)
        #todo logika append
    def insert(self,item, index):
        pass
        #todo logika insert
    def delete(self, index):
        pass
        #todo logika delete
        
    def get(self, index):
        pass
        return self.data[index]
        #todo logika get
        
        
#todo membuat class node untuk linklist, belum tau fungsinya
        
class Linklist:
    def __init__(self):
        self.head = None
    
    def append(self, item):
        pass
        #todo logika append
    def insert(self, item, index):
        pass
        #todo logika insert
    def delete(self, index):
        pass
        #todo logika delete
    def get(self, index):
        pass
        #todo logika get
        
        
    