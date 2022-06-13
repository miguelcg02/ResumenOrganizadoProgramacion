# Definicion MongoDB

```
Son de tipo no relacional y ha sido deseñadas para almacenar y consultar datos que se encuentran en formato JSON

Debido a que los datos son semi estructurados, es posible evolucionar según las necesidades de las aplicaciones
```

# Ejemplo

```
[
    {
        "year" : 2013,
        "title" : "Turn it Down, or Else!",
        "info" : {
            "directors" : ["Alice Smith", "Bob Jones"],
            "release_date" : "2013-01-18T00:00:00Z",
            "rating" : 6.2,
            "genres" : ["comedy", "Drama"],
            "image_url" : "https://a.com"
            "plot" : "A rock bands..."
            "Actors" : ["David Matthewman", "John G. Neff"]
        },
        {
            "year" : 2015,
            "title" : "The big new movie",
            "info": {
                "plot" : "Nothing happends at all",
                "rating" : 0
            }
        }
    }
]
```
# Diferencias Documental y key value

```
Las bases de datos documental son distintas a las bases de datos llave valor. Sus caracterisitcas más notables son:

Llave valor:
-Tiene una llave única (hash) que apunta a un elemento
- Se pueden crear particiones a través de su llave única
- Carece ded consistencia

Documentales:
- Permite almacenar documentos con formato XML, JSON o BJOSN
- Facilidad en cambio de estructura
- Carece de coherencia

```

# Diferencias con SQL

```
MongoDB     | SQL
Colecciones -> Tablas
Documentos -> Filas(registros)
Campos -> Columnas
```









