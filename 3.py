import json

# Dados de faturamento em formato JSON
faturamento_diario = json.loads('{"faturamento": [100, 200, 150, 300, 0, 0, 250, 100, 0, 400]}')['faturamento']

# Filtra os dias com faturamento
faturamento_valido = [f for f in faturamento_diario if f > 0]

# Calcula o menor e maior faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Calcula a média de faturamento diário
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

# Conta os dias com faturamento acima da média
dias_acima_da_media = len([f for f in faturamento_valido if f > media_faturamento])

# Exibe os resultados
print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")