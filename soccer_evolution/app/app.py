
from flask import Flask, make_response, render_template, jsonify, request, redirect, session, url_for, flash
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
from mail_3 import send_outlook3
from mail_2 import send_outlook2
from mail import send_outlook
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

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
        print ("EL USER ESTA EN LA SESSION: " )
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        usuario = session.get('username')
        nombre_usuario=session.get('nombre_usuario')
        if usuario == 'admin@gmail.com':
            print ("EL ADMIN ESTA EN EL LA SESSION: " )
            admin =True
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
            rows = cur.fetchall()
            carro_compras = []
            print('rows: ', rows)
            for row in rows:
                carrito_producto = {
                'id_carro' : row[0],
                'nombre_producto' : row[1],
                'fecha' : row[2],
                'hora_inicio' : row[3],
                'hora_fin' : row[4],
                'valor_producto' : row[5],
                'id_producto' : row[6],
                'id_cliente' : row[7]
                }
                carro_compras.append(carrito_producto)
            cur.close()
            if carro_compras:
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                count_productos = cur.fetchone()[0]
                cur.close()

                return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario,count_productos=count_productos, admin = admin)
            else:
                cc_vacio ="El carro de compras esta vacío"
                return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario,cc_vacio=cc_vacio,admin = admin)
        else:
            admin =False
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
            rows = cur.fetchall()
            carro_compras = []
            print('rows: ', rows)
            for row in rows:
                carrito_producto = {
                'id_carro' : row[0],
                'nombre_producto' : row[1],
                'fecha' : row[2],
                'hora_inicio' : row[3],
                'hora_fin' : row[4],
                'valor_producto' : row[5],
                'id_producto' : row[6],
                'id_cliente' : row[7]
                }
                carro_compras.append(carrito_producto)
            cur.close()
            if carro_compras:
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                count_productos = cur.fetchone()[0]
                cur.close()

                return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario,count_productos=count_productos,nombre_usuario=nombre_usuario)
            else:
                cc_vacio ="El carro de compras esta vacío"
                return render_template('index.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario,cc_vacio=cc_vacio, nombre_usuario=nombre_usuario)
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
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
        rows = cur.fetchall()
        carro_compras = []
        print('rows: ', rows)
        for row in rows:
            carrito_producto = {
            'id_carro' : row[0],
            'nombre_producto' : row[1],
            'fecha' : row[2],
            'hora_inicio' : row[3],
            'hora_fin' : row[4],
            'valor_producto' : row[5],
            'id_producto' : row[6],
            'id_cliente' : row[7]
            }
            carro_compras.append(carrito_producto)
        cur.close()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
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
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
        rows = cur.fetchall()
        carro_compras = []
        print('rows: ', rows)
        for row in rows:
            carrito_producto = {
            'id_carro' : row[0],
            'nombre_producto' : row[1],
            'fecha' : row[2],
            'hora_inicio' : row[3],
            'hora_fin' : row[4],
            'valor_producto' : row[5],
            'id_producto' : row[6],
            'id_cliente' : row[7]
            }
            carro_compras.append(carrito_producto)
        cur.close()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
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
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
        rows = cur.fetchall()
        carro_compras = []
        print('rows: ', rows)
        for row in rows:
            carrito_producto = {
            'id_carro' : row[0],
            'nombre_producto' : row[1],
            'fecha' : row[2],
            'hora_inicio' : row[3],
            'hora_fin' : row[4],
            'valor_producto' : row[5],
            'id_producto' : row[6],
            'id_cliente' : row[7]
            }
            carro_compras.append(carrito_producto)
        cur.close()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
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
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
        rows = cur.fetchall()
        carro_compras = []
        print('rows: ', rows)
        for row in rows:
            carrito_producto = {
            'id_carro' : row[0],
            'nombre_producto' : row[1],
            'fecha' : row[2],
            'hora_inicio' : row[3],
            'hora_fin' : row[4],
            'valor_producto' : row[5],
            'id_producto' : row[6],
            'id_cliente' : row[7]
            }
            carro_compras.append(carrito_producto)
        cur.close()

        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
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
        
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
        rows = cur.fetchall()
        carro_compras = []
        print('rows: ', rows)
        for row in rows:
            carrito_producto = {
            'id_carro' : row[0],
            'nombre_producto' : row[1],
            'fecha' : row[2],
            'hora_inicio' : row[3],
            'hora_fin' : row[4],
            'valor_producto' : row[5],
            'id_producto' : row[6],
            'id_cliente' : row[7]
            }
            carro_compras.append(carrito_producto)
        cur.close()
        print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
        if carro_compras:
            cur = mysql.connection.cursor()
            cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
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
            data = request.get_json()  # Obtener los datos enviados en formato JSON
            id_pelota = data['id_pelota']
            nombre_pelota = data['nombre_pelota']
            valor_pelota = data['valor_pelota']
            img_pelota = data['img_pelota']
            if 'username' in session:
                inicio_sesion = True
                id_usuario = session.get('id_usuario')
                pelotas = pelotas_dao['select_all']()
                producto_pelotas = {'nombre_producto': nombre_pelota, 'fecha': 0, 'hora_inicio':0, 'hora_fin': 0, 'valor_producto': valor_pelota, 'id_producto': id_pelota,'id_cliente':id_usuario, 'img_producto': img_pelota}
                nuevo_producto = carro_compras_dao['insert'](producto_pelotas)
                bandera = 0
                if nuevo_producto:
                    return jsonify(bandera=bandera)
                else:
                    bandera = 1
                    return jsonify(bandera=bandera)
            else:
                inicio_sesion = False
                pelotas = pelotas_dao['select_all']()
                return render_template('productos/pelotas.html', inicio_sesion=inicio_sesion, pelotas=pelotas)
        else:
            if 'username' in session:
                inicio_sesion = True
                id_usuario = session.get('id_usuario')
                pelotas = pelotas_dao['select_all']()
                cur = mysql.connection.cursor()
                cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                rows = cur.fetchall()
                carro_compras = []
                print('rows: ', rows)
                for row in rows:
                    carrito_producto = {
                    'id_carro' : row[0],
                    'nombre_producto' : row[1],
                    'id_cliente' : row[2],
                    'hora_inicio' : row[3],
                    'hora_fin' : row[4],
                    'valor_producto' : row[5],
                    'id_producto' : row[6],
                    'id_cliente' : row[7]
                    }
                    carro_compras.append(carrito_producto)
                cur.close()
                print ("carro_compras: ", carro_compras)
                if  carro_compras:
                    cur = mysql.connection.cursor()
                    cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
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
    if request.method == 'POST':
            data = request.get_json()  # Obtener los datos enviados en formato JSON
            id_camiseta = data['id_camiseta']
            nombre_camiseta = data['nombre_camiseta']
            valor_camiseta = data['valor_camiseta']
            img_camiseta = data['img_camiseta']
            if 'username' in session:
                inicio_sesion = True
                id_usuario = session.get('id_usuario')
                camisetas = camisetas_dao['select_all']()
                producto_camisetas = {'nombre_producto': nombre_camiseta, 'fecha': 0, 'hora_inicio':0, 'hora_fin': 0, 'valor_producto': valor_camiseta, 'id_producto': id_camiseta,'id_cliente':id_usuario, 'img_producto':img_camiseta}
                nuevo_producto = carro_compras_dao['insert'](producto_camisetas)
                bandera = 0
                if nuevo_producto:
                    return jsonify(bandera=bandera)
                else:
                    bandera = 1
                    return jsonify(bandera=bandera)
            else:
                inicio_sesion = False
                camisetas = camisetas_dao['select_all']()
                return render_template('productos/camisetas.html', inicio_sesion=inicio_sesion, camisetas=camisetas)
    else:
        if 'username' in session:
            inicio_sesion = True
            id_usuario = session.get('id_usuario')
            camisetas = camisetas_dao['select_all']()
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
            rows = cur.fetchall()
            carro_compras = []
            print('rows: ', rows)
            for row in rows:
                carrito_producto = {
                'id_carro' : row[0],
                'nombre_producto' : row[1],
                'fecha' : row[2],
                'hora_inicio' : row[3],
                'hora_fin' : row[4],
                'valor_producto' : row[5],
                'id_producto' : row[6],
                'id_cliente' : row[7]
                }
                carro_compras.append(carrito_producto)
            cur.close()
            print("AQUI ESTA EL CARRO DE COMPRAS: ", carro_compras)
            if carro_compras:
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                count_productos = cur.fetchone()[0]
                cur.close()
                return render_template('productos/camisetas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, camisetas=camisetas,count_productos=count_productos)
            else:
                cc_vacio = "El carro de compras está vacío"
                return render_template('productos/camisetas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, camisetas=camisetas, cc_vacio=cc_vacio)
        else:
            inicio_sesion = False
            camisetas = camisetas_dao['select_all']()
            return render_template('productos/camisetas.html', inicio_sesion=inicio_sesion, camisetas=camisetas)
    


@app.route('/bebidas', methods=['GET', 'POST'])
def bebidas ():
    if request.method == 'POST':
            data = request.get_json()  # Obtener los datos enviados en formato JSON
            id_bebida = data['id_bebida']
            nombre_bebida = data['nombre_bebida']
            valor_bebida = data['valor_bebida']
            img_bebida = data['img_bebida']
            producto_bebidas=0
            if 'username' in session:
                inicio_sesion = True
                id_usuario = session.get('id_usuario')
                bebidas = bebidas_dao['select_all']()
                producto_bebidas = {'nombre_producto': nombre_bebida, 'fecha': 0, 'hora_inicio':0, 'hora_fin': 0, 'valor_producto': valor_bebida, 'id_producto': id_bebida,'id_cliente':id_usuario,'img_producto':img_bebida}
                nuevo_producto = carro_compras_dao['insert'](producto_bebidas)
                bandera = 0
                if nuevo_producto:
                    return jsonify(bandera=bandera)
                else:
                    bandera = 1
                    return jsonify(bandera=bandera)
            else:
                inicio_sesion = False
                bebidas = bebidas_dao['select_all']()
                return render_template('productos/bebidas.html', inicio_sesion=inicio_sesion, bebidas=bebidas)
    else:
        if 'username' in session:
            inicio_sesion = True
            id_usuario = session.get('id_usuario')
            bebidas = bebidas_dao['select_all']()
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
            rows = cur.fetchall()
            carro_compras = []
            print('rows: ', rows)
            for row in rows:
                carrito_producto = {
                'id_carro' : row[0],
                'nombre_producto' : row[1],
                'fecha' : row[2],
                'hora_inicio' : row[3],
                'hora_fin' : row[4],
                'valor_producto' : row[5],
                'id_producto' : row[6],
                'id_cliente' : row[7]
                }
                carro_compras.append(carrito_producto)
            cur.close()
            print("AQUI ESTA EL CARRO DE COMPRAS: ", carro_compras)
            if carro_compras:
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                count_productos = cur.fetchone()[0]
                cur.close()
                return render_template('productos/bebidas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, bebidas=bebidas,count_productos=count_productos)
            else:
                cc_vacio = "El carro de compras está vacío"
                return render_template('productos/bebidas.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, bebidas=bebidas, cc_vacio=cc_vacio)
        else:
            inicio_sesion = False
            bebidas = bebidas_dao['select_all']()
            return render_template('productos/bebidas.html', inicio_sesion=inicio_sesion, bebidas=bebidas)

@app.route('/lista_canchas')
def lista_canchas ():
    canchas_futbol = cancha_futbol_dao['select_all']()
    canchas_basket = cancha_basket_dao['select_all']()
    canchas_tenis = cancha_tenis_dao['select_all']()
    camiseta = camisetas_dao['select_all']()
    pelota = pelotas_dao['select_all']()
    bebida = bebidas_dao['select_all']()
    
    return render_template('admin/lista_canchas.html', canchas_futbol = canchas_futbol, canchas_basket = canchas_basket, canchas_tenis = canchas_tenis, camisetas = camiseta, pelotas = pelota, bebidas = bebida )

@app.route('/campeonatos')
def campeonatos ():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        return render_template('canchas/campeonatos.html',inicio_sesion=inicio_sesion,id_usuario=id_usuario)
    else:
        return redirect(url_for('login'))


@app.route('/contacto' , methods=['GET', 'POST'])
def contacto ():
    if request.method == 'POST':
        id_usuario = session.get('id_usuario')
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        tipo_contacto=1
        contacto = {'nombre_contacto': nombre, 'mensaje_contacto': mensaje, 'correo_contacto':email,'tipo_contacto':tipo_contacto, 'id_cliente':id_usuario }
        new_contacto = contacto_dao['insert'](contacto)
        to_list = 'soccer_evoution91@outlook.com'
        email = 'soccer_evoution91@outlook.com'
        password = 'soccer_evolution'
        send_outlook(to_list, email, password)
        return render_template('contacto.html')
    else:
         return render_template('contacto.html')

@app.route('/quienes_somos')
def quienes_somos ():
    return render_template('/quienes_somos.html')

@app.route('/estacionamientos')
def estacionamientos ():
    return render_template('/estacionamientos.html')

@app.route('/new_producto')
def new_producto ():
    return render_template('admin/new_producto.html')

@app.route('/administrador')
def administrador ():
    return render_template('admin/administrador.html')

@app.route('/trabajador')
def trabajador ():
    trabajadores = trabajadores_dao['select_all']()
    mantenciones = mantenciones_dao['select_all']()
    servicios = servicios_dao['select_all']()
    liquidaciones = liquidaciones_dao['select_all']()
    return render_template('admin/trabajador.html', trabajadores = trabajadores, mantenciones = mantenciones, servicios = servicios, liquidaciones = liquidaciones)

@app.route('/carro_compras')
def carro_compras():
    if 'username' in session:
        inicio_sesion = True
        id_usuario = session.get('id_usuario')
        correo = session.get('username')
        print('id_usuario: ', id_usuario)
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
        rows = cur.fetchall()
        carro_compras = []
        print('rows: ', rows)
        for row in rows:
            carrito_producto = {
            'id_carro' : row[0],
            'nombre_producto' : row[1],
            'fecha' : row[2],
            'hora_inicio' : row[3],
            'hora_fin' : row[4],
            'valor_producto' : row[5],
            'id_producto' : row[6],
            'id_cliente' : row[7],
            'img_producto' : row[8]
            }
            carro_compras.append(carrito_producto)
        cur.close()

        print("AQUI ESTA EL CARRO DE COMPRAS:  ", carro_compras)
        if carro_compras:

            valor_total = 0
            for row in carro_compras:
                valor = row['valor_producto']
                valor_total += valor
            return render_template('carro_compras.html', inicio_sesion=inicio_sesion, id_usuario=id_usuario, productos=carro_compras, valor_total=valor_total, correo=correo)

        else:
            cc_vacio ="El carro de compras esta vacío"
            return render_template('carro_compras.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,productos=[], cc_vacio=cc_vacio)
    else:
         return redirect(url_for('login'))
    
      
@app.route('/agregar_al_carrito', methods=['POST', 'GET'])
def agregar_al_carrito():
    # Lógica para agregar el producto al carrito en la base de datos
    
    id_usuario = session.get('id_usuario')
    # Consulta para obtener el nuevo número de productos en el carrito
    cur = mysql.connection.cursor()
    cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
    count_productos = cur.fetchone()[0]
    cur.close()
    if count_productos>0:
    # Devuelve el resultado en formato JSON
        return jsonify({'count_productos': count_productos})
    else:
        count_productos=0
        return jsonify({'count_productos': count_productos})

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

@app.route('/vaciar_carro_compras', methods=['DELETE'])
def eliminar_carro():
    id_cliente=session.get('id_usuario')
    cur = mysql.connection.cursor()

    try:
        cur.execute("DELETE FROM carro_compras WHERE id_cliente = %s", (id_cliente,))
        mysql.connection.commit()
        response = {'message': 'Carro eliminado exitosamente'}
    except:
        mysql.connection.rollback()
        response = {'message': 'Error al eliminar el producto'}
    finally:
        cur.close()

    return jsonify(response)



@app.route('/region', methods=['POST', 'GET'])
def region():
    id_cliente=session.get('id_usuario')
    region = region_dao['select_all']()
    print("ESTAS SON LAS REGIONES: ", region)
    regiones = []
    for row in region:
        regiones_array = {
                'id_region' : row['id_region'],
                'region' : row['region']
                }
        regiones.append(regiones_array)
    return jsonify(regiones)

@app.route('/horario', methods=['POST', 'GET'])
def horario():
    data = request.get_json()  # Obtener los datos enviados en formato JSON
    hora_inicio = data['horaInicio']

    # Convertir la hora de inicio a formato de fecha
    formato_hora = "%H:%M"  # Formato de hora
    fecha_inicio = datetime.strptime(hora_inicio, formato_hora)

    # Sumar una hora a la fecha de inicio
    fecha_fin = fecha_inicio + timedelta(hours=1)

    # Convertir la fecha de fin a formato de hora
    hora_fin = fecha_fin.strftime(formato_hora)

    return jsonify(hora_fin)

def pagina_no_encontrada(error):
    return render_template('404.html'), 404


# LOAD GENERIC DAO FOR COMUNAS
tbl_comunas = 'comunas'
tbl_comunas_columnas = ['id_comuna', 'comuna', 'id_provincia']
comuna_dao = dao.dao_generic(app, mysql, tbl_comunas, tbl_comunas_columnas)

tbl_provincia = 'provincias'
tbl_provincia_columnas = ['id_provincia', 'provincia', 'id_region']
provincia_dao = dao.dao_generic(app, mysql, tbl_provincia, tbl_provincia_columnas)

tbl_region = 'regiones'
tbl_region_columnas = ['id_region', 'region', 'abreviatura', 'capital']
region_dao = dao.dao_generic(app, mysql, tbl_region, tbl_region_columnas)

tbl_usuario = 'usuario'
tbl_usuario_columnas = ['id_usuario', 'nombre_usuario', 'apellido_usuario','correo_usuario','password_usuario','telefono_usuario','direccion_usuario','rut_usuario','region_usuario','provincia_usuario','comuna_usuario']
usuario_dao = dao.dao_generic(app, mysql, tbl_usuario, tbl_usuario_columnas)

tbl_arriendo = 'arriendo'
tbl_arriendo_columnas = ['id_arriendo', 'fecha_arriendo', 'hora_arriendo','valor_arriendo','id_cliente','id_cancha','nombre_producto']
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
tbl_carro_compras_columnas = ['id_carro', 'nombre_producto', 'fecha', 'hora_inicio', 'hora_fin', 'valor_producto', 'id_producto','id_cliente', 'img_producto']
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

tbl_arriendos_historial = 'arriendos_historial'
tbl_arriendos_historial_columnas = ['id_arriendos_historial', 'fecha_arriendo', 'hora_arriendo','valor_arriendo','id_cliente','id_cancha','nombre_producto']
arriendos_historial_dao = dao.dao_generic(app, mysql, tbl_arriendos_historial, tbl_arriendos_historial_columnas)

tbl_transaccion = 'transaccion'
tbl_transaccion_columnas = ['id_transanccion', 'tipo_tarjeta', 'fecha_transaccion', 'orden_compra', 'session','estado', 'id_cliente']
transaccion_dao = dao.dao_generic(app, mysql, tbl_transaccion, tbl_transaccion_columnas)

tbl_contacto = 'contacto'
tbl_contacto_columnas = ['id_contacto', 'nombre_contacto', 'mensaje_contacto', 'correo_contacto', 'tipo_contacto','id_cliente']
contacto_dao = dao.dao_generic(app, mysql, tbl_contacto, tbl_contacto_columnas)

tbl_trabajadores = 'trabajador'
tbl_trabajadores_columnas = ['id_trabajador','nombre_trabajador', 'apellido_trabajador', 'fecha_nacimiento_trabajador', 'direccion_trabajador', 'comuna_trabajador', 'provincia_trabajador', 'region_trabajador', 'sueldo_trabajador', 'fecha_contratacion_trabajador']
trabajadores_dao = dao.dao_generic(app, mysql, tbl_trabajadores, tbl_trabajadores_columnas)

tbl_mantenciones = 'mantencion'
tbl_mantenciones_columnas = ['id_mantencion','id_trabajador', 'nombre_cancha', 'nombre_trabajador','fecha_mantencion']
mantenciones_dao = dao.dao_generic(app, mysql, tbl_mantenciones, tbl_mantenciones_columnas)

tbl_servicios = 'servicio'
tbl_servicios_columnas = ['id_servicio','nombre_servicio', 'monto_pago', 'numero_cliente','fecha_ulpago']
servicios_dao = dao.dao_generic(app, mysql, tbl_servicios, tbl_servicios_columnas)

tbl_liquidaciones = 'liquidacion'
tbl_liquidaciones_columnas = ['id_liquidacion','id_trabajador', 'nombre_trabajador', 'mes_pago','monto_liquido']
liquidaciones_dao = dao.dao_generic(app, mysql, tbl_liquidaciones, tbl_liquidaciones_columnas)

tbl_datos_transaccion_transbank = 'datos_transaccion_transbank'
tbl_datos_transaccion_transbank_columnas = ['id_datos_transaccion', 'correo_cliente', 'id_cliente']
datos_transaccion_transbank_dao = dao.dao_generic(app, mysql, tbl_datos_transaccion_transbank, tbl_datos_transaccion_transbank_columnas)


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

        data = request.get_json()  # Obtener los datos enviados en formato JSON
        hora_inicio = data['hora_inicio']
        hora_fin = data['hora_fin']
        fecha = data['datepicker']
        if 'username' in session:
            inicio_sesion = True
            id_usuario = session.get('id_usuario')
            id_cancha = session['id_cancha']
            nombre_cancha = session['nombre_cancha']
            valor_cancha = session['valor_cancha']
            img_cancha = session['img_cancha']

            hora_final= hora_inicio + "-" + hora_fin
            arriendo = {'nombre_producto': nombre_cancha, 'fecha': fecha, 'hora_inicio':hora_inicio, 
                        'hora_fin': hora_fin, 'valor_producto': valor_cancha, 'id_producto': id_cancha,'id_cliente':id_usuario, 'img_producto': img_cancha}
            arriendo_2 = { 'fecha_arriendo': fecha, 'hora_arriendo':hora_final, 'valor_arriendo': valor_cancha,'id_cliente':id_usuario, 'id_producto': id_cancha, 'nombre_producto':nombre_cancha}
            print('id_usuario: ', id_usuario)

            arriendo_si = arriendo_dao['select_all']()
            horarios = horarios_dao['select_all']()
            arriendo_existente = False
            for row in arriendo_si:
                if (row['fecha_arriendo'] == fecha and row['hora_arriendo'] == hora_final and row['valor_arriendo'] == valor_cancha and row['nombre_producto'] == nombre_cancha ):
                    arriendo_existente = True
                    
                    break 
            print ("ESTE ES EL VALOR DE ARRENDO EXISTENTE: ", arriendo_existente)        
            if arriendo_existente:
                bandera = 0
                mensaje= "La hora seleccionada (" + hora_inicio + "-" + hora_fin + ") para el dia "+ fecha+" no esta disponible"
                print (" NOOOOOOO  HICE EL INSERT !!!!!!!!!!!!!!!!!")     
                return jsonify(mensaje=mensaje,bandera=bandera)
            else:
                bandera = 1
                arriendo_existente =False  
                new_arriendo = carro_compras_dao['insert'](arriendo)
                new_arriendo2 = arriendo_dao['insert'](arriendo_2)
                print ("HICE EL INSERT !!!!!!!!!!!!!!!!!", new_arriendo)
                consulta_eliminar = "DROP TRIGGER IF EXISTS insertar_arriendo_historial"
                with mysql.connection.cursor() as cursor:
                    cursor.execute(consulta_eliminar)
                    mysql.connection.commit()

                cursor =  mysql.connection.cursor()
                # Definir la consulta para crear el trigger
                consulta ="""
                        CREATE TRIGGER insertar_arriendo_historial
                        AFTER INSERT ON arriendo
                        FOR EACH ROW
                        BEGIN
                            INSERT INTO arriendos_historial (fecha_arriendo, hora_arriendo, valor_arriendo, id_cliente, id_cancha, nombre_producto)
                            VALUES (NEW.fecha_arriendo, NEW.hora_arriendo, NEW.valor_arriendo, NEW.id_cliente, NEW.id_cancha, NEW.nombre_producto);
                        END
                    """

                with mysql.connection.cursor() as cursor:
                    cursor.execute(consulta)
                    mysql.connection.commit()
                            

                mensaje =''
                return jsonify(mensaje=mensaje,bandera=bandera)
        else:
            return render_template('registro/login.html')
    else:
        if 'username' in session:
            inicio_sesion = True
            id_usuario = session.get('id_usuario')
            id_cancha = request.args.get('id_cancha')
            nombre_cancha = request.args.get('nombre_cancha')
            valor_cancha = request.args.get('valor_cancha')
            img_cancha = request.args.get('img_cancha')
            session['nombre_cancha'] = nombre_cancha
            session['valor_cancha'] = valor_cancha
            session['id_cancha'] = id_cancha
            session['img_cancha'] = img_cancha
            horarios = horarios_dao['select_all']()

            print('id_usuario: ', id_usuario)
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
            rows = cur.fetchall()
            carro_compras = []
            print('rows: ', rows)
            for row in rows:
                carrito_producto = {
                'id_carro' : row[0],
                'nombre_producto' : row[1],
                'fecha' : row[2],
                'hora_inicio' : row[3],
                'hora_fin' : row[4],
                'valor_producto' : row[5],
                'id_producto' : row[6],
                'id_cliente' : row[7]
                }
                carro_compras.append(carrito_producto)
            cur.close()

            print("AQUI ESTA EL CARRO DE COMPRAS:  ", carro_compras)
            if carro_compras:
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                count_productos = cur.fetchone()[0]
                print("este es el select count id ", count_productos)
                cur.close()
            print("AQUI ESTA EL CARRO DE COMPRAS:  " , carro_compras)
            if carro_compras:
                return render_template('arrendar.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,id_cancha=id_cancha,nombre_cancha=nombre_cancha, valor_cancha= valor_cancha, horarios=horarios, count_productos=count_productos)
            else:
                cc_vacio ="El carro de compras esta vacío"
                return render_template('arrendar.html',inicio_sesion=inicio_sesion, id_usuario=id_usuario,id_cancha=id_cancha,nombre_cancha=nombre_cancha, valor_cancha= valor_cancha, horarios=horarios, cc_vacio=cc_vacio)
                
        else:
            return render_template('registro/login.html')
       
#### FIN ARRENDAR CANCHA  ######

#@app.route('/suspender_arriendo/<int:id_arriendos_historial>', methods=['DELETE'])
#def suspender_arriendo(id_arriendos_historial):
#
#    cur = mysql.connection.cursor()
#    try:
#        cur.execute("DELETE FROM carro_compras WHERE id_carro = %s", (id_arriendos_historial,))
#        mysql.connection.commit()
#        response = {'message': 'Producto eliminado exitosamente'}
#    except:
#        mysql.connection.rollback()
#        response = {'message': 'Error al eliminar el producto'}
#    finally:
#        cur.close()
#
#    return jsonify(response)
#

###### REGISTER #######
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
      
 #       rut_usuario = request.form['rut_usuario']
 #       nombre_usuario = request.form['nombre_usuario']
 #       apellido_usuario = request.form['apellido_usuario']
 #       correo_usuario = request.form['correo_usuario']
 #       password_usuario = request.form['password_usuario']
 #       hashed_password = generate_password_hash(password_usuario)
 #       telefono_usuario = request.form['telefono_usuario']
 #       direccion_usuario = request.form['direccion_usuario']
 #       region_usuario = request.form['region_usuario']
 #       provincia_usuario = request.form['provincia_usuario']
 #       comuna_usuario = request.form['comuna_usuario']
        data = request.get_json()  # Obtener los datos enviados en formato JSON

        rut_usuario = data['rut_usuario']
        nombre_usuario = data['nombre_usuario']
        apellido_usuario = data['apellido_usuario']
        correo_usuario = data['correo_usuario']
        password_usuario = data['password_usuario']
        hashed_password = generate_password_hash(password_usuario)
        telefono_usuario = data['telefono_usuario']
        direccion_usuario = data['direccion_usuario']
        region_usuario = data['region_usuario']
        provincia_usuario = data['provincia_usuario']
        comuna_usuario = data['comuna_usuario']
        if region_usuario !='' and provincia_usuario !='' and comuna_usuario !='':
            cur = mysql.connection.cursor()
            cur.execute('SELECT region FROM regiones WHERE id_region = %s', (region_usuario,))
            nombre_region = cur.fetchone()[0]
            print("este es el select count id ", nombre_region)
            cur.close()

            cur = mysql.connection.cursor()
            cur.execute('SELECT provincia FROM provincias WHERE id_provincia = %s', (provincia_usuario,))
            nombre_provincia = cur.fetchone()[0]
            print("este es el select count id ", nombre_provincia)
            cur.close()

            cur = mysql.connection.cursor()
            cur.execute('SELECT comuna FROM comunas WHERE id_comuna = %s', (comuna_usuario,))
            nombre_comuna = cur.fetchone()[0]
            print("este es el select count id ", nombre_comuna)
            cur.close()
        else:
            nombre_region=0
            nombre_provincia=0
            nombre_comuna=0

                # Validar si el correo ya existe
        cur = mysql.connection.cursor()
        cur.execute('SELECT correo_usuario FROM usuario WHERE correo_usuario = %s', (correo_usuario,))
        existe_correo = cur.fetchone()
        cur.close()

        if existe_correo:
            # El correo ya existe, enviar mensaje de error
            flash('El correo ya está registrado', 'error')
            return redirect(url_for('index'))

        usuario = { 'nombre_usuario': nombre_usuario, 'apellido_usuario': apellido_usuario, 
                    'correo_usuario': correo_usuario, 'password_usuario': hashed_password, 
                    'telefono_usuario': telefono_usuario, 'direccion_usuario': direccion_usuario,
                    'rut_usuario': rut_usuario, 'region_usuario': nombre_region, 
                    'provincia_usuario': nombre_provincia, 'comuna_usuario': nombre_comuna }
                    
        new_usuario = usuario_dao['insert'](usuario)

        to_list = correo_usuario
        email = 'soccer_evoution91@outlook.com'
        password = 'soccer_evolution'
        send_outlook(to_list, email, password)
        print('new_usuario: ', new_usuario)
        bandera = 0
        if new_usuario:
            session['nombre_usuario'] = nombre_usuario 
            bandera = 1
            return jsonify (bandera) 
        else:
            return jsonify (bandera) 
         # Inicia sesión automáticamente después del registro
        return jsonify () # Redirige al usuario al panel de control después del registro
    else:
            region = region_dao['select_all']()
            print("ESTAS SON LAS REGIONES: ", region)
            regiones = []
            for row in region:
                regiones_array = {
                        'id_region' : row['id_region'],
                        'region' : row['region']
                        }
                regiones.append(regiones_array)

            provincia = provincia_dao['select_all']()
            print("ESTAS SON LAS provincias: ", provincia)
            provincias = []
            for row in provincia:
                provincias_array = {
                        'id_provincia' : row['id_provincia'],
                        'provincia' : row['provincia']
                        }
                provincias.append(provincias_array)

            comuna = comuna_dao['select_all']()
            print("ESTAS SON LAS comuna: ", comuna)
            comunas = []
            for row in comuna:
                comunas_array = {
                        'id_comuna' : row['id_comuna'],
                        'comuna' : row['comuna']
                        }
                comunas.append(comunas_array)
            flash('Usuario registrado', 'success')
            return render_template('Registro/registro.html',regiones=regiones,provincias=provincias,comunas=comunas)

###### FIN REGISTER #######

@app.route('/obtener_provincias', methods=['POST'])
def obtener_provincias():
    region_id = request.form.get('region_id')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM provincias WHERE id_region = %s', (region_id,))
    rows = cur.fetchall()
    provincias = []
    print('rows: ', rows)
    for row in rows:
        provincia = {
        'id_provincia' : row[0],
        'provincia' : row[1],
        'id_region' : row[2],
        }
        provincias.append(provincia)
    cur.close()

    return jsonify(provincias)

@app.route('/obtener_comunas', methods=['POST'])
def obtener_comunas():
    provincia_id = request.form.get('provincia_id')

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM comunas WHERE id_provincia = %s', (provincia_id,))
    rows = cur.fetchall()
    comunas = []
    print('rows: ', rows)
    for row in rows:
        comuna = {
        'id_comuna' : row[0],
        'comuna' : row[1],
        'id_provincia' : row[2],
        }
        comunas.append(comuna)
    cur.close()

    return jsonify(comunas)

###### LOGIN #######

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_login = request.form['correo_login']
        password_login = request.form['contraseña_login']

        cur = mysql.connection.cursor()
        cur.execute('SELECT correo_usuario FROM usuario')
        rows = cur.fetchall()
        validacion_login = []
        print('rows: ', rows)
        for row in rows:
            usuario_correo = {
            'correo_usuario' : row[0]
            }
            validacion_login.append(usuario_correo)
        cur.close()


        for row in validacion_login:
            correo_login=row['correo_usuario']
            if correo_login == username_login:
                
                #print("Este es el nombre de la persona que se esta buscando
                cur = mysql.connection.cursor()
                cur.execute('SELECT password_usuario FROM usuario WHERE correo_usuario = %s', (username_login,))
                password_bd = cur.fetchone()[0]
                cur.close()
                
                cur = mysql.connection.cursor()
                cur.execute('SELECT id_usuario, nombre_usuario FROM usuario WHERE correo_usuario = %s', (username_login,))
                rows = cur.fetchall()
                usuarios_by_id = []
                print('rows: ', rows)
                for row in rows:
                    usuario_by_id = {
                    'id_usuario' : row[0],
                    'nombre_usuario' : row[1]
                    }
                    usuarios_by_id.append(usuario_by_id)
                cur.close()

                id_usuario = None
                if password_bd is not None:
                    print("ESte es el usuario by id: ", usuarios_by_id )
                    if check_password_hash(password_bd,password_login):
                        
                        for row in usuarios_by_id:
                            id_usuario = row['id_usuario']
                            nombre_usuario = row['nombre_usuario']
                            break
                                
                        session['username'] = username_login
                        session['id_usuario'] = id_usuario
                        session['nombre_usuario'] = nombre_usuario
                        if 'username' in session:
                            # El usuario ha iniciado sesión
                            username_login = session['username']
                            id_usuario_login = session['id_usuario']
                            if username_login == 'admin@gmail.com':
                                session['admin'] = username_login
                                print ('INGRESO EL ADMIN;', username_login )
                                admin = True
                                return redirect(url_for('index', id_usuario=id_usuario_login, admin=admin))
                            else:
                                admin = False
                                return redirect(url_for('index', id_usuario=id_usuario_login, nombre_usuario=nombre_usuario))
                        else:
                            # El usuario no ha iniciado sesión
                            return 'Inicia sesión para continuar'
        else:
            flash( 'Credenciales inválidas')

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
    session.clear()
    return redirect('/')

@app.route('/recuperar_correo', methods=['GET', 'POST'])
def recuperar_correo():
    data = request.get_json()  # Obtener los datos enviados en formato JSON
    correo = data['correo']
    cur = mysql.connection.cursor()
    cur.execute('SELECT correo_usuario FROM usuario')
    rows = cur.fetchall()
    correos_usuarios = []
    print('rows: ', rows)
    for row in rows:
        correos = {
        'correo_usuario' : row[0]
        }
        correos_usuarios.append(correos)
    cur.close()
    correo_existe = 0
    for row in correos_usuarios:
        correo_bd = row['correo_usuario']
        if correo_bd == correo:
            correo_existe = 1
            to_list3 = correo_bd
            email3 ='soccer_evoution91@outlook.com'
            password3 = 'soccer_evolution'
            send_outlook3(to_list3, email3, password3)
            break

        else:
            correo_existe = 0
    return jsonify(correo_existe)



@app.route('/cambio_contrasena', methods=['GET', 'POST'])
def cambio_contraseña():
        return render_template('registro/cambio_contraseña.html')
    
@app.route('/cambio_contraseña_ajax', methods=['GET', 'POST'])
def cambio_contraseña_ajax():
    data = request.get_json()  # Obtener los datos enviados en formato JSON
    correo_login_cambio = data['correo_login_cambio']
    contraseña_login_cambio = data['contraseña_login_cambio']
    hashed_password = generate_password_hash(contraseña_login_cambio)

    print ("contraseña hashed: " + hashed_password)
    cur = mysql.connection.cursor()
    cur.execute('UPDATE usuario SET password_usuario = %s WHERE correo_usuario = %s', (hashed_password, correo_login_cambio))
    mysql.connection.commit()
    cur.close()
    update=1
    return jsonify(update)

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
        rut_usuario = request.form['rut_usuario']
        id_usuario = request.form['id_usuario']
        nombre_usuario = request.form['nombre_usuario']
        apellido_usuario = request.form['apellido_usuario']
        correo_usuario = request.form['correo_usuario']
        telefono_usuario = request.form['telefono_usuario']
        direccion_usuario = request.form['direccion_usuario']
        region_usuario = request.form['region_usuario_editar']
        provincia_usuario = request.form['provincia_usuario_editar']
        comuna_usuario = request.form['comuna_usuario_editar']

        cur = mysql.connection.cursor()
        cur.execute('SELECT region FROM regiones WHERE id_region = %s', (region_usuario,))
        nombre_region = cur.fetchone()[0]
        print("este es el select count id ", nombre_region)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute('SELECT provincia FROM provincias WHERE id_provincia = %s', (provincia_usuario,))
        nombre_provincia = cur.fetchone()[0]
        print("este es el select count id ", nombre_provincia)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute('SELECT comuna FROM comunas WHERE id_comuna = %s', (comuna_usuario,))
        nombre_comuna = cur.fetchone()[0]
        print("este es el select count id ", nombre_comuna)
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute('SELECT password_usuario FROM usuario WHERE id_usuario = %s', (id_usuario,))
        password = cur.fetchone()[0]
        print("este es el select count id ", password)
        cur.close()
        usuario = { 'id_usuario':id_usuario, 'nombre_usuario': nombre_usuario, 'apellido_usuario': apellido_usuario, 
                    'correo_usuario': correo_usuario, 'password_usuario':password,
                    'telefono_usuario': telefono_usuario, 'direccion_usuario': direccion_usuario,'rut_usuario':rut_usuario, 
                    'region_usuario':nombre_region,'provincia_usuario':nombre_provincia,'comuna_usuario':nombre_comuna,}
        
        usuario_actualizado = usuario_dao['update'](usuario)
        print('Usuario actualizado correctamente', usuario_actualizado)
        inicio_sesion = True
        return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_actualizado, id_usuario=id_usuario)
    else:

        region = region_dao['select_all']()
        print("ESTAS SON LAS REGIONES: ", region)
        regiones = []
        for row in region:
            regiones_array = {
                    'id_region' : row['id_region'],
                    'region' : row['region']
                    }
            regiones.append(regiones_array)

        provincia = provincia_dao['select_all']()
        print("ESTAS SON LAS provincias: ", provincia)
        provincias = []
        for row in provincia:
            provincias_array = {
                    'id_provincia' : row['id_provincia'],
                    'provincia' : row['provincia']
                    }
            provincias.append(provincias_array)

        comuna = comuna_dao['select_all']()
        print("ESTAS SON LAS comuna: ", comuna)
        comunas = []
        for row in comuna:
            comunas_array = {
                    'id_comuna' : row['id_comuna'],
                    'comuna' : row['comuna']
                    }
        comunas.append(comunas_array)

        print("ID del usuario:", id)
        usuario_2 = usuario_dao['select_by_id'](id)
        print("datos del usuario:", usuario_2)
        if usuario_2:
            print("ENTRO AL IF" ,region,provincia,comuna)
            return render_template('registro/editar_usuario.html', usuarios=usuario_2,regiones=regiones,provincias=provincias,comunas=comunas)
            
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
                
                cur = mysql.connection.cursor()
                cur.execute('SELECT * FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                rows = cur.fetchall()
                carro_compras = []
                print('rows: ', rows)
                for row in rows:
                    carrito_producto = {
                    'id_carro' : row[0],
                    'nombre_producto' : row[1],
                    'fecha' : row[2],
                    'hora_inicio' : row[3],
                    'hora_fin' : row[4],
                    'valor_producto' : row[5],
                    'id_producto' : row[6],
                    'id_cliente' : row[7]
                    }
                    carro_compras.append(carrito_producto)
                cur.close()

                print("AQUI ESTA EL CARRO DE COMPRAS:  ", carro_compras)
                if carro_compras:
                    cur = mysql.connection.cursor()
                    cur.execute('SELECT COUNT(*) FROM carro_compras WHERE id_cliente = %s', (id_usuario,))
                    count_productos = cur.fetchone()[0]
                    print("este es el select count id ", count_productos)
                    cur.close()


                cur = mysql.connection.cursor()
                cur.execute('SELECT * FROM arriendos_historial WHERE id_cliente = %s', (id_usuario,))
                rows = cur.fetchall()
                arriendos_historial = []
                print('rows: ', rows)
                for row in rows:
                    arriendo = {
                    'id_arriendos_historal' : row[0],
                    'fecha_arriendo' : row[1],
                    'hora_arriendo' : row[2],
                    'valor_arriendo' : row[3],
                    'id_cliente' : row[4],
                    'id_cancha' : row[5],
                    'nombre_producto' : row[6]
                    }
                    arriendos_historial.append(arriendo)
                cur.close()
                print (id_usuario)
                print (arriendos_historial)
                if carro_compras:
                    return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_2, id_usuario=id_usuario,arriendos_historial=arriendos_historial,count_productos=count_productos)
                else:
                    cc_vacio ="El carro de compras esta vacío"
                    return render_template('registro/perfil_usuario.html', inicio_sesion=inicio_sesion, usuarios=usuario_2, id_usuario=id_usuario,cc_vacio=cc_vacio,arriendos_historial=arriendos_historial)

              
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

@app.route('/mail', methods=['GET', 'POST'])
def mail():
   return render_template('mail.html')
############## TRANSBANK ####################

@app.route('/transbank/commit-pay', methods=['GET', 'POST'])
def transbank_commit_pay():
    # SE DEBE APLICAR ESTA DESCOMENTAR ESTA SECCIÓN Y AGREGAR LÓGICA PARA LA RESPUESTA RECIBIDA EN EL RESPONSE
    # DE SER CORRECTA SE DEBE CONFIRM
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
         
            correo=0
            id_usuario=0
            datos_usuario = datos_transaccion_transbank_dao['select_all']()
            print(datos_usuario)
            for row in datos_usuario:
                correo_cliente = row['correo_cliente']
                id_usuario = row['id_cliente']
                print(correo_cliente)
                print(id_usuario)
                break
            transaccion ={'tipo_tarjeta': tipoTarjeta, 'fecha_transaccion': fecha, 'orden_compra': ordenCompra, 'session': session, 'estado':status, 'id_cliente':id_usuario}
            to_list2 = correo_cliente
            email2 = 'soccer_evoution91@outlook.com'
            password2 = 'soccer_evolution'
            send_outlook2(to_list2, email2, password2,transaccion)
            new_transaccion = transaccion_dao['insert'](transaccion)
            cur = mysql.connection.cursor()
            if new_transaccion:
                try:
                    cur.execute("DELETE FROM datos_transaccion_transbank ")
                    mysql.connection.commit()
                    response = {'message': 'Carro eliminado exitosamente'}
                except:
                    mysql.connection.rollback()
                    response = {'message': 'Error al eliminar el producto'}
                finally:
                    cur.close()
                print("ELIMINE LOS DATOS DE USUARIO ")
                
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
    print('transbank_create')
    print('request.form: ', request.form)
    amount = request.form.get('amount')
    session_id = '2334567' # ID SESSION
    buy_order = request.form.get('buy_order')
    id_usuario = request.form.get('id_usuario')
    correo = request.form.get('correo')
    session['transbank_correo'] =correo
    session['transbank_id_usuario'] =id_usuario
    datos_cliente = {'correo_cliente':correo, 'id_cliente':id_usuario }
    new_datos_transaccioN = datos_transaccion_transbank_dao['insert'](datos_cliente) 

    print("id_usuario:" , id_usuario)
    print("correo:" , correo)
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



