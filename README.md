# 📊 Desafio Técnico - Coleta de Dados do IBGE com Python + Playwright

Este projeto realiza a coleta automatizada de dados dos 27 estados brasileiros a partir do site oficial do IBGE: (https://cidades.ibge.gov.br), utilizando as bibliotecas **Playwright**, **Pandas** e **Datetime**.

---

## 🚀 Tecnologias Utilizadas

- [Playwright](https://playwright.dev/python/) — Automação de navegador.
- **Pandas** — Salvamento dos dados.
- **Datetime** —Pegar data e hora atual.

---

## 🧠 Objetivo do Projeto

O desafio consiste em extrair os dados principais disponíveis para cada estado brasileiro, diretamente do site do IBGE, sem a utilização de APIs, organizá-los em uma planilha `.xlsx`.

---

## 🏗️ Estrutura do Código

A lógica principal está encapsulada em uma classe chamada `Desafio`, que possui os seguintes métodos:

- `__init__`: Define os links de cada estado.
- `abrir navegador`: inicia o processo tentando acessar o link e caso positivo chama a função extrair_dados.
_`extrair_dados`: extrai e filtra os dados de cada estado verificando cada um com tempo de atraso para cada estado diferente, dando tempo da página carregar e os dados também, armazenando numa lista e  chama a função salvar_dados.
- `salvar_dados` : nessa função acontece a conversão da lista num dataframe salvando e concatenado valores que representam o mesmo dados mas que foram nomeados de forma distinta em alguns estados, salvando os dados junto a hora e data que foi pedido.



---

## 📦 Saída

A execução do programa gera um arquivo `.xlsx` contendo os dados de todos os estados brasileiros em linhas, com cada coluna representando um dado extraído.

---

## 🏷️ Categorias

Os dados estão organizados em colunas que podem pertencer às seguintes categorias :

- População: 
- Educação:
- Economia:
- Saúde:
- Trabalho e Rendimento:
- Meio Ambiente:
- Território:

---

Alguns estados não possuem dados de todas as categorias.


## ▶️ Como Executar

1. Clone este repositório:

   ```bash 
git clone https://github.com/Allysson987/desafioTecnico.git




## Instalando Dependências 

```bash
pip install -r requirements.txt
pip install pandas 
pip install datetime
playwright install
```

## Execute o Script
```bash
python desafio.py
```
## ⚠️Problemas encontrados

- Muitos valores possuem nomes diferentes embora representem o mesmo dado, após a filtragem de alguns dados foi encontrado outros problemas, alguns dados não existem em determinados estados o que representa uma falha nos dados do IBGE que desfavorece regiões Norte e Nordeste com dados mais escassos e incompletos.

- Além de existirem dados maiores em São Paulo, Rio de Janeiro e parte do Sul, erro encontrado ainda existe dados de 2023, 2022 o que resulta em muitos estados com dados vazios na coluna.

- Para a análise de dados esses dados são ótimos para avaliar as condições do sudeste a curto e médio prazo, o  sul do país a curto prazo e o norte e nordeste sendo os menos atendidos, o que leva a um problema crônico de muitos dados nulos.
Na tentativa de filtrar os dados, para diminuir valores nulos acaba-se perdendo muitos dados de estados do sudeste prejudicando parte da análise.

## ⚙️ Atualização futura para melhor análise 

- Incluir uma requisição para a API do IBGE para coletar dados de forma mais eficiente, unificar os dados e padronizados para análise mais completa de todas as 5 regiões do país.
