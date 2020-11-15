from os.path import join, abspath
from os import getcwd

DESKTOP_TEMPLATE = """\
[Desktop Entry]
Name={}
Exec={}
Terminal=false
Type=Application
Icon={}
Encoding=UTF-8
X-Desktop-File-Install-Version=0.26
"""

class App:
    def __init__(self, name, reg, icon, mime_types, keywords):
        self.name = name
        self.reg = reg
        self.icon = icon
        self.mime_types = mime_types or []
        self.keywords = keywords or []
        self.display_name = "{} (RDP)".format(self.name)
        
    @staticmethod
    def from_dict(d: dict, path):
        keys = list(d.keys())
        if "name" not in keys or "reg" not in keys:
            return None
            
        if "icon" not in keys:
            icon = "None"
        else:
            icon = abspath(join(path, d["icon"]))
            
        return App(d["name"], d["reg"], icon, d["opens"], d["keywords"])
        
    def get_desktop(self):
        command = "{} {}".format(join(getcwd(), "Run.py"), self.name)
        return DESKTOP_TEMPLATE.format(self.display_name, command, self.icon)
        
        
    def __repr__(self):
        return "{} ({})".format(self.name, self.reg)
        
    def get_command(self, username, password, ip):
        return 'xfreerdp /u:"{}" /p:"{}" /v:"{}" /wm-class:"{}" /app:"{}" /span /dynamic-resolution +auto-reconnect +home-drive -wallpaper /sec:rdp /app-icon:"{}"'.format(username, password, ip, self.display_name, self.reg, self.icon)
