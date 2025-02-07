# Faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento_estados.values())

# Cálculo do percentual de cada estado
percentuais = {estado: (faturamento / faturamento_total) * 100 for estado, faturamento in faturamento_estados.items()}

# Exibe os percentuais
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")