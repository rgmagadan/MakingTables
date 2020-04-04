import time
from pynput.keyboard import Key, Controller
from pandas import read_clipboard

time.sleep(2)

keyboard = Controller()

df = read_clipboard()
cadena = df.to_markdown()



for i in cadena:
	keyboard.press(i)





