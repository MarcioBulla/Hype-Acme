import mysql.connector


print("Iniciando")
# try:
    # print("fazendo conexão")
db = mysql.connector.connect(host = 'mydb', user = 'root', password = 'acme', port = 3306)
print("Deu Boa")
db.close()
# except:
    # print("Deu Ruim")