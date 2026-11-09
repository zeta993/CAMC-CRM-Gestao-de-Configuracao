def cadastrar_cliente(nome, telefone):
    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    print("Cliente cadastrado com sucesso!")
    print(cliente)


cadastrar_cliente("Cliente Teste", "(22) 99999-9999")