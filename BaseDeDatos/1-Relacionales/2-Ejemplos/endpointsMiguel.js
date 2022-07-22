async getInfoUsuario(nombre,contrasena_usuario){
    const querySelect = `SELECT U.nombre,U.correo,U.telefono, U.tarjeta, CIU.nombre AS Ciudad  FROM "Grupo 3 - T2"."USUARIOS" AS U
    JOIN "Grupo 3 - T2"."CIUDADES" AS CIU ON U.id_ciudad = CIU.id_ciudad
    WHERE U.nombre = '${nombre}' and U.contrasena_usuario = '${contrasena_usuario}';`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getInfoUsuario/:nombre/:contrasena', function (req, res, next) {
    const nombre = req.params.nombre
    const contrasena_usuario = req.params.contrasena
    moviesModel.getInfoUsuario(nombre, contrasena_usuario).then(serie=>{
        res.status(200).send(serie.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})
//------------------------------------------------------------------------------------------------------
async getPeliculaSerieDeCategoria(nombre){
    const querySelect = `SELECT ser.titulo, ser.cartel, cat.nombre 
    FROM "Grupo 3 - T2"."CATEGORIAS" as cat
    INNER JOIN
        "Grupo 3 - T2"."PELICULAS_CATEGORIAS" as pelcat
        ON pelcat.id_categoria = cat.id_categoria
    INNER JOIN
        "Grupo 3 - T2"."PELICULAS" as pel
        ON pelcat.id_pelicula = pel.id_pelicula
    WHERE cat.nombre = '${nombre}';
    UNION
    SELECT ser.titulo, ser.cartel, cat.nombre 
        FROM "Grupo 3 - T2"."CATEGORIAS" as cat
    INNER JOIN
        "Grupo 3 - T2"."SERIES_CATEGORIAS" as sercat
        ON sercat.id_categoria = cat.id_categoria
    INNER JOIN
        "Grupo 3 - T2"."SERIES" as ser
        ON sercat.id_serie = ser.id_serie
    WHERE cat.nombre = '${nombre}';`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getPeliculaSerieDeCategoria/:nombre', function (req, res, next) {
    const nombre = req.params.nombre
    moviesModel.getPeliculaSerieDeCategoria(nombre).then(categoria=>{
        res.status(200).send(categoria.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting categories')
    })
})
//------------------------------------------------------------------------------------------------------
async getPeliculaDeBuscador(busqueda){
    const querySelect = `SELECT titulo FROM "Grupo 3 - T2"."PELICULAS" WHERE nombre iLIKE  '%${busqueda}%';`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getPeliculaDeBuscador/:busqueda', function (req, res, next) {
    const busqueda = req.params.busqueda
    moviesModel.getPeliculaDeBuscador(busqueda).then(peliculas=>{
        res.status(200).send(peliculas.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting movies')
    })
})
//------------------------------------------------------------------------------------------------------
async getPeliculaSeleccionada(seleccion){
    const querySelect = `SELECT * FROM "Grupo 3 - T2"."PELICULAS" WHERE id.película = ${seleccion};;`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/getPeliculaSeleccionada/:seleccion', function (req, res, next) {
    const seleccion = req.params.seleccion
    moviesModel.getPeliculaDeBuscador(seleccion).then(peliculas=>{
        res.status(200).send(peliculas.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting the movie')
    })
})
