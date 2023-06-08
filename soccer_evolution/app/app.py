
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
# URL DEFINED
from urllib.parse import urlparse

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
        carro_compras = carro_compras_dao['select_all']()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario,cc_vacio=cc_vacio)
        
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
        carro_compras = carro_compras_dao['select_all']()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('canchas/cancha_futbol.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_futbol=cancha_futbol,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('canchas/cancha_futbol.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_futbol=cancha_futbol, cc_vacio=cc_vacio)
    else:
        inicio_sesion = False
        cancha_futbol = cancha_futbol_dao['select_all']()
        return render_template('canchas/cancha_futbol.html', cancha_futbol=cancha_futbol)
    
@app.route('/cancha_basket')
def cancha_basket ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        cancha_basket = cancha_basket_dao['select_all']()
        carro_compras = carro_compras_dao['select_all']()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('canchas/cancha_basket.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_basket=cancha_basket,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('canchas/cancha_basket.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_basket=cancha_basket, cc_vacio=cc_vacio)
    else:
        inicio_sesion = False
        cancha_basket = cancha_basket_dao['select_all']()
        return render_template('canchas/cancha_basket.html', cancha_basket=cancha_basket)
    
@app.route('/cancha_tenis')
def cancha_tenis ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        cancha_tenis = cancha_tenis_dao['select_all']()
        carro_compras = carro_compras_dao['select_all']()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('canchas/cancha_tenis.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_tenis=cancha_tenis,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('canchas/cancha_tenis.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, cancha_tenis=cancha_tenis, cc_vacio=cc_vacio)
    else:
        inicio_sesion = False
        cancha_tenis = cancha_tenis_dao['select_all']()
        return render_template('canchas/cancha_tenis.html', cancha_tenis=cancha_tenis)
    
@app.route('/canchas')
def canchas ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        carro_compras = carro_compras_dao['select_all']()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('canchas/canchas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('canchas/canchas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario, cc_vacio=cc_vacio )
    else:
        inicio_sesion = False
        return render_template('canchas/canchas.html' )
    

@app.route('/otros')
def otros ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        
        carro_compras = carro_compras_dao['select_all']()
        print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('productos/otros.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('productos/otros.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario, cc_vacio=cc_vacio )
    else:
        inicio_sesion = False
        return render_template('productos/otros.html' )


@app.route('/pelotas', methods=['GET', 'POST'])
def pelotas():
        if request.method == 'POST':
            id_pelota = request.form['id_pelota']
            nombre_pelota = request.form['nombre_pelota']
            valor_pelota = request.form['valor_pelota']
            if 'username' in session:
                inicio_sesion = True
                id_usuario = session.get('id_usuario')
                pelotas = pelotas_dao['select_all']()
                producto_pelotas = {'nombre_producto': nombre_pelota, 'fecha': 0, 'hora_inicio':0, 'hora_fin': 0, 'valor_producto': valor_pelota, 'id_producto': id_pelota}
                nuevo_producto = carro_compras_dao['insert'](producto_pelotas)
                carro_compras = carro_compras_dao['select_all']()
                if carro_compras:
                    cur = mysql.connection.cursor()
                    cur.execute('SELECT COUNT(*) FROM carro_compras')
                    count_productos = cur.fetchone()[0]
                    cur.close()
                    return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, pelotas=pelotas,count_productos=count_productos)
                else:
                    cc_vacio = "El carro de compras está vacío"
                    return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, pelotas=pelotas, cc_vacio=cc_vacio)
            else:
                inicio_sesion = False
                pelotas = pelotas_dao['select_all']()
                return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, pelotas=pelotas)
        else:
            if 'username' in session:
                inicio_sesion = True
                id_usuario = session.get('id_usuario')
                pelotas = pelotas_dao['select_all']()
                carro_compras = carro_compras_dao['select_all']()
                print("AQUI ESTA EL CARRO DE COMPRAS: ", carro_compras)
                if carro_compras:
                    cur = mysql.connection.cursor()
                    cur.execute('SELECT COUNT(*) FROM carro_compras')
                    count_productos = cur.fetchone()[0]
                    cur.close()
                    return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, pelotas=pelotas,count_productos=count_productos)
                else:
                    cc_vacio = "El carro de compras está vacío"
                    return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, pelotas=pelotas, cc_vacio=cc_vacio)
            else:
                inicio_sesion = False
                pelotas = pelotas_dao['select_all']()
                return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, pelotas=pelotas)

@app.route('/camisetas', methods=['GET', 'POST'])
def camisetas ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        camisetas = camisetas_dao['select_all']()
        carro_compras = carro_compras_dao['select_all']()
        print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('productos/camisetas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,camisetas=camisetas,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('productos/camisetas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,camisetas=camisetas, cc_vacio=cc_vacio )
    else:
        inicio_sesion = False
        camisetas = camisetas_dao['select_all']()
        return render_template('productos/camisetas.html' ,camisetas=camisetas)
    


@app.route('/bebidas', methods=['GET', 'POST'])
def bebidas ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        bebidas = bebidas_dao['select_all']()
        carro_compras = carro_compras_dao['select_all']()
        print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            return render_template('productos/bebidas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,bebidas=bebidas,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('productos/bebidas.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,bebidas=bebidas, cc_vacio=cc_vacio )
    else:
        inicio_sesion = False
        bebidas = bebidas_dao['select_all']()
        return render_template('productos/bebidas.html',bebidas=bebidas )



@app.route('/campeonatos')
def campeonatos ():
    
    return render_template('canchas/campeonatos.html')

@app.route('/contacto')
def contacto ():
    return render_template('contacto.html')

@app.route('/quienes_somos')
def quienes_somos ():
    return render_template('/quienes_somos.html')

@app.route('/estacionamientos')
def estacionamientos ():
    return render_template('/estacionamientos.html')

@app.route('/carro_compras')
def carro_compras ():
    if 'username' in session:        
        inicio_sesion = True
        id_usuario = session.get('id_usuario')  
        carro_compras = carro_compras_dao['select_all']()
        print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras')
            count_productos = cur.fetchone()[0]
            cur.close()
            valor_total=0
            valor=0
            for row in carro_compras:
                valor= row['valor_producto']
                valor_total=valor_total+valor
            return render_template('carro_compras.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,productos=carro_compras,valor_total=valor_total,count_productos=count_productos)
        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('carro_compras.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,productos=[], cc_vacio=cc_vacio)
    
@app.route('/carro_compras/<int:id_carro>', methods=['DELETE'])
def eliminar_producto(id_carro):
    cur = mysql.connection.cursor()

    try:
        cur.execute("DELETE FROM carro_compras WHERE id_carro = %s", (id_carro,))
        mysql.connection.commit()
        response = {'message': 'Producto eliminado exitosamente'}
    except:
        mysql.connection.rollback()
        response = {'message': 'Error al eliminar el producto'}
    finally:
        cur.close()

    return jsonify(response)



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
tbl_horarios_columnas = ['id_horarios', 'inicio', 'termino']
horarios_dao = dao.dao_generic(app, mysql, tbl_horarios, tbl_horarios_columnas)

tbl_carro_compras = 'carro_compras'
tbl_carro_compras_columnas = ['id_carro', 'nombre_producto', 'fecha', 'hora_inicio', 'hora_fin', 'valor_producto', 'id_producto']
carro_compras_dao = dao.dao_generic(app, mysql, tbl_carro_compras, tbl_carro_compras_columnas)

tbl_pelotas = 'pelota'
tbl_pelotas_columnas = ['id_pelota', 'sku_pelota', 'nombre_pelota', 'imagen_pelota', 'valor_pelota', 'descripcion_pelota']
pelotas_dao = dao.dao_generic(app, mysql, tbl_pelotas, tbl_pelotas_columnas)

tbl_camisetas = 'camiseta'
tbl_camisetas_columnas = ['id_camiseta', 'sku_camiseta', 'nombre_camiseta', 'imagen_camiseta', 'valor_camiseta', 'descripcion_camiseta']
camisetas_dao = dao.dao_generic(app, mysql, tbl_camisetas, tbl_camisetas_columnas)

tbl_bebidas = 'bebida'
tbl_bebidas_columnas = ['id_bebida', 'sku_bebida', 'nombre_bebida', 'imagen_bebida', 'valor_bebida', 'descripcion_bebida']
bebidas_dao = dao.dao_generic(app, mysql, tbl_bebidas, tbl_bebidas_columnas)
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

@app.route('/arrendar', methods=['GET', 'POST'])
def arrendar ():
    if request.method == 'POST':
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        fecha = request.form['datepicker']
        if 'username' in session:
            inicio_sesion = True
            id_usuario = session.get('id_usuario')
            id_cancha = session['id_cancha']
            nombre_cancha = session['nombre_cancha']
            valor_cancha = session['valor_cancha']
            arriendo = {'nombre_producto': nombre_cancha, 'fecha': fecha, 'hora_inicio':hora_inicio, 'hora_fin': hora_fin, 'valor_producto': valor_cancha, 'id_producto': id_cancha}
            
            productos_carro = carro_compras_dao['select_all']()
            
            arriendo_existente = False

            print (" PRODUCTOS QUE YA ESTAN EN EL CARRO: ", productos_carro)
            print (" PRODUCTOS QUE NO ESTA EN EL CARRO: ", fecha, hora_inicio, hora_fin, id_cancha )
            for row in productos_carro:
                if (row['fecha'] == fecha and row['hora_inicio'] == hora_inicio and row['hora_fin'] == hora_fin and row['nombre_producto'] == nombre_cancha ):
                    arriendo_existente = True
                    break

            if arriendo_existente:
                print (" NOOOOOOO  HICE EL INSERT !!!!!!!!!!!!!!!!!")
                return 'Ya tienes el arriendo de esa cancha en la hora seleccionada en tu carrito'

            new_arriendo = carro_compras_dao['insert'](arriendo)
            print ("HICE EL INSERT !!!!!!!!!!!!!!!!!")
            return redirect(url_for('carro_compras'))
        else:
            return render_template('registro/login.html')
    else:
        if 'username' in session:
            inicio_sesion = True
            id_usuario = session.get('id_usuario')
            id_cancha = request.args.get('id_cancha')
            nombre_cancha = request.args.get('nombre_cancha')
            valor_cancha = request.args.get('valor_cancha')
            session['nombre_cancha'] = nombre_cancha
            session['valor_cancha'] = valor_cancha
            session['id_cancha'] = id_cancha
            horarios = horarios_dao['select_all']()

            carro_compras = carro_compras_dao['select_all']()
            print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
            if carro_compras:
                return render_template('arrendar.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,id_cancha=id_cancha,nombre_cancha=nombre_cancha, valor_cancha= valor_cancha, horarios=horarios)
            else:
                cc_vacio ="El carro de compras esta vacío"
                return render_template('arrendar.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,id_cancha=id_cancha,nombre_cancha=nombre_cancha, valor_cancha= valor_cancha, horarios=horarios, cc_vacio=cc_vacio)
                
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

        usuario = usuario_dao['select_all']()  # Elimina los corchetes cuadrados para llamar al método select_all()

        id_usuario = None
        correo = None
        password = None

        for row in usuario:
            id_usuario = row['id_usuario']
            correo = row['correo_usuario']
            password = row['password_usuario']
        
            # Verifica las credenciales (aquí puedes implementar tu lógica de autenticación)
            if password_login == password and username_login == correo:
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
        return 'Credenciales inválidas'  # Mueve el retorno al final del bucle for

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
        inicio_sesion = True
        return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_actualizado, id_usuario=id_usuario)
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
        print("ID del usuario:", id)
        usuario_2 = usuario_dao['select_by_id'](id)
        print("datos del usuario:", usuario_2)
        if 'username' in session:
            inicio_sesion=True
            if usuario_2:
                print("ENTRO AL IF")
                id_usuario = session.get('id_usuario')
                carro_compras = carro_compras_dao['select_all']()
                print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
                if carro_compras:
                    return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_2, id_usuario=id_usuario)
                else:
                    cc_vacio ="El carro de compras esta vacío"
                    return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_2, id_usuario=id_usuario,cc_vacio=cc_vacio)

              
            #render_template('registro/perfil_usuario.html', usuarios=usuario_2, id_usuario=id_usuario)
        else:
            return "Usuario no encontrado"


######FIN PERFIL USUARIO#######

#@app.route('/comunas')
##def listar_comunas ():
  #  comunas = comuna_dao['select_all']()
   # print('comunas: ', comunas)
    #return render_template('comunas.html', comunas=comunas)

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



###### CARRO COMPRAS ###############



############## TRANSBANK ####################

@app.route('/transbank/commit-pay', methods=['GET', 'POST'])
def transbank_commit_pay():
    # SE DEBE APLICAR ESTA DESCOMENTAR ESTA SECCIÓN Y AGREGAR LÓGICA PARA LA RESPUESTA RECIBIDA EN EL RESPONSE
    # DE SER CORRECTA SE DEBE CONFIRMAR Y MOSTRAR VOUCHER
    # EN CASO CONTRARIO SE DEBE CANCELAR Y MOSTRAR ERROR 
    tokenws = request.args.get('token_ws')
    print('tokenws: ', tokenws)
    ## DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}".format(tokenws)
    ## CABECERA SOLICITADA POR TRANSBANK
    headers = header_request_transbank()
    ## INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK   

    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()  # Verificar si la respuesta es exitosa

        data = response.json()
        status = data['status']
        monto = data['amount']

        if status == "AUTHORIZED" or status == "FAILED":
            titulo = ""

            if status == "AUTHORIZED":
                titulo = "DETALLE DEL PAGO"

            else:
                titulo = "ERROR PAGO RECHAZADO."


            ordenCompra = data['buy_order']
            tarjeta = data['card_detail']['card_number']
            tipoTarjeta = ""

            if data['payment_type_code'] == 'VD':
                tipoTarjeta = "Débito"
            elif data['payment_type_code'] in ['BV', 'VC', 'YES', 'S2', 'NC']:
                tipoTarjeta = "Crédito"
            elif data['payment_type_code'] == 'PV':
                tipoTarjeta = "Débito Prepago"
                reversOrCancel(tokenws, monto)
                return render_template('transbank/payment_error.html', dataHTML=dataHTML)

            session = data['session_id']
            fecha = data['transaction_date']

            dataHTML ={'titulo': titulo, 'tarjeta': tarjeta, 'tipo_tarjeta': tipoTarjeta,'fecha': fecha,
                        'orden_de_compra': ordenCompra,'session': session,'monto': monto,'estado': status}
            
            return render_template('transbank/commit_pay.html', dataHTML=dataHTML)

        else:
            reversOrCancel(tokenws, monto)
            return render_template('transbank/payment_error.html', dataHTML=dataHTML)

    except requests.exceptions.RequestException as err:
        print('ERROR:', err)
        return render_template('transbank/payment_error.html', dataHTML='')

def reversOrCancel(tokenws, amount):
    url = f"http://127.0.0.1:8900/api/v1/transbank/transaction/reverse-or-cancel/{tokenws}"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    payload = {
        'amount': amount
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Verificar si la respuesta es exitosa

        data = response.json()
        tipo = data['type']
        codigoAutorizacion = data['authorization_code']
        fechaAutorizacion = data['authorization_date']
        montoAnulado = data['nullified_amount']
        balance = data['balance']
        codigo = data['response_code']

        dataHTML = {'tipo': tipo,'codigo_autorizacion': codigoAutorizacion,'fecha_autorizacion':fechaAutorizacion,
                    'monto_anulado':montoAnulado,'monto_pendiente':balance,'codigo_respuesta':codigo}

        return render_template('transbank/payment_error.html', dataHTML=dataHTML)

    except requests.exceptions.RequestException as err:
        print('ERROR:', err)
        return render_template('transbank/payment_error.html', dataHTML='')

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
    print('request.form: ', request.form)
    amount = request.form.get('amount')
    session_id = '2334567' # ID SESSION
    buy_order = request.form.get('buyorder')
    object_url = urlparse(request.base_url)
    return_url = '{0}://{1}/transbank/commit-pay'.format(object_url.scheme, object_url.netloc)
    print('return_url:', return_url)

    # LECTURA DE PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
    print('headers: ', request.headers)
    data = {
            'buy_order': buy_order,
            'session_id': session_id,
            'amount': amount,
            'return_url': return_url
    }
    print('data: ', data)
    # DEFINICIÓN DE URL DE TRANSBANK PARA CREAR UNA TRANSACCIÓN
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    # CABECERA SOLICITADA POR TRANSBANK
    headers = header_request_transbank()
    # INVOCACIÓN POR POST A API REST QUE CREA UNA TRANSACCIÓN EN TRANSBANK
    response = requests.post(url, json = data, headers=headers)
    response_json = response.json()
    token = response_json['token']
    url = response_json['url']
    print('token: ', token)
    print('url: ', url)
    # RETORNO DE LA RESPUESTA DE TRANSBANK
    return render_template('transbank/send_pay.html', url=url, token=token)

# DEFINICIÓN DE RUTA API REST CON UN PARAMETRO DE ENTRADA (tokenws) EN EL PATH, PERMITIENDO SOLO SER LLAMADO POR GET
#@app.route('/api/v1/transbank/transaction/commit/<string:tokenws>', methods=['PUT'])
#def transbank_commit(tokenws):
#    print('tokenws: ', tokenws)
#    # DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
#    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}".format(tokenws)
#    # CABECERA SOLICITADA POR TRANSBANK
#    headers = header_request_transbank()
#    # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK    
#    response = requests.put(url, headers=headers)
#    print('response: ', response.json())
#    # RETORNO DE LA RESPUESTA DE TRANSBANK
#    return response.json()
#
## DEFINICIÓN DE RUTA API REST CON UN PARAMETRO DE ENTRADA (tokenws, amount) EN EL PATH, PERMITIENDO SOLO SER LLAMADO POR POST
#@app.route('/api/v1/transbank/transaction/reverse-or-cancel/<string:tokenws>', methods=['POST'])
#def transbank_reverse_or_cancel(tokenws):
#    print('tokenws: ', tokenws)
#    # LECTURA DE PAYLOAD (BODY) CON INFORMACIÓN DE TIPO JSON
#    data = request.json
#    print('data: ', data)
#    # DEFINICIÓN DE URL DE TRANSBANK PARA CONFIRMAR UNA TRANSACCIÓN
#    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{0}/refunds".format(tokenws)
#    # CABECERA SOLICITADA POR TRANSBANK
#    headers = header_request_transbank()
#    # INVOCACIÓN POR GET A API REST QUE CONFIRMA UNA TRANSACCIÓN EN TRANSBANK    
#    response = requests.post(url, json = data, headers=headers)
#    print('response: ', response.json())
#    # RETORNO DE LA RESPUESTA DE TRANSBANK
#    return response.json()       



################# FIN TRANSBANK ###################


if __name__=='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=os.getenv('APP_PORT'))



