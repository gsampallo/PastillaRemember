import sys
import json,io
import os.path

class Parameters:

    def exist_config(self):
        return os.path.isfile(self.__file_config)

    def load_parameters(self):
        self.parameters = ""
        if os.path.isfile(self.__file_config):
            with open(self.__file_config) as f:
                self.parameters = json.load(f) 
        else:
            print("No existe archivo de parametros")

    def save_parameters(self):
        with open(self.__file_config, 'w') as outfile:
            json.dump(self.parameters, outfile)        

    def get_date(self):
        return self.parameters["pastilla_fecha"]


    def get_intentos(self):
        intentos = self.parameters["intentos"]
        return int(intentos)

    def set_intentos(self,intentos):
        self.parameters["intentos"] = str(intentos)
        self.save_parameters()


    def set_file_config(self,file_config):
        self.__file_config = file_config
            
