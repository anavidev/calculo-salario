import pandas as pd

pd.options.display.float_format = '{:.2f}'.format



### salario liquido com descontos obrigatorios ###

print("--- Descontos obrigatórios ---\n\n")

desconto_obrigatorio = pd.DataFrame({
    "Meses": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Salario_Bruto": 10000.00,
    "INSS": 14,
    "IRRF": 27.5,
    "FGTS": 8
})

print("Tabela com valores definidos (R$)\nOBS: Os valores de 'INSS', 'IRRF' e 'FGTS' estão em %\n")
print(desconto_obrigatorio)
print("\n\n")

# calculo do inss
desconto_obrigatorio["Desconto_INSS"] = 105.90 + 99.22 + 160.00 + 433.86

# calculo do irrf
desconto_obrigatorio["Desconto_IRRF"] = (desconto_obrigatorio["Salario_Bruto"] - desconto_obrigatorio["Desconto_INSS"]) * (desconto_obrigatorio["IRRF"] / 100) - 896

# calculo do fgts
desconto_obrigatorio["Desconto_FGTS"] = desconto_obrigatorio["Salario_Bruto"] * (desconto_obrigatorio["FGTS"] / 100)

# calculo do salario liquido
desconto_obrigatorio["Salario_Liquido"] = desconto_obrigatorio["Salario_Bruto"] - (desconto_obrigatorio["Desconto_INSS"] + desconto_obrigatorio["Desconto_IRRF"])

print("Tabela com os descontos aplicados\nOBS: O valor do 'Desconto_FGTS' não foi considerado no cálculo do salário líquido\n")
print(desconto_obrigatorio)

# gasto total para a empresa
total_empresa = (desconto_obrigatorio["Salario_Bruto"].iloc[0] + desconto_obrigatorio["Desconto_INSS"].iloc[0] + desconto_obrigatorio["Desconto_IRRF"].iloc[0] + desconto_obrigatorio["Desconto_FGTS"].iloc[0]) * 12

print(f'\nGasto total para a empresa: R${total_empresa:.2f}')

print("\n\n\n")


### salario liquido com descontos obrigatorios + extras ###

print("--- Descontos obrigatórios + extras ---\n\n")

desconto_extra = pd.DataFrame({
    "Meses": desconto_obrigatorio["Meses"],
    "Salario_Bruto": desconto_obrigatorio["Salario_Bruto"],
    "Descontos_Obrigatorios": desconto_obrigatorio["Desconto_INSS"] + desconto_obrigatorio["Desconto_IRRF"],
    "Desconto_FGTS": desconto_obrigatorio["Desconto_FGTS"],
    "Plano_Saude_Completo": 1500.00
})

print("Tabela com valores definidos (R$)\nOBS: 'Descontos_Obrigatorios' == Valor do INSS + Valor do IRRF\n")
print(desconto_extra)
print("\n\n")

# calculo da parte do plano de saude
desconto_extra["Parte_Plano_Saude"] = desconto_extra["Plano_Saude_Completo"] * 0.5

# calculo da primeira parcela do 13º salario
desconto_extra["13_Salario_1"] = desconto_extra.apply(
    lambda row: row["Salario_Bruto"] / 2 
    if row["Meses"] == "Nov" else 0.00,
    axis = 1
)

# calculo da segunda parcela do 13º salario
desconto_extra["13_Salario_2"] = desconto_extra.apply(
    lambda row: row["Salario_Bruto"] / 2 - row["Descontos_Obrigatorios"]
    if row["Meses"] == "Dez" else 0.00,
    axis=1
)

# calculo de salario de ferias
desconto_inss = desconto_obrigatorio["Desconto_INSS"].iloc[0]
desconto_irrf = desconto_obrigatorio["Desconto_IRRF"].iloc[0]
desconto_extra["Ferias"] = desconto_extra.apply(
    lambda row: row["Salario_Bruto"] / 3 - (desconto_inss + desconto_irrf)
    if row["Meses"] == "Ago" else 0.00,
    axis = 1
)

# calculo do salario liquido
desconto_extra["Salario_Liquido"] = desconto_extra.apply(
    lambda row: row["Salario_Bruto"] - (row["Descontos_Obrigatorios"] + row["Parte_Plano_Saude"]) + (row["13_Salario_1"] + row["13_Salario_2"] + row["Ferias"])
    if row["Meses"] != "Ago" else row["Ferias"] + row["Salario_Bruto"],
    axis = 1
)

print("Tabela com os descontos aplicados\nOBS: O valor do 'Desconto_FGTS' não foi considerado no cálculo do salário líquido\n")
print(desconto_extra)

# gasto total para a empresa
total_empresa = (desconto_extra["Salario_Bruto"].iloc[0] * 9) + ((desconto_extra["Descontos_Obrigatorios"].iloc[0] + desconto_extra["Parte_Plano_Saude"].iloc[0] + desconto_extra["Desconto_FGTS"].iloc[0]) * 12) + (desconto_extra["Salario_Liquido"].iloc[10] + desconto_extra["Salario_Liquido"].iloc[11] + desconto_extra["Salario_Liquido"].iloc[7])

print(f'\nGasto total para a empresa: R${total_empresa:.2f}')


### salvar dataframes ###
desconto_obrigatorio.to_csv("outputs/desconto_obrigatorio.csv", float_format='%.2f', index=False)
desconto_extra.to_csv("outputs/desconto_extra.csv", float_format='%.2f', index=False)