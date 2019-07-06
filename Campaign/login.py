#in order to connect you need to connect to embray network and not guest

import psycopg2
try:
    connection = psycopg2.connect(user = "ckcheruiyot",
                                  password = "!@c0!!1n5V3ryS3c&3",
                                  host = "172.21.200.55",
                                  port = "5432",
                                  database = "analytics_db")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
