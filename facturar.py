import mysql.connector

password = input("Introduce la contraseña de MySQL: ")

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="termopac"
)

cursor = conexion.cursor()
def mostrar_inventario():
    cursor.execute("SELECT id, nombre, stock FROM productos")
    productos = cursor.fetchall()
    print("\nInventario actual:")
    print("------------------")
    for prod in productos:
        print(f"ID: {prod[0]}, Producto: {prod[1]}, Stock: {prod[2]}")
    print("------------------\n")

print("Inventario antes de facturar:")
mostrar_inventario()

# Crear factura
cursor.execute("INSERT INTO facturas () VALUES ()")
factura_id = cursor.lastrowid

# Agregar productos facturados (id producto, cantidad)
productos_facturados = [
    (factura_id, 1, 2),  # 2 unidades del producto 1
    (factura_id, 2, 3)   # 1 unidad del producto 2
]

# Insertar productos facturados
sql = "INSERT INTO detalle_factura (factura_id, producto_id, cantidad) VALUES (%s, %s, %s)"
cursor.executemany(sql, productos_facturados)

conexion.commit()
cursor.close()
conexion.close()

print("Factura creada y stock actualizado.")