# Inicializar repo

Empezar con el repo, estar ubicado en la carpeta donde se inicializará el repo. Se crea un directorio oculto

```
git init
```
Para ver los directorios y archivos ocultos

```
ls -a
```

Para entrar en la carpeta 

```
cd .git/
```

otra vez se puede ver las carpetas oculatas dentro de la carpeta de git. En estas carpetas ocultas se almacenan las versiones de nuestro código, las ramas, los commit. Todo

```
ls -a
```

# Flujo de trabajo de git

1. Se inica con los archivos en el computador. Que son editados, pero no son directamente montados al repo.
2. Con git add se pasa a la etapa de stage que se agregan los archivos que quieran ser pasados. Que sirven para verificar los archivos que queremos pasar al repo. Es una etapa intermedia para indicar los cambios efectuados que sean seleccionados y pasen al repo.
3. Con git commit se pasa a la etapa commit. Los cambios que fueron comprometidos podran ser enviados al server (repo).
4. Con git push se manda al server.


