""" ----------------- Exercício 5 - Classes --------------- """

# Definição da classe Supermercado (classe mãe)
class Supermercado:
    # método construtor da classe Supermercado
    def __init__(self, produto, categoria):
        self.produto = produto
        self.categoria = categoria
        self.stock = 0
    
    # métodos da classe Supermercado
    def comprasProdutos(self, stockEntrada):
        self.stock +=  stockEntrada
        
    def vendasProdutos(self, stockSaida):
        self.stock -=  stockSaida
        
    def imprimirRelatorio(self):
       print(self.produto, "\t", self.categoria, "\t", self.stock)
     

# Definição da classe Produtos filha da classe Supermercado
class Produtos(Supermercado):
    # método construtor da classe Produtos
    def __init__(self, produto, categoria, tipo, marca):
        # Com a função super chamamos o construtor da classe Supermercado
        super().__init__(produto, categoria)
        self.tipo = tipo
        self.marca = marca
        self.stock = 0
        self.situacao = ""

    # métodos da classe Produtos
    def controloStock(self):
        if(self.stock == 0):
            self.situacao = "Vermelho"
        elif(self.stock <= 10):
            self.situacao = "Amarelo"
        else:
            self.situacao = "Verde"
        return self.situacao
    
    def imprimirRelatorio(self):
        print(self.produto, "\t", self.categoria, "   ", self.tipo, "\t", self.marca, "\t  ", self.stock,  "\t", self.controloStock())

# Definição da função 'main' aonde serão instanciados os objetos das classes
def main():
    # instanciar os objetos da classe Supermercado
    produto1 = Supermercado("Arroz", "Mercearia")
    produto2 = Supermercado("Massa", "Mercearia")
    produto3 = Supermercado("Atum", "Mercearia")
    produto4 = Supermercado("Maçã", "Frutas")
    produto5 = Supermercado("Pepino", "Legumes")
    
    # chamada do método imprimirRelatorio da classe Supermercado
    print("\n*** Listagem de Produtos ***")
    print("Produto   Categoria    Stock")
    print("-----------------------------")
    produto1.imprimirRelatorio()
    produto2.imprimirRelatorio()
    produto3.imprimirRelatorio()
    produto4.imprimirRelatorio()
    produto5.imprimirRelatorio()
    print("-----------------------------") 
    print("*** Fim da listagem ***\n")

    # Alterar os objetos da classe Supermercado
    produto1.comprasProdutos(10)
    produto4.comprasProdutos(50)
    produto5.comprasProdutos(20)
    produto4.vendasProdutos(23)

    # chamada do método imprimirRelatorio da classe Supermercado
    print("\n*** Listagem de Produtos ***")
    print("Produto   Categoria    Stock")
    print("-----------------------------")
    produto1.imprimirRelatorio()
    produto2.imprimirRelatorio()
    produto3.imprimirRelatorio()
    produto4.imprimirRelatorio()
    produto5.imprimirRelatorio()
    print("-----------------------------")
    print("*** Fim da listagem ***\n")

    print("------------------------------------------------------------------------")
    # instanciar os objetos da classe Produtos
    produto6 = Produtos("Arroz", "Mercearia", "Agulha", "Rice")
    produto7 = Produtos("Maçã", "Frutas", "Verde", "Apple")
    
    # chamada do método imprimirRelatorio da classe Produtos
    print("\n*** Listagem de Produtos ***")
    print("Produto  Categoria   Tipo       Marca     Stock  Situação")
    print("----------------------------------------------------------")
    produto6.imprimirRelatorio()
    produto7.imprimirRelatorio()
    print("----------------------------------------------------------")
    print("*** Fim da listagem ***\n")

    # Alterar os objetos da classe Produtos
    produto6.comprasProdutos(23)
    produto7.comprasProdutos(20)
    produto6.vendasProdutos(14)

    # chamada do método imprimirRelatorio da classe Produtos
    print("\n*** Listagem de Produtos ***")
    print("Produto  Categoria   Tipo       Marca     Stock  Situação")
    print("----------------------------------------------------------")
    produto6.imprimirRelatorio()
    produto7.imprimirRelatorio()
    print("----------------------------------------------------------")
    print("*** Fim da listagem ***\n")


# Chamada da função 'main' por onde será inicializado o programa
main()
