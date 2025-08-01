import pandas as pd
from playwright.sync_api import sync_playwright
from datetime import datetime
import requests
import time

class Desafio:
    def __init__(self):
        self.link = "https://cidades.ibge.gov.br/brasil/"
        self.estados = {
            "Acre": "ac/",
            "Alagoas": "al/",
            "Amapá": "ap/",
            "Amazonas": "am/",
            "Bahia": "ba/",
            "Ceará": "ce/",
            "Distrito Federal": "df/",
            "Espírito Santo": "es/",
            "Goiás": "go/goias",
            "Maranhão": "ma/",
            "Mato Grosso": "mt/",
            "Mato Grosso do Sul": "ms/",
            "Minas Gerais": "mg/",
            "Pará": "pa/",
            "Paraíba": "pb/",
            "Paraná": "pr/",
            "Pernambuco": "pe/",
            "Piauí": "pi/",
            "Rio de Janeiro": "rj/",
            "Rio Grande do Norte": "rn/",
            "Rio Grande do Sul": "rs/",
            "Rondônia": "ro/",
            "Roraima": "rr/",
            "São Paulo": "sp/",
            "Sergipe": "se/",
            "Tocantins": "to/",
        }
        self.dados_estados = []
        self.abrir_navegador()
    def verificar_conexao(self):
        url = "https://www.google.com"
        while True:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print("✅ Internet conectada.")
                    break
            except requests.RequestException:
                print("⛔ Sem conexão. Aguardando reconexão...")
                time.sleep(5) 
    def abrir_navegador(self):
        try:
            with sync_playwright() as p:
                self.verificar_conexao
                navegador = p.chromium.launch(headless=True)
                self.pagina = navegador.new_page()
                self.extrair_dados()
                self.salvar_dados()
                navegador.close()
        except Exception as e:
            print(f"Erro ao abrir o navegador: {e}")

    def extrair_dados(self):
        for nome_estado, caminho in self.estados.items():
            self.verificar_conexao()
            try:
                url_estado = f"{self.link}{caminho}/panorama"
                print(f"\nURL: {url_estado}")
                self.pagina.goto(url_estado, timeout=60000)
                self.pagina.wait_for_timeout(4000)
                seletor_territorio = "section#dados"
                self.pagina.wait_for_selector(seletor_territorio, timeout=60000)
                self.pagina.wait_for_timeout(4000)
                territorio = self.pagina.query_selector_all(seletor_territorio + " div.topo__celula-direita")
                dados = {"Estado": nome_estado}

                print(f"Extraindo dados de {nome_estado}...")

                for bloco in territorio:
                    try:
                        titulo = bloco.query_selector("p.topo__titulo") or bloco.query_selector("h3.topo__titulo")
                        valor = bloco.query_selector("p.topo__valor")
                        if titulo and valor:
                            titulo_texto = titulo.inner_text().strip()
                            valor_texto = valor.inner_text().strip()
                            dados[titulo_texto] = valor_texto
                            print(f"{titulo_texto}: {valor_texto}")
                    except Exception as e:
                        print(f"Erro ao extrair dados do bloco de território: {e}")
                        continue
                        
                tabela_populacao = self.pagina.query_selector_all(seletor_territorio + " table.lista tr.lista__indicador")
                for linha in tabela_populacao:
                    try:
                        colunas = linha.query_selector_all("td")
                        if len(colunas) >= 2:
                            nome = colunas[1].inner_text().strip()  
                            valor = colunas[2].inner_text().strip() 
                            dados[nome] = valor
                            print(f"{nome}: {valor}")
                    except Exception as e:
                        print(f"Erro ao extrair dados da população: {e}")

                self.dados_estados.append(dados)
                
                print(f"✔ Dados extraídos de {nome_estado}")
            except Exception as e:
                print(f"❌ Erro ao extrair dados de {nome_estado}: {e}")
                self.dados_estados.append(dados)
                print(f" Dados extraídos com sucesso para {nome_estado}.")

            except Exception as e:
                print(f"Erro ao processar {nome_estado}: {e}")



    def salvar_dados(self, nome_base_arquivo="dados_ibge.xlsx"):
        try:
            nome_arquivo_com_data = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{nome_base_arquivo}"
            tabela = pd.DataFrame(self.dados_estados)

           
            mapeamento_colunas = {
                'Área da unidade territorial                     [2024]': 'Área territorial',
                'Taxa de mortalidade infantil [2023]': 'Mortalidade Infantil                     [2023]',
                'População no último censo [2022]': 'População no último censo',
                'População estimada [2024]': 'População estimada',
                'Densidade demográfica [2022]': 'Densidade demográfica',
                'Salário médio mensal dos trabalhadores formais [2022]': 'Salário médio mensal',
                'PIB per capita [2022]': 'PIB per capita',
                'IDHM Índice de desenvolvimento humano municipal [2010]': 'IDHM',
                'Mortalidade infantil [2023]': 'Taxa de mortalidade infantil',
                'Receitas realizadas [2017]': 'Receitas realizadas',
                'Despesas empenhadas [2017]': 'Despesas empenhadas',
                'Escolarização de 6 a 14 anos de idade [2010]': 'Escolarização de 6 a 14 anos',
                'Taxa de fecundidade total [2021]': 'Taxa de fecundidade',
                'Domicílios com lixo coletado [2022]': 'Domicílios com lixo coletado diretamente',
                'Domicílios com rede geral de abastecimento de água [2022]': 'Domicílios com rede geral como principal forma de abastecimento de água',
                'Domicílios com esgotamento sanitário (Rede geral ou fossa séptica ligada à rede) [2022]': 'Domicílios com esgotamento sanitário (Rede geral ou fossa séptica ligada à rede)',
                'Domicílios com iluminação elétrica [2015]': 'Domicílios com iluminação elétrica',
                'Domicílios com microcomputador ou tablet [2021]': 'Domicílios com microcomputador ou tablet',
                'Domicílios com acesso à Internet [2021]': 'Domicílios com acesso à Internet',
                'Domicílios com telefone móvel celular [2021]': 'Domicílios com telefone móvel celular',
                'Domicílios com televisão [2021]': 'Domicílios com televisão'
            }

            

            tabela.columns = tabela.columns.str.replace('\n', ' ').str.strip()
            tabela = tabela.rename(columns=mapeamento_colunas)
            print(tabela.columns) 
            novas_colunas = []
            novos_nomes = []
            colunas_processadas = set()

            for i, col in enumerate(tabela.columns):
                if i in colunas_processadas:
                    continue
                iguais = [j for j, c in enumerate(tabela.columns) if c == col]

                colunas_processadas.update(iguais)

                colunas_iguais = tabela.iloc[:, iguais]
                mesclada = colunas_iguais.bfill(axis=1).iloc[:, 0]

                novas_colunas.append(mesclada)
                novos_nomes.append(col)
            tabela_mesclada = pd.concat(novas_colunas, axis=1)
            tabela_mesclada.columns = novos_nomes
            pasta = 'dados/'
            tabela_mesclada.to_excel(pasta+nome_arquivo_com_data, index=False)
            print(f"✔ Arquivo Excel salvo como '{nome_arquivo_com_data}'")
        except Exception as e:
            print(f"❌ Erro ao salvar o arquivo Excel: {e}")

Desafio()
