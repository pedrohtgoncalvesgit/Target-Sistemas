# Função para inverter uma string
def inverter_string(s):
    s_invertida = ''
    for i in range(len(s) - 1, -1, -1):
        s_invertida += s[i]
    return s_invertida

# Entrada de string
texto = input("Informe uma string: ")

# Inverter e exibir o resultado
texto_invertido = inverter_string(texto)
print(f"A string invertida é: {texto_invertido}")