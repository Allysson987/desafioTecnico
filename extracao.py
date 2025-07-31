import pandas as pd
from playwright.sync_api import sync_playwright


class Desafio:
    def __init__(self):
        self.link = "https://cidades.ibge.gov.br/brasil/"
        self.estados = {
            "Acre": "ac/acre",
            "Alagoas": "al/alagoas",
            "Amapá": "ap/amapa",
            "Amazonas": "am/amazonas",
            "Bahia": "ba/bahia",
            "Ceará": "ce/ceara",
            "Distrito Federal": "df/distrito-federal",
            "Espírito Santo": "es/espirito-santo",
            "Goiás": "go/goias",
            "Maranhão": "ma/maranhao",
            "Mato Grosso": "mt/mato-grosso",
            "Mato Grosso do Sul": "ms/mato-grosso-do-sul",
            "Minas Gerais": "mg/minas-gerais",
            "Pará": "pa/para",
            "Paraíba": "pb/paraiba",
            "Paraná": "pr/parana",
            "Pernambuco": "pe/pernambuco",
            "Piauí": "pi/piaui",
            "Rio de Janeiro": "rj/rio-de-janeiro",
            "Rio Grande do Norte": "rn/rio-grande-do-norte",
            "Rio Grande do Sul": "rs/rio-grande-do-sul",
            "Rondônia": "ro/rondonia",
            "Roraima": "rr/roraima",
            "São Paulo": "sp/sao-paulo",
            "Sergipe": "se/sergipe",
            "Tocantins": "to/tocantins",
        }
        self.dados_estados = []
        self.abrir_navegador()

    def abrir_navegador(self):
        try:
            with sync_playwright() as p:
                navegador = p.chromium.launch(headless=True)
                self.pagina = navegador.new_page()
                navegador.close()
        except Exception as e:
            print(f"Erro ao abrir o navegador: {e}")
Desafio()