from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Base de datos simulada de usuarios (ajusta según lo que tengas configurado)
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Usuarios de prueba o conectados a tu base de datos
usuarios_db = {
    "admin": User("1", "admin", "123456")
}

@login_manager.user_loader
def load_user(user_id):
    for u in usuarios_db.values():
        if u.id == user_id:
            return u
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in usuarios_db and usuarios_db[username].password == password:
            login_user(usuarios_db[username])
            return redirect(url_for('index'))
        flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Base de datos simulada o real de vehículos por placa
vehiculos_db = {
    "ABC-123": {
        "vehiculo": {
            "placa": "ABC-123",
            "marca": "Toyota",
            "modelo": "Corolla",
            "anio": "2020",
            "km": "45000",
            "color": "Plata",
            "chasis": "1NXBR32E...",
            "motor": "2ZR-FE..."
        },
        "cliente": {
            "tipo_doc": "DNI",
            "num_doc": "12345678",
            "nombre": "Juan Pérez",
            "telefono": "987654321",
            "correo": "juan@example.com",
            "direccion": "Av. Principal 123"
        }
    }
}

@app.route('/buscar-vehiculo/<placa>')
@login_required
def buscar_vehiculo(placa):
    placa_limpia = placa.strip().upper()
    if placa_limpia in vehiculos_db:
        return jsonify({"encontrado": True, "datos": vehiculos_db[placa_limpia]})
    return jsonify({"encontrado": False})

@app.route('/generar-ticket', methods=['POST'])
@login_required
def generar_ticket():
    data = request.json
    # Aquí procesas la orden y guardas la placa en tu base de datos si deseas
    placa = data.get('vehiculo', {}).get('placa', '').upper()
    if placa:
        vehiculos_db[placa] = data  # Guarda o actualiza en memoria/base de datos

    # Renderiza la vista del ticket para imprimir
    return render_template('ticket.html', orden=data)

if __name__ == '__main__':
    app.run(debug=True)
