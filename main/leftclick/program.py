import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()
stop_key = KeyCode(char='k')
running = True

def on_press(key):
    global running
    if key == stop_key:
        running = False
        return False

print("Escolha uma opção:")
print("1 - Clique do mouse")
print("2 - Tecla W")
opcao = input("Digite sua opção (1 ou 2): ")

print("O programa começará em 5 segundos...")
time.sleep(5)

with Listener(on_press=on_press) as listener:
    if opcao == '1':
        print("Segurando clique esquerdo... pressione 'k' para parar.")
        mouse.press(Button.left)
        while running:
            time.sleep(0.01)
        mouse.release(Button.left)
    elif opcao == '2':
        print("Segurando tecla 'w'... pressione 'k' para parar.")
        keyboard.press('w')
        while running:
            time.sleep(0.01)
        keyboard.release('w')
    listener.join()

print("Programa finalizado.")

