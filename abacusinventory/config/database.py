SQL_USER = 'root'
SQL_NAME = 'user'
GAE_PROJECT_ID = 'abacus-app'
SQL_ENGINE = 'django.db.backends.mysql'

SQL_HOST_DEV = ''
SQL_UNIX_SOCKET = ''
#SQL_HOST_QA
#SQL_HOST_STAGING
#SQL_HOST_PROD

SQL_PW = '*******'

DATABASE_DEV = {
    'ENGINE': SQL_ENGINE,
    'HOST': SQL_UNIX_SOCKET,#SQL_HOST_DEV,
    'USER': SQL_USER,
    'PASSWORD': SQL_PW,
    'NAME': SQL_NAME,
    'GAE_PROJECT_ID': GAE_PROJECT_ID,
}
