from pyodbc import *
db = connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=tabel.mdb') #order.mdb - собственно мое файло БД
dbc = db.cursor()


dbc.execute('select * from Табель where god=2020 and mes=9')
rows = [row for row in dbc.fetchall()]
print(rows[1])
db.close()
