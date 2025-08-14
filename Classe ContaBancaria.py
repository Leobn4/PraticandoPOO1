class ContaBancaria :
    def __init__(self,titular, saldo , numero_conta):
        self.titular = titular
        self.saldo = 0
        self.numero_conta = numero_conta
       

    def depositar(self,valor):
         self.saldo += valor

    def sacar(valor):
        self.saldo -= valor

        if self.saldo < self.sacar:
            print("Valor invalido digite um valor maior que seu saldo")
        else:
            print("Foi sacado: {self.valor} da conta")
        

    def consultar_saldo(self):
            print(self.saldo)
        
    def exibir_extrato(self):
            
            print(f"Titular:{self.titular}")
            print(f"Numero da conta:{self.numero_conta}")
            print(f"Saldo:{self.saldo}")




Conta1 = ContaBancaria ("Thiago", 2500, 5916)

Conta1.exibir_extrato()
      

