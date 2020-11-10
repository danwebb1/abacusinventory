SQL_USER = 'root'
SQL_NAME = 'abacus_inventory_v1'
GAE_PROJECT_ID = 'abacus-app'
SQL_ENGINE = 'django.db.backends.mysql'

#SQL_HOST_DEV = '34.66.101.207'
SQL_HOST_DEV = '127.0.0.1'
SQL_UNIX_SOCKET = 'abacus-app-284522:us-central1:abacus-inventory'
#SQL_HOST_QA
#SQL_HOST_STAGING
#SQL_HOST_PROD

SQL_PW = 'Cr3st68132'

DATABASE_DEV = {
    'ENGINE': SQL_ENGINE,
    'HOST': SQL_HOST_DEV,
    'USER': SQL_USER,
    'PASSWORD': SQL_PW,
    'NAME': SQL_NAME,
    'GAE_PROJECT_ID': GAE_PROJECT_ID,
    'UNIX_SOCKET': SQL_UNIX_SOCKET
}
