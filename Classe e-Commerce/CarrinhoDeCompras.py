class CarrinhoDeCompras():
    def __init__(self) -> None:
        
        self.produtos = []


    def inserir_produto(self, produto: str) -> None:
        self.produtos.append(produto)


    def lista_produto(self) -> None:
        for i in self.produtos:
            print(i)


    def soma_total(self) -> float:
        soma_total = sum(self.produtos)
        return soma_total
    
