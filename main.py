from fastapi import FastAPI
import pandas as pd

app = FastAPI (title= 'Consultas a plataformas de streaming',
                description= 'Aquí podrás realizar consultas sobre el contenido de las plataformas Amazon, Disney, Hulu y Netflix.' 
                            'Para relizar consultas, utiliza: a para Amazon, d para Disney, h para Hulu y n para Netflix',
                version= '1.0.1')

bbdd_plat_compl = pd.read_csv("bbdd_plataformas_completo.csv", sep= ";")

@app.get('/')
async def index():
    return 'Consultas plataformas'


@app.get("/Contenido con mayor duración, por plataforma, año y tipo de duración/")
def get_max_duration(year: int, platform: str, duration_type: str):
    peliculas = []
    peli_mayor = []
    for indice, x in enumerate (bbdd_plat_compl['release_year']):
        if x == year:
            if bbdd_plat_compl['id'][indice][0] == platform:
                if bbdd_plat_compl['duration_type'][indice] == duration_type:
                    peliculas.append(int(bbdd_plat_compl['duration_int'][indice]))
                    peli_mayor.append(indice)
                    mayor_time = max(peliculas)
                    peli = peliculas.index(mayor_time)
                    respuesta = bbdd_plat_compl['title'][peli_mayor[peli]]

    return respuesta


@app.get("/Cantidad de títulos por plataforma con 'score' mayor a.../")
def get_score_count(platform: str, scored: float, year: int):
    puntaje_mayor = []
    for indice, x in enumerate(bbdd_plat_compl['release_year']):
        if x == year:
            if bbdd_plat_compl['id'][indice][0] == platform:
                if bbdd_plat_compl['score'][indice] > scored:
                    puntaje_mayor.append(x)
    
    return len(puntaje_mayor)


@app.get("/Cantidad de títulos por plataforma/")
def get_count_platform(platform):
    pelis_plataforma = []
    for indice, x in enumerate(bbdd_plat_compl['id']):
        if bbdd_plat_compl['id'][indice][0] == platform:
            pelis_plataforma.append(x)
    
    return len(pelis_plataforma)


@app.get("/Actor que estuvo en más cantidad de títulos/")
def get_actor(platform: str, year: int):
    filtro = []
    contador = 0
    
    for indice, x in enumerate(bbdd_plat_compl['release_year']):
        if x == year:
            if bbdd_plat_compl['id'][indice][0] == platform:
                filtro.append(bbdd_plat_compl['cast'][indice])
    
    for ind, z in enumerate(filtro):
        if type(z) == str:
            actores = filtro[ind].split(',')
    
    for ind, z in enumerate(actores):
        if actores.count(z) > contador:
            contador = actores.count(z)
            actor_mayor = actores[ind]

    return actor_mayor

