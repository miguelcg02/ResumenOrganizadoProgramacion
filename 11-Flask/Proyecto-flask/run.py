from market import app #Se ejecuta la variable app que esta creada en el __init__ de la carpeta market

if __name__ == '__main__': #Checks if the run.py file has executed directly and  not imported
    app.run(debug=True) 