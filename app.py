from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/api/crear-orden', methods=['POST'])
def crear_orden():
    datos = request.json
    
    cliente = datos.get('cliente', {})
    vehiculo = datos.get('vehiculo', {})
    servicios = datos.get('servicios', [])
    repuestos = datos.get('repuestos', [])
    
    # Imprimir resumen claro en la consola para verificación
    print("\n" + "=" * 50)
    print("📋 NUEVA ORDEN REGISTRADA EN PYTHON")
    print("=" * 50)
    print(f"👤 CLIENTE : {cliente.get('nombre')} ({cliente.get('tipo_doc')}: {cliente.get('num_doc')})")
    print(f"📞 TELÉFONO: {cliente.get('telefono')} | CORREO: {cliente.get('correo')}")
    print(f"📍 DIRECCIÓN: {cliente.get('direccion')}")
    print("-" * 50)
    print(f"🚗 VEHÍCULO: {vehiculo.get('marca')} {vehiculo.get('modelo')} ({vehiculo.get('anio')})")
    print(f"🚘 PLACA   : {vehiculo.get('placa')} | KM: {vehiculo.get('km')} | COLOR: {vehiculo.get('color')}")
    print(f"⚙️ MOTOR   : {vehiculo.get('motor')} | CHASIS: {vehiculo.get('chasis')}")
    
    print("\n🛠️ SERVICIOS:")
    total_serv = 0
    for s in servicios:
        desc = s.get('descripcion', '')
        precio = float(s.get('precio', 0))
        print(f" - {desc} | S/ {precio:.2f}")
        total_serv += precio
        
    print("\n📦 REPUESTOS:")
    total_rep = 0
    for r in repuestos:
        desc = r.get('descripcion', '')
        precio = float(r.get('precio', 0))
        print(f" - {desc} | S/ {precio:.2f}")
        total_rep += precio
        
    subtotal = total_serv + total_rep
    igv = subtotal * 0.18
    total_final = subtotal + igv
    
    print("-" * 50)
    print(f"Subtotal Servicios: S/ {total_serv:.2f}")
    print(f"Subtotal Repuestos: S/ {total_rep:.2f}")
    print(f"SubTotal          : S/ {subtotal:.2f}")
    print(f"IGV (18%)         : S/ {igv:.2f}")
    print(f"TOTAL GENERAL     : S/ {total_final:.2f}")
    print("=" * 50 + "\n")
    
    return jsonify({
        "status": "success",
        "mensaje": f"¡Orden capturada correctamente para la placa {vehiculo.get('placa')}!"
    })

if __name__ == '__main__':
    print("🚀 Servidor MecanixPro corriendo en http://localhost:5000")
    app.run(debug=True, port=5000)