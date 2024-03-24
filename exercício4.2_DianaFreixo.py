""" ----------------- Exercício 4.2 - Funções --------------- """

# Função 'trim_meses' que recebe o argumento trimestre
def trim_meses(trimestre):

    # Dicionário fornecido com o nome dos meses correspondentes a cada trimestre
    MESES = {1:'Janeiro, Fevereiro, Março', 2:'Abril, Maio, Junho', 3:'Julho, Agosto, Setembro', 4:'Outubro, Novembro, Dezembro'}

    # Uso do ciclo 'for' para iterar sobre as chaves do dicionário 'MESES'
    for chave in MESES:
        # Verifica qual o trimestre escolhido pelo utilizador e apresenta os meses correspondentes
        if trimestre == chave:
            print('Os meses correspondentes ao %iº Trimestre são: %s'%(chave,MESES.get(chave)))
            break

    # Caso o utilizador introduza um valor errado, apresenta uma msg de erro
    else: 
        print("Erro!! Introduza o número do trimestre entre 1 e 4.")


# Função 'main' recebe o número do trimestre fornecido pelo utilizador e chama a função 'trim_meses' que
# apresenta os meses do trimestre indroduzido pelo utilizador
def main():
    # Pede ao utlizador para introduzir o número do trimestre entre 1 e 4
    trimestre = int(input("Informe o número do trimestre [1 a 4]: "))

    # Chamada da função com o argumento trimestre
    trim_meses(trimestre)

# Chamada da função 'main' por onde será inicializado o programa
main()