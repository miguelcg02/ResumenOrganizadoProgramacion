# Validar por consola

```
Para saber que tenemos instalado el servidor ejecutar:

mongod --version

Nota: El bin de mongo debe estar en el path
```

# Iniciar mongo por consola

```
Escribir:

mongo
```

# Ver información de la base de datos

```
Para ver las colecciones creadas para la bases de datos, tamaño y demas:

db.stats()
```

# Para usar una base de datos

```
Escribir: 

use nombre_bd
```

# Para ver las bases de datos en el sistema

```
Escribir:

show dbs
```

# Para ver la base de datos en la que esta posicionado actualmente

```
Escribir: 

db
```

# Crear una nueva colección

```
db.createCollection("Envios")

ó

dbcreatCollection("Envios",{capped: true, max:1, size:200})

esta última agrega con espacio limitado
```

# Ver las colecciones creadas

```
Para ver las colecciones de una bd escribir:

show collections
```

# Insertar un solo registro

```
db.nameDB.insertOne({id_envio: "123",nombre_repartidor: "pepe", origen:"xyz", destino:"xyz"})
```

# Insertar varios registros al mismo tiempo

```
db.nameBD.insertMany({
    {id_envio: "123", nombre_repartidor:"pepe", origen: "xyz", destino:"xyz"},
    {id_envio: "124", nombre_repartidor:"violeta", origen: "xyz", destino:"xyz"}
})
```

# Regisstro uno a uno

```
Var bulk = db.nameDB.initializeBulkOp();
bulk.insert({id_envio: "123", nombre_repartidor:"pepe", origen: "xyz", destino:"xyz"});
bulk.execute();
```

# Buscar los documentos de la colección

```
db.nameBD.find()
```

# Buscar los documentos de la colección con parametros

```
db.nameBD.find({idenvio:{$eq:"123"}})
```

# Buscar los documentos de la colección con salida formateada

```
db.nameDB.findOne()
```

# Para dar formato a la consulta de datos agregar al final

```
.pretty()
```

# Actualizar datos de un documento

```
db.nameDB.update({"idenvio":"123",{$set: {"origen":"AAA"}}})
```

# Actualizar múltiples datos

```
db.nameDB.updateMany({"idenvio":{$eq: "123"},{$set: {"origen":"AAA"}}})
```

# Eliminar un elemento

```
db.nameDB.deleteOne({"idenvio":"123"})
```

# Eliminar varios elementos

```
db.nameDB.deleteMany({"origen":"xyz"})
```


