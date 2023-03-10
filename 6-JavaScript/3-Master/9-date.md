# date

Api usada para cosas relacionadas a la fecha

```js
const fecha = new Date();

fecha.getDate(); //Nos devuelve el numero del día
fecha.getDay(); //Nos devuelve el día de la semana, siendo Domingo 0, Lunes 1, Martes 2, etc
fecha.getMonth(); //Nos devuelve el mes, enero 0, feb 1, marzo 2, abril 3, etc
fecha.getYear(); //Nos devuelve 2022-1900 = 120, le resta 1900. Año actual - 1900
fecha.getHours(); // nos da la hora
fecha.getMinutes();
fecha.getSeconds();
console.log(fecha)
```