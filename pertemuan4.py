class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        self.no = no

        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.saldo = saldo


Ibra = BankAccount("1234567890", 1000)
Ibro = BankAccount("1234567890", -1000)