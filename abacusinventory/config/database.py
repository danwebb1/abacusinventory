SQL_USER = 'root'
SQL_NAME = 'abacus_inventory_v1'
GAE_PROJECT_ID = 'abacus-app'
SQL_ENGINE = 'django.db.backends.mysql'

#SQL_HOST_DEV = '34.66.101.207'
SQL_HOST_DEV = '10.111.176.3'
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
    'GAE_PROJECT_ID': GAE_PROJECT_ID
}
