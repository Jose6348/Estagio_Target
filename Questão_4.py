# Função para inverter uma string
def reverse_string(s):
    reversed_str = ""  # String vazia para armazenar o resultado
    for char in s:
        reversed_str = char + reversed_str  # Adiciona cada caractere no início da nova string
    return reversed_str

# Entrada da string (você pode alterar para ser entrada do usuário ou pré-definida)
input_string = input("Informe uma string: ")

# Inverter a string usando a função criada
inverted_string = reverse_string(input_string)

# Exibir a string invertida
print("String invertida:", inverted_string)
