import pynput.keyboard as keyboard

def callingBack(key):
 print(key)

key_Listener = keyboard.Listener(on_press=callingBack)

with key_Listener:
 key_Listener.join()
