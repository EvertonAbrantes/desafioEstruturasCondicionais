salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

if salario_atual <= 2800:
    percentual_aumento = 20
elif salario_atual <= 7000:
    percentual_aumento = 15
elif salario_atual <= 15000:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + valor_aumento

aumento_ajustado_inflacao = valor_aumento - (0.038 * novo_salario)

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o reajuste: R$ {novo_salario:.2f}")
print(f"Valor real do aumento considerando a inflação de 3.8%: R$ {aumento_ajustado_inflacao:.2f}")