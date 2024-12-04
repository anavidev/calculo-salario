**Status do Projeto:** Em Desenvolvimento 🚧  

# Cálculo de Salário
Aplicação que calcula o salário líquido fictício de um funcionário e determina o custo total dele para a empresa durante 1 ano. O objetivo do algoritmo é simular cenários financeiros utilizando as principais regras trabalhistas brasileiras de 2024.

## Funcionalidades  

- **Cálculo do Salário Líquido:** Com base no salário bruto, considerando descontos obrigatórios e opcionais.  
- **Cálculo do Custo Anual para a Empresa:** Inclui 13º salário, férias, FGTS e outros encargos trabalhistas.

## Conceitos de programação
- **Variáveis:** Armazenamento de valores para cálculos, como salário bruto, descontos e deduções.  
- **Estruturas de Controle:** Utilização de condicionais para adaptar cálculos com base em diferentes condições.  
- **Bibliotecas:** Uso do Pandas para manipular dados e facilitar cálculos.

## Tecnologias Utilizadas
- **Python:** Linguagem principal para desenvolver a lógica do algoritmo.
- **Pandas:** Biblioteca para manipulação de dados, permitindo maior flexibilidade nos cálculos.

## Fórmulas Utilizadas

**OBS:** Todos os cálculos seguem as regras estabelecidas para o ano de 2024.

- **Salário Líquido:** Salário Bruto - Descontos
- **INSS:** Calculado com alíquotas progressivas, aplicadas por faixa salarial, considerando possíveis deduções e limites.
- **IRRF:** Calculado sobre a base de cálculo (Salário Bruto - INSS), utilizando as alíquotas progressivas e deduções previstas na tabela.
- **FGTS:** Salário Bruto * 0.08
- **1ª Parcela do 13º Salário:** Salário Bruto * 0.5
- **2ª Parcela do 13º Salário:** Salário Bruto * 0.5 - (INSS + IRRF)
- **Salário de Férias:** (Salário Bruto + Salário Bruto / 3) - (INSS + IRRF)
- **Plano de Saúde:** Valor variável de acordo com o acordo entre funcionário e empresa.

## Possíveis Melhorias Futuras  

- **Adição de mais descontos extras para cálculo do salário líquido:** Incluindo vale-transporte e outros benefícios/descontos.  
- **Criação de gráficos:** Uso das bibliotecas Matplotlib e Seaborn para apresentar a distribuição de custos e rendimentos.  
- **Exportação de Dados:** Permitir que os resultados sejam exportados para arquivos CSV ou Excel.