texto = "Alele"
try:
    with open('C:\\Users\\Darth Kaida\\Desktop\\Programação\\Python\\Projeto Museu\\RegistroDeEmprestimos.txt', 'a') as file:
        file.write(texto)
except FileNotFoundError:
    print("Error: O Arquivo Não Foi Encontrado, Verifique o Caminho Manualmente.")