class BaseConfig(object):
    WEB_DOMAIN = 'http://localhost'

    ENV = 'dev'

    # POSTGRES
    POSTGRES_URI = 'postgresql+psycopg2://postgres:vccloud123@10.3.53.162:5432/postgres'


class PublicApiConfig(BaseConfig):
    DEBUG = True
