# Que es

-Git es la herramienta de manejo de versiones más popular del mundo
-Se tiene acceso a un servidor con el código
-Entrega historial de todo el trabajo realizado en el código
-Almacena código
-Trabajar en equipo facil y rápido
-Saber cuando se introdujo un error en una aplicación y saber el commit que dio el error

# Git Bash

-Una linea de comandos especial para git

# Configuracion basica

Para agregar un nombre a nuestro usuario

```
git config --global user.name "calva"
```

Para poner el correo

```
git config --global user.email calvache116@gmail.com
```

Para indicar el editor

```
git config --global core.editor "code --wait"
```

Para ver los archivos de configuracion global

```
git config --global -e
```

Para configurar correspondiendo al sistema operativo
Para windows: true
Para Linux/mac: input

```
git config --global core.autocrlf true
```

Para revisar el listado de todas las configuraciones que se pueden agregar

```
git config -h
```