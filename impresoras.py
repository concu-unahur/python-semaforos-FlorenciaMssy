import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaforo = threading.Semaphore(3)

class Impresora:
  def __init__(self, numero):
    self.numero = numero

  def imprimir(self, texto):
    # Simulamos un tiempo de impresión. No cambiar esta línea.
    time.sleep(0.5)
    logging.info(f'(Impresora {self.numero}) "{texto}"')

class Computadora(threading.Thread):
  def __init__(self, texto):
    super().__init__()
    self.texto = texto

  def run(self):
    # Tomo una impresora de la lista.
    # (Esta línea va a fallar si no quedan impresoras, agregar sincronización para que no pase)
    semaforo.acquire()
    try:
      impresora = impresorasDisponibles.pop()
      impresora.imprimir(self.texto)
      impresorasDisponibles.append(impresora)
    finally:
      semaforo.release()
    # La vuelvo a dejar en la lista para que la use otro.
    

impresorasDisponibles = []
for i in range(3):
  # Creo tres impresoras y las meto en la lista. Se puede cambiar el 3 por otro número para hacer pruebas.
  impresorasDisponibles.append(Impresora(i))

Computadora('hola').start()
Computadora('qué tal').start()
Computadora('todo bien').start()
Computadora('esta explota').start()
Computadora('esta también').start()
