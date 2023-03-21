# Proyecto_Individual_1_DZS
Repo del proyecto invividual 1 "MLOps" - Etapa Labs

# **Proyecto individual 1: "MLOps Engineer" (Data Engineer & Machine Learning)**

## **Por Daniela Zarich Santi**

Comencé a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming, como Amazon, Disney, Hulu y Netflix. 

Mi primer trabajo es crear un sistema de recomendación con datos que posee la empresa. Pero el desafío es ún mayor: la madurez de los datos... no existe!! Debo transformarlos, tampoco están automatizados los procesos para la actualización de nuevas películas o series, entre otras pálidas. 

Así que... manos a la obra!!

### **Etapa 1: Transformaciones**
En primer lugar decidí crear una base de datos limpia y ordenada con toda la información disponible en la empresa.

En MySQL, creé una tabla para cada plataforma y luego realicé las transformaciones necesarias para lograr mi objetivo:

•	Generé un campo id, componiéndose de la primera letra del nombre de la plataforma, seguido del show_id.

![sql_id](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/01%20sql%20id.jpg)

•	Reemplacé por 'G' los valores nulos del campo rating ya que corresponde al maturity rating: “general for all audiences”.

![sql_G](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/02%20sql%20G.jpg)

•	Modifiqué la fecha de agregación a la plataforma, que estaba en formato 'Mes dd, aaaa' (muy poco práctico para trabajar) a formato 'AAAA-mm-dd'.

![sql_fecha](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/03%20sql%20fecha.jpg)

•	Cambié los campos de texto a letras minúsculas, ya que es más sencillo que esté estandarizado para evitar inconvenientes tanto en las consultas como en trabajos posteriores.

![sql_minusc](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/04%20sql%20minus.jpg)

•	Convertí el campo duration en dos campos: 'duration_int' y 'duration_type'. Esto permitirá agilizar las consultas.

![sql_duration](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/05%20sql%20duration.jpg)

Luego de realizar esas transformaciones exporté los datos limpios en formato csv para continuar mi trabajo en Visual Studio Code.
_______
*Realicé todo ese trabajo, pero al fin no lo usé, ya que posteriormente (en desarrollo API) me surgieron errores y decidí re-comenzar tratando los datos desde Python. Pero también me seguía surgiendo el mismo error, hasta que pude darme cuenta qué era (más adelante lo explico). De todas formas, todo este proceso forma parte del presente trabajo, por eso lo detallo.* 
_______

Retomé nuevamente la etapa de transformaciones y las realicé en Python, desde Visual Studio Code:

•	Primero importé los datos de las plataformas

![pyt_imp](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/06%20p%20import.jpg)

•	Generé un campo id...

![pyt_id](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/07%20p%20id.jpg)

•	Armé un único df para realizar el resto de las transformaciones una sola vez y no cuatro. También reorganicé las columnas del mismo para mejor visualización.

![pyt_df_unico](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/08%20p%20df%20unico.jpg)

![pyt_reorg_col](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/09%20p%20reorg%20col.jpg)

•	Reemplacé por 'G' los valores nulos del campo rating... 

![pyt_G](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/10%20p%20G.jpg)

•	Modifiqué la fecha de agregación a la plataforma a formato 'AAAA-mm-dd'...

![pyt_fecha](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/11%20p%20fecha.jpg)

•	Cambié los campos de texto a letras minúsculas... 

![pyt_minusc](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/12%20p%20minus.jpg)

•	Convertí el campo duration en dos campos... 

![pyt_duration](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/13%20p%20duration.jpg)

**Luego de todo eso, trabajé con los datos de 'ratings'**

•	Me brindaron 8 archivos con distintas puntuaciones de rating para el contenido de las plataformas, por lo que seguí trabajando con eso. Primero creé un daframe con cada uno de los 8 archivos de rating y posteriormente un único archivo con toda esa información (quedó un df muy grande!! más de 11 millones de registros!!).

![pyt_rating](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/14%20p%20ratings.jpg)

![pyt_rat_unico](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/15%20p%20unico%20ratings.jpg)

•	Cambié el nombre de las columnas:
        - 'movieId' por 'id': ya que si no no podría unir este df al de plataformas por no tener campo común.
        - 'rating' por 'score': ya que podría confundirse con el campo 'rating' de plataformas que se refiere a la clasificación de audiencia.

![pyt_col](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/17%20p%20rename%20cols.jpg)

*Exporté los datos del df ratings (ratings_compl) para utilizarlo más adelante.*

![pyt_exp](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/18%20p%20export%20rat.jpg)

•	Agrupé los raitings por id de película/serie e hice promedio, para que figure una única calificación promedio por título. Este paso tiene dos funciones: en primer lugar, reducir considerablemente el tamaño del dataset rating ya que tiene más de 11 millones de registros; en segundo lugar, permitir que puedan unirse los dos df (plataformas y ratings).

![pyt_group](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/19%20p%20prom%20rat.jpg)

•	Para terminar con las transformaciones, uní los dos df que me quedaron: bbdd_plataformas y rating_promedio por medio de la columna 'id'.

![pyt_df_compl](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/20%20p%20merge%20completo.jpg)

•	Eliminé columnas innecesarias para el trabajo

![pyt_elim_cols](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/21%20p%20drop.jpg)

•	Como último paso en esta etapa, exporté la base de datos completa como csv ("bbdd_pataformas.csv")

![pyt_exp_bbdd](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/22%20p%20export%20bbdd%20compl.jpg)

### **Etapa 2: Desarrollo API**
Disponibilicé los datos de la empresa usando el framework FastAPI. 
Para lograr eso tuve que crear un entorno virtual, activarlo y descargarle las librerías necesarias.
Creé dos archivos: 'main' y 'auxiliar'. En el primero está el código de la API; en el segundo, todas las transformaciones y funciones que se implementan en la API, con consultas de ejemplo.

Propuse las siguientes consultas:
•	Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. La función se llama get_max_duration(year, platform, duration_type), recibe como parámetros de entrada:

        - year: año en que se agregó la película/serie a la plataforma

        - platform: inicial de la plataforma a consultar (por ejemplo, a para Amazon, d para Disney, etc.)

        - duration_type: tipo de duración del contenido (min para películas y seasons para series)

![api_func_1](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/23%20p%20funcion%20api%201.jpg)

•	Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. La función se llama get_score_count(platform, scored, year), recibe como parámetros de entrada:

        - platform: inicial de la plataforma a consultar (por ejemplo, a para Amazon, d para Disney, etc.)

        - scored: puntuación a partir de la cuál queremos saber la cantidad de películas/series hay en esa plataforma

        - year: año en que se agregó la película/serie a la plataforma

![api_func_2](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/24%20p%20funcion%20api%202.jpg)

•	Cantidad de películas por plataforma con filtro de PLATAFORMA. La función se llama get_count_platform(platform), recibe como parámetro:

        - platform: inicial de la plataforma a consultar (por ejemplo, a para Amazon, d para Disney, etc.)

![api_func_3](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/25%20p%20funcion%20api%203.jpg)

•	Actor que más se repite según plataforma y año. La función se llama get_actor(platform, year), recibe como parámetros:

        - platform: inicial de la plataforma a consultar (por ejemplo, a para Amazon, d para Disney, etc.)

        - - year: año en que se agregó la película/serie a la plataforma

![api_func_4](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/26%20p%20funcion%20api%204.jpg)

Una vez terminada la estapa de confección de la API, continué con la disponibilización en la web (Etapa 3, a continuación).

________
*El error que me daba las funciones para las consultas en la API y por el cual rehice todo el trabajo de transformación fue que debía definir el tipo de parámetros de entrada, de esa forma funcionó a la perfección!!*
________


### **Etapa 3: Deployment**
Decidí hacer pública la API utilizando Render. Para ello, primero creé un repositorio en Github y subí los archivos. Luego, inicié sesión en Render (render.com) con mi cuenta de Google (envía un correo electrónico de verificación con un link, a través de él puede accederse a la página principal de Render). Para disponibilizar la API hay que continuar desde 'Servicios web, nuevo servicio web' y conectar con repositorio público de Git (copié el link de Gisthub) y luego de completar algunos campos para la configuración... listo! Creada la API.

El link a mi API de consultas es:

https://servicio-de-consultas-plataformas-de.onrender.com/docs#/


![api](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/27%20p%20api.jpg)

### **Etapa 4: Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)**
Luego de limpiar los datos necesito investigar las relaciones que hay entre las variables de los datasets y ver si hay outliers, anomalías o algún patrón interesante que valga la pena explorar en un análisis posterior.

Para ello utilicé la librería pandas profiling (ver archivo 'EDA').

•	Importé librerías necesarias.

•	Importé los datos de plataformas

•	Realicé el reporte

![eda](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/28%20p%20eda.jpg)

______
*Con pandas profiling se utilizan muy pocas líneas de código pero el análisis es sorprendente!!*
______

Algunos ejemplos del resultado del análisis:

![eda2](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/29%20p%20eda%202.jpg)

![eda3](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/29%20p%20eda%203.jpg)

![eda4](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/30%20p%20eda%204.jpg)

### **Etapa 5: Sistema de recomendación**

Como úmtima instancia de trabajo, me pidieron realizar un modelo de machine learning para armar un sistema de recomendación de películas/series para usuarios, donde dando un od de usuario y una película/serie, nos diga se la recomienda o no para dicho usuario.

_______
*Luego de realizar muchas, pero muchas pruebas llegué a un resultado. Lo explico...*
_______

**Trabajo previo**

•	Importé las librerías necesarias.

•	Importé el csv 'ratings_completo' que había exportado con anterioridad (sí, el que contiene más de 11 millones de registros)

![ml_import_csv](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/31%20ml%20import.jpg)

•	Eliminé las columnas innecesarias para que el modelo funcione correctamente y reordené las existentes.

![ml_drop_columns](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/32%20ml%20drp.jpg)

![ml_reindex](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/33%20ml%20reord.jpg)

•	Para definir la variable objetivo creé una columna 'visualización' que indica si el usuario vería o no esa película/serie. En una primera instancia la columna está vacía, para luego llenarla con 1 si el score es mayor o igual a 3 o con 0 si el score es menor que 3. Tomé ese valor límite porque supuse que con una valoración media el usuario sí vería ese contenido.

![ml_visual](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/34%20ml%20visualiza.jpg)

![ml_visual_func](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/35%20ml%20func.jpg)

![ml_visual_aplic](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/36%20ml%20aply.jpg)

•	Otro 'problema' con el que me encontré, fue que el campo 'id' era un string por lo que al modelo no le gustaba y tiraba error. Entonces decidí convertirlo a int. Para ello:

        - Creé el campo id_int (vacío)
        - Dividí el campo id en dos: plataforma (str) y id_plat (int)
        - Definí el diccionario de transformación ('as': 100, 'ds': 200, 'hs': 300, 'ns': 400) y la apliqué
        - Uní las columnas del código de la plataforma y el id de la plataforma, ambos como str ya que si los definía como int se iban a sumar y se alteraría el id de película/serie. Una vez unidas las columnas en una sola, cambié el tipo a int.

![ml_id_int](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/38%20ml%20id%20int.jpg)

![ml_div](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/39%20ml%20divido%20cols.jpg)

![ml_claves](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/40%20ml%20dicc%20clave.jpg)

![ml_aplic](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/41%20ml%20map.jpg)

![ml_union](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/42%20ml%20union.jpg)

![ml_cambio_tipo](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/43%20ml%20camnio%20tipo.jpg)

•	Una vez que terminé con la preparación, eliminé columnas innecesarias (plataforma, id_plat) y reordené para que la variable objetivo quede dispuesta al final.

![ml_ratings_final](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/37%20ml%20vis%20compl.jpg)

**Armado/entrenamiento del modelo**

•	Seleccioné las variables para entrenar el modelo

![ml_var](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/44%20ml%20elijo%20variables.jpg)

•	Dividí los datos en conjunto de entrenamiento y conjunto de prueba

![ml_div_datos](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/45%20ml%20divido%20datos.jpg)

•	Creé un modelo

![ml_model](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/46%20ml%20creo%20modelo.jpg)

•	Entrené el modelo con el conjunto de entrenamiento

![ml_fit](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/47%20ml%20entrenM.jpg)

•	Realicé predicciones en el conjunto de prueba

![ml_predict](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/48%20ml%20predicc.jpg)

•	Evalué el rendimiento del modelo (precisión: 0.87)

![ml_precision](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/49%20ml%20precision.jpg)

•	Por último, guardé el modelo entrenado en un archivo con formato pkl

![ml_exp_model](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/50%20ml%20guardo%20model.jpg)

_____
*Debo aclarar que probé con varios modelos pero la precisión daba 1, por lo que se entiende que estaba en 'overfitting' por lo que había aprendido los datos de memoria, por eso los descarté*
_____


**Utilizando el modelo**

•	Para utilizar el modelo, en otro archivo cargué los datos del csv de ratings y el pkl de modelo entrenado

![ml_carga](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/51%20ml%20cargo%20models.jpg)

•	Definí la función de recomendación de modo que arroje los mensaje *'El usuario vería ese contenido'* o *'El usuario no vería ese contenido'* 

![ml_func](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/52%20ml%20funcion%20ml.jpg)

•	Probé la función y... anduvo!

![ml_results](https://github.com/Daniela-ZS/Proyecto_Individual_1_DZS/blob/main/Im%C3%A1genes%20para%20readme/53%20ml%20resultados.jpg)

______
*Pidieron que, de ser posible, este sistema de recomendación fuera deployado para tener una interfaz gráfica amigable para ser utilizada. Para ello podía utilizar Gradio para su deployment o bien con alguna solución como Streamlit o algo similar en local.*

*Luego de horas de investigación, visualización de videos, lectura y pruebas, llegó la hora de entregar el proyecto y no pude terminar de realizarlo.*

*Entiendo que este punto suma un plus al trabajo total, pero no me voy a dar por vencida, continuaré probando para tener la solución para un futuro, que espero no sea muy lejano.*
______


