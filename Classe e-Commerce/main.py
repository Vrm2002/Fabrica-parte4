from CarrinhoDeCompras import CarrinhoDeCompras
from Produto import Produto

produto = Produto("Banana", 2000)
produto2 = Produto("Maçã", 5000)
carrinho = CarrinhoDeCompras()
carrinho.inserir_produto(produto)
carrinho.inserir_produto(produto2)
carrinho.lista_produto()
carrinho.soma_total()