# Program Siswa

class Siswa:
    
    def __init__(self, nama, rombel):
        self.nama = nama
        self.rombel = rombel

    def cetakInfo(self):
        print("{} Adalah Rombel {}".format(self.nama, self.rombel))

class Rpl(Siswa):
    def __init__(self, nama):
        super().__init__(nama, "RPL")
        super().cetakInfo()

class Mmd(Siswa):
    def __init__(self, nama):
        super().__init__(nama, "MMD")
        super().cetakInfo()


siswa1 = Rpl("Azriel Fauzi Hermansyah")
siswa2 = Mmd("Ragetha Prameswari Kirana")
