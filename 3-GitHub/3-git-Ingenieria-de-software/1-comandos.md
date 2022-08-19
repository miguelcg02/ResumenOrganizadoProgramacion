# Que es?

- Gestor de versiones de forma optimizada, manejable y guardada en un repositorio.
- Permite organizar el trabajo.
- Colaborar con más personas que trabajan en el código.

# Como funciona

- Se basa en comparaciones de los documentos a traves del contenido de los archivos
- En windows hay un comando para comparar las lineas diferentes: FC fileV1.html FileV2.html


En Git

```
diff fileV1.html FileV2.html
```

# Goals 

- Controlar
- Seguridad
- Recuperación

# Comandos de consola

* Moverse entre carpetas

```
cd 
```

* Crear directorio

```
mkdir
```

* Iniciar repositorio

```
git init
```

* Revisar el status, los archivos modificados, borrados, movidos, etc

```
git status
```

* trazar sobre un archivo, poder hacerle seguimiento

```
git add archivo1.txt

git add .
```

* agregar cambios

```
git commit -m "mensaje indicativo del cambio que estoy haciendo"
```

* Revisar las lineas que cambiaron

```
git diff version_archivo1 versio_archivo2
```

* Revisar que paso, para hacerle trazabilidad a las versiones

```
git log
```

checkout:camibar entre ramas y revisar una información
merge: combinar cambios

# Estados

- Local
- Stage (Es con el add) trazar el archivo
- commit (Es con el commit) llevar el commit al repositorio local
- server (Es con el push) llevarlo a la nube

# Branching

- En desarrollo se debe trabajar con 3 ramas como minimo

1. Desarrollo (Donde se trabaja)
2. Pruebas (Una vez se valide el trabajo se pasa a la rama de pruebas, donde se mira que todo este en orden)
3. Despliegue (Una vez se vea todo melosky, se pasa al despliegue) Main/Master.

- En equipos cada uno tiene su rama de developer

* Para crear una rama

```
git branch nombre_rama
```

* Para listar las ramas

```
git branch
```

* Para moverse entre ramas

```
git checkout nombre_rama
```

- Si estas ubicado en una rama, ahí se llevará acabo la acción que se dice (Add, comiit, push)

* Para fucionar el contenido de dos ramas o dos archivos. OJO ES ESTAR UBICADO DESDE LA RAMA QUE QUIERO FUNCIONAR Y SE LLAMA A LA OTRA RAMA 

```
git merge nombre_otra_rama
```

* Para enviar la información al repositorio remoto

```
git push
```

* Para traer información. Se necesitan permisos.

```
git pull
```

* Clonar el repositorio y traerlo por primera vez (Hacer una copia exacta). No se requieren permisos

```
git clone
```

* Equivalente al status local pero en remoto

```
git fetch
```


