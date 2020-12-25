from random import uniform
import mysql.connector as MySQL
from mysql.connector import errorcode
from csv import reader, writer

CAMP_ROW_COLUMNS = [5, 14]  # id
CAMP_ROW_LOCATIONS_COLUMNS = [0, 1, 3, 11]  # type, id
PARKS_ROW_COLUMNS = [6, 21]  # id
PARKS_ROW_LOCATIONS_COLUMNS = [23, 24]  # type, id
AIRBNB_ROW_COLUMNS = [0, 6, 13, 15, 16]  # id
AIRBNB_ROW_LOCATIONS_COLUMNS = [1, 7, 11, 12]  # type, id


class DbCreator:
    def create_db(self):
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
        # Campsites
        # curr.execute("DROP TABLE IF EXISTS Campsites")
        # curr.execute("TRUNCATE TABLE Campsites")


        # NEW
        # curr.execute("CREATE TABLE IF NOT EXISTS campsites("
        #              "campsite_id varchar(255) NOT NULL,"
        #              "phone varchar(50) DEFAULT NULL,"
        #              "city varchar(50) NOT NULL,"
        #              "PRIMARY KEY (campsite_id`)"
        #              ")")

        # OLD
        # curr.execute("CREATE TABLE IF NOT EXISTS Campsites ("
        #              "longitude double NOT NULL,"
        #              "latitude double NOT NULL,"
        #              "name VARCHAR(50),"
        #              "phone VARCHAR(50),"
        #              "state VARCHAR(50),"
        #              "city VARCHAR(50),"
        #              "campsite_id VARCHAR(255)"
        #              ")")

        infilecomp = open("us_campsites.csv")
        csv_reader = reader(infilecomp)
        next(csv_reader)
        flag = False
        for row in csv_reader:
            try:

                # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
                #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                #              row[11], row[12], row[13], row[14])
                if not flag:
                    flag = True
                    continue
                locations_row, res_row = create_row(row, "us_campsites.csv")
                if not res_row:
                    continue
                my_insert_data = (
                    locations_row[0], locations_row[1], locations_row[2], locations_row[3], locations_row[4],
                    locations_row[5])
                my_query = """INSERT INTO locations VALUES (%s,%s,%s,%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
                my_insert_data = (res_row[0], res_row[1], res_row[2])
                my_query = """INSERT INTO Campsites VALUES (%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
            except MySQL.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

        # Listing_url, name, city, state, latitude, longitude, root_type,price,review_score] + airbbn_id
        # Airbnb [0,1,6,7,11,12,13,15,16] +17
        # curr.execute("DROP TABLE IF EXISTS Airbnb")
        curr.execute("TRUNCATE TABLE Airbnb")

        # # NEW
        # curr.execute("CREATE TABLE IF NOT EXISTS Airbnb("
        #              "airbnb_id varchar(255) NOT NULL,"
        #              "listing_url varchar(255) DEFAULT NULL,"
        #              "city varchar(50) NOT NULL,"
        #              "property_type varchar(50) DEFAULT NULL,"
        #              "price double NOT NULL,"
        #              "rank_score double NOT NULL,"
        #              "PRIMARY KEY (airbnb_id)")

        # curr.execute("CREATE TABLE IF NOT EXISTS Airbnb ("
        #              "listing_url VARCHAR(255),"
        #              "name VARCHAR(255),"
        #              "city VARCHAR(50),"
        #              "state VARCHAR(50),"
        #              "latitude double NOT NULL,"
        #              "longitude double NOT NULL,"
        #              "property_type VARCHAR(50),"
        #              "price double NOT NULL,"
        #              "rank_score double NOT NULL,"
        #              "airbnb_id VARCHAR(255)"
        #              ")")
        infilecomp = open("airbnb_all.csv", encoding="utf8")
        csv_reader = reader(infilecomp)
        next(csv_reader)
        for row in csv_reader:
            try:

                # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
                #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                #              row[11], row[12], row[13], row[14])
                locations_row, res_row = create_row(row, "airbnb_all.csv")
                if not res_row:
                    continue
                my_insert_data = (
                    locations_row[0], locations_row[1], locations_row[2], locations_row[3], locations_row[4],
                    locations_row[5])
                my_query = """INSERT INTO locations VALUES (%s,%s,%s,%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
                my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5])
                my_query = """INSERT INTO Airbnb VALUES (%s,%s,%s,%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
            except MySQL.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

        # states
        # curr.execute("DROP TABLE IF EXISTS states")
        # curr.execute("TRUNCATE TABLE states")

        # # NEW
        # curr.execute("CREATE TABLE states ("
        #              "state varchar(50) NOT NULL,"
        #              "state_code char(2) NOT NULL,"
        #              "PRIMARY KEY (state)")
        #

        # # OLD
        # curr.execute("CREATE TABLE states ("
        #              "state varchar(50) NOT NULL,"
        #              "state_code char(2) NOT NULL"
        #              ")")
        infilecomp = open("states.csv")
        csv_reader = reader(infilecomp)
        next(csv_reader)
        flag = False
        for row in csv_reader:
            try:
                if not flag:
                    flag = True
                    continue
                locations_row, res_row = create_row(row, "states.csv")
                if not res_row:
                    continue
                my_insert_data = (res_row[0], res_row[1])
                my_query = """INSERT INTO states VALUES (%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
            except MySQL.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

        # cities
        curr.execute("DROP TABLE IF EXISTS cities")
        curr.execute("TRUNCATE TABLE cities")

        # #  NEW
        # curr.execute("CREATE TABLE cities ("
        #              "city_id varchar(255) NOT NULL,"
        #              "city varchar(50) NOT NULL,"
        #              "state varchar(50) NOT NULL,"
        #              "latitude double NOT NULL,"
        #              "longitude double NOT NULL,"
        #              "county varchar(50) NOT NULL,"
        #              "PRIMARY KEY (city_id),"
        #              "KEY fk_state_from_states_idx (state),"
        #              "CONSTRAINT fk_state_from_states FOREIGN KEY (state) REFERENCES states (state)")


        # # OLD
        # curr.execute("CREATE TABLE cities ("
        #              "city varchar(50) NOT NULL,"
        #              "state varchar(50) NOT NULL,"
        #              "latitude double NOT NULL,"
        #              "longitude double NOT NULL,"""
        #              "county varchar(50) NOT NULL,"
        #              "city_id varchar(255) NOT NULL"
        #              ")")
        infilecomp = open("cities_extended.csv")
        csv_reader = reader(infilecomp)
        next(csv_reader)
        flag = False
        for row in csv_reader:
            try:
                if not flag:
                    flag = True
                    continue
                locations_row, res_row = create_row(row, "cities_extended.csv")
                if not res_row:
                    continue
                my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5])
                my_query = """INSERT INTO cities VALUES (%s,%s,%s,%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
            except MySQL.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

        # parks [6, 21, 23, 24]
        # curr.execute("DROP TABLE IF EXISTS Parks")
        # curr.execute("TRUNCATE TABLE Parks")

        # # NEW
        # curr.execute("CREATE TABLE IF NOT EXISTS Parks ("
        #              "park_id varchar(255) NOT NULL,"
        #              "website varchar(255) DEFAULT NULL,"
        #              "national_or_state varchar(10) DEFAULT NULL,"
        #              "PRIMARY KEY (park_id)")

        # OLD
        # curr.execute("CREATE TABLE IF NOT EXISTS Parks ("
        #              "website VARCHAR(255),"
        #              "national_or_state VARCHAR(10),"
        #              "name VARCHAR(50),"
        #              "state VARCHAR(50),"
        #              "longitude double NOT NULL,"
        #              "latitude double NOT NULL,"
        #              "park_id varchar(255) NOT NULL"
        #              ")")
        infilecomp = open("National-Park-Database-DFE.csv", encoding="utf8")
        csv_reader = reader(infilecomp)
        next(csv_reader)
        flag = False
        for row in csv_reader:
            try:

                # curr.execute("INSERT INTO 'Parks' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
                #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                #              row[11], row[12], row[13], row[14])
                if not flag:
                    flag = True
                    continue
                locations_row, res_row = create_row(row, "National-Park-Database-DFE.csv")
                if not res_row:
                    continue
                my_insert_data = (
                    locations_row[0], locations_row[1], locations_row[2], locations_row[3], locations_row[4],
                    locations_row[5])
                my_query = """INSERT INTO locations VALUES (%s,%s,%s,%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
                my_insert_data = (res_row[0], res_row[1], res_row[2])
                my_query = """INSERT INTO Parks VALUES (%s,%s,%s)"""
                curr.execute(my_query, my_insert_data)
                curr.connection.commit()
            except MySQL.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        curr.close()
        curr.connection.commit()
        curr.connection.close()


def create_row(row, csv_name):
    res_row = []
    locations_row = []
    row_id = ""
    hash_id = ""
    if csv_name == "us_campsites.csv":
        # CAMP_ROW_LOCATIONS_COLUMNS = [0, 1, 3, 11]
        # CAMP_ROW_COLUMNS = [5, 14]
        for i in CAMP_ROW_LOCATIONS_COLUMNS:
            element = row[i]
            if element == "":
                return True, False
            if i == 0 or i == 1:
                temp = str(element)
                hash_id += temp
            locations_row.append(element)
        locations_row.append(0)
        row_id += "campsite_" + str(hash(hash_id))
        locations_row.insert(0, row_id)
        for i in CAMP_ROW_COLUMNS:
            element = row[i]
            if element == "":
                return True, False
            res_row.append(element)
        res_row.insert(0, row_id)
    elif csv_name == "National-Park-Database-DFE.csv":
        # PARKS_ROW_COLUMNS = [6, 21]  # id
        # PARKS_ROW_LOCATIONS_COLUMNS = [23, 24]  # type, id
        longitude, latitude = uniform(-124, -67), uniform(25, 49)
        locations_row.append(latitude)
        locations_row.append(longitude)
        for i in PARKS_ROW_LOCATIONS_COLUMNS:
            element = row[i]
            if element == "":
                return True, False
            locations_row.append(element)
        locations_row.append(1)
        hash_id = str(row[23]) + str(row[24])
        row_id += "park_" + str(hash(hash_id))
        locations_row.insert(0, row_id)
        for i in PARKS_ROW_COLUMNS:
            element = row[i]
            if element == "":
                return True, False
            res_row.append(element)
        res_row.insert(0, row_id)
    elif csv_name == "airbnb_all.csv":
        # AIRBNB_ROW_COLUMNS = [0, 6, 13, 15, 16]  # id
        # AIRBNB_ROW_LOCATIONS_COLUMNS = [1, 7, 11, 12]  # type, id
        for i in AIRBNB_ROW_LOCATIONS_COLUMNS:
            element = row[i]
            if element == "":
                return True, False
            if i == 11 or i == 12:
                temp = str(element)
                hash_id += temp
                locations_row.insert(0, element)
            else:
                locations_row.append(element)
        locations_row.append(2)
        row_id += "airbnb_" + str(hash(hash_id))
        locations_row.insert(0, row_id)
        for i in AIRBNB_ROW_COLUMNS:
            element = row[i]
            if element == "":
                return True, False
            res_row.append(element)
        res_row.insert(0, row_id)
    elif csv_name == "cities_extended.csv":
        for i in row:
            res_row.append(i)
        hash_id = str(row[2]) + str(row[3])
        row_id += "city_" + str(hash(hash_id))
        res_row.insert(0, row_id)
    elif csv_name == "states.csv":
        for i in row:
            res_row.append(i)
    else:
        return
    return locations_row, res_row
