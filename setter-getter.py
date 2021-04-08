class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "Name {} : \n\tHealth : {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di hapus')
        self.__armor = None


sniper = Hero('Azriel',  100, 50)

print('Merubah info')
print(sniper.info)
sniper.name = 'ragetha'
print(sniper.info)

print('getter dan setter untuk __armor : ')
print(sniper.armor)

print('delete armor')
del sniper.armor
print(sniper.__dict__)
