# Branches/ramas

cuando hay varios desarrolladores en un código, se crean varias ramas para que cada uno trabaje en su rama y no en la principal.

cuando se quiere añadir los cambios de una rama secundaria a la principal se le llama merge.

Para ver la rama en la que estamos trabajando

```
git branch
```

Luego, para crear una nueva rama

```
git checkout -b nombre_rama
```

Para visualizar el código dentro del archivo

```
cat nombre_archivo
```

pasar de una rama a otra

```
git checkout nombre_rama
```

Para hacer el merge en la rama principal, nos ubicamos en esta rama principal
 
```
git merge nombre_rama
```

Para hacer un push en una rama especifica

```
git push –u origin development.
```