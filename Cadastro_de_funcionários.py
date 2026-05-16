"""
📌 Desafio: Cadastro de Funcionários
Crie um programa que gerencie o cadastro de funcionários de uma empresa. 
O programa deve permitir adicionar funcionários e exibir um relatório com os dados cadastrados.
"""

menu = """
 Cadastro de Funcionários 
-----------------------------------------
[1] Adicionar Funcionário
[2] Remover Funcionário
[3] Relatório de Funcionários Cadastrados
[4] Sair
------------------------------------------
"""

# Lista única para armazenar os funcionários (eliminando variáveis globais desnecessárias)
lista_funcionarios = []

def adicionar_funcionario():
    """Adiciona um novo funcionário à lista"""
    funcionario = {
        "Nome": input("Nome do funcionário: "),
        "Idade": input("Idade: "),
        "Cargo": input("Cargo: "),
        "Salário": f"R$ {input('Salário: ')}"
    }
    
    lista_funcionarios.append(funcionario)
    print(f"\n✅ Funcionário cadastrado com sucesso! (Código: {len(lista_funcionarios)})")

def remover_funcionario():
    """Remove um funcionário pelo código"""
    if not lista_funcionarios:
        print("\n⚠️ Nenhum funcionário cadastrado!")
        return
    
    exibir_relatorio()
    
    try:
        op = int(input("\nDigite o código do funcionário que deseja excluir: ")) - 1
        
        if 0 <= op < len(lista_funcionarios):
            removido = lista_funcionarios.pop(op)
            print(f"\n✅ Funcionário '{removido['Nome']}' removido com sucesso!")
        else:
            print("\n❌ Código inválido!")
    except ValueError:
        print("\n❌ Digite um número válido!")

def exibir_relatorio():
    """Exibe o relatório de funcionários cadastrados"""
    if not lista_funcionarios:
        print("\n📋 Nenhum funcionário cadastrado ainda.")
        return
    
    print(f"\n{'='*60}")
    print(" RELATÓRIO DE FUNCIONÁRIOS ".center(60, "="))
    print(f"{'='*60}")
    
    for idx, funcionario in enumerate(lista_funcionarios, 1):
        print(f"Código: {idx}")
        for chave, valor in funcionario.items():
            print(f"  {chave}: {valor}")
        print("-" * 40)
    
    print(f"📊 Total de funcionários cadastrados: {len(lista_funcionarios)}")
    print(f"{'='*60}\n")

def main():
    """Função principal do programa"""
    while True:
        opcao = input(menu).strip()
        
        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            remover_funcionario()
        elif opcao == "3":
            exibir_relatorio()
        elif opcao == "4":
            print("\n👋 Programa encerrado. Até logo!")
            break
        else:
            print("\n❌ Opção incorreta! Digite um número de 1 a 4.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()