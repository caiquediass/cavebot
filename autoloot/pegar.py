from time import sleep
import pyautogui as pya
import os


def pegar_loot():
    pya.keyDown('shift')
    pya.rightClick(x=871, y=351)  # norte
    pya.rightClick(x=793, y=351)  # norte esquerda
    pya.rightClick(x=801, y=426)  # esquerda
    pya.rightClick(x=800, y=497)  # sul esquerda
    pya.rightClick(x=866, y=495)  # sul
    pya.rightClick(x=943, y=489)  # sul direita
    pya.rightClick(x=940, y=420)  # direita
    pya.rightClick(x=943, y=343)  # norte direita
    pya.rightClick(x=872, y=423)  # centro
    pya.keyUp('shift')
    
    return None

