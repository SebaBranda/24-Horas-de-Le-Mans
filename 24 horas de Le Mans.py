import random
import threading
import time

listaBoxes = []
listaPista = []

cantidadMaximaDeCorredores = 100
cantidadMaximaDePitsHabilitados = 4

monitorPista = threading.Condition()

def tiempoEspera(maximo):
    time.sleep(random.randrange(1,maximo))

class Autos(threading.Thread):
    def __init__(self,nro):
        super().__init__()
        self.nro = nro

    def entroABoxes(self):
        while True:
            if(len(listaBoxes) < cantidadMaximaDePitsHabilitados):
                print("corredor", self.nro, "- Bandera verde, me meto al pit.")
                listaBoxes.append(self)
                tiempoEspera(5)
                self.vuelvoALaPista()
            else:    
                print("corredor",self.nro, "- Boxes cerrados, otra vuelta mas, a ver si llego...")
                exit()

    def vuelvoALaPista(self):
            listaPista.append(self)
            with monitorPista:
                if (len(listaPista) > 1):
                    monitorPista.notify()
                print("corredor", self.nro, "- Le meto a fondo, ahora si...")
                tiempoEspera(10)    

    def run(self):
        self.entroABoxes()

class Pista(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while(True):
            with monitorPista:
                while(len(listaPista) < 1):
                    monitorPista.wait()
                c = listaPista.pop(0)
                print("- Bandera verde de salida de boxes para: ", c.nro)
                listaBoxes.pop(0)
                tiempoEspera(10)  

LeMans = Pista()
LeMans.start()

while (True):
    nroCorredor=random.randrange(1,cantidadMaximaDeCorredores)
    corredor1 = Autos(nroCorredor)
    time.sleep(5)
    corredor1.start()        