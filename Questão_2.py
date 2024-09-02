import json

def analyze_revenue(daily_revenue):
    # Remove dias com faturamento zero (ex: finais de semana e feriados)
    valid_revenue = [day for day in daily_revenue if day > 0]
    
    # Calcula o menor e maior faturamento
    min_revenue = min(valid_revenue)
    max_revenue = max(valid_revenue)
    
    # Calcula a média do faturamento diário
    average_revenue = sum(valid_revenue) / len(valid_revenue)
    
    # Conta o número de dias com faturamento acima da média
    days_above_average = len([day for day in valid_revenue if day > average_revenue])

    return min_revenue, max_revenue, days_above_average

# Carregar dados de faturamento de um arquivo JSON
with open('faturamento.json', 'r') as file:
    data = json.load(file)

# Extrair a lista de faturamento diário
daily_revenue = data["faturamento_diario"]

# Analisar o faturamento
min_revenue, max_revenue, days_above_average = analyze_revenue(daily_revenue)

# Exibir os resultados
print(f"Menor faturamento diário: R${min_revenue:.2f}")
print(f"Maior faturamento diário: R${max_revenue:.2f}")
print(f"Número de dias com faturamento acima da média: {days_above_average}")
