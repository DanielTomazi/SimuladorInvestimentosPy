# -*- coding: utf-8 -*-
"""DANIEL TOMAZI DE OLIVEIRA - ATIVIDADE_AG_ALUNOS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1saVcO3bgodNgTeMxI2GLjfiujinnxRrH

# ATIVIDADE 05 - AG Aplicado a Investimentos

O **retorno de investimentos** é um tema crucial para qualquer pessoa ou instituição que deseje fazer seu dinheiro crescer ao longo do tempo. O retorno de um investimento é a quantia de dinheiro que se espera receber em relação ao valor inicialmente investido. Esse retorno pode vir na forma de juros, dividendos, valorização de ativos, ou qualquer outra forma de lucro gerado pelo investimento.

No entanto, ao buscar um retorno mais alto, é importante considerar os riscos envolvidos. O risco de um investimento é a probabilidade de que o retorno real seja diferente do retorno esperado. Em outras palavras, é a possibilidade de perder parte ou todo o dinheiro investido.

Existem diferentes tipos de riscos associados aos investimentos, e é importante entendê-los para tomar decisões informadas. Alguns dos principais tipos de riscos incluem:

* **Risco de Mercado**: Refere-se à possibilidade de perdas devido a flutuações nos mercados financeiros, como variações nos preços das ações, taxas de juros, taxas de câmbio, entre outros.

* **Risco de Crédito**: É o risco de que a instituição financeira ou empresa na qual você investiu não consiga cumprir suas obrigações financeiras, resultando em perdas para o investidor.

* **Risco de Liquidez**: Refere-se à dificuldade de vender um investimento rapidamente sem afetar seu preço de mercado. Investimentos menos líquidos podem apresentar maior risco de perda.

* **Risco de Inflação**: É o risco de que a taxa de inflação seja maior do que a taxa de retorno do investimento, reduzindo assim o poder de compra do dinheiro investido.

* **Risco de Concentração**: Refere-se ao risco de investir em apenas um ou alguns poucos ativos, setores ou regiões geográficas, aumentando a exposição a eventos específicos que possam afetar esses investimentos.

Para lidar com os riscos, os investidores geralmente buscam diversificar suas carteiras, investindo em diferentes tipos de ativos e em diferentes setores da economia. Dessa forma, se um investimento não performar bem, outros investimentos podem compensar as perdas.

Em resumo, entender o retorno de investimentos e os riscos associados é fundamental para construir uma estratégia de investimento sólida e alcançar os objetivos financeiros de longo prazo. É importante buscar aconselhamento financeiro profissional e realizar uma análise cuidadosa antes de tomar decisões de investimento.


## TIPOS DE INVESTIMENTOS

* **Ações**: Investir em ações significa comprar parte de uma empresa e se tornar um acionista. O retorno vem na forma de valorização das ações e pagamento de dividendos.

* **Títulos públicos**: São investimentos de baixo risco, nos quais você empresta dinheiro para o governo e recebe juros em troca.

* **Títulos privados (debêntures e CDBs)**: Semelhantes aos títulos públicos, mas emitidos por empresas privadas. As debêntures são títulos de dívida de empresas e os CDBs são Certificados de Depósito Bancário.

* **Fundos de investimento**: São pools de dinheiro gerenciados por profissionais que investem em uma variedade de ativos, como ações, títulos e imóveis. Os investidores compram cotas do fundo.

* **Imóveis**: Investir em imóveis envolve comprar propriedades para alugar ou revender. O retorno pode vir do aluguel ou da valorização do imóvel.

* **Fundos imobiliários**: Semelhantes aos fundos de investimento, mas investem em empreendimentos imobiliários, como prédios comerciais, shoppings e hospitais.

* **Previdência privada**: São planos de aposentadoria oferecidos por instituições financeiras. Os investidores fazem contribuições ao longo do tempo e recebem benefícios no futuro.

* **Mercado de câmbio (Forex)**: Investir em Forex envolve a compra e venda de moedas estrangeiras com o objetivo de obter lucro com as variações cambiais.

* **Criptomoedas**: São moedas digitais descentralizadas, como o Bitcoin, que podem ser compradas e vendidas em plataformas de câmbio específicas.

* **Ouro e metais preciosos**: Investir em ouro e outros metais preciosos pode servir como proteção contra a inflação e a volatilidade do mercado.

O código a seguir faz previsões de retorno de investimentos, utilizando Algoritmo Genético.

Sua tarefa é desenvolver e implementar no código:

* Valores aleatórios para **retorno e risco** na função `def lista_investimentos():`
* Gerar um Simulador de Investimentos que permitar simular `n` investimentos
* Salvar os dados em um arquivo "csv"
* Mostrar um gráfico de dispersão com as simulações

**Você deverá implementar os tipos de investimentos descritos anteriormente**.
"""

import os
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Função de avaliação de uma carteira
def avaliar_carteira(carteira):
    retornos = np.array([investimentos[investimento]['retorno'] for investimento, escolhido in zip(investimentos.keys(), carteira) if escolhido])
    riscos_individuais = [investimentos[investimento]['risco'] for investimento, escolhido in zip(investimentos.keys(), carteira) if escolhido]

    if not riscos_individuais:
        return -np.inf  # Retorna um valor negativo grande para indicar que a carteira é inválida

    risco = np.std(riscos_individuais)
    retorno_esperado = np.mean(retornos)

    return retorno_esperado - risco

# Funções genéticas
def selecao_torneio(populacao, avaliacoes):
    indice1 = np.random.randint(len(populacao))
    indice2 = np.random.randint(len(populacao))
    return populacao[indice1] if avaliacoes[indice1] > avaliacoes[indice2] else populacao[indice2]

def crossover_um_ponto(individuo1, individuo2):
    ponto = np.random.randint(len(individuo1))
    filho1 = np.concatenate((individuo1[:ponto], individuo2[ponto:]))
    filho2 = np.concatenate((individuo2[:ponto], individuo1[ponto:]))
    return filho1, filho2

def mutacao_troca(individuo):
    if len(individuo) < 2:
        return individuo

    indice1, indice2 = np.random.choice(len(individuo), 2, replace=False)
    while indice1 == indice2:
        indice2 = np.random.randint(len(individuo))

    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    return individuo

# Lista de investimentos com valores aleatórios para "investimento" e "risco"
# Você deverá utilizar intervalos entre 0 e 10 apenas.
# A função abaixo mostra um exemplo de como deverá ser implementado.
# Não se esqueça de usar os tipos de investimentos explicados acima.

def lista_investimentos():
  investimentos = {
        'Ações': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Títulos Públicos': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Títulos Privados (debêntures e CDBs)': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Fundos de Investimento': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Imóveis': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Fundos Imobiliários': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Previdência Privada': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Mercado de Câmbio (Forex)': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Criptomoedas': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)},
        'Ouro e Metais Preciosos': {'retorno': np.random.uniform(0, 10), 'risco': np.random.uniform(0, 10)}
  }

  return investimentos

# Simulando oscilações nos investimentos

# Parâmetros do algoritmo genético
tamanho_populacao = 10
taxa_mutacao = 0.1
num_geracoes = 100

# Gerando investimentos aleatórios
investimentos = lista_investimentos()

# Inicialização da população
populacao = [np.random.choice([0, 1], len(investimentos)) for _ in range(tamanho_populacao)]

# Algoritmo genético
for _ in range(num_geracoes):
    avaliacoes = [avaliar_carteira(carteira) for carteira in populacao]
    nova_populacao = []

    for _ in range(tamanho_populacao):
        pai1 = selecao_torneio(populacao, avaliacoes)
        pai2 = selecao_torneio(populacao, avaliacoes)
        filho1, filho2 = crossover_um_ponto(pai1, pai2)

        if np.random.rand() < taxa_mutacao:
            filho1 = mutacao_troca(filho1)
        if np.random.rand() < taxa_mutacao:
            filho2 = mutacao_troca(filho2)

        nova_populacao.extend([filho1, filho2])

    populacao = nova_populacao[:tamanho_populacao]

# Encontrando a melhor carteira
melhor_carteira = max(populacao, key=avaliar_carteira)
retorno_esperado = np.mean([investimentos[investimento]['retorno'] for investimento, escolhido in zip(investimentos.keys(), melhor_carteira) if escolhido])
risco = np.std([investimentos[investimento]['retorno'] for investimento, escolhido in zip(investimentos.keys(), melhor_carteira) if escolhido])

print("Melhor carteira encontrada: ", end="")
for investimento, escolhido in zip(investimentos.keys(), melhor_carteira):
    if escolhido:
        print(f"{investimento} \nRetorno={investimentos[investimento]['retorno']}, Risco={investimentos[investimento]['risco']}")
print()

import csv
import numpy as np

def simular_investimentos(n_investimentos):
    investimentos = []
    for i in range(1, n_investimentos + 1):
        nome_investimento = f'Investimento {i}'
        retorno = np.random.uniform(0, 10)
        risco = np.random.uniform(0, 10)
        investimentos.append({'Nome': nome_investimento, 'Retorno': retorno, 'Risco': risco})
    return investimentos


dados_simulados = simular_investimentos(15)


nome_arquivo = 'simulacao_investimentos.csv'
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    colunas = ['Nome', 'Retorno', 'Risco']
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=colunas)

    escritor_csv.writeheader()
    for investimento in dados_simulados:
        escritor_csv.writerow(investimento)

import csv
import matplotlib.pyplot as plt


dados_simulados = []
with open('simulacao_investimentos.csv', newline='') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
        dados_simulados.append(linha)


retornos = [float(investimento['Retorno']) for investimento in dados_simulados]
riscos = [float(investimento['Risco']) for investimento in dados_simulados]
nomes = [investimento['Nome'] for investimento in dados_simulados]


cores = [risco / 10 for risco in riscos]


plt.figure(figsize=(10, 6))
plt.scatter(riscos, retornos, c=cores, cmap='coolwarm', marker='o', alpha=0.8)
for i, nome in enumerate(nomes):
    plt.text(riscos[i], retornos[i], nome, fontsize=8, ha='right')
plt.title('Simulação de Investimentos')
plt.xlabel('Risco')
plt.ylabel('Retorno')
plt.colorbar(label='Risco (0 - Baixo, 1 - Alto)')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.hist(retornos, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histograma dos Retornos')
plt.xlabel('Retorno')
plt.ylabel('Frequência')
plt.grid(True)
plt.tight_layout()
plt.show()

