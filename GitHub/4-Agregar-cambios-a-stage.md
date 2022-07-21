# Empezar código

Para abrir código en la carpeta 

```
code .
```

ver el estado del archivo, ver si hay algun commit y los archivos que git no esta siguiendo.

```
git status
```

Agregar los archivos al commit, hay varias formas. Lo idea es NO meter todo de una e ir metiendo de una en una, además también ver el status.

```
git add archivo1.txt

git add .txt

git add .

git add archivo1.txt archivo2.txt archivo3.txt ... 
```

Se puede revisar el status otra vez y mostrará la rama en la que esta ubicada, los commit realizados y los cambios que pueden ser comprometidos al commit.

```
git status
```

para quitar un archivo del add

```
git rm --cached archivo1.txt
```

para comprometer los archivos que estan stage

```
git commit -m "Aqui se hace una descricpión detalla sobre lo que se hizo exactamente"
```

Para quitar un archivo que esta en el commit rápido

```
git rm archivo.txt
```

