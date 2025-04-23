'''
nome = input("Qual é o seu nome? ")
senha = input("Digite uma senha: ")

while nome == senha:
    print("Sua SENHA não pode ser igual o seu NOME 😡🤬👹")
    nome = input("Qual é o seu nome? ")
    senha = input("Digite uma senha: ")

print("Cadastrado 😍😘🥰") '''

#Professor

senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
tentativas = 1

while senha != senha_cadastrada and tentativas < 3:
    print(f"Invalido, só mais {3-tentativas} tentativas")
    senha = input("Diga sua senha: ")