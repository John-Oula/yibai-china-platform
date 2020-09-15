import os
import sys



activate_this = '/var/www/App/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

path = os.path.join(os.path.dirname(__file__), os.pardir)
if path not in sys.path:
    sys.path.append(path)
sys.path.insert(0,"/var/www/App/")


from webapp import app as application

application.secret_key = 'Adawug;irwugw79536870635785ty0875y03davvavavdey'

