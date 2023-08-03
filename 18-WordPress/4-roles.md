# Tipos

1. Admin: full acceso
2. Editor: Puede manejar el contenido de todos, pero no tiene acceso al diseño o a ajustes
3. Autor: Solo puede manejar su contenido
4. Colaborado: Puede crear contenido pero no lo puede guardar
5. Suscriptor: Solo puede hacer comentarios


# Crear un rol de usuario

Para crear un rol de usuario podés utilizar la función add_role() que nos provee WordPress, la tenés que utilizar dentro de una función y asignarla al hook init. Esto tiene que hacerse desde el archivo functions.php.

```php
function add_administrador_tema_role() { //nombre de nuestra función, puede ser el nombre que quieras
    add_role(
        'administrador_tema', //Nombre de role.
        'Administrador Tema', //Nombre que se visualará en la creación o página de opciones de usuarios.
       array(    
            'read' => true, //Permite el acceso al dashboard del adminitrador.
            'switch_themes' => true, //Permite el cambio de temas.
            'edit_themes'   => true, //Permite editar archivos desde el administrado de archivos del tema.
            'edit_theme_options' => true, //Permite modificar Widgets,Menús, Personalizar.
            'install_themes'    => true,  //Permite instalar temas nuevos.
            'update_themes' => true, //Permite actualizar temas instalados.
            'delete_themes' => true, //Permite eliminar temas.

            )   //Array con las capabilities
    );
}

//add_action(Hook, Nombre de la función)
add_action('init', 'add_administrador_tema_role');
```

Una vez que este código esté inicializado, el usuario ya quedará creado con esa configuración. Si necesitás eliminarlo, no bastará con eliminar la función, tendrás que usar el método que veremos a continuación.

# Eliminar un rol de usuario

Para eliminar un rol de usuario podés a utilizar la función remove_role() y, de la misma forma que para crearlo, tenés que utilizarla dentro de una función asignada al hook init, en el archivo function.php.

```php
function remove_role_administrado_temas() { //Nombre de la función
    remove_role( 'administrador_tema' ); 
}
 
//add_action(Hook, Nombre de la función)
add_action( 'init', 'remove_role_administrado_temas' );
```

# Modificando capabilities en roles

Para agregar capabilities en un role, lo primero que tenés que hacer es instanciar el role dentro de una variable conla función get_role(). Una vez hecho eso puedes utilizar los métodos add_cap() y remove_cap().

En el siguiente ejemplo se le dará al role de usuario subscriptor el permiso para editar posts (entradas de blog, custom post type).

```php
function add_cap_subscriber(){ //Nombre de la función
    $role = get_role( 'subscriber' ); //Instaciamos el role en la variable $role
    $role->add_cap( 'edit_posts'); //Agregamos la cabability usando el método add_cap().
}

//add_action(Hook, Nombre de la función)
add_action( 'init', 'add_cap_subscriber');
```

En el siguiente ejemplo se removerá al role de usuario editor, el permiso para modificar contenidos (entradas de blog, custom post type, etc).

```php
function remove_cap_editor(){ //Nombre de la función
    $role = get_role( 'editor' ); //Instaciamos el role en la variable $role
    $role->remove_cap('edit_pages'); //Removemos la cabability usando el método remove_cap().
}

//add_action(Hook, Nombre de la función)
add_action( 'init', 'remove_cap_editor');
```

# Lista de todas las posibles acciones

https://wordpress.org/support/article/roles-and-capabilities/#administrator
