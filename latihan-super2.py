class Mahasiswa(object):

    def __init__(self, name, nim, jurusan):
         self.name = name
         self.nim = nim
         self.jurusan = jurusan

    def cetakInfo(self):
        print('Mahasiswa yang bernama {} dengan NIM {} adalah jurusan {}'.format(self.name, self.nim, self.jurusan))

class Fakultas(Mahasiswa):

    def __init__(self, name, nim):
        self.name = name
        self.nim = nim
        super().__init__(name, nim, "Fakultas")
        super().cetakInfo()

class TIK(Mahasiswa):

    def __init__(self, name, nim):
        self.name = name
        self.nim = nim
        super().__init__(name, nim, "TIK")
        super().cetakInfo()

class TBG(Mahasiswa):

    def __init__(self, name, nim):
        self.name = name
        self.nim = nim
        super().__init__(name, nim, "TBG")
        super().cetakInfo()



mahasiswa1 = Fakultas('Ragetha', 11907066)
mahasiswa2 = TIK('Azriel', 11907065)
mahasiswa3 = TBG('Raihan', 11807655)