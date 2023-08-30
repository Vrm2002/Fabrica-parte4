class Calculadora():


    def calcular(self, op):
        if op == "Adição":
            result = self.__adicionar()
            return result


        elif op == "Subtrair":
            result = self.__subtrair()
            return result


    def __adicionar(self):

        a = int(input("Primeiro número: "))

        b = int(input("Segundo número: "))

        c = a+b

        return c


    def __subtrair(self):

        a = int(input("Primeiro número: "))

        b = int(input("Segundo número: "))

        c = a-b

        return c


a = input("Digite a sua operação para ser realizada: ")

conta = Calculadora()

print(conta.calcular(a))