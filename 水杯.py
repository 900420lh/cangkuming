
class cap:
    __height = 0
    __volume = 0.0
    __color = ""
    __material = ""

    def setHeight(self, height):
        self.__height = height
    def getHeight(self):
        return self.__height
    def setVolume(self, volume):
        self.__volume = volume
    def getVolume(self):
        return self.__volume
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setMaterial(self,material):
        self.__material = material
    def getMaterial(self):
        return self.__material

    def store_liquid(self):
        print(self.__color, "色的杯子能存放", self.__volume, "毫升液体")
cap = cap()
cap.setColor("白")
cap.setVolume(500)
cap.setHeight(23)
cap.setMaterial("304不锈钢")
cap.store_liquid()


print()

class laptop:
    __screen_size = 0.0
    __price = 0.00
    __cpu = ""
    __RAM = ""
    __stanby_time = 5

    def setSize(self,size):
        self.__screen_size = size
    def getSize(self):
        return self.__screen_size

    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        self.__cpu = cpu
    def getCpu(self):
        return self.__cpu

    def setRam(self,ram):
        self.__RAM = ram
    def getRam(self):
        return self.__RAM

    def setStanby_time(self,time):
        self.__stanby_time = time
    def getStanby_time(self):
        return self.__stanby_time


    def typing(self):
        print(self.__price, "元、CPU型号为", self.getCpu(), "的笔记本电脑可以打字")

    def game(self):
        print(self.__price, "元、CPU型号为", self.getCpu(), "的笔记本电脑可以打游戏")

    def video(self):
        print(self.__price, "元、CPU型号为", self.getCpu(), "的笔记本电脑可以看视频")

laptop = laptop()
laptop.setPrice(6999)
laptop.setSize(24)
laptop.setCpu("intel i7-7200")
laptop.setRam(255)
laptop.setStanby_time(6)
laptop.video()
laptop.game()
laptop.typing()



