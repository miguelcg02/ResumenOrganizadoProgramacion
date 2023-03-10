# History

* Back()

Vuelve para atras en una pagina

```js
history.back()
```

* forward()

Va para adelante en una pagina

```js
history.forward()
```

* go()

Recarfa la página

```js
history.go(0) //recargar
history.go(1) //Va pa delante
history.go(-1) //Va pa atras
```

* pushState()

La url la cambia y crea una nueva entrada en el historial

```js
console.log(location.href) // Se presenta un cambio en la url
history.pushState({nombre:"pedro"},"","?url")
console.log(location.href) //Se presenta un cambio en la URL
console.log(history.state) // Muestra pedro

addEventlistener("popstate",(e)=>{ //Escucha en window
    console.log(e.state); //Detecta el estado en el que esta apenas entre a la página
})
```

* replaceState()

La url la cambia pero no crea una nueva entrada en el historial

```js
console.log(location.href) // Se presenta un cambio en la url
history.replaceState({nombre:"pedro"},"","?url")
console.log(location.href) //Se presenta un cambio en la URL
console.log(history.state) // Muestra pedro

addEventlistener("popstate",(e)=>{ //Escucha en window
    console.log(e.state); //Detecta el estado en el que esta apenas entre a la página
})
```

* 