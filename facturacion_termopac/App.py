from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
from flask import Flask, render_template, request, redirect, flash, session

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="termopac"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, stock FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', productos=productos)

@app.route('/facturar', methods=['GET', 'POST'])
def facturar():
    if request.method == 'POST':
        # ... tu código para insertar la factura ...

        flash('Producto facturado correctamente.')
        return redirect('/')

    if request.method == 'POST':
        productos = request.form.getlist('producto_id')
        cantidades = request.form.getlist('cantidad')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO facturas () VALUES ()")
        factura_id = cursor.lastrowid

        detalles = []
        for prod_id, cant in zip(productos, cantidades):
            detalles.append((factura_id, int(prod_id), int(cant)))

        sql = "INSERT INTO detalle_factura (factura_id, producto_id, cantidad) VALUES (%s, %s, %s)"
        cursor.executemany(sql, detalles)
        conn.commit()

        cursor.close()
        conn.close()
        return redirect('/')
    else:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('facturar.html', productos=productos)


if __name__ == '__main__':
    app.run(debug=True)

