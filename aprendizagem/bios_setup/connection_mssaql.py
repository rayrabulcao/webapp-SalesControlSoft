# importing module Like Namespace in .Net
import pyodbc
from bios_setup import db
import sqlalchemy



print(pyodbc.drivers())

# creating connection Object which will contain SQL Server Connection
#connection = pyodbc.connect('Driver={SQL Server};Server=BRG220F5YC;Database=bios;uid=gbi;pwd=fpf@1212')

# connection = pyodbc.connect("DRIVER={SQL Server};SERVER=BRG220F5YC;DATABASE=bios;UID=gbi;PWD=fpf@1212")
# connection = pyodbc.connect(driver='FreeTDS', server="10.6.0.144", database="bios", uid="gbi", pwd="fpf@1212")
connection = pyodbc.connect("DSN=SQLServer;UID=gbi;PWD=fpf@1212")

print("Connected.")

cursor = connection.cursor()
cursor.execute("use bios;")

#cursor.execute("CREATE TABLE Etapa ( id integer not null, descricao varchar(2000), status BIT NULL DEFAULT 0, primary key(id) );")
#cursor.execute("CREATE TABLE Instrucao (id integer not null, id_etapa integer not null, id_codigo_bios INTEGER not null, posicao integer, descricao varchar(2000), FOREIGN KEY (id_etapa) REFERENCES Etapa(id), FOREIGN KEY (id_codigo_bios) REFERENCES Codigo_BIOS(id), primary key(id) );")

print("Created.")

# cursor.execute("select  e.descricao as descEtapa,cb.descricao as descBios FROM Instrucao i inner join etapa e on e.id = i.id_etapa inner join codigo_bios cb on cb.id = i.id_codigo_bios GROUP BY e.descricao, cb.descricao")
# cursor.execute("select * from tapas;")
#cursor.execute("select descricao from Etapas;")
# # cursor.execute("exec sp_help Codigo_BIOS;")
#cursor.execute("select name from syscolumns where id=object_id('Codigo_BIOS')")
# # cursor.execute("select biosVersionRascunho from Codigo_BIOS;")
# # cursor.execute("insert into Codigo_bios (codigo, biosVersion, status, arquivo_id, placa_mae_id, descricao) VALUES (123321, 'TESTE-1', 'ativo', 2, 2, 'TESTE-1'); ")

# cursor.execute("insert into Configuracao (id_placa_mae, id_instrucao, comandos) VALUES (1, 1, '50 60 70')");

cursor.execute("select * from Configuracao");

# #

# row = cursor.fetchall()
# while row:
#     print(row)
#     row = cursor.fetchall()
# #

#db.session.query(db.quer)

#cur.execute("select * from table")

# closing connection
connection.close()