# Systems Development life Cycle (SDLC)

- En nuestro caso se despliega solo al final
- 

# Stages

* Así cómo los requisitos, también hay pasos:
- Development and deplyment
- Testing
- Monitoring

* No basta con decir que ya esta montado, si no también ver cuando este montado


# Deployment stages

1. Plan release: Tener un plan de lo que se va a entregar
2. Build release:

# Best deplyment practices

- Hacer ckeclist
- Escoger bien el metodo de despliegue
- Automatizacion
- Entrega continua
- Integración continua
- Usar herramientas

# Pasos para despliegue en GCP

1. Se debe tener un proyecto desarrollado, ojalá en GitHub o si no toca pegarlo manualmente.
2. Se usa una maquina virtual desde google para tener espacio de procesamiento. Esta te permite hacer lo que se hace en un pc local.
3. Se debe configurar el proyecto de DESPLIEGUE (No de desarrollo) y se debe activar compute engine (Que es el comuptador practicamente)
4. Crear una maquina virtual desde el compute engine. (En nuestro caso se va a usar micro que tiene SO linux). Habilitar trafico HTTP y HTTPS
5. Activar instancia (Mauquina virtual) -> Se nos da una IP externa que es la que se usa pal buscador
6. Editar en el proyecto de desarrollo la IP en el Settings, toca actualizarlo y hacer el push en el github. (En el allowed host de settings es donde se edita)
7. Del lado del proyecto de despliegue también se tiene una terminal, se debe instalar git con comando linux (sudo apt install -y git), luego se clona el proyecto git de la maquina virtual (git clone PROJECT_URL) e instalar las librerias también.
8. El paso 12 es por el firewall de la universidad
9. Ejecutar las migraciones en la maquina virtual para la base de datos (Esta porq es sqlite3 que viene con Django)
10. Lanzar servidor en la maquina virtual con su puerto.
11. Una vez lanzado aparece el mensaje de que ya esta runeando el servidor, PERO se debe ingresar desde el buscador con la IP no con el puerto que aparece el mensaje. 
12. Cuando no se use apagarla porque nosotros no necesitamos gastar recursos ahí bobamente.


