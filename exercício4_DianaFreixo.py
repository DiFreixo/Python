""" Exercício 4 - Programação Conditional """

# Dicionário fornecido com o nome dos meses correspondentes a cada trimestre
MESES = {1:'Janeiro, Fevereiro, Março', 2:'Abril, Maio, Junho', 3:'Julho, Agosto, Setembro', 4:'Outubro, Novembro, Dezembro'}
"""
 #algumas propriedades e métodos do  tipo de dados Dicionário
print(type(MESES))
print(dir(MESES))
print(len(MESES))
print(MESES.keys())
print(MESES.values())
print(MESES.get(3))
print(MESES[1])
print(MESES.items())
"""
print(dir(MESES))
# Pede ao utlizador para introduzir o número do trimestre entre 1 e 4
trimestre = int(input("Informe o número do trimestre [1 a 4]: "))

# Verifica qual o trimestre escolhido pelo utilizador e apresenta os meses correspondentes
if trimestre == 1:
    print('Os meses correspondentes ao %iº Trimestre são: %s'%(1,MESES.get(1)))
elif trimestre == 2:
    print('Os meses correspondentes ao %iº Trimestre são: %s'%(2,MESES.get(2)))
elif trimestre == 3:
    print('Os meses correspondentes ao %iº Trimestre são: %s'%(3,MESES.get(3)))
elif trimestre == 4:
    print('Os meses correspondentes ao %iº Trimestre são: %s'%(4,MESES.get(4)))
else: # Caso o utilizador introduza um valor errado, apresenta uma msg de erro
    print("Erro!! Introduza o número do trimestre entre 1 e 4.")

