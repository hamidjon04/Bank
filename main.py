from bank import Bank
from mijoz import Mijoz


bank = Bank("Najot bank")

m1 = Mijoz("Doston", "+998944040244")
m2 = Mijoz("Sardor", "+998978562454")
m3 = Mijoz("Eldor", "+998932200409")

bank.account(m1)
bank.bankInfo()