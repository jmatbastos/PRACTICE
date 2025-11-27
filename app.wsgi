import sys
sys.path.insert(0,'/users/a12345/public_html/wsgi')

#activate_this ='/users/a12345/public_html/wsgi/PRACTICE/.virtualenv/bin/activate_this.py'

#with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

from PRACTICE import app as application
