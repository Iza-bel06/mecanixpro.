from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/generar", methods=["POST"])
def generar():
  # Recoger los datos del formulario
  datos = {
      "tipo_doc": request.form.get("tipo_doc"),
      "n_doc": request.form.get("n_doc"),
      "cliente": request.form.get("cliente"),
      "telefono": request.form.get("telefono"),
      "correo": request.form.get("correo"),
      "direccion": request.form.get("direccion"),
      "placa": request.form.get("placa"),
      "marca": request.form.get("marca"),
      "modelo": request.form.get("modelo"),
      "anio": request.form.get("anio"),
      "kilometraje": request.form.get("kilometraje"),
      "color": request.form.get("color"),
      "chasis": request.form.get("chasis"),
      "motor": request.form.get("motor"),
  }

  # Recoger listas dinamicas de servicios y repuestos
  servicios_desc = request.form.getlist("servicio_desc[]")
  servicios_imp = request.form.getlist("servicio_imp[]")
  servicios = list(zip(servicios_desc, servicios_imp))

  repuestos_desc = request.form.getlist("repuesto_desc[]")
  repuestos_imp = request.form.getlist("repuesto_imp[]")
  repuestos = list(zip(repuestos_desc, repuestos_imp))

  # Calcular totales
  total_servicios = sum(
      float(imp) for imp in servicios_imp if imp.replace(".", "", 1).isdigit()
  )
  total_repuestos = sum(
      float(imp) for imp in repuestos_imp if imp.replace(".", "", 1).isdigit()
  )
  total_general = total_servicios + total_repuestos

  return render_template(
      "ticket.html",
      datos=datos,
      servicios=servicios,
      repuestos=repuestos,
      total_servicios=total_servicios,
      total_repuestos=total_repuestos,
      total_general=total_general,
  )


if __name__ == "__main__":
  app.run(debug=True)
