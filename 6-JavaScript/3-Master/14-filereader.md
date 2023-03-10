# FileReader

- Objeto que actua para trabajar con los eventos para leer archivos
- Entra con input type file


* Para leer txt

```js

const archivo = document.getElementById('archivo')

archivo.addEventListener("change",(e)=>{
    leerArchivo(archivo.files[0])
})

const leerArvhico = ar => {
    const reader = new FileReader();
    reader.readAsText(ar);
    reader.addEventListener("load",(e)=>console.log(e))
}

console.log(reader)

```

* Para leer Jsons

```js

const archivo = document.getElementById('archivo')

archivo.addEventListener("change",(e)=>{
    leerArchivo(archivo.files[0])
})

const leerArvhico = ar => {
    const reader = new FileReader();
    reader.readAsText(ar);
    reader.addEventListener("load",(e)=>{
        console.log(JSON.parse(e.currentTarget.result))
    })
}
```

* Para multiples archivos, se pone el inpult en multiple y se cambia asi...

```js

const archivo = document.getElementById('archivo')

archivo.addEventListener("change",(e)=>{
    leerArchivo(archivo.files)
})

const leerArvhico = ar => {
    for (var i=0;ar.length;i++){
        console.log(ar[i])
        const reader = new FileReader();
        reader.readAsText(ar[i]);
        reader.addEventListener("load",(e)=>{
        console.log(JSON.parse(e.currentTarget.result))
    })
    }
}
```

* readAsDataURL()

```js

const archivo = document.getElementById('archivo')

archivo.addEventListener("change",(e)=>{
    leerArchivo(archivo.files)
})

const leerArvhico = ar => {
    for (var i=0;ar.length;i++){
        console.log(ar[i])
        const reader = new FileReader();
        reader.readAsText(ar[i]);
        reader.addEventListener("load",(e)=>{
            let newImg = `<img src='${e.currentTarget.result}'>`
            document.querySelector(".resultado").innerHTML += newImg
        })
    }
}
```