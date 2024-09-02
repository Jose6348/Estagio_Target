def fibonacci_sequence(n):
    # Inicializa a sequência de Fibonacci com os dois primeiros números
    sequence = [0, 1]
    
    # Gera a sequência até o próximo número ser maior ou igual a 'n'
    while sequence[-1] < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    # Retorna a sequência completa
    return sequence

def is_fibonacci(n, sequence):
    # Verifica se o número está na sequência calculada
    return n in sequence

# Solicita ao usuário para inserir um número
number = int(input("Informe um número: "))

# Calcula a sequência de Fibonacci até o número informado
fib_sequence = fibonacci_sequence(number)

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci(number, fib_sequence):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

# Exibe a sequência de Fibonacci gerada
print("Sequência de Fibonacci gerada:", fib_sequence)
