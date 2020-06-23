import pandas.io.formats.csvs
import os
import sys
import numpy as np
import psycopg2
import psycopg2.extras
# Grafico
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mddates
import dateutil
from datetime import datetime

#Opcão para ler dados do Banco
table_name = 'view_categoria'
data_coluna = 'descricao'
var_coluna = 'descricao'
data_ini = '2020-06-20 17:00:00'
data_fim = '2020-06-20 17:10:00'
conn = psycopg2.connect(host = "127.0.0.1", database = "Lemobs", password="deziele", user="postgres")
cursor = conn.cursor()
query = "SELECT %s,%s FROM %s WHERE %s BETWEEN '%s' AND '%s' ORDER BY %s;" % (data_coluna,var_coluna,table_name,data_coluna,data_ini,data_fim,data_coluna)
cursor.execute(query)
lst = cursor.fetchall()
# Fechar ponteiro e conexão


# Opção para ler dados de arquivo CSV
#Gráfico Pizza

x = pd.read_csv(r"C:\Users\Mario\Desktop\view_categoria.csv")
plt.pie(x["id"],labels=x["descricao"],autopct="%1.0f%%")
plt.show()

#Gráfico de Linha
x = pd.read_csv(r"C:\Users\Mario\Desktop\view_categoria.csv")
plt.plot(x["descricao"])
plt.show()

#Gráfico Histrograma
x = pd.read_csv(r"C:\Users\Mario\Desktop\view_categoria.csv")
plt.hist(x["descricao"],bins=20)
plt.show()

  
