# Para mandar datos a una ruta

Se retornan más items, en este caso un phone con el nombre de una variable llamado item_name.

```
@app.route('/market')
def market_page():
    return render_template('market.html', item_name='Phone')
```

# Jinja

Es una especial forma de templating syntax que nos permite ir a traves de html. Cómo se ve en el ejemplo se abren 2 corchetes y se coloca el nombre de la variable que se esta retornando

```
<p>{{ item_name }}</p>
```

# Crear estructuras de datos para pasar información

Se pueden crear arreglos y diccionarios para poner información, ademas se podrá trabajar de forma dinamica gracias a los id y su estructura.

```
@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)
```

# Para crear trablas con la información para lo diccionarios

```
<table class="table table-hover table-dark">
    <thead>
        <tr>
            <!-- Your columns here -->
            <th scope="col">ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <!-- You row inside the table here -->
            <td>Value for ID</td>
        </tr>
    </tbody>
</table>
```

# Para colocar código de py en html, para poder colocar la información de forma dinamica

A la sección de las filas en html, se le va a colocar esta sintaxis jinja {% %} para escribir código de py y hacerlo dinamico. Se tiene que colocar en donde empieza y en donde termina.

```
<tbody>
    {% for item in items %}
        <tr>
        <!-- You row inside the table here -->
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.barcode }}</td>
            <td>{{ item.price }}$</td>
        </tr>
    {% endfor %}
</tbody>
```

Incluso se le puede agregar más caracteres a la información, por ej vea el signo $ en el price

# Agregar botones a la tabla para interactuar con cada Item

Agregar las lineas de código en su lugar correspondiente

```
<th scope="col">Options</th>

<td>
    <button class="btn btn-outline btn-info">More info</button>
    <button class="btn btn-outline btn-success">Purchase This Item</button>
</td>
```

