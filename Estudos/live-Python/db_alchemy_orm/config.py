DB_HOST = '50160'
DB_PORT = '5432'
DB_USER = 'admin'
DB_PASS = 'admin'
DB_DATA = '/var/lib/postgresql/data'

SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATA}'