//Punto 5: Traer toda la información de una serie cuando esta se selecciona como sinopsis, cantidad capítulos, poster, enlace de trailer (link de youtube).

async getInfoSerie(idSerie) {
    const querySelect = `SELECT * FROM "Grupo 3 - T2"."SERIES" WHERE id_serie = '${idSerie}';`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/infoSeries/:id_serie', function (req, res, next) {
    const  id_serie  = req.params.id_serie
    moviesModel.getInfoSerie(id_serie).then(series=>{
        res.status(200).send(series.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting serie')
    })
})

//Punto 6: Traer la información de las películas favoritas de un usuario (nombre película, poster)

async getFavMovies(id_perfil) {
    const querySelect = `SELECT peli.titulo, peli.cartel
                            FROM "Grupo 3 - T2"."PELICULAS" as peli
                        INNER JOIN
                            "Grupo 3 - T2"."PELICULAS_FAVORITAS" as fav
                            ON fav.id_pelicula = peli.id_pelicula
                        WHERE fav.id_perfil = '${id_perfil}';`
    const result = await connection.query(querySelect)
    return result
},

router.get('/api/favMovies/:id_perfil', function (req, res, next) {
    const  id_perfil  = req.params.id_perfil
    moviesModel.getFavMovies(id_perfil).then(favMovies=>{
        res.status(200).send(favMovies.rows)
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting favorite movies')
    })
})

//Punto 7: Permitir al usuario editar la información de su perfil como por ejemplo modificar la tarjeta vinculada, contraseña, teléfono, correo

async updateProfile(correo, id_usuario) {
    const queryUpdate = `UPDATE "Grupo 3 - T2"."USUARIOS" SET correo = '${correo}' WHERE id_usuario = '${id_usuario}';`
    const result = await connection.query(queryUpdate)
    return result
},

router.post('/api/updateProfile', function (req, res, next) {
    const { correo, id_usuario } = req.body
    moviesModel.updateProfile(correo, id_usuario).then(user=>{
        res.status(200).send({message: 'update data user ' + id_usuario, rowCount: user.rowCount})
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})

//Punto 8: Permitir al usuario cambiar la fecha de facturación de la suscripción a un plan

async updatePayDate(fecha_pago, id_usuario) {
    const queryUpdate = `UPDATE "Grupo 3 - T2"."SUSCRIPCIONES" SET fecha_pago = '${fecha_pago}' WHERE id_usuario = '${id_usuario}';`
    const result = await connection.query(queryUpdate)
    return result
},

router.post('/api/updatePayDate', function (req, res, next) {
    const { fecha_pago, id_usuario } = req.body
    moviesModel.updatePayDate(fecha_pago, id_usuario).then(user=>{
        res.status(200).send({message: 'update data user ' + id_usuario, rowCount: user.rowCount})
    }).catch(err => {
        console.log(err)
        return res.status(500).send('Error getting user')
    })
})