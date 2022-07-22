# Introduccion a MongoDB

```
MongoDb es un gestor de bases de datos NoSQL orientado a documentos, no utiliza esquemas ni datos estructurados. Se centra puntualmente en el almacenamiento de colecciones las cuales son un conjunto de docuemntos.

Es fácil de escalar a nivel vertical u horizontal, agregando o modificando solamente el documento
```

# Atomicidad

```
Un documento atómico sera aquel que tendrá varios documentos relaiconados entre si en uno solo, ya qu ela escritura atómica es posible que se de a nivel d eun solo documento.

Solo se "normaliza" un documento el cual contiene toda la información que se necesita desde una apicación para la interacción con los datos.

En Mongo es posible modificar varios docs que se encuentre realcionados entre si y aunque un doc es atómico a nivel de modificaciones, la operación en conjunto no.
```






