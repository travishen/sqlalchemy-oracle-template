import cx_Oracle
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'oracle',
        'HOST': env.str('ORACLE_HOST'),
        'PORT': env.int('ORACLE_PORT'),
        'NAME': env.str('ORACLE_SID'),
        'USER': env.str('ORACLE_PDB'),
        'PASSWORD': env.str('ORACLE_PWD'),
        'OPTIONS': {
            'mode': cx_Oracle.SYSDBA
        },
    },
}
