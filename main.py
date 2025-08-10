import database

def clear_screen():
    """Limpa a tela do console (funciona em Windows, Mac e Linux)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_hardware(hardware):
    """Função auxiliar para exibir os dados de hardware de forma formatada."""
    print(f"ID: {hardware[0]}")
    print(f"  Nome: {hardware[1]}")
    print(f"  Tipo: {hardware[2]}")
    print(f"  Modelo: {hardware[3]}")
    print(f"  Nº Série: {hardware[4]}")
    print(f"  Status: {hardware[5]}")
    print(f"  Localização: {hardware[6]}")

def menu_hardware():
    while True:
        clear_screen()
        print("--- Gerenciamento de Hardware ---")
        print("1. Adicionar Hardware")
        print("2. Listar Hardware")
        print("3. Atualizar Status de Hardware")
        print("4. Deletar Hardware")
        print("5. Gerenciar Software de um Hardware")
        print("6. Voltar ao menu principal")
        
        choice = input("Escolha uma opção: ")

        if choice == '1':
            nome = input("Nome (ex: PC Sala A): ")
            tipo = input("Tipo (ex: Desktop, Notebook): ")
            modelo = input("Modelo: ")
            numero_serie = input("Número de Série: ")
            status = input("Status (ex: Em uso, Em manutenção): ")
            localizacao = input("Localização: ")
            database.add_hardware(nome, tipo, modelo, numero_serie, status, localizacao)
            input("Pressione Enter para continuar...")
        
        elif choice == '2':
            hardware_list = database.get_all_hardware()
            clear_screen()
            print("--- Inventário de Hardware ---")
            if not hardware_list:
                print("Nenhum hardware encontrado.")
            else:
                for item in hardware_list:
                    print_hardware(item)
                    print("-" * 20)
            input("Pressione Enter para continuar...")
        
        elif choice == '3':
            hardware_id = input("Digite o ID do hardware para atualizar o status: ")
            new_status = input("Digite o novo status: ")
            if database.find_hardware_by_id(hardware_id):
                database.update_hardware_status(hardware_id, new_status)
                print("Status atualizado com sucesso!")
            else:
                print("Hardware não encontrado.")
            input("Pressione Enter para continuar...")
        
        elif choice == '4':
            hardware_id = input("Digite o ID do hardware para deletar: ")
            if database.find_hardware_by_id(hardware_id):
                database.delete_hardware(hardware_id)
                print("Hardware e softwares associados deletados com sucesso.")
            else:
                print("Hardware não encontrado.")
            input("Pressione Enter para continuar...")
        
        elif choice == '5':
            menu_software()
        
        elif choice == '6':
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")

def menu_software():
    while True:
        clear_screen()
        print("--- Gerenciamento de Software ---")
        hardware_id = input("Digite o ID do hardware para gerenciar o software (ou 'voltar'): ")
        if hardware_id.lower() == 'voltar':
            break

        hardware_item = database.find_hardware_by_id(hardware_id)
        if not hardware_item:
            print("Hardware não encontrado.")
            input("Pressione Enter para continuar...")
            continue
        
        clear_screen()
        print(f"Gerenciando software para o hardware: {hardware_item[1]} (ID: {hardware_id})")
        print("1. Adicionar Software")
        print("2. Listar Softwares")
        print("3. Deletar Software")
        print("4. Voltar ao menu anterior")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            nome_software = input("Nome do Software: ")
            versao = input("Versão: ")
            chave_licenca = input("Chave de Licença: ")
            database.add_software(nome_software, versao, chave_licenca, hardware_id)
            input("Pressione Enter para continuar...")
        
        elif choice == '2':
            software_list = database.get_software_for_hardware(hardware_id)
            if not software_list:
                print("Nenhum software encontrado para este hardware.")
            else:
                for software in software_list:
                    print(f"  ID: {software[0]} - Nome: {software[1]} (Versão: {software[2]}, Chave: {software[3]})")
            input("Pressione Enter para continuar...")
        
        elif choice == '3':
            software_id = input("Digite o ID do software para deletar: ")
            database.delete_software(software_id)
            print("Software deletado com sucesso.")
            input("Pressione Enter para continuar...")

        elif choice == '4':
            break

def main():
    """Função principal do sistema."""
    database.setup_database()
    while True:
        clear_screen()
        print("--- Sistema de Gerenciamento de Inventário ---")
        print("1. Gerenciar Hardware")
        print("2. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == '1':
            menu_hardware()
        elif choice == '2':
            print("Saindo do sistema. Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()