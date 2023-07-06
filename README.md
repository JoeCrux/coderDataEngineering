# Data Engineering Flex
## Repositorio actividades curso Data Engineering Flex
# Entregable 1
### Objetivos generales
Tener un código inicial que será usado en el proyecto final como un script ETL inicial. 
- El script debe extraer datos en JSON y poder leer el formato en un diccionario de Python. 
- La entrega involucra la creación de una versión inicial de la tabla donde los datos serán cargados.

Actividades
- Se genero el script: scriptDesafioClase5.py que se encuentra en el repositorio
- Se creo la tabla en Redshift


| Comentario | Imagen |
| ------ | ------ |
| Tabla creada en Redshift. | ![printPantallaTablaCreadaRedshift](https://github.com/JoeCrux/coderDataEngineering/assets/118003007/0be35b5e-5106-4904-8a12-37092fd64514) |

# Entregable 2
### Objetivos generales
El script de la entrega 1 deberá adaptar datos leídos de la API y cargarlos en la tabla creada en la pre-entrega anterior en Redshift con transformaciones
- Implementar funcionalidades de la librería Pandas en el código cargándolos en la tabla creada en la misma.
- Solucionar una situación real de ETL donde puedan llegar a aparecer duplicados durante la ingesta de los datos

Actividades
- Se tomaron las sugerencias de correccion del entregable 1, al crear la tabla se agregaron conceptos de SORTKEY y DISTKEY
  
![comandoSqlActualizado](https://github.com/JoeCrux/coderDataEngineering/assets/118003007/ac0f11f5-2e40-4bd1-b318-60395ccf3ccf)

- Se ordeno el data frame por dos columnas. Se puede visualizar en los comentarios los pasos realizados para la insercion de datos en el script: scriptDesafioClase7.py que se encuentra en el repositorio

| Comentario | Imagen |
| ------ | ------ |
| Datos de Data Frame | ![datosAinsertarDataFrame](https://github.com/JoeCrux/coderDataEngineering/assets/118003007/8ae57d8b-9d01-46af-b3c4-8bd62e3604d3) |
| Visualizacion antes de insercion de datos | ![imagenAntesDeInsercion](https://github.com/JoeCrux/coderDataEngineering/assets/118003007/698be0d4-5f84-48f1-8a04-c9ddb823586d) |
| Visualizacion despues de insercion de datos | ![imagenDatosInsertados](https://github.com/JoeCrux/coderDataEngineering/assets/118003007/6fc28c90-707d-41aa-98a1-193b148b3283) |




