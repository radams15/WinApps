from apps import Apps
from os.path import join
from os import system

USERNAME = "rhys"
PASSWORD = "winpass"
IP = "192.168.122.33"

APP_FOLDER = "/home/rhys/.local/share/applications/"

def get_reg(name, reg):
    commands = []
    commands.append('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\TSAppAllowList\Applications\{}" /v "Name" /t REG_SZ /d "{}" /f'.format(name, name))
    commands.append('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\TSAppAllowList\Applications\{}" /v "Patg" /t REG_SZ /d "{}" /f'.format(name, reg))
    return commands

apps = Apps()
apps.load("apps")

for app in apps.apps:
    desktop = app.get_desktop(USERNAME, PASSWORD, IP)
    file = join(APP_FOLDER, "{}_Win.desktop".format(app.name.replace(" ", "_").replace(".", "_")))
    
    with open(file, "w") as f:
        f.write(desktop)    
    
    system("chmod +x {}".format(file))
    
    print(file)
