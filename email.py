import time
import pyautogui
import pyperclip

pyautogui.PAUSE = 1
# 1- abrir Opera
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("Enter")
# 2- Pesquisar o Drive
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(3)
# 2.5- Achar Pasta
pyautogui.click ( x=413, y=310, clicks=2)
time.sleep(2)
# 3- baixar
pyautogui.click ( x=413, y=311)
pyautogui.click(x=1713, y=186)
# pyautogui.click(x=1510, y=589)
time.sleep(5)
# 3.5- Pegar informações
import pandas as pd
caminho = r"C:\Users\User\Downloads\Vendas - Dez.xlsx"
tabela = pd.read_excel(caminho)
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)
# 4- abrir gmail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3)
# 5- enviar 
pyautogui.click(x=142, y=194 )
time.sleep(2)
pyautogui.write("mvalvesgoulart@gmail.com")
pyautogui.press("tab")

# 5.5- assunto
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("tab")
# 6- Relatórios
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs ! 
Marcos Vincius Goulart"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl" , "enter")


# posição MOUSE:
time.sleep(3)
pyautogui.position()






