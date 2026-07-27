from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar-orden', methods=['POST'])
def generar_orden():
    # Recibe los datos JSON enviados desde el formulario web
    data = request.get_json()
    
    # Renderiza el ticket.html pasando los datos de la orden
    return render_template('ticket.html', orden=data)

if __name__ == '__main__':
    app.run(debug=True)
