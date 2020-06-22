import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="deziele",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Lemobs")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from categoria"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from categoria table using cursor.fetchall")
   descricao = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in descricao:
       print("Id = ", row[0], )
       print("Descricao = ", row[1])
       print("Status  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")