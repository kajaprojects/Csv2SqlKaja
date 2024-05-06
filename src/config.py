import os

user = os.environ.get('POSTGRES_USER', 'test')
password = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('POSTGRES_HOST', 'database')
database = os.environ.get('POSTGRES_DB', 'sensorData')
port = os.environ.get('POSTGRES_PORT', '5432')

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'