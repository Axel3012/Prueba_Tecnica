import sqlite3
import requests

'''
SELECT id,fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to FROM movimientos ORDER BY fecha
'''

class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultaSQL(self, consulta):
        '''
        Este metodo devuelve los datos de la base de datos
        en base a una consulta 
        '''
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()  
        cursor.execute(consulta)
        self.movimientos = []
        nombres_columna = []
        for desc_columna in cursor.description:
            nombres_columna.append(desc_columna[0]) 
        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()
        
        return self.movimientos

    def consultaConParametros(self, consulta, params):
        '''
        Este metodo resive una consulta sql con datos y los ejecuta en la base de datos
        '''
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except Exception as error:
            print("ERROR DB:", error)
            conexion.rollback()
        conexion.close()

        return resultado
  
    def solicitudConParametros(self, consulta, params):
        '''
        Este metodo resive una consulta sql con datos y los ejecuta en la base de datos
        y debuelve el dato solicitado

        '''
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = 0
        try:
            cursor.execute(consulta, params)
            dato = cursor.fetchone()
            dato = dato[0]
            if dato == None:
                dato = 0
            resultado = dato
        except Exception as error:
            print("ERROR DB:", error)

        conexion.close()

        return resultado



    