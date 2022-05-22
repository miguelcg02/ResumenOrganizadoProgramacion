# Que es?

```
-NoSql
-Resultados a altas velocidades
-Escalable
-Operaciones automaticas
-Posibilidad de hacer una base de datos distribuida
-Alto rendimiento
-Copia de seguridad bajo demanda
-Acceso por api o por consola
-Todas las tablas son colecciones de items
-Los items son colecciones de atributos o llaves
```


# Componentes

```
1. Tablas
2. Elementos
3. Atributos
```

# Descarga AWS y Dynamo

```
1. https://docs.aws.amazon.com/es_es/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html

2. https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

3. Después de descargar y ejecutar

4. Revisar por consola con aws --version

5. Hacer la configuración del ambiente de manera local:
  -aws configure
  AWS Acess Key ID: foo
  AWS Secret Access Kat: bar
  Default region name: us-east-2
  Default output format: json

6. Crear el servicio que permita interactuar con la base de datos local de dynamo con este comando:
    java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb


    nota: Con esa linea se levanta el servicio y se debe abrir otro cmd en paralelo, para levantarlo hacer desde la carpeta del dynamo

7. Crear el servicio que te permitirá interactuar con la bdD local de Dynamo por medio del sig comando:
    aws dynamodb list-tables --endpoint-url http://localhost:8000

    nota: Ojo al puerto c:

bonus: netstat -a muestra los puertos que estan ocupados

```

# Estructura

```
{
    "TableName" : "Movies-Grupo-3",
    "KeySchema": [
        {
        "AttributeName" : "id",
        "KeyType": "HASH"
        }
],
    "AttributeDefinitions": [
        {
            "AttributeName": "id",
            "AttributeType": "S"
        }
    ],
    "ProvisionedThroughput" : {
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1
    }
}
```

# Inicializar

```
1. npm init    <--- iniciar el package.json

2. npm i aws-sdk  <--- iniciar servicios con aws

3. crear carpeta config:

4. llenar los datos de la data-table.json que creamos con:

{
    "TableName" : "Movies-Grupo-3",
    "KeySchema": [
        {
        "AttributeName" : "id",
        "KeyType": "HASH"
        }
],
    "AttributeDefinitions": [
        {
            "AttributeName": "id",
            "AttributeType": "S"
        }
    ],
    "ProvisionedThroughput" : {
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1
    }
}

4. aws dynamodb create-table --cli-input-json file///Users/calva/Desktop/Hola Mundo/baseDeDatos/practicaDynamo data-table.json --endpoint-url http://localhost:8000

ej:
aws dynamodb create-table --cli-input-json "file:///Users/calva/Desktop/Hola Mundo/baseDeDatos/practicaDynamo/config/data-table.json" --endpoint-url http://localhost:8000

5. Revisar si existe en un nuevo cmd:
aws dynamodb list-tables --endpoint-url http://localhost:8000

6. Crear config.js en la carpeta config:

module.exports = {
    table_course: 'Movies-Grupo-3', //Nombre de la tabla
    aws_local_config:{ //Se usa esta configuración de manera local
        region: 'local',
        endpoint: 'http://localhost:8000',
    },
    aws_remote_config:{ //Se usa esta configuracion al momento de aconectarno a la base de datos en AWS de manera remota
        accessKeyId: 'AKIA45CQWSXZ2PE4FCBV',
        secretAccessKey: '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',
        region: 'us-east-2',
    }
}

OJO AL SUBIR A UN REPO NO SUBIR CREDENCIALES

7. Crear carpeta de servicios

8. Para el servicio del put crear un write.js:

var AWS = require("aws-sdk") //Se importa librería
const config = require("../config/config.js") //Se llama archivo creado previamente de configuración
AWS.config.update(config.aws_local_config) //Se define en AWS la configuración local
const doClient = new AWS.DynamoDB.DocumentClient() //Se crea el cliente de AWS
const saveStudents = function(){ //Se define la función encargada de crear los datos en la table de Dynamo
    var object = { //Crear objeto para almacenar en la base de datos
        "id": "111",
        "name": "Pepe Gutierrez",
        "email": "ejgutierrb@eafit.edu.co",
        "cellphone": "0000000000",
        "created_at": new Date().toString()
    }
    const params = {
        TableName: config.table_course, //Nombre de la table donde se almacenará la información
        Item: object //Datos a insertar
    }
    doClient.put(params, function(err, data) { //Se llama función del objeto encargado de crear información
    if(err)
        console.log("Error: ", err)
    else
        console.log("Datos almacenados correctamente ", data)
    })
}
saveStudents()

9. Para el servicio del get crear un read.js:

var AWS = require("aws-sdk") //Se importa librería
const config = require("../config/config.js") //Se llama archivo creado previamente de configuración
AWS.config.update(config.aws_local_configu) //Se define en AWS la configuración local
const doClient = new AWS.DynamoDB.DocumentClient() //Se crea el cliente de AWS
const readStudents = function(){
    const params = {
        TableName: config.table_course,
        Key: {"id": "15" }
      }
      doClient.get(params, function(err, data) { //Se cambia función para obtener
        if(err)
          console.log("Error: ", err)
        else
          console.log("Datos: ", data)
    })
  }
readStudents()

10. Para crear el servicio del update crer un update.js:

var AWS = require("aws-sdk") //Se importa librería
const config = require("../config/config.js") //Se llama archivo creado previamente de configuración
AWS.config.update(config.aws_local_configu) //Se define en AWS la configuración local
const doClient = new AWS.DynamoDB.DocumentClient() //Se crea el cliente de AWS
const readStudents = function(){
    const params = {
        TableName: config.table_course,
        Key: {"id": "15" },
        UpdateExpression: "set #name= :newNameAttri",
        ExpressionAttributeValues: {
            ":newNameAttri": "Jissel"
        },
        ExpressionAttributeNames: {
            "#name": "name"
        },
        ReturnValues: "UPDATED_NEW"
    }
    doClient.update(params, function(err, data) {
        if(err)
            console.log("Error: ", err)
        else
            console.log("Datos actualizados correctamente ", data)
    })
}
readStudents()

11. Para crear el servicio de delete crear un delete.js:

var AWS = require("aws-sdk") //Se importa librería
const config = require("../config/config.js") //Se llama archivo creado previamente de configuración
AWS.config.update(config.aws_local_configu) //Se define en AWS la configuración local
const doClient = new AWS.DynamoDB.DocumentClient() //Se crea el cliente de AWS
const saveStudents = function(){
    const params = {
        TableName: config.table_course,
        Key: {"id": "111" }
    }
    doClient.delete(params, function(err, data) {
        if(err)
            console.log("Error: ", err)
        else
            console.log("Datos eliminados correctamente ", data)
    })
}
saveStudents()

Bonus: 12. Para reemplazar las credenciales para conectarse a un servidor tirar:

aws configure

y meter los nuevos datos
```














