from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_super_segura'  # Cambiala por una clave aleatoria

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Base de datos simulada de usuarios
users_db = {
    "1": {
        "id": "1",
        "username": "admin",
        "password": generate_password_hash("123456")
    }
}

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    user_data = users_db.get(user_id)
    if user_data:
        return User(id=user_data["id"], username=user_data["username"])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_found = None
        for uid, udata in users_db.items():
            if udata["username"] == username:
                user_found = udata
                break
                
        if user_found and check_password_hash(user_found["password"], password):
            user_obj = User(id=user_found["id"], username=user_found["username"])
            login_user(user_obj)
            return redirect(url_for('index'))
        else:
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

@app.route('/generar-ticket', methods=['POST'])
@login_required
def generar_ticket():
    data = request.get_json()
    return render_template('ticket.html', orden=data)

if __name__ == '__main__':
    app.run(debug=True)
