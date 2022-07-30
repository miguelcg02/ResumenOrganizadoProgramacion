# Por que

Se quiere que sean solo de archivos en la maquina local. Por ej: Una base de datos en local con credenciales.

En un nuevo archivo llamado .gitignore se envia lo que no se quiere para el reposotrio

```
crear archivo .gitignore
```

se colocan los archivos y directorios que se quieran ignorar dentro del archivo

```
.env
node_modules/
```

una alternativa a git status simplificandolo

```
git status -s
```