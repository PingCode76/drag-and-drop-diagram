import os

ERROR_404_HELP = False
SECRET_KEY = os.getenv('APP_SECRET', '&_(+gcl$^3$i&5e(+%c0hacx$chg9t$zs&(wghe9q*f&!+e*2m')
TEST = "test"

POSTGRES = {
    'user': 'postgres',
    'pw': '000000',
    'db': 'bdddragdrop',
    'host': 'localhost',
    'port': '5432',
}
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:000000@localhost:5432/bdddragdrop'