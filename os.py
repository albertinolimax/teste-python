# Função para adicionar uma nova ordem de serviço
def adicionar_ordem(ordens, numero, descricao):
    ordens[numero] = descricao
    print(f"Ordem de serviço {numero} adicionada com sucesso!")

# Função para exibir todas as ordens de serviço
def exibir_ordens(ordens):
    if not ordens:
        print("Não há ordens de serviço registradas.")
    else:
        print("Lista de Ordens de Serviço:")
        for numero, descricao in ordens.items():
            print(f"Número: {numero} - Descrição: {descricao}")

# Dicionário para armazenar as ordens de serviço (número como chave e descrição como valor)
ordens_de_servico = {}

while True:
    print("\n=== Menu ===")
    print("1. Adicionar Ordem de Serviço")
    print("2. Exibir Ordens de Serviço")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        numero_os = input("Digite o número da ordem de serviço: ")
        descricao_os = input("Digite a descrição da ordem de serviço: ")
        adicionar_ordem(ordens_de_servico, numero_os, descricao_os)
    elif escolha == "2":
        exibir_ordens(ordens_de_servico)
    elif escolha == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
