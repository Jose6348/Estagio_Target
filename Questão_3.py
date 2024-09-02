# Valores de faturamento mensal por estado
revenue_by_state = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
total_revenue = sum(revenue_by_state.values())

# Calcula e imprime o percentual de cada estado
for state, revenue in revenue_by_state.items():
    percentage = (revenue / total_revenue) * 100
    print(f"{state}: {percentage:.2f}%")
