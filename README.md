# ChallengeALKEMY
Challenge de Data Analytics en python: normalización, procesamiento, disponibilización y creación de base de datos, Challenge Data Analytics - Python


## Paso 1 - Procesamiento de Datos.
Para comenzar, use Python y Requests con el objeto de realizar el pedido a los datasets ubicados en la web de  https://datos.cultura.gob.ar, y almacenarlos de forma local. Luego, utilice Pandas para el análisis, exploración y normalización de los datos. Todo el siguiente análisis debe seguirse utilizando consultas en Pandas.

### Normalización de toda la información de Museos, Salas de Cine y Bibliotecas, creando una tabla que se dispone y contiene lo siguiente:
o cod_localidad
o id_provincia
o id_departamento
o categoría
o provincia
          o localidad
o nombre
o domicilio
o código postal
o número de teléfono
o mail
o web

### Procesamiento de los datos para poder generar una tabla con la siguiente información:

o Cantidad de registros totales por categoría
o Cantidad de registros totales por fuente
o Cantidad de registros por provincia y categoría Utilice 

###	Procesamiento de la información de cines para poder crear una tabla que contenga:

o Provincia
o Cantidad de pantallas
o Cantidad de butacas
o Cantidad de espacios INCAA
## Paso 2 - Creación de tablas en Base de Datos
•	Para disponibilizar la información obtenida y procesada en los pasos previos, el proyecto utiliza como base datos PosgreSQL.
•	Utilicé SQLAlchemy ORM create_engine para conectar la base de datos

## Paso 3 - Se crearon las tablas .sql
• todos los registros existentes sean reemplazados por una nueva informacion, si se requiera.
• Para poder manipular la base de datos desde un script

# Todo estos pasos estan hechos en Jupyter Notebook para una mejor visualizacion y control del proceso. [main.ipynb](ChallengeALKEMY/main.ipynb)

## Paso 3 - Deploy
• Para facilitar el deploy cree un script usando cursor donde se conecta fácilmente a la base de datos PostgreSQL y podemos a empezar a manipular los datos y updatearlos.
#
pip install virtualenv
python -m virtualenv env
env\Scripts\activate
pip install -r requirements.txt
________________________________________

