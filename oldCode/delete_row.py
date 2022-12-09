# TEST DELETE OPERATION 

# LIBRARIES AND MODULES
import psycopg2 # For Postgre SQL

# Properties of the connection string
database = "metsastys"
user = "postgres"
password = "Q2werty"
host = "lacolhost"
port = "5432"

# Try to establish a connection to DB server
try:
    # Create a connection object
    dbaseconnection = psycopg2.connect(database=database, user=user, password=password,
                                        host=host, port=port)

    #  Create a cursor to execute commands and retrieve the result set
    cursor = dbaseconnection.cursor()

    # Execute a SQl command to remove a group
    command = "DELETE FROM pablic.jakoryhma WHERE RYHMA_id = 5;"
    cursor.execute(command)

    # Commit the transaction 
    dbaseconnection.commit()
    print("Tietue poistettiin")        


# Throw an error if connection or cursor creation fails
except(Exception, psycopg2. Error) as e:
    print("Tietokantayhteydessä tapahtui virhe", e)

# If or if not successfull close the cursor and the connection
finally:
    if (dbaseconnection):
        cursor.close()
        dbaseconnection.close()
        print("Yhteys tietokantaan katkaistiin")       