from mijoz import Mijoz
class Bank:
    def __init__(self, name):
        self.name = name
        self.location = "Chilonzor"
        self.tel = "+998977075544"
        self.__summa = 1000000000


    def account(self, mijoz):
        print(f"{mijoz.name} accountingizga kirish uchun quyidagi oynalarni to'ldiring: ")
        Id = int(input("ID: "))
        Tel = input("Tel: ")
        if Id == mijoz.ID and Tel == mijoz.nomer:
            self.__checkbox(mijoz)
        else: 
            print("Ma'lumotlar xato kiritildi.")
            buyruq = int(input("""
1 - Qayta urunish        2 - Yangi account ochish
3 - Chiqish
>>> """))
            if buyruq == 1:
                self.account(mijoz)
            elif buyruq == 2:
                self.__checkbox(Mijoz(input("Name: "), input("Tel: ")))
            elif buyruq == 3:
                exit()


    def __checkbox(self, mijoz):
        buyruq = int(input("""
1 - Info                       2 - Depozit (10%)
3 - To'lov                     4 - Pul o'tkazish
5 - Hisobdan o'zgartirish      6 - Kredit  (20%)
7 - Kreditni so'ndirish        8 - Chiqish
>>> """))
        if buyruq == 1: 
            self.__info(mijoz)
        elif buyruq == 2:
            self.__depozit(mijoz)
        elif buyruq == 3:
            self.__tolov(mijoz)
        elif buyruq == 4:
            self.__tolov(mijoz)
        elif buyruq == 5:
            self.__setBalans(mijoz)
        elif buyruq == 6:
            self.__kredit(mijoz)
        elif buyruq == 7:
            self.returnKredit(mijoz)
        elif buyruq == 8:
            print("Najot bank xizmatlaridan foydalanganingiz uchun tashakkur.")
            exit()

    def __info(self, mijoz):
        print(f"""
ID: {mijoz.ID}
Name: {mijoz.name}
Tel: {mijoz.nomer}
Balance: {mijoz.getBalance()}
Kredit: {mijoz.kredit}""")
        self.func(mijoz)
        

    def __depozit(self, mijoz):
        depozit = int(input("Summa: "))
        self.__summa += depozit
        mijoz.depozit(depozit)
        print("Depozitingiz muvaffaqiyatli qo'yildi.")
        self.func(mijoz)

    def __kredit(self, mijoz):
        kredit = int(input("Summa: "))
        if mijoz.kredit >= 500000000:
            print("Kreditingiz juda ham ko'p, avval ularni qaytaring.")
            return
        self.__summa -= kredit
        mijoz.setBalance(kredit)
        mijoz.kredit += kredit * 1.2
        print("Kreditingiz muvaffaqiyatli rasmiylashtirildi.")
        self.func(mijoz)


    def returnKredit(self, mijoz):
        print(f"Kridetingiz miqdori: {mijoz.kredit}")
        summa = int(input("Summa: "))
        if summa <= mijoz.getBalance():
            if summa <= mijoz.kredit:
                mijoz.setBalance(-summa)
                mijoz.kredit -= summa
                self.__summa += summa
                print("Kreditingiz muvaffaqiyatli so'ndirildi.")
            else:
                print("Kreditingiz miqdori kamroq, qayta urunib ko'ring.")
        else: 
            print("Hisobingizda pul yetarli emas, qayta urunib ko'ring.")
        self.func(mijoz)

    def __setBalans(self, mijoz):
        buyruq = int(input("""
1 - To'ldirish        2 - Pul olish
>>> """))
        summa = int(input("Summa: "))
        if buyruq == 1:
            mijoz.setBalance(summa)
            self.__summa += summa
        elif buyruq == 2:
            if summa > mijoz.getBalance():
               print("Hisobingizda pul yetarli emas.")
               self.func(mijoz)
               return
            mijoz.setBalance(-summa)
            self.__summa -= summa
            print("Pul mablag'i muvaffaqiyatli yechildi.")
        self.func(mijoz)
            


    def __tolov(self, mijoz):
        summa = int(input("Summa: "))
        if summa > mijoz.getBalance():
            print("Hisobingizda pul yetarli emas.")
            self.func(mijoz)
            return
        self.__summa -= summa
        mijoz.setBalance(-summa)
        print("To'lov muvaffaqiyatli amalga oshirildi.")
        self.func(mijoz)

        
    def __transfer(self, mijoz):
        summa = int(input("Summa: "))
        if summa > mijoz.getBalance():
            print("Hisobingizda pul yetarli emas.")
            self.func(mijoz)
            return
        self.__summa -= summa
        mijoz.setBalance(-summa)
        print("Pul o'tkazmasi muvaffaqiyatli amalga oshirildi.")
        self.func(mijoz)

    def func(self, mijoz):
        buyruq = int(input("""
1 - ortga        2 - chiqish
>>> """))
        if buyruq == 1:
            self.__checkbox(mijoz)
        elif buyruq == 2:
            print("Najot bank xizmatlaridan foydalanganingiz uchun tashakkur.")
            exit()

    def bankInfo(self):
        return f"""
Name: {self.name}
Location: {self.location}
Tel: {self.location}
Balance: {self.__summa}"""