import pyautogui as pag
import pandas as pd

# Definindo uma pausa padrão de meio segundo para cada comando do pyautogui
pag.PAUSE = 0.5

# Entrando no sistema de Cadastro
pag.press("win")
pag.write("chrome")
pag.press("enter")
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")


# Fazendo login no sistema
pag.click(x=694, y=403)
pag.write("rafamaza07@gmail.com")
pag.press("tab")
pag.write("0731004ram")
pag.press("tab")
pag.press("enter")

# Importando a base de dados com pandas
tabela = pd.read_csv("produtos.csv")


# Cadastrando os produtos percorrendo cada linha do arquivo csv
for linha in tabela.index:
    pag.click(x=771, y=288)
    pag.write(str(tabela.loc[linha, "codigo"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "marca"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "tipo"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "categoria"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "preco_unitario"]))
    pag.press("tab")
    pag.write(str(tabela.loc[linha, "custo"]))
    pag.press("tab")
    obs = tabela.loc[linha, "obs"]
    # Fazendo a verificação caso o campo de OBS esteja vazio seja ignorado
    if not pd.isna(obs):
        pag.write(str(tabela.loc[linha, "obs"]))
    pag.press("tab")
    pag.press("enter")
    pag.press("home")
