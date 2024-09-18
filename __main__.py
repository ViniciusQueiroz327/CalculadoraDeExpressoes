# Função para validar se a expressão é válida
def validar_expressao(expressao):
    try:
        eval(expressao)  # Tenta avaliar a expressão
        return True
    except:
        return False

# Função para calcular o resultado da expressão
def calcular(expressao):
    return eval(expressao)

# Função para ler a expressão do usuário ou de um arquivo .txt
def ler_expressao():
    opcao = input("Deseja digitar uma expressão (1) ou ler de um arquivo (2)? ")

    if opcao == "1":
        expressao = input("Digite a expressão: ")
        return expressao
    elif opcao == "2":
        try:
            with open("expressoes.txt", "r") as arquivo:
                expressao = arquivo.readline().strip()
            return expressao
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return None
    else:
        print("Opção inválida.")
        return None

# Função para salvar a expressão e o resultado em um arquivo
def salvar_resultado(expressao, resultado):
    with open("historico.txt", "a") as arquivo:
        arquivo.write(f"{expressao} = {resultado}\n")

# Função principal
def main():
    while True:
        expressao = ler_expressao()
        
        if expressao is not None:
            if validar_expressao(expressao):
                resultado = calcular(expressao)
                print("Resultado:", resultado)
                salvar_resultado(expressao, resultado)
            else:
                print("Expressão inválida.")
        
        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
