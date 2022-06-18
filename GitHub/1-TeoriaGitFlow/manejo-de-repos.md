# Que es GIT

```
Git es un sistema de control de versiones, que permite gestionar proyectos de software de manera distribuida, permitiendo acceder al historial de todos los cambios realizados sobre el código del proyecto
```

# Que es git flow

```
Es un conjunto de extensiones de git para proporcionar operaciones de repositorios de alto nivel para le medelo de ramificaciones.

Facilita el manejo de las ramas, el orden del proyecto y la división de los diferentes momentos por los que pasa un proyecto de software, además e desplegar y leberar cambios sobre cada rama según su ambiente.

Se tienen usualmente 3 ramas: Master, Develop y feature.
```

# Pasos iniciar un proyecto con git-flow

```
0. Descargar Gitbash

1. Descargar el proyecto del repositorio, en este caso, de GITHUB
2. Ejecutar el comando "git flow init" en la consola o terminal.
3. Ejecutar el comando "git flow start MYFEATURE" si quieres sacar una copia del proyecto desde la rama de desarrollo.
4. Para finalizar un feature ejecutar el comando "git flow feature finish MYFEATURE"
(Se debe tener en cuenta que un feature es creado siempre que vamos a agregar funcionalidades nuevas nuestro desarrollo. A nivel industri el feature se utiliza uno por cada sprint, o cada que sale un nuevo release)
5. Para compartir tu rama con otros desarrolladores y programar en conjunto utiliza el comando "git flow feature publish MYFEATURE"
6. Para obtener los cambios creados por otro usuario sobre la rama que hemos creado usar el comando git flow feature pull origin MYFEATURE
7. Los hotfix son utilizados para resolver problemas presentados en el código que ocurren sobre producción "git flow start VERSION name"
8. Cuando se finaliza un hotfix el ajuste se libera tanto en la rama principal (master) como en el desarrollo (develop) "git flow hotfix VERSION".
(El hotfix también puede ser publicado con el comando "git flow publish" y descargar cambios con git flow pull).
9. El release permite crear una nueva versión de la app y llevar ocntrol de las características desplegadas "git flow release start RELEASE (BASE)"
10. El release debe ser publicado para garantizar por parte de todo el equipo que los ajustes a liberar para la versión o sprint son correctos, el comando es "git flow release publish RELEASE"
11. Para finilizar este release, utilice elcomando "git flow release finish RELEASE"
```