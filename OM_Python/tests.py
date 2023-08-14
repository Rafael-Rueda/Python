import time

import pyautogui


def press_key(key, duration):
    if key != 'delay':
        pyautogui.press(key)
        time.sleep(duration / 2500.0)
    else:
        time.sleep(duration / 1000.0)

def play_heavy_metal():
    # Defina a sequência de teclas e durações aqui
    sequence = [
        ('h', 30),
        ('z', 30),
        ('x', 30),
        ('h', 0),
        ('g', 30),
        ('s', 30),
        ('j', 0)
    ]

    for key, duration in sequence:
        press_key(key, duration)

if __name__ == "__main__":
    print("Prepare-se para tocar o ritmo de heavy metal!")
    time.sleep(3)  # Aguarde 2 segundos antes de iniciar o macro
    play_heavy_metal()
