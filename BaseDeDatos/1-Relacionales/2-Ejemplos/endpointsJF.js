//Punto 10: Obtener el valor promedio que se debe pagar al mes según las suscripciones de los usuarios a los planes que ofrece la plataforma
async getPromedioMensual() {
    const querySelect = `SELECT ROUND(AVG(precio),2) Avg_precio
    FROM "Grupo 3 - T2"."PLANES" JOIN "Grupo 3 - T2"."SUSCRIPCIONES" AS s
        USING (id_plan)
        WHERE 
        EXTRACT(MONTH FROM s.fecha_pago)=EXTRACT(MONTH FROM CURRENT_TIMESTAMP) 
        AND 
        EXTRACT(YEAR FROM s.fecha_pago)=EXTRACT(YEAR FROM CURRENT_TIMESTAMP);`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getPromedioMensual', function (req, res, next) {
    moviesModel.getPromedioMensual().then(promedio=>{
        res.status(200).send(promedio.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})

//Punto 11: Obtener la cantidad de peliculas y series que se encuentran en la base de datos de la plataforma
async getNumSeriesPelis() {
    const querySelect = `SELECT COUNT(*) 
    FROM (
      SELECT titulo FROM "Grupo 3 - T2"."PELICULAS"
      UNION 
      SELECT titulo FROM "Grupo 3 - T2"."SERIES"
    ) AS tem;`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getNumSeriesPelis', function (req, res, next) {
    moviesModel.getNumSeriesPelis().then(numSeriesPelis=>{
        res.status(200).send(numSeriesPelis.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})

//Punto 12: Obtener la información de todas las películas que aún no han sido calificadas o valoradas
async getSeriesPelisNoValoradas() {
    const querySelect = `SELECT p.titulo,p.duracion,p.sinopsis,p.cartel,p.archivo_trailer FROM "Grupo 3 - T2"."PELICULAS" AS p
    LEFT JOIN "Grupo 3 - T2"."CALIFICACIONES_PELICULAS" AS c
    ON p.id_pelicula = c.id_pelicula
    WHERE c.id_pelicula is NULL
    UNION
    SELECT s.titulo,s.temporadas,s.sinopsis,s.cartel,s.archivo_trailer FROM "Grupo 3 - T2"."SERIES" AS s
    LEFT JOIN "Grupo 3 - T2"."CALIFICACIONES_SERIES" AS cs
    ON s.id_serie = cs.id_serie
    WHERE cs.id_serie is NULL;`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getSeriesPelisNoValoradas', function (req, res, next) {
    moviesModel.getSeriesPelisNoValoradas().then(noValoradas=>{
        res.status(200).send(noValoradas.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})

//Punto 9: Permitir editar la información de una película o serie
//mejor varios o con un switch??
async updatePeliSerie(id_serie, titulo){
    const queryUpdate = `UPDATE "Grupo 3 - T2"."SERIES" SET titulo='${titulo}' WHERE id_serie= '${id_serie}';`
    const result = await connection.query(queryUpdate)
    return result
},

router.post('/api/updatePeliSerie', function (req, res, next) {
    const { id_serie, titulo } = req.body
    moviesModel.updatePeliSerie(id_serie, titulo).then(serie=>{
        res.status(200).send(serie.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})