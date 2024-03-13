from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash ,redirect

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos)

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)

##Rutas individuales 

@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html",
                            med = medico )
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                            pac = paciente )

@app.route("/citas/<int:id>")
def get_citas_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html",
                            cit = cita )

@app.route("/consultorio/<int:id>")
def get_consultorios_by_id(id):
    consultorio= Consultorio.query.get(id)
    return render_template("consultorio.html",
                            con = consultorio )

#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ "GET" , "POST"] )
def create_medico():
    ####### mostrar el formulario : get ###########
    if( request.method == "GET" ):
        #el usuario ingreso con navegador con https://localhost.....
        especialidades = [
            "Cardiologia",
            "Pediatria",
            "Oncologia"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades)

#### Cuando el usuario presiona el boton de guardar#####
#### los datos del formulario viajan al servidor
    
    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        new_medico = Medico(nombre = request.form["nombre"],
                            apellido = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect("/medicos")
    
@app.route("/medicos/update/<int:id>" , methods = [ "POST" , "GET"] )
def update_medicos(id):
    especialidades = [
            "Cardiologia",
            "Pediatria",
            "Oncologia"
        ]
    
    medico_update = Medico.query.get(id)
    if (request.method == "GET"):
        return render_template("medico_update.html" ,
                               medico_update = medico_update,
                               especialidades = especialidades)
    elif(request.method == "POST"):
        #actualizar el medico, con los datos del form 
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellido"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"] 
        db.session.commit()
        return "medico actualizado"     
    
@app.route("/pacientes/create" , methods = [ "GET" , "POST"] )
def create_paciente():
    ####### mostrar el formulario : get ###########
    if( request.method == "GET" ):
        #el usuario ingreso con navegador con https://localhost.....
        tipo_sangre = [
            "A+",
            "O+",
            "B+",
            "AB+",
            "A-",
            "O-",
            "B-",
            "AB-"
        ]
        return render_template("paciente_form.html",
                            tipo_sangre = tipo_sangre)

#### Cuando el usuario presiona el boton de guardar#####
#### los datos del formulario viajan al servidor
    
    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellido = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["ts"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_paciente)
        db.session.commit()
        flash("Paciente registrado correctamente")
        return redirect("/pacientes")
    
@app.route("/pacientes/update/<int:id>" , methods = [ "POST" , "GET"] )
def update_pacientes(id):
    tipo_sangre = [
            "A+",
            "O+",
            "B+",
            "AB+",
            "A-",
            "O-",
            "B-",
            "AB-"
        ]
    paciente_update = Paciente.query.get(id)
    if (request.method == "GET"):
        return render_template("paciente_update.html" ,
                               paciente_update = paciente_update,
                               tipo_sangre = tipo_sangre)
    elif(request.method == "POST"):
        #actualizar el medico, con los datos del form 
        paciente_update.nombre = request.form["nombre"]
        paciente_update.apellido = request.form["apellido"]
        paciente_update.tipo_identificacion = request.form["ti"]
        paciente_update.numero_identificacion = request.form["ni"]
        paciente_update.altura = request.form["al"]
        paciente_update.tipo_sangre = request.form["ts"] 
        db.session.commit()
        return "paciente actualizado"  

@app.route("/pacientes/delete/<int:id>")
def delete_pacientes(id):
    paciente_delete = Paciente.query.get(id)
    db.session.delete( paciente_delete)
    db.session.commit()
    return redirect("/pacientes")
    
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html",
                            con = consultorio )

@app.route("/consultorios/create" , methods = [ "GET" , "POST"] )
def create_consultorio():
    ####### mostrar el formulario : get ###########
    if( request.method == "GET" ):
        #el usuario ingreso con navegador con https://localhost.....
        numero = [
            "102",
            "203",
            "206"
        ]
        return render_template("consultorio_form.html",
                            numero = numero)
    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        new_consultorio = Consultorio(
                            numero = request.form["num"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_consultorio)
        db.session.commit()
        return "nuevo consultorio"

