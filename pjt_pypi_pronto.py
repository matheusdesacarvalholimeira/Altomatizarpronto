import pyautogui
import time
import customtkinter

#customtkinter.set_appearance_mode("lightgray")
#customtkinter.set_default_color_theme("lightgray")

janela = customtkinter.CTk()
janela.geometry("350x700")


def whatsapp():
    pyautogui.PAUSE = 2

    pyautogui.hotkey("win")
    pyautogui.write("whatsapp")
    pyautogui.click(x=554, y=391)
    pyautogui.click(x=371, y=275)
    pyautogui.click(x=856, y=916)

def chrome():
    pyautogui.PAUSE = 1
    pyautogui.hotkey("win")
    pyautogui.write("chrome")
    pyautogui.hotkey("enter")

def youtube():
    pyautogui.PAUSE = 1
    pyautogui.hotkey("win")
    pyautogui.write("chrome")
    pyautogui.hotkey("enter")
    time.sleep(5)
    pyautogui.write("youtube")
    pyautogui.hotkey("enter")

def classroom():
    pyautogui.PAUSE = 1
    pyautogui.hotkey("win")
    pyautogui.write("chrome")
    pyautogui.hotkey("enter")
    time.sleep(4)
    pyautogui.write("https://classroom.google.com/u/0/h?hl=pt-BR")
    pyautogui.hotkey("enter")





    

texto = customtkinter.CTkLabel(janela, text="O que você deseja? ")   
texto.pack(pady=50)

botao = customtkinter.CTkButton(janela, text="whatsapp", command=whatsapp)
botao.pack(pady=30)

botao = customtkinter.CTkButton(janela, text="chrome", command=chrome)
botao.pack(pady=30)

botao = customtkinter.CTkButton(janela, text="youtube", command=youtube)
botao.pack(pady=30)

botao = customtkinter.CTkButton(janela, text="classroom", command=classroom)
botao.pack(pady=30)










janela.mainloop()