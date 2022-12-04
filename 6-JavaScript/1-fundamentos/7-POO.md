# Ejemplo

```js
class Animal {
    constructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Aqui pongo la info del animal`;
    }
    verInfo(){
        document.write(this.info);
    }
}

class Perro extends Animal{
    constructor(especie,edad,color,raza){
        super(especie,edad,color);
        this.raza = null;
    }
    static ladrar(){
        alert("WAW");
    }
    set setRaza(nuevaRaza){
        this.raza = nuevaRaza;
    }
    get getRaza(){
        return this.raza;
    }
}

const perro = new Perro("perro",5,"rojo","golden");
const gato = new Animal("gato",7,"verde");

perro.setRaza = "Golden";

perro.verInfo();
```