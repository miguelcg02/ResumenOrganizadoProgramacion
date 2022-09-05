# Punto 1

```
package javaapplication2;
import java.lang.Math;

public class Ecuacion {
    private int coeficientes[] = new int[3];
    
    
    public Ecuacion(int a, int b, int c){
        coeficientes[0] = a;
        coeficientes[1] = b;
        coeficientes[2] = c;
    }
    
    public void resolver(){
        int a = coeficientes[0];
        int b = coeficientes[1];
        int c = coeficientes[2];
        
        double x = ((-1*b)+Math.sqrt(Math.pow(b,2)-(4*a*c))/2*a);
        System.out.print(x);
    }
}
```

```
package javaapplication2;

public class JavaApplication2 {

    public static void main(String[] args) {
        int n1 = 2;
        int n2 = 4;
        int n3 = 5;
        
        Ecuacion miEcuacion = new Ecuacion(n1, n2, n3);
        miEcuacion.resolver();
    }   
}
```

# Punto 2

https://app.diagrams.net/#G1BX6nImUCGawwbp5qMpKF423kPS4emMSV

# Punto 3

```
public class Clave {
    private int codigo;
}
```

```
public class Usuario {
    private String nombre;
    public Clave clave;
}
```

# Punto 4

```
public class Perro {
    private String nombre;
    public Persona proprietario;
}
```

```
public class Persona {
    private String nombre;
    public ArrayList<Perro> mascotas= new ArrayList<Perro>();
}
```

# Punto 5

https://app.diagrams.net/#G1BX6nImUCGawwbp5qMpKF423kPS4emMSV


# Punto 6

```
public class Equipo {
     public ArrayList<Jugador> jugadores= new ArrayList<Jugador>();
     public Jugador capitan;
}
```

```
public class Jugador {
    public Equipo juegaEn;
    public Equipo capitanea;
}

```

# Punto 7

Relacion recursiva apuntan a la misma clase

```
public class Gente {
    public ArrayList<Gente> esQueridaPor= new ArrayList<Gente>();
    public ArrayList<Gente> quiereA= new ArrayList<Gente>();
}
```

# Punto 8

https://app.diagrams.net/#G1BX6nImUCGawwbp5qMpKF423kPS4emMSV

y

```
public class Motor {
    
}
```

```
public class Estereo {
    
}
```

```
public class Automovil {
    public Estereo estereo;
    public Motor motor;
    
    public Automovil(Motor motor,Estereo estereo){
        estereo = new Estereo();
        motor = new Motor();
    }
}
```

Como este es de agregación, se debe instanciar en el constructor.

En composición llegaria como parametro en un set.


# punto 9 HERENCIA

```
public class Animal {
    private int edad;
    
    public void comer(){
        
    }
}

```

```
public class Oso extends Animal{
     @Override
     public void comer(){
         
     }
}
```
