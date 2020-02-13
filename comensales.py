import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


semaforoCocinero = threading.Semaphore(0)
semaforoComensal = threading.Semaphore(3)

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    semaforoCocinero.acquire
    global platosDisponibles
    try:
      while (True):
        logging.info('Reponiendo los platos...')
        platosDisponibles = 3
    finally:
        semaforoComensal.release()
        semaforoCocinero.release()


class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
      global platosDisponibles

      semaforoComensal.acquire()
      try:
          if platosDisponibles > 0:
            platosDisponibles -= 1
            logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
          else:
            semaforoComensal.acquire()
            semaforoCocinero.release()
            
      finally:
          semaforoComensal.release()
      

platosDisponibles = 3

Cocinero().start()

for i in range(5):
  Comensal(i).start()