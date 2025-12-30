# 1) Solicita ao usuário que digite seu nome
nome = input("insira seu nome:")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float((input("insira seu salario:")))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("insira o valor do seu bonus:"))
# 4) Calcule o valor do bônus final
bonus_final = (bonus/salario) * 100
# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print("olá", nome, "seu salário é de:", salario, "seu bonus é", bonus_final)
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Possíveis bugs e riscos:
# - Não há validação de entrada para garantir que o salário não seja zero, o que    
#   causaria uma divisão por zero ao calcular o KPI.
# - Não há tratamento de exceções para entradas inválidas (por exemplo, se o usuário



