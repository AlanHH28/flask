from flask import Flask, render_template, request
import numpy as np
import joblib
import requests
from io import BytesIO

app = Flask(__name__)

# URL compartida de Google Drive (asegúrate de que sea pública y accesible)
drive_url = "https://drive.google.com/file/d/1Cgf9L8JzGeX3qkPLbYpHrnyeB10yldQE/view?usp=sharing"

# Función para cargar el modelo desde Google Drive
def load_model_from_drive(drive_url):
    response = requests.get(drive_url)
    model_content = BytesIO(response.content)
    model = joblib.load(model_content)
    return model

# Cargar el modelo desde Google Drive al iniciar la aplicación Flask
model = load_model_from_drive(drive_url)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los valores de x desde el formulario
    sqft_living = float(request.form['sqft_living'])
    grade = float(request.form['grade'])
    lat = float(request.form['lat'])
    long = float(request.form['long'])
    waterfront = float(request.form['waterfront'])
    view = float(request.form['view'])

    # Crear un arreglo numpy con los valores de entrada
    features = np.array([[sqft_living, grade, lat, long, waterfront, view]])

    # Realizar la predicción utilizando el modelo cargado desde Google Drive
    predicted_price = model.predict(features)

    # Mostrar el resultado en una nueva página
    return render_template('result.html', predicted_price=predicted_price)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Aquí puedes realizar cualquier acción adicional con los datos recibidos, como guardar en una base de datos
    return f"Nombre: {name}, Correo electrónico: {email}"

if __name__ == '__main__':
    app.run(debug=True)


#from flask import Flask, render_template, request

#app = Flask(__name__)

#@app.route('/')
#def home():
   # return render_template('index.html')

#@app.route('/submit', methods=['POST'])
#def submit():
#    name = request.form['name']
#    email = request.form['email']
#    return f"Nombre: {name}, Correo electrónico: {email}"

#if __name__ == '__main__':
#    app.run(debug=True)
