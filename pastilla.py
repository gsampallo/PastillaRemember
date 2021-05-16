# Guillermo Sampallo
# gsampallo.com
#
# https://github.com/gsampallo/PastillaRemember
#
import sys
import os,io,json
import datetime
from pathlib import Path

import paho.mqtt.client as mqtt

from Parameters import Parameters
from Weather import Weather

class Pastilla:

    def send_message(self,topic,message):
        client = mqtt.Client()
        client.connect("localhost", 1883, 60)
        client.publish(topic, message)


    

    def __init__(self):
        self._param = Parameters()
        self._param.set_file_config("/home/pi/pastillaRemember.json")
        #self._param.set_file_config("/home/pi/.node-red/context/global/global.json")
        self._param.load_parameters()

        self._weather = Weather()


        if(self.control_date_time()):
            clima = self._weather.get_data()
            self.send_message("MENSAJE",clima)            
            
        else:

            intentos_str = self._param.parameters["intentos"]
            print(intentos_str)
            intentos = int(intentos_str)

            intentos = intentos + 1
            self.send_message("MENSAJE","PASTILLA")
            self.send_message("MENSAJE_ALERTA",str(intentos))

            self._param.set_intentos(intentos)

            

    def control_date_time(self):
        ahora = datetime.datetime.now()
        fecha = str(ahora.year)+""+str(ahora.month)+""+str(ahora.day)
        ultima_fecha = self._param.get_date()

        if(fecha == ultima_fecha ):
            return True
        else:

            #Monday to Friday
            if ahora.weekday in range(0,4):
                #if(ahora.hour >= 7 and hour < 9):
                if (ahora.hour == 7 and ahora.minute in range(15,59)) or (ahora.hour == 8):
                    return False
                else:
                    return True
                
            else:
                #if(ahora.hour >= 8 and hour < 10):
                #if ahora.hour in range (8,10) and ahora.minute in range(15,59):
                if (ahora.hour == 8 and ahora.minute in range(0,59)) or (ahora.hour == 9):
                    return False
                else:
                    return True                


if __name__ == "__main__":

    pastilla = Pastilla()