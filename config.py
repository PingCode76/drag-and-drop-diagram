import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
# or use https://miniwebtool.com/django-secret-key-generator/

SECRET_KEY = "&_(+gcl$^3$i&5e(+%c0hacx$chg9t$zs&(wghe9q*f&!+e*2m"
TEST = "test"

#basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')