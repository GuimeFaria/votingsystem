candidatos = {}
eleitores = {}
votos = {"branco": 0, "nulo": 0}

def nome_valido(nome):
    return nome.isalpha()

def cpf_valido(cpf):
    return cpf.isdigit()

def cadastrar_candidato():
    while True:
        nome = input("Nome do candidato: ")
        if not nome_valido(nome):
            print("Escolha um nome válido, sem números.")
        else:
            break
    
    while True:
        try:
            numero = int(input("Número do candidato: "))
            if numero in candidatos:
                print("Esse número já está cadastrado.")
            else:
                candidatos[numero] = nome
                votos[numero] = 0
                print(f"Candidato {nome} cadastrado.")
                break
        except ValueError:
            print("Escolha um número válido para o candidato.")

def cadastrar_eleitor():
    while True:
        nome = input("Nome do eleitor: ")
        if not nome_valido(nome):
            print("Escolha um nome válido, sem números.")
        else:
            break

    while True:
        cpf = input("CPF do eleitor (apenas números): ")
        if not cpf_valido(cpf):
            print("CPF inválido. Digite apenas números.")
        else:
            break

    if cpf in eleitores:
        print("Eleitor já cadastrado.")
    else:
        eleitores[cpf] = {"nome": nome, "votou": False}
        print(f"Eleitor {nome} cadastrado.")

def registrar_voto():
    cpf = input("CPF do eleitor: ")
    if cpf not in eleitores:
        print("Eleitor não encontrado.")
        return
    if eleitores[cpf]["votou"]:
        print("Eleitor já votou.")
        return
    for numero, nome in candidatos.items():
        print(f"Número: {numero} | Nome: {nome}")
    print("Digite 0 para voto em branco ou qualquer outro número para voto nulo.")
    escolha = int(input("Número do candidato ou 0/1: "))
    if escolha == 0:
        votos["branco"] += 1
        print("Voto em branco.")
    elif escolha not in candidatos:
        votos["nulo"] += 1
        print("Voto nulo.")
    else:
        votos[escolha] += 1
        print(f"Voto registrado para {candidatos[escolha]}.")
    eleitores[cpf]["votou"] = True

def gerar_relatorio():
    print("Relatório final:")
    print("Votos em branco:", votos["branco"])
    print("Votos nulos:", votos["nulo"])
    for numero, nome in candidatos.items():
        print(f"Candidato {nome}: {votos[numero]} votos")

def candidato_vencedor():
    max_votos = -1
    vencedores = []
    for numero, nome in candidatos.items():
        if votos[numero] > max_votos:
            max_votos = votos[numero]
            vencedores = [nome]
        elif votos[numero] == max_votos and max_votos > 0:
            vencedores.append(nome)
    return vencedores

def sistema_votacao():
    while True:
        print("\n1. Cadastrar candidato")
        print("2. Cadastrar eleitor")
        print("3. Registrar voto")
        print("4. Gerar relatório")
        print("5. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_candidato()
        elif opcao == "2":
            cadastrar_eleitor()
        elif opcao == "3":
            registrar_voto()
        elif opcao == "4":
            gerar_relatorio()
        elif opcao == "5":
            vencedores = candidato_vencedor()
            if len(vencedores) == 1:
                print(f"O candidato {vencedores[0]} foi eleito.")
            elif len(vencedores) > 1:
                print(f"Houve um empate entre os candidatos: {', '.join(vencedores)}.")
            else:
                print("Nenhum candidato foi eleito.")
            print("Fim.")
            break
        else:
            print("Opção inválida.")

sistema_votacao()
