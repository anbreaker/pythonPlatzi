# Para crear entornos virtuales de Python
sudo apt install virtualenv

# Para instalar la version que queramos de python
virtualenv venv --python=python3.7

# activar el servidor
source venv/bin/activate

# Desactivar
deactivate

# Instalar flask
pip install flask

# ver lo instalado
pip freeze

# Lista los elementos de nuestro entorno virtual
pip list

# Crear archivo con instrucciones para instalar los requisitos de nuestro entorno virtual
pip3 freeze > requirements.txt

# Para instalar las dependencias del entorno virtual
pip install -r requirements.txt

# Configuración de Flask
# Variable de entorno, el valor de la Variable sera donde se encuentra nuestra instancia de Flask
export FLASK_APP=main.py
# Para comprobar funcionamiento correcto nos debe devolver la instancia de flask
echo $FLASK_APP

# Variable de entorno modo debug
export FLASK_DEBUG=1
echo $FLASK_DEBUG

# Para activar el development mode debes escribir lo siguiente en la consola:

export FLASK_ENV=development
echo $FLASK_ENV

# Arrancar nuestro servidor: (Para seleccionar el puerto colocar las opciones)
flask run --port=5002

# Para saber que puertos tienes abiertos con el nmap:
nmap localhost

# Para cerrar algún puerto:
fuser -k "NºPuerto"/tcp



