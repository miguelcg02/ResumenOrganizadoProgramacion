int numeroRandom; //El digito que genera el sistema
int intentos; // numero de intentos que el usuario desea
long double ti,tf;// definimos los tiempos que se toman con millis
int tiempo;// definimos la diferencia de tiempos
bool adivino;//variable que nos indica si adivinó o no en los intentos que desea el usuario
String generada,ingresada;//cadenas que comparamos
int pica, fama;//número de picas y de famas por cada intento

void setup(){
  Serial.begin(9600);// inicializamos monitor serial
}

void loop(){ //Hacer por siempre
  bool revisar[] = {false,false,false,false,false,false,false,false,false,false};//usamos un arreglo que verificará que los 4 números serán diferentes
  generada = "";
  randomSeed(millis()); // genera una semilla para aleatorio a partir de la función millis()
  
  while (generada.length() != 4){ //Genera el string con los 4 num diferentes
    numeroRandom = random(0,10); // genera número aleatorio entre 0 y 9
    if (revisar[numeroRandom]==false){ //Se revisa que el número no se ha usado mediante el arreglo revisar[], para que cada digito sea diferente
      revisar[numeroRandom] = true;
      generada += String(numeroRandom);// se agrega el número a la cadena generada 
    }
  }

  do{// repetimos la petición hasta ingresar correctamente un número posible de intentos
    Serial.print("Ingrese el número de intentos que desee: ");
    while(Serial.available()==0){ // Se para el serial hasta que coloque el numero de intento que desea
      
    }
    intentos=Serial.parseInt();// se ingresan los intentos que desea hacer el usuario
    Serial.println(intentos);
    Serial.readStringUntil('\n');//limpiamos el serial

    if(intentos<0){ //Se hace la restriccion de que solo reciba un numero positivo
      Serial.println("no puedes tener intentos negativos, por favor inténtalo de nuevo");
    }else{
      break;//Salimos de la petición
    }
  }while(true);
  
  ti=millis();// se comienza a tomar el tiempo

  adivino=false;//se inicializa nuestro verificador en false

  while(intentos--){//se repiten las siguientes preguntas segun el numero de intentos
    Serial.println("----");// se muestra los campos a llenar

    do{//repetimos la consideración del usuario hasta que ingrese 4 dígitos estrictamente

      while(Serial.available()==0){
    
      }
      ingresada = Serial.readStringUntil('\n');// se ingresan los numeros que el usuario cree

      if(ingresada.length()==4){
        break;
      }else{
        Serial.println("Por favor ingrese nuevamente la cadena, recuerde que deben ser 4 digitos");
      }
    }while(true);
    
    pica=0;//iniciamos picas en 0
    fama=0;//iniciamos famas en 0
    for(int i=0; i<4; i++){//revisamos dígito a dígito la cadena ingresada
      if(generada.indexOf(ingresada[i])>=0){//revisamos si el dígito actual está en la generada
        if(generada.indexOf(ingresada[i])==i){//revisamos si aparte de estar, está en la misma posición que estamos revisando
          fama++;//si cumple lo último aumenta la fama
        }else{
          pica++;// si simplemente está aumenta la pica
        }
      }//de lo contrario no aumenta ninguna variable
    }

    if(fama==4){//si hay 4 famas indicamos que adivinó el número 
      tf=millis();
      tiempo=(tf-ti)/1000;//encontramos el tiempo que transcurrió entre ti y tf y lo pasamos a segundos
      Serial.print("¡Lo has adivinado en ");
      Serial.print(tiempo);
      Serial.println(" segundos!");
      Serial.print("El número era: ");
      Serial.println(generada);

      adivino=true;//indicamos a nuestro verificador que se ha adivinado el número
      break;//dejamos de preguntar el número de intentos y salimos
    
    }else{// si no adivina el número

      Serial.println(ingresada);//mostramos el número ingresado

      if(fama==0 && pica==0){//si no hay picas ni famas, no se adivinó nada
        Serial.println("No adivinaste nada");
      }else{//de lo contrario se muestran el número correspondiente de picas y famas
        if(fama==0){
          Serial.print(pica);
          Serial.println(" Pica(s)");
        }else if(pica==0){
          Serial.print(fama);
          Serial.println(" Fama(s)");
        }else{
          Serial.print(pica);
          Serial.print(" Pica(s) y ");
          Serial.print(fama);
          Serial.println(" Fama(s)");
        }
      }
    }
  }

  if(!adivino){//si finalmente el usuario no adivino en los intentos que el establecio
    tf=millis();
    tiempo=(tf-ti)/1000;//encontramos el tiempo que transcurrió entre ti y tf y lo pasamos a segundos
    Serial.print("Se acabaron tus intentos, te tardaste: ");
    Serial.print(tiempo);
    Serial.println(" segundos");
    Serial.print("El número era: ");
    Serial.println(generada);//y mostramos cuál fue el número que no se adivinó
  }

  Serial.println("Fin del juego\n.......................................................................................");
  
}
