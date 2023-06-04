
from flask import Flask, render_template, jsonify, request, redirect, session, url_for
from flask_cors import CORS
# IMPORT MYSQL LIB CONNECTION
from flask_mysqldb import MySQL
# IMPORT LIB OPERATION SYSTEM
import os
# IMPORT LOAD ENVIRONMENT (FILE .env)
from dotenv import load_dotenv
load_dotenv()
# IMPORT GENERIC DAO
from dao import dao
import requests

app =Flask(__name__)
app.secret_key = 'Lion333' 

CORS(app)
# SE HABILITA ACCESO PARA API DESDE EL ORIGEN http://127.0.0.1:5500 (PÁGINA WEB EN HTML + JAVASCRIPT [FRONT END])
cors = CORS(app, resource={
    # RUTA O RUTAS HABILTADAS PARA EL ORIGEN http://127.0.0.1:5500
    r"/api/v1/transbank/*":{
        "origins":"http://127.0.0.1:5500"
    }
})


# CONNECTION DATABASE
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DATABASE')
mysql = MySQL(app)

@app.route('/')
def index ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario)
    else:
        inicio_sesion = False
        return render_template('index.html')
    #return redirect(url_for('index', inicio_sesion=inicio_sesion))

@app.route('/cancha_futbol')
def cancha_futbol ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        cancha_futbol = cancha_futbol_dao['select_all']()
        print (cancha_futbol)
        return render_template('canchas/cancha_futbol.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_futbol=cancha_futbol)
    else:
        inicio_sesion = False
        return render_template('canchas/cancha_futbol.html')
    
@app.route('/cancha_basket')
def cancha_basket ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        cancha_basket = cancha_basket_dao['select_all']()
        print (cancha_basket)
        return render_template('canchas/cancha_basket.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_basket=cancha_basket)
    
@app.route('/cancha_tenis')
def cancha_tenis ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        cancha_tenis = cancha_tenis_dao['select_all']()
        print (cancha_tenis)
        return render_template('canchas/cancha_tenis.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_tenis=cancha_tenis)
    
@app.route('/canchas')
def canchas ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        return render_template('canchas/canchas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario)
    else:
        inicio_sesion = False
        return render_template('canchas/canchas.html')

@app.route('/campeonatos')
def campeonatos ():
    return render_template('canchas/campeonatos.html')

@app.route('/contacto')
def contacto ():
    return render_template('contacto.html')

@app.route('/carro_compras')
def carro_compras ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')

        return render_template('carro_compras.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario)
    
@app.route('/canchas')


def pagina_no_encontrada(error):
    return render_template('404.html'), 404


# LOAD GENERIC DAO FOR COMUNAS
tbl_comunas = 'comunas'
tbl_comunas_columnas = ['id_comuna', 'comuna', 'id_provincia']
comuna_dao = dao.dao_generic(app, mysql, tbl_comunas, tbl_comunas_columnas)

tbl_usuario = 'usuario'
tbl_usuario_columnas = ['id_usuario', 'nombre_usuario', 'apellido_usuario','correo_usuario','password_usuario','telefono_usuario','direccion_usuario']
usuario_dao = dao.dao_generic(app, mysql, tbl_usuario, tbl_usuario_columnas)

tbl_arriendo = 'arriendo'
tbl_arriendo_columnas = ['id_arriendo', 'fecha_arriendo', 'hora_arriendo','valor_arriendo','id_cliente','id_cancha',]
arriendo_dao = dao.dao_generic(app, mysql, tbl_arriendo, tbl_arriendo_columnas)

tbl_cancha_futbol = 'cancha_futbol'
tbl_cancha_futbol_columnas = ['id_cancha_futbol', 'nombre_cancha_futbol', 'descripcion_cancha_futbol','valor_cancha_futbol', 'img_cancha_futbol']
cancha_futbol_dao = dao.dao_generic(app, mysql, tbl_cancha_futbol, tbl_cancha_futbol_columnas)

tbl_cancha_basket = 'cancha_basket'
tbl_cancha_basket_columnas = ['id_cancha_basket', 'nombre_cancha_basket', 'descripcion_cancha_basket','valor_cancha_basket', 'img_cancha_basket']
cancha_basket_dao = dao.dao_generic(app, mysql, tbl_cancha_basket, tbl_cancha_basket_columnas)

tbl_cancha_tenis = 'cancha_tenis'
tbl_cancha_tenis_columnas = ['id_cancha_tenis', 'nombre_cancha_tenis', 'descripcion_cancha_tenis','valor_cancha_tenis', 'img_cancha_tenis']
cancha_tenis_dao = dao.dao_generic(app, mysql, tbl_cancha_tenis, tbl_cancha_tenis_columnas)

tbl_horarios = 'horarios'
tbl_horarios_columnas = ['id_horarios', 'franja_horarios']
horarios_dao = dao.dao_generic(app, mysql, tbl_horarios, tbl_horarios_columnas)
#________________________________________________
#se tienen los métodos:
# BUSCAR TODOS
# comunas = comuna_dao['select_all']()
# print('comunas: ', comunas)
#________________________________________________
# INSERTAR
# comuna = {'comuna': 'nueva comuna', 'id_provincia': 1}
# new_comuna = comuna_dao['insert'](comuna)
# print('new_comuna: ', new_comuna)
#________________________________________________
# UPDATE
# comuna = {'id_comuna': 1, 'comuna': 'actualizar comuna', 'id_provincia': 1}
# update_comuna = comuna_dao['update'](comuna)
# print('update_comuna: ', update_comuna)
#________________________________________________
# BUSCAR POR ID
# id = 1
# comuna = comuna_dao['select_by_id'](id)
# print('comuna: ', comuna)
#________________________________________________
# BORRAR POR ID
# id = 1
# comuna = comuna_dao['delete_by_id'](id)
# print('comuna {0} eliminada.'.format(id))
#________________________________________________

#### ARRENDAR CANCHA  ######
@app.route('/arrendar/')
def arrendar ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        id_cancha = request.args.get('id_cancha')
        nombre_cancha = request.args.get('nombre_cancha')
        valor_cancha = request.args.get('valor_cancha')
        horarios = horarios_dao['select_all']()
        
        return render_template('arrendar.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,id_cancha=id_cancha,nombre_cancha=nombre_cancha, valor_cancha= valor_cancha, horarios=horarios)
    else:
        return render_template('registro/login.html')
#### FIN ARRENDAR CANCHA  ######

###### REGISTER #######
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        apellido_usuario = request.form['apellido_usuario']
        correo_usuario = request.form['correo_usuario']
        password_usuario = request.form['password_usuario']
        telefono_usuario = request.form['telefono_usuario']
        direccion_usuario = request.form['direccion_usuario']

        usuario = { 'nombre_usuario': nombre_usuario, 'apellido_usuario': apellido_usuario, 
                    'correo_usuario': correo_usuario, 'password_usuario': password_usuario, 
                    'telefono_usuario': telefono_usuario, 'direccion_usuario': direccion_usuario }
        new_usuario = usuario_dao['insert'](usuario)
        print('new_usuario: ', new_usuario)

        session['nombre_usuario'] = nombre_usuario  # Inicia sesión automáticamente después del registro
        return redirect('/index')  # Redirige al usuario al panel de control después del registro

    return render_template('Registro/registro.html')

###### FIN REGISTER #######

###### LOGIN #######

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_login = request.form['correo_login']
        password_login = request.form['contraseña_login']

        usuario = usuario_dao['select_all']()

        id_usuario = None
        correo = None
        password = None

        for row in usuario:
            
            id_usuario = row['id_usuario']
            correo = row['correo_usuario']
            password = row['password_usuario']
        
        # Verifica las credenciales (aquí puedes implementar tu lógica de autenticación)
        if  password_login == password and username_login == correo:
            
            session['username'] = username_login
            session['id_usuario'] = id_usuario
            if 'username' in session:
            # El usuario ha iniciado sesión
                username_login = session['username']
                id_usuario_login = session['id_usuario']
                return redirect(url_for('index', id_usuario=id_usuario_login))
            else:
                # El usuario no ha iniciado sesión
                return 'Inicia sesión para continuar'
        
        # return redirect(url_for('layout', usuario_incia=usuario_iniciado_sesion))
        else:
            return 'Credenciales inválidas'

    return render_template('registro/login.html')

@app.route('/dashboard')
def dashboard():
    # Verifica si el usuario ha iniciado sesión
    if 'username' in session:
        username = session['username']
        return f'Bienvenido, {username}!'
    else:
        return redirect('registro/login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('id_usuario', None)
    return redirect('/')

######FIN LOGIN#######

######LISTA USUARIO#######

@app.route('/lista_usuarios')
def lista_usuarios ():
    usuarios = usuario_dao['select_all']()
    return render_template('registro/lista_usuarios.html', usuarios=usuarios)

######FIN LISTA USUARIO#######

######EDITAR USUARIO#######

@app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
def editar_usuarios (id):
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        nombre_usuario = request.form['nombre_usuario']
        apellido_usuario = request.form['apellido_usuario']
        correo_usuario = request.form['correo_usuario']
        password_usuario = request.form['password_usuario']
        telefono_usuario = request.form['telefono_usuario']
        direccion_usuario = request.form['direccion_usuario']

        usuario = { 'id_usuario':id_usuario, 'nombre_usuario': nombre_usuario, 'apellido_usuario': apellido_usuario, 
                'correo_usuario': correo_usuario, 'password_usuario': password_usuario, 
                'telefono_usuario': telefono_usuario, 'direccion_usuario': direccion_usuario }
        
        usuario_actualizado = usuario_dao['update'](usuario)
        print('Usuario actualizado correctamente', usuario_actualizado)

        return redirect(url_for('lista_usuarios'))
    else:
        print("ID del usuario:", id)
        usuario_2 = usuario_dao['select_by_id'](id)
        print("datos del usuario:", usuario_2)
        if usuario_2:
            print("ENTRO AL IF")
            return render_template('registro/editar_usuario.html', usuarios=usuario_2)
            
        else:
            return "Usuario no encontrado"

# PERFIL USUARIO

@app.route('/perfil_usuario/<int:id>', methods=['GET', 'POST'])
def perfil_usuario (id):
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        nombre_usuario = request.form['nombre_usuario']
        apellido_usuario = request.form['apellido_usuario']
        correo_usuario = request.form['correo_usuario']
        password_usuario = request.form['password_usuario']
        telefono_usuario = request.form['telefono_usuario']
        direccion_usuario = request.form['direccion_usuario']

        usuario = { 'id_usuario':id_usuario, 'nombre_usuario': nombre_usuario, 'apellido_usuario': apellido_usuario, 
                'correo_usuario': correo_usuario, 'password_usuario': password_usuario, 
                'telefono_usuario': telefono_usuario, 'direccion_usuario': direccion_usuario }
        print('Usuario antes de actualizar ', usuario)
        usuario_actualizado = usuario_dao['update'](usuario)
        print('Usuario actualizado correctamente', usuario_actualizado)
        return redirect(url_for('lista_usuarios'))
    else:
        print("ID del usuario:", id)
        usuario_2 = usuario_dao['select_by_id'](id)
        print("datos del usuario:", usuario_2)
        if 'username' in session:
            inicio_sesion=True
            if usuario_2:
                print("ENTRO AL IF")
                id_usuario = session.get('id_usuario')
                return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_2, id_usuario=id_usuario)
            #render_template('registro/perfil_usuario.html', usuarios=usuario_2, id_usuario=id_usuario)
        else:
            return "Usuario no encontrado"


######FIN PERFIL USUARIO#######

@app.route('/comunas')
def listar_comunas ():
    comunas = comuna_dao['select_all']()
    print('comunas: ', comunas)
    return render_template('comunas.html', comunas=comunas)

@app.route('/agregar_trabajador', methods=['GET', 'POST'])
def agregar_trabajador():
    if request.method == 'POST':
    # Aquí puedes procesar los datos del formulario enviado
        nombre = request.form['nombre_trabajador']
        print (nombre )
        apellido = request.form['apellido_trabajador']
        email = request.form['email_trabajador']
        password = request.form['password_trabajador']
        telefono = request.form['telefono_trabajador']
        direccion = request.form['direccion_trabajador']
        # Realiza alguna lógica con los datos recibidos

        # Muestra una página de éxito o redirige a otra página
        return nombre
    # Si es un GET, muestra el formulario
    return render_template('trabajador/agregar_trabajador.html')


############## TRANSBANK ####################


# MÉTODO QUE CREA LA CABECERA SOLICITADA POR TRANSBANK EN UN REQUEST (SOLICITUD)
def header_request_transbank():
    headers = { # DEFINICIÓN TIPO DE AUTORIZACIÓN Y AUTENTICACIÓN
                "Authorization": "Token",
                # LLAVE QUE DEBE SER MODIFICADA PORQUE ES SOLO DEL AMBIENTE DE INTEGRACIÓN DE TRANSBANK (PRUEBAS)
                "Tbk-Api-Key-Id": "597055555532",
                # LLAVE QUE DEBE SER MODIFICADA PORQUE DEL AMBIENTE DE INTEGRACIÓN DE TRANSBANK (PRUEBAS)
                "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
                # DEFINICIÓN DEL TIPO DE INFORMACIÓN ENVIADA
                "Content-Type": "application/json",
                # DEFINICIÓN DE RECURSOS COMPARTIDOS ENTRE DISTINTOS SERVIDORES PARA CUALQUIER MÁQUINA
                "Access-Control-Allow-Origin": "*",
                'Referrer-Policy': 'origin-when-cross-origin',
                } 
    return headers   

# DEFINICIÓN DE RUTA API REST, PERMITIENDO SOLO SER LLAMADO POR POST
@app.route('/api/v1/transbank/transaction/create', methods=['POST'])
def transbank_create():
    # LECTURA DE PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
    print('headers: ', request.headers)
    data = request.json
    print('data: ', data)
    # DEFINICIÓN DE URL DE TRANSBANK PARA CREAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    # CABECERA SOLICITADA POR TRANSBANK
    headers = header_request_transbank()
    # INVOCACIÓN POR POST A API REST QUE CREA UNA TRANSACCIÓN EN TRANSBANK
    response = requests.post(url, json = data, headers=headers)
    print('response: ', response.json())
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return response.json()

# DEFINICIÓN DE RUTA API REST CON UN PARAMETRO DE ENTRADA (tokenws) EN EL PATH, PERMITIENDO SOLO SER LLAMADO POR GET
@app.route('/api/v1/transbank/transaction/commit/<string:tokenws>', methods=['PUT'])
def transbank_commit(tokenws):
    print('tokenws: ', tokenws)
    # DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}".format(tokenws)
    # CABECERA SOLICITADA POR TRANSBANK
    headers = header_request_transbank()
    # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK    
    response = requests.put(url, headers=headers)
    print('response: ', response.json())
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return response.json()

# DEFINICIÓN DE RUTA API REST CON UN PARAMETRO DE ENTRADA (tokenws, amount) EN EL PATH, PERMITIENDO SOLO SER LLAMADO POR POST
@app.route('/api/v1/transbank/transaction/reverse-or-cancel/<string:tokenws>', methods=['POST'])
def transbank_reverse_or_cancel(tokenws):
    print('tokenws: ', tokenws)
    # LECTURA DE PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
    data = request.json
    print('data: ', data)
    # DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}/refunds".format(tokenws)
    # CABECERA SOLICITADA POR TRANSBANK
    headers = header_request_transbank()
    # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK    
    response = requests.post(url, json = data, headers=headers)
    print('response: ', response.json())
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return response.json()       



################# FIN TRANSBANK ###################


if __name__=='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=os.getenv('APP_PORT'))



