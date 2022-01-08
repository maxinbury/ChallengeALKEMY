from decouple import Config

DEBUG = True

postgres = {'DB_USER':Config('DB_USER'),
              'BD_PASSWORD':Config('BD_PASSWORD'),
              'BD_HOST':Config('BD_HOST'),
              'DB_PORT ':Config('DB_PORT'),
              'DB_NAME':Config('DB_NAME')
             }