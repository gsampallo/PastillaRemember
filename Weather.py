import requests
import json
from Parameters import Parameters
class Weather:

    def __init__(self):
        self._param = Parameters()
        self._param.set_file_config("/home/pi/PastillaRemember/config.json")
        self._param.load_parameters()
        
        self.__token = self._param.parameters["token"]



    def get_data(self):
        page = requests.get(self.build_query())
        #print(page.content)
        data = json.loads(page.content)

        clima = "{}C {}%".format(data["main"]["temp"],data["main"]["humidity"])

        return clima

    def build_query(self):
        url = "https://api.openweathermap.org/data/2.5/weather?q=Corrientes, AR&appid={}&units=metric".format(self.__token)
        return url

if __name__ == "__main__":
    weather = Weather()