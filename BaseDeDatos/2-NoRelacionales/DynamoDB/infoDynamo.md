# Niveles de consistencia

```
1. Eventualmente consistente: Leerá el primer registro encontrado en las réplicas
2. Fuertemente consistente: Leerá el registro el cual se encuentra en todas las réplicas
3. Consistencia transaccional: Asegura que todos los datos se escriben en las réplicas cuando es exitoso el proceso
```

# Indice local secundario (LSI)

```
-Requiere llave de partición en la tabla
-Se puede crear al momento de crear la tabla
-Máximo 5 indices por tabla
-Hace que los atributos sean mandatorios
```

# índice global secundario (GSI)

```
-Estructura distinta a la tabla
-Máximo 2 por tabla
-Se crean independientemente
```

# Manejo de índices en Dynamo

```
- Partition key: Permite particionar los datos que coinciden con la misma clave de partición y se almacenan juntos (Clave principal)
- Sort key: Permite ordenar los datos que se almacenan con la misma partition key. Esto permite consultar mucho datos en una sola consulta 
```
