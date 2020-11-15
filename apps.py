from glob import glob
import yaml
from App import App

from os.path import exists, join

class Apps:
    def __init__(self):
        self.apps = []
    
    def load(self, path):
        
        for app in glob(path+"/**"):
            if exists(join(app, "app.yaml")):
                raw = open(join(app, "app.yaml"), "r").read()
                data = yaml.load(raw, Loader=yaml.SafeLoader)
                
                app = App.from_dict(data, app)
                
                self.apps.append(app)
                

                
