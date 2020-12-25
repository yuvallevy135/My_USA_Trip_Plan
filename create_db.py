import mysql
import mysql.connector as MySQL
from mysql.connector import errorcode
import os
from csv import reader, writer
import random
import time


def main():
    # with open('us_campsites.csv', 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     for line in csv_reader:
    #         print(line[2])

    conn = MySQL.connect(
        host="localhost",
        database='plan_trip',
        user="root",
        password="Aa123456",
    )
    if conn:
        print("Yes")
    else:
        print("No")
    curr = conn.cursor()
    curr.execute("DROP TABLE IF EXISTS Campsites")
    #
    # # curr.execute('DROP TABLE IF EXISTS Campsites,')
    # DB_NAME = 'plan_trip'
    # TABLES = {}
    #
    # TABLES['Campsites'] = (
    #     "CREATE TABLE Campsites ("
    #     "longitude DECIMAL,"
    #     "latitude DECIMAL,"
    #     "code STRING,"
    #     "name STRING,"
    #     "type STRING,"
    #     "phone STRING,"
    #     "dates_open STRING,"
    #     "comments STRING,"
    #     "num_sites INT,"
    #     "elevation STRING,"
    #     "amenities STRING,"
    #     "state STRING,"
    #     "nearest_town_distance DECIMAL,"
    #     "nearest_town_bearing STRING,"
    #     "city VARCHAR"
    #     ")")

    curr.execute("CREATE TABLE IF NOT EXISTS Campsites ("
                 "longitude DECIMAL(10,3),"
                 "latitude DECIMAL(10,3),"
                 "code VARCHAR(255),"
                 "name VARCHAR(255),"
                 "type VARCHAR(255),"
                 "phone VARCHAR(255),"
                 "dates_open VARCHAR(255),"
                 "comments VARCHAR(255),"
                 "num_sites INTEGER(10),"
                 "elevation VARCHAR(255),"
                 "amenities VARCHAR(255),"
                 "state VARCHAR(255),"
                 "nearest_town_distance DECIMAL,"
                 "nearest_town_bearing VARCHAR(255),"
                 "city VARCHAR(255)"
                 ")")
    # for table_name in TABLES:
    #     table_description = TABLES[table_name]
    #     try:
    #         print("Creating table: ".format(table_name), end='')
    #         curr.execute(table_description)
    #     except mysql.connector.Error as err:
    #         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
    #             print("already exists.")
    #         else:
    #             print(err.msg)
    #     else:
    #         print("OK")
    #
    infilecomp = open("us_campsites.csv")
    csv_reader = reader(infilecomp)
    next(csv_reader)
    for row in csv_reader:
        try:

            # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
            #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
            #              row[11], row[12], row[13], row[14])
            my_insert_data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12], row[13], row[14])
            my_query = """INSERT INTO Campsites VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            curr.execute(my_query, my_insert_data)
            conn.commit()
        except MySQL.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    curr.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
