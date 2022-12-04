# Objetivo

Saber que beneficios ofrecen, que desventajas tienen, las capas de los procesos, etc.

# Definición de aplicación

Cualquier programa de computo que desarrolle una funcionalidad especifica y que ofrece una solución al cliente.

# Funciones principales de una aplicación

- Manegar información
- Manipular datos
- Manegar recursos

# Las 5 categorias de los tipos de aplicaciones más utilizados

1. Aplicaciones mobiles
2. Aplicaciones RCA, Rich client apps: Se comen los recursos del cliente xd.
3. Aplicaciones RIA, Rich internet apps: Necesitan internet
4. APIs
5. WEB

## 1. Aplicaciones mobiles

- Pueden ser de clientes livianos o clientes robustos

Liviano: No necesita muchos recursos del cliente. Pocos datos, pocos procesamientos. (El mejor ej es Web porque agarra todo de internet). En caso de mobile puede ser una red social
Robustos: Necesita muchos recursos del cliente. Muchos datos, Muchos procesamientos. (El mejor ej es RCA porque agarra todo de la maquina del cliente). En caso de mobile puede ser un jueguito

* Se debe considerar:
- Saber si se necesita escenarios offline.
- Usualmente se usan por necesidades de desplazamiento.
- Antes se pensaba en facilitar a los trabajadores de oficina.

* Problemas:
- Limitado en perifericos y en tamaños del dispositivo
- Tiene dependencia de recursos

* Cuando usarlo:
- Dependencia a dispositivos moviles
- Cuando la interfaz grafica se puede trabajar en pantallas pequeñas
- La conectividad puede depender de internet 

Ej: http://www.guidanceshare.com/images/6/6d/AppArchGuide_-_App_Types_-_Mobile.png
Ej: https://os-system.com/blog/wp-content/uploads/2020/10/Three-Layers-of-Mobile-App-Architecture.png


## 2. RCA

* Se debe considerar
- Normalmente no tiene necesidad de conexión a internet
- Cumple una funcionalidad en especifico y nada más
- Es dependiente de dispositivos físicos
- Por ejemplo, la panatalla de compra de productos de una tienda

* Ventajas:
- Tiempo de respuesta son muy rápidos
- Mejor UX
- Suele servir para ser offline
- Proveer los recursos del cliente

* Desventajas:
- Es muy díficl de versionar.
- Dependencia de hardware especifico.
- Es dependiente de una plataforma.
- El despliegue es más complejo.

* Cuando usarlo?
- Cuando debe ser muy ineteractiva y de rta rápido.
- Cuando se quiere proveer una mejor UX.
- Cuando se quiere desplegar en un computador.


Ej: http://www.guidanceshare.com/images/7/74/AppArchGuide_-_App_Types_-_Rich_Client.png

## RIA

- Completamente dependiente de internet y es necesario un navegador
- Es rico en manejó de media (Se necesita internet)

Ventajas:
- Facil de versionar
- Multiplataforma

Desventajas:
- Se necesita un especio del cliente

Cuando usuarlo?
- Cuando se necesita entrega buena interactiva, no se tienen recursos físicos.
- Cuando se accede a traves de la web
- Cuando se necesita mucha interactividad

Ej: http://www.guidanceshare.com/images/2/26/AppArchGuide_-_RIA_App_Type.png

## Service applications (APIs)

- No necesariamente tienen interfaz graficas
- XML / Json
- Es para traer información más que todo

Ventajas:
- No tienen dependencia cliente - servidor
- Puede ser consumida por cualquier aplicacion
- Es interoperable

Desventajas:
- Depende siempre de conectividad
- No tiene UI

Cuando usuarlo?
- Cuando no se quiere trabajarle a un cliente en especifico
- Cuando no quiero dllar UI
- Se debe garantizar la conexión a internet

Ej: http://www.guidanceshare.com/images/0/02/AppArchGuide_-_App_Types_-_Services.png

## Web

- Que se corre en el navegador
- No se garantiza nada en particular
- Es muy sencilla de dllar

Ventajas:
- Multiplataforma
- Muy usado y muy expandido
- Facil de utilizar, versionar, etc

Desventaja:
- Dependencia de internet
- UI no tan enriquecida

Ej: http://www.guidanceshare.com/images/1/17/AppArchGuide_-_Web_App_App_Type.png