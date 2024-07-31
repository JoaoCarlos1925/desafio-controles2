while True:
    # Solicita que o usuário digite um número
    numero = input("Digite um número para ver sua tabuada (ou 0 para sair): ")
    
    # Verifica se a entrada é um número válido
    if not numero.isdigit():
        print("Por favor, digite um número válido.")
        continue

    numero = int(numero)
    
    # Verifica se o usuário quer sair
    if numero == 0:
        print("Saindo do programa.")
        break

    # Gera e imprime a tabuada
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
