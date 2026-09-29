@app.route('/api/repuestos-frecuentes')
@login_required
def repuestos_frecuentes():
    # Aquí puedes extraer de tu base de datos los servicios/repuestos únicos más usados o guardados
    # Por ahora, devolvemos una lista base combinada para que el autocompletado empiece a nutrirlos
    servicios_base = [
        "Afinamiento electrónico", "Mantenimiento preventivo 5,000 km", 
        "Mantenimiento preventivo 10,000 km", "Cambio de pastillas de freno", 
        "Diagnóstico con escáner automotriz", "Limpieza de inyectores", "Cambio de líquido de frenos"
    ]
    repuestos_base = [
        "Aceite sintético 5W-30 (Litro)", "Aceite semisintético 10W-40 (Litro)", 
        "Filtro de aceite estándar", "Filtro de aire de motor", 
        "Filtro de cabina / aire acondicionado", "Juego de pastillas de freno delanteras", 
        "Bujía de encendido convencional", "Limpiador de frenos (Spray)"
    ]
    return jsonify({
        "servicios": servicios_base,
        "repuestos": repuestos_base
    })
