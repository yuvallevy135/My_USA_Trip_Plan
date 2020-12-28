from random import uniform

import self as self
import simplejson as json
# from flask_restful.representations import json
from mysql.connector import errorcode
from csv import reader, writer
from flask import Flask, request, jsonify, redirect, render_template, url_for
from flask_restful import Api, Resource, abort
from flask_mysqldb import MySQL

from db_creator import DbCreator

CAMP_ROW_COLUMNS = [5, 14]  # id
CAMP_ROW_LOCATIONS_COLUMNS = [0, 1, 3, 11]  # type, id
PARKS_ROW_COLUMNS = [6, 21]  # id
PARKS_ROW_LOCATIONS_COLUMNS = [23, 24]  # type, id
AIRBNB_ROW_COLUMNS = [0, 6, 13, 15, 16]  # id
AIRBNB_ROW_LOCATIONS_COLUMNS = [1, 7, 11, 12]  # type, id
DASHBOARD_URL = "http://127.0.0.1:5500/wwwroot/Dashboard.html"
#
#
# def main():
#     # with open('us_campsites.csv', 'r') as csv_file:
#     #     csv_reader = csv.reader(csv_file)
#     #     for line in csv_reader:
#     #         print(line[2])
#
#     # Campsites
#     # curr.execute("DROP TABLE IF EXISTS Campsites")
#     curr = mysql.connection.cursor()
#     # curr.execute("TRUNCATE TABLE Campsites")
#     # curr.execute("CREATE TABLE IF NOT EXISTS Campsites ("
#     #              "longitude double NOT NULL,"
#     #              "latitude double NOT NULL,"
#     #              "name VARCHAR(50),"
#     #              "phone VARCHAR(50),"
#     #              "state VARCHAR(50),"
#     #              "city VARCHAR(50),"
#     #              "campsite_id VARCHAR(255)"
#     #              ")")
#     infilecomp = open("us_campsites.csv")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#
#             # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
#             #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#             #              row[11], row[12], row[13], row[14])
#             if not flag:
#                 flag = True
#                 continue
#             locations_row, res_row = create_row(row, "us_campsites.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (locations_row[0], locations_row[1], locations_row[2], locations_row[3], locations_row[4],
#                               locations_row[5])
#             my_query = """INSERT INTO locations VALUES (%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#             my_insert_data = (res_row[0], res_row[1], res_row[2])
#             my_query = """INSERT INTO Campsites VALUES (%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # Listing_url, name, city, state, latitude, longitude, root_type,price,review_score] + airbbn_id
#     # Airbnb [0,1,6,7,11,12,13,15,16] +17
#     # curr.execute("DROP TABLE IF EXISTS Airbnb")
#     curr.execute("TRUNCATE TABLE Airbnb")
#
#     # curr.execute("CREATE TABLE IF NOT EXISTS Airbnb ("
#     #              "listing_url VARCHAR(255),"
#     #              "name VARCHAR(255),"
#     #              "city VARCHAR(50),"
#     #              "state VARCHAR(50),"
#     #              "latitude double NOT NULL,"
#     #              "longitude double NOT NULL,"
#     #              "property_type VARCHAR(50),"
#     #              "price double NOT NULL,"
#     #              "rank_score double NOT NULL,"
#     #              "airbnb_id VARCHAR(255)"
#     #              ")")
#     infilecomp = open("airbnb_all.csv", encoding="utf8")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     for row in csv_reader:
#         try:
#
#             # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
#             #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#             #              row[11], row[12], row[13], row[14])
#             locations_row, res_row = create_row(row, "airbnb_all.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (locations_row[0], locations_row[1], locations_row[2], locations_row[3], locations_row[4],
#                               locations_row[5])
#             my_query = """INSERT INTO locations VALUES (%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#             my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5])
#             my_query = """INSERT INTO Airbnb VALUES (%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # states
#     # curr.execute("DROP TABLE IF EXISTS states")
#     # curr.execute("TRUNCATE TABLE states")
#
#     # curr.execute("CREATE TABLE states ("
#     #              "state varchar(50) NOT NULL,"
#     #              "state_code char(2) NOT NULL"
#     #              ")")
#     infilecomp = open("states.csv")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#             if not flag:
#                 flag = True
#                 continue
#             locations_row, res_row = create_row(row, "states.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1])
#             my_query = """INSERT INTO states VALUES (%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # cities
#     curr.execute("DROP TABLE IF EXISTS cities")
#     curr.execute("TRUNCATE TABLE cities")
#
#     curr.execute("CREATE TABLE cities ("
#                  "city varchar(50) NOT NULL,"
#                  "state varchar(50) NOT NULL,"
#                  "latitude double NOT NULL,"
#                  "longitude double NOT NULL,"""
#                  "county varchar(50) NOT NULL,"
#                  "city_id varchar(255) NOT NULL"
#                  ")")
#     infilecomp = open("cities_extended.csv")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#             if not flag:
#                 flag = True
#                 continue
#             locations_row, res_row = create_row(row, "cities_extended.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5])
#             my_query = """INSERT INTO cities VALUES (%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # parks [6, 21, 23, 24]
#     # curr.execute("DROP TABLE IF EXISTS Parks")
#     # curr.execute("TRUNCATE TABLE Parks")
#     # curr.execute("CREATE TABLE IF NOT EXISTS Parks ("
#     #              "website VARCHAR(255),"
#     #              "national_or_state VARCHAR(10),"
#     #              "name VARCHAR(50),"
#     #              "state VARCHAR(50),"
#     #              "longitude double NOT NULL,"
#     #              "latitude double NOT NULL,"
#     #              "park_id varchar(255) NOT NULL"
#     #              ")")
#     infilecomp = open("National-Park-Database-DFE.csv", encoding="utf8")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#
#             # curr.execute("INSERT INTO 'Parks' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
#             #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#             #              row[11], row[12], row[13], row[14])
#             if not flag:
#                 flag = True
#                 continue
#             locations_row, res_row = create_row(row, "National-Park-Database-DFE.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (locations_row[0], locations_row[1], locations_row[2], locations_row[3], locations_row[4],
#                               locations_row[5])
#             my_query = """INSERT INTO locations VALUES (%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#             my_insert_data = (res_row[0], res_row[1], res_row[2])
#             my_query = """INSERT INTO Parks VALUES (%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             mysql.connection.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#     curr.close()
#     mysql.connection.commit()
#     mysql.connection.close()
#
#
# def create_row(row, csv_name):
#     res_row = []
#     locations_row = []
#     row_id = ""
#     hash_id = ""
#     if csv_name == "us_campsites.csv":
#         # CAMP_ROW_LOCATIONS_COLUMNS = [0, 1, 3, 11]
#         # CAMP_ROW_COLUMNS = [5, 14]
#         for i in CAMP_ROW_LOCATIONS_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return True, False
#             if i == 0 or i == 1:
#                 temp = str(element)
#                 hash_id += temp
#             locations_row.append(element)
#         locations_row.append(0)
#         row_id += "campsite_" + str(hash(hash_id))
#         locations_row.insert(0, row_id)
#         for i in CAMP_ROW_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return True, False
#             res_row.append(element)
#         res_row.insert(0, row_id)
#     elif csv_name == "National-Park-Database-DFE.csv":
#         # PARKS_ROW_COLUMNS = [6, 21]  # id
#         # PARKS_ROW_LOCATIONS_COLUMNS = [23, 24]  # type, id
#         longitude, latitude = uniform(-124, -67), uniform(25, 49)
#         locations_row.append(latitude)
#         locations_row.append(longitude)
#         for i in PARKS_ROW_LOCATIONS_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return True, False
#             locations_row.append(element)
#         locations_row.append(1)
#         hash_id = str(row[23]) + str(row[24])
#         row_id += "park_" + str(hash(hash_id))
#         locations_row.insert(0, row_id)
#         for i in PARKS_ROW_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return True, False
#             res_row.append(element)
#         res_row.insert(0, row_id)
#     elif csv_name == "airbnb_all.csv":
#         # AIRBNB_ROW_COLUMNS = [0, 6, 13, 15, 16]  # id
#         # AIRBNB_ROW_LOCATIONS_COLUMNS = [1, 7, 11, 12]  # type, id
#         for i in AIRBNB_ROW_LOCATIONS_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return True, False
#             if i == 11 or i == 12:
#                 temp = str(element)
#                 hash_id += temp
#                 locations_row.insert(0, element)
#             else:
#                 locations_row.append(element)
#         locations_row.append(2)
#         row_id += "airbnb_" + str(hash(hash_id))
#         locations_row.insert(0, row_id)
#         for i in AIRBNB_ROW_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return True, False
#             res_row.append(element)
#         res_row.insert(0, row_id)
#     elif csv_name == "cities_extended.csv":
#         for i in row:
#             res_row.append(i)
#         hash_id = str(row[2]) + str(row[3])
#         row_id += "city_" + str(hash(hash_id))
#         res_row.insert(0, row_id)
#     elif csv_name == "states.csv":
#         for i in row:
#             res_row.append(i)
#     else:
#         return
#     return locations_row, res_row


# -----------------------------------------------------------------------------

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "plan_trip"
mysql = MySQL(app)


# SELECT locations.*, plan_trip.campsites.phone, plan_trip.campsites.city FROM locations join plan_trip.campsites on locations.location_id = plan_trip.campsites.campsite_id


# A function that creates a dynamic query
def create_exists_query(select_what, table_name, value_name, extra_condition):
    select_part = "SELECT " + str(select_what)
    from_part = " FROM " + str(table_name)
    condition_part = " WHERE " + str(value_name) + " = %s " + extra_condition
    my_query = select_part + from_part + condition_part
    return my_query


# Check if the value that we are looking for is already in DB. If yes - let the user know!
def abort_if_username_exist(table_name, value_name, value_id):
    # create connection to db to check if username in db.
    try:
        cur = mysql.connection.cursor()
        # my_query = "SELECT * FROM " + str(my_class) + " WHERE username = %s"
        my_query = create_exists_query('*', table_name, value_name, "")
        cur.execute(my_query, (value_id,))
        data = cur.fetchall()
        cur.close()
        if len(data) != 0:
            abort(409, message="Username already exists... Pick different a user name.")
    except:
        abort(409, message="Lost connection with DB")


# Check if the value that we are looking for does not  in DB. If not - let the user know. Else - return it.
def abort_if_username_doesnt_exist(select_what, table_name, value_name, value_id, extra_condition, method):
    try:
        # create connection to db to check if username in db.
        cur = mysql.connection.cursor()
        # my_query = "SELECT " + str(select_what) + " FROM " + str(table_name) + " WHERE " + str(value_name) + " = %s"
        my_query = create_exists_query(select_what, table_name, value_name, extra_condition)
        cur.execute(my_query, (value_id,))
        data = cur.fetchall()
        if len(data) == 0:
            cur.close()
            abort(404, message="Could not find that user.")
        elif method == 'delete':
            cur.close()
            return
        else:
            # row_headers = [x[0] for x in cur.description]  # this will extract row headers
            # json_data = []
            # for result in data:
            #     json_data.append(dict(zip(row_headers, result)))
            json_data = make_res_as_json_with_col_names(data, cur)
            cur.close()
            json.dumps(json_data, use_decimal=True)
            return json_data
    except:
        abort(409, message="Lost connection with DB")


# A function that create a json back with the columns from the DB of the values that we want to return.
def make_res_as_json_with_col_names(data, cur):
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


# A Class that takes care of everything that relates to the User table.
class Username(Resource):
    # Add new user.
    # @app.route('/add_user', methods=['POST'])
    def post(self, username):
        try:
            if request.method == 'POST':
                data = request.form
                username = data['username']
                password = data['psw']
                cur = mysql.connection.cursor()
                my_query = """SELECT * FROM users where username = %s and password = %s"""
                cur.execute(my_query, (username, password,))
                user = cur.fetchall()
                user = make_res_as_json_with_col_names(user, cur)
                # json.dumps(user, use_decimal=True)
                return redirect(url_for("dashboard", user_name=username))
            # data = request.get_json()
            data = request.form
            username = data['username']
            param = []
            for i in data:
                param.append(data[i])
            abort_if_username_exist('users', 'username', username)
            cur = mysql.connection.cursor()
            my_query = 'INSERT INTO users VALUES(%s,%s,%s,%s)'
            # param = (username, password, email)
            cur.execute(my_query, param)
            mysql.connection.commit()
            mysql.connection.close()
            try:
                return redirect(url_for("dashboard"))
                # return render_template("http://127.0.0.1:5500/wwwroot/Pages/Dashboard.html")
                # return username, 204
            except Exception as e:
                print("Problem: " + str(e))
        except:
            abort(409, message="Lost connection with DB")

    def get(self, username):
        try:
            if not username == 'login':
                extra_condition = ""
                user = abort_if_username_doesnt_exist('*', "users", 'username', username, extra_condition, 'get')
        except:
            abort(409, message="Lost connection with DB")

    def delete(self, username):
        try:
            # DONT FORGET to delete all rows in tables that are relevant to user...
            extra_condition = ""
            user = abort_if_username_doesnt_exist('*', 'users', 'username', username, extra_condition, 'delete')
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM users WHERE username = %s"
            cur.execute(my_query, (username,))
            mysql.connection.commit()
            mysql.connection.close()
            # delete the user.
            return 204
            # return '',204
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Airbnb table.
class Airbnb(Resource):

    # Add new user.
    # @app.route('/add_user', methods=['POST'])
    def post(self, airbnb_id):
        try:
            data = request.get_json()
            param = []
            for i in data:
                param.append(data[i])
            abort_if_username_exist('airbnb', 'location_id', airbnb_id)
            cur = mysql.connection.cursor()
            my_query = 'INSERT INTO airbnb VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # param = (username, password, email)
            cur.execute(my_query, param)
            mysql.connection.commit()
            mysql.connection.close()
            return 201
            # return username, 204
        except:
            abort(409, message="Lost connection with DB")

    def get(self, airbnb_id):
        try:
            # select_what = "locations.*, airbnb.listing_url, airbnb.city, airbnb.property_type, " \
            #               "airbnb.price, airbnb.rank_score"
            # table_name = "locations join airbnb on locations.location_id = airbnb.airbnb_id"
            select_what = "airbnb.listing_url, airbnb.city, airbnb.property_type, " \
                          "airbnb.price, airbnb.rank_score"
            table_name = "airbnb"
            extra_condition = ""
            # condition = "where locations.location_id = %s"
            airbnb = abort_if_username_doesnt_exist(select_what, table_name, 'airbnb_id', airbnb_id, extra_condition, 'get')
            return airbnb
        except:
            abort(409, message="Lost connection with DB")

    def delete(self, airbnb_id):
        try:
            extra_condition = ""
            user = abort_if_username_doesnt_exist('*', 'airbnb', 'airbnb_id', airbnb_id, extra_condition, 'delete')
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM airbnb WHERE airbnb_id = %s"
            cur.execute(my_query, (airbnb_id,))
            mysql.connection.commit()
            mysql.connection.close()
            # delete the user.
            return 204
        # return '',204
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Parks table.
class Parks(Resource):
    # Add new user.
    # @app.route('/add_user', methods=['POST'])
    def post(self, park_id):
        try:
            data = request.get_json()
            param = []
            for i in data:
                param.append(data[i])
            abort_if_username_exist('parks', 'location_id', park_id)
            cur = mysql.connection.cursor()
            my_query = 'INSERT INTO parks VALUES(%s,%s,%s,%s,%s,%s,%s)'
            # param = (username, password, email)
            cur.execute(my_query, param)
            mysql.connection.commit()
            mysql.connection.close()
            return 201
            # return username, 204
        except:
            abort(409, message="Lost connection with DB")

    def get(self, park_id):
        try:
            select_what = "locations.*, parks.website, parks.national_or_state"
            table_name = "locations join parks on locations.location_id = parks.park_id"
            extra_condition = ""
            # condition = "where locations.location_id = %s"
            park = abort_if_username_doesnt_exist(select_what, table_name, 'park_id', park_id, extra_condition, 'get')
            return park
        except:
            abort(409, message="Lost connection with DB")

    def delete(self, park_id):
        try:
            extra_condition = ""
            user = abort_if_username_doesnt_exist('*', 'parks', 'park_id', park_id, extra_condition, 'delete')
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM parks WHERE park_id = %s"
            cur.execute(my_query, (park_id,))
            mysql.connection.commit()
            mysql.connection.close()
            # delete the user.
            return 204
            # return '',204
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Campsites table.
class Campsites(Resource):

    # Add new user.
    # @app.route('/add_user', methods=['POST'])
    def post(self, campsite_id):
        try:
            data = request.get_json()
            param = []
            for i in data:
                param.append(data[i])
            abort_if_username_exist('campsites', 'location_id', campsite_id)
            cur = mysql.connection.cursor()
            my_query = 'INSERT INTO campsites VALUES(%s,%s,%s,%s,%s,%s,%s)'
            # param = (username, password, email)
            cur.execute(my_query, param)
            mysql.connection.commit()
            mysql.connection.close()
            return 201
            # return username, 204
        except:
            abort(409, message="Lost connection with DB")

    def get(self, campsite_id):
        try:
            select_what = "locations.*, campsites.phone, campsites.city"
            table_name = "locations join campsites on locations.location_id = campsites.campsite_id"
            extra_condition = ""
            # condition = "where locations.location_id = %s"
            campsite = abort_if_username_doesnt_exist(select_what, table_name, 'campsite_id', campsite_id,
                                                      extra_condition, 'get')
            return campsite
        except:
            abort(409, message="Lost connection with DB")

    def delete(self, campsite_id):
        try:
            extra_condition = ""
            user = abort_if_username_doesnt_exist('*', 'campsites', 'campsite_id', campsite_id, extra_condition, 'delete')
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM campsites WHERE park_id = %s"
            cur.execute(my_query, (campsite_id,))
            mysql.connection.commit()
            mysql.connection.close()
            # delete the user.
            return 204
            # return '',204
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Cities table.
class Cities(Resource):

    # Add new user.
    # @app.route('/add_user', methods=['POST'])
    def post(self, city_id):
        try:
            if request.method == 'POST':
                # data = request.get_json()
                data = request.json
                cities_list = []
                for city in data['cities']:
                    extra_condition = ""
                    city = abort_if_username_doesnt_exist('*', 'cities', 'city', city, extra_condition, 'get')
                    cities_list.append(city)
                json.dumps(cities_list, use_decimal=True)
                return cities_list
            else:
                data = request.get_json()
                param = []
                for i in data:
                    param.append(data[i])
                abort_if_username_exist('cities', 'city', city_id)
                cur = mysql.connection.cursor()
                my_query = 'INSERT INTO cities VALUES(%s,%s,%s,%s,%s,%s)'
                # param = (username, password, email)
                cur.execute(my_query, param)
                mysql.connection.commit()
                mysql.connection.close()
                return 201
                # return username, 204
        except:
            abort(409, message="Lost connection with DB")

    def get(self, city_id):
        try:
            # Either its regular city get or its the start screen and we need to return multiple.
            if not city_id == 'start_cities':
                extra_condition = ""
                user = abort_if_username_doesnt_exist('*', 'cities', 'city', city_id, extra_condition, 'get')
                return user
            # else:
            #     data = request.get_json()
            #     cities_list = []
            #     for city in data['cities']:
            #         extra_condition = ""
            #         city = abort_if_username_doesnt_exist('*', 'cities', 'city', city, extra_condition, 'get')
            #         cities_list.append(city)
            #     json.dumps(cities_list, use_decimal=True)
            # return cities_list
        except:
            abort(409, message="Lost connection with DB")

    def delete(self, city_id):
        try:
            extra_condition = ""
            user = abort_if_username_doesnt_exist('*', 'cities', 'city', city_id, extra_condition, 'delete')
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM campsites WHERE park_id = %s"
            cur.execute(my_query, (city_id,))
            mysql.connection.commit()
            mysql.connection.close()
            # delete the user.
            return 204
            # return '',204
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Locations table.
class Locations(Resource):

    def post(self):
        try:
            cur = mysql.connection.cursor()
            type_to_table = {'campsites': 0, 'parks': 1, 'airbnb': 2}
            select_part = "SELECT *"
            from_part = " FROM locations"
            condition = " Where "
            tables_names_list = request.json['filterList']
            my_query = select_part + from_part
            flag = False
            for i in tables_names_list:
                if (flag):
                    condition += " or "
                flag = True
                type = type_to_table[i]
                condition += "type=" + str(type)
            my_query += condition
            cur.execute(my_query)
            data = cur.fetchall()
            row_headers = [x[0] for x in cur.description]  # this will extract row headers
            json_data = make_res_as_json_with_col_names(data, cur)
            json.dumps(json_data, use_decimal=True)
            return json_data
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Trips table.
class Trips(Resource):
    def post(self, trip_id):
        try:
            data = request.get_json()
            # abort_if_username_exist('trips', 'trip_id', trip_id)
            # trip_id = data['trip_id']
            username = data['username']
            waypoint_list = data['locations']
            cur = mysql.connection.cursor()
            my_query = """INSERT INTO trips VALUES(DEFAULT,%s)"""
            # insert the trip - dont forget to only commit after all waypoints are in!
            cur.execute(my_query, (username,))
            id = cur.lastrowid
            # waypoint now... loop and insert each waypoint and commit at the end.
            for i in waypoint_list:
                waypoints_param = []
                waypoints_param.insert(0, id)
                waypoints_param.extend(i)
                my_query = """INSERT INTO waypoints_in_trip VALUES(%s,%s,%s)"""
                cur.executemany(my_query, (waypoints_param,))
            # insert the trip - don't forget to only commit after all waypoints are in!
            mysql.connection.commit()
            mysql.connection.close()
            return 201
            # return username, 204
        except:
            abort(409, message="Lost connection with DB")

    def get(self, trip_id):
        try:
            # Get all trips with waypoints.
            if not trip_id == 'get_all' and not trip_id == 'username':
                # select_what = "trips.trip_id, location_id, station_number"
                select_what = "location_id, station_number"
                table_name = "trips join waypoints_in_trip"
                condition = "on trips.trip_id = waypoints_in_trip.trip_id " \
                            "order by trips.trip_id, waypoints_in_trip.station_number"
                data = abort_if_username_doesnt_exist(select_what, table_name, 'trips.trip_id', trip_id, condition, 'get')
            else:
                select_what = "select trips.trip_id, location_id, station_number "
                from_table = "from trips join waypoints_in_trip "
                where = ""
                limit = ""
                if trip_id == 'username':
                    data = request.get_json()
                    username = data['username']
                    where = "where username = '" + str(username) + "' "
                condition = "order by trips.trip_id, station_number"
                cur = mysql.connection.cursor()
                my_query = select_what + from_table + where + condition
                cur.execute(my_query)
                data = cur.fetchall()
                data = make_res_as_json_with_col_names(data, cur)
            json.dumps(data, use_decimal=True)
            return data
        except:
            abort(409, message="Lost connection with DB")

    def delete(self, trip_id):
        try:
            # select_what = "trips.trip_id, location_id, station_number"
            select_what = "*"
            table_name = "trips"
            condition = ""
            trip = abort_if_username_doesnt_exist(select_what, table_name, 'trips.trip_id', trip_id, condition, 'delete')
            cur = mysql.connection.cursor()
            my_query = "DELETE FROM waypoints_in_trip WHERE trip_id = %s"
            cur.execute(my_query, (trip_id,))
            my_query = "DELETE FROM trips WHERE trip_id = %s"
            cur.execute(my_query, (trip_id,))
            mysql.connection.commit()
            mysql.connection.close()
            # delete the user.
            return 204
            # return '',204
        except:
            abort(409, message="Lost connection with DB")

    def put(self, trip_id):
        try:
            # Get all waypoints of that trip and delete them... then - create new ones..
            # select_what = "trips.trip_id, location_id, station_number"
            my_query = "DELETE FROM waypoints_in_trip WHERE trip_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(my_query, (trip_id,))
            # now re add all waypoints.
            data = request.get_json()
            # abort_if_username_exist('trips', 'trip_id', trip_id)
            username = data['username']
            waypoint_list = data['locations']
            # waypoint now... loop and insert each waypoint and commit at the end.
            for i in waypoint_list:
                waypoints_param = []
                waypoints_param.insert(0, trip_id)
                waypoints_param.extend(i)
                my_query = """INSERT INTO waypoints_in_trip VALUES(%s,%s,%s)"""
                cur.executemany(my_query, (waypoints_param,))
            # insert the trip - don't forget to only commit after all waypoints are in!
            mysql.connection.commit()
            mysql.connection.close()
            return 201
        except:
            abort(409, message="Lost connection with DB")


# A Class that takes care of everything that relates to the Radius calculation.
class Radius(Resource):
    def get(self):
        try:
            data = request.get_json()
            latitude = data['latitude']
            longitude = data['longitude']
            distance = data['distance']
            params = [latitude, longitude, latitude, distance]
            my_query = """SELECT
                      location_id, name, state, latitude, longitude, (
                        3959 * acos (
                          cos ( radians(%s) )
                          * cos( radians( latitude ) )
                          * cos( radians( longitude ) - radians(%s) )
                          + sin ( radians(%s) )
                          * sin( radians( latitude ) )
                        )
                      ) AS distance
                    FROM locations
                    HAVING distance < %s
                    ORDER BY distance
                    LIMIT 0 , 100;"""
            cur = mysql.connection.cursor()
            cur.executemany(my_query, (params,))
            data = cur.fetchall()
            data = make_res_as_json_with_col_names(data, cur)
            json.dumps(data, use_decimal=True)
            return data
        except:
            abort(409, message="Lost connection with DB")


@app.route("/livesearch", methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "select city,state from cities where city LIKE '{}%' order by city limit 0,5".format(searchbox)#This is just example query , you should replace field names with yours
    cursor.execute(query)
    result = cursor.fetchall()
    result = make_res_as_json_with_col_names(result, cursor)
    return jsonify(result)


@app.route("/<user_name>")
def dashboard(user_name):
    #http://127.0.0.1:5500
    return render_template("Dashboard.html", username=user_name)


@app.route("/MemberIndex")
def memberIndex():
    #http://127.0.0.1:5500
    return render_template("MemberIndex.html")



@app.route("/")
def home():
    return render_template("index.html")


api.add_resource(Username, "/users/<string:username>")
api.add_resource(Airbnb, "/airbnb/<string:airbnb_id>")
api.add_resource(Parks, "/parks/<string:park_id>")
api.add_resource(Campsites, "/campsites/<string:campsite_id>")
api.add_resource(Cities, "/cities/<string:city_id>")
api.add_resource(Trips, "/trips/<string:trip_id>")
api.add_resource(Locations, "/locations")
api.add_resource(Radius, "/radius")
if __name__ == "__main__":
    # main()
    # db_creator = DbCreator
    # db_creator.create_db(self)
    app.run(debug=True)

# ...............................................................................
# from random import uniform
# import simplejson as json
# import mysql.connector as MySQL
# # from flask_restful.representations import json
# from mysql.connector import errorcode
# from csv import reader, writer
# from flask import Flask, request, jsonify
# from flask_restful import Api, Resource, abort
# from flask_mysqldb import MySQL
#
# CAMP_ROW_COLUMNS = [0, 1, 3, 5, 11, 14]
# PARKS_ROW_COLUMNS = [6, 21, 23, 24]
# AIRBNB_ROW_COLUMNS = [0, 1, 6, 7, 11, 12, 13, 15, 16]
#
#
# def main():
#     # with open('us_campsites.csv', 'r') as csv_file:
#     #     csv_reader = csv.reader(csv_file)
#     #     for line in csv_reader:
#     #         print(line[2])
#
#     conn = MySQL.connect(
#         host="localhost",
#         database='plan_trip',
#         user="root",
#         password="Aa123456",
#     )
#     if conn:
#         print("Yes")
#     else:
#         print("No")
#     curr = conn.cursor()
#
#     # Campsites
#     curr.execute("TRUNCATE TABLE IF EXISTS Campsites")
#     curr.execute("CREATE TABLE IF NOT EXISTS Campsites ("
#                  "longitude double NOT NULL,"
#                  "latitude double NOT NULL,"
#                  "name VARCHAR(50),"
#                  "phone VARCHAR(50),"
#                  "state VARCHAR(50),"
#                  "city VARCHAR(50),"
#                  "campsite_id VARCHAR(255)"
#                  ")")
#     infilecomp = open("us_campsites.csv")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#
#             # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
#             #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#             #              row[11], row[12], row[13], row[14])
#             if not flag:
#                 flag = True
#                 continue
#             res_row = create_row(row, "us_campsites.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5], res_row[6])
#             my_query = """INSERT INTO Campsites VALUES (%s,%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             conn.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # Listing_url, name, city, state, latitude, longitude, root_type,price,review_score] + airbbn_id
#     # Airbnb [0,1,6,7,11,12,13,15,16] +17
#     curr.execute("TRUNCATE TABLE IF EXISTS Airbnb")
#
#     curr.execute("CREATE TABLE IF NOT EXISTS Airbnb ("
#                  "listing_url VARCHAR(255),"
#                  "name VARCHAR(255),"
#                  "city VARCHAR(50),"
#                  "state VARCHAR(50),"
#                  "latitude double NOT NULL,"
#                  "longitude double NOT NULL,"
#                  "property_type VARCHAR(50),"
#                  "price double NOT NULL,"
#                  "rank_score double NOT NULL,"
#                  "airbnb_id VARCHAR(255)"
#                  ")")
#     infilecomp = open("airbnb_all.csv", encoding="utf8")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     for row in csv_reader:
#         try:
#
#             # curr.execute("INSERT INTO 'Campsites' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
#             #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#             #              row[11], row[12], row[13], row[14])
#             res_row = create_row(row, "airbnb_all.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5], res_row[6],
#                               res_row[7], res_row[8], res_row[9])
#             my_query = """INSERT INTO Airbnb VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             conn.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # states
#     curr.execute("TRUNCATE TABLE IF EXISTS states")
#
#     curr.execute("CREATE TABLE states ("
#                  "state varchar(50) NOT NULL,"
#                  "state_code char(2) NOT NULL"
#                  ")")
#     infilecomp = open("states.csv")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#             if not flag:
#                 flag = True
#                 continue
#             res_row = create_row(row, "states.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1])
#             my_query = """INSERT INTO states VALUES (%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             conn.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # cities
#     curr.execute("TRUNCATE TABLE IF EXISTS cities")
#
#     curr.execute("CREATE TABLE cities ("
#                  "city varchar(50) NOT NULL,"
#                  "state varchar(50) NOT NULL,"
#                  "latitude double NOT NULL,"
#                  "longitude double NOT NULL,"""
#                  "county varchar(50) NOT NULL,"
#                  "city_id varchar(255) NOT NULL"
#                  ")")
#     infilecomp = open("cities_extended.csv")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#             if not flag:
#                 flag = True
#                 continue
#             res_row = create_row(row, "cities_extended.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5])
#             my_query = """INSERT INTO cities VALUES (%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             conn.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#
#     # parks [6, 21, 23, 24]
#     curr.execute("TRUNCATE TABLE IF EXISTS Parks")
#     curr.execute("CREATE TABLE IF NOT EXISTS Parks ("
#                  "website VARCHAR(255),"
#                  "national_or_state VARCHAR(10),"
#                  "name VARCHAR(50),"
#                  "state VARCHAR(50),"
#                  "longitude double NOT NULL,"
#                  "latitude double NOT NULL,"
#                  "park_id varchar(255) NOT NULL"
#                  ")")
#     infilecomp = open("National-Park-Database-DFE.csv", encoding="utf8")
#     csv_reader = reader(infilecomp)
#     next(csv_reader)
#     flag = False
#     for row in csv_reader:
#         try:
#
#             # curr.execute("INSERT INTO 'Parks' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s",
#             #              row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#             #              row[11], row[12], row[13], row[14])
#             if not flag:
#                 flag = True
#                 continue
#             res_row = create_row(row, "National-Park-Database-DFE.csv")
#             if not res_row:
#                 continue
#             my_insert_data = (res_row[0], res_row[1], res_row[2], res_row[3], res_row[4], res_row[5], res_row[6])
#             my_query = """INSERT INTO Parks VALUES (%s,%s,%s,%s,%s,%s,%s)"""
#             curr.execute(my_query, my_insert_data)
#             conn.commit()
#         except MySQL.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
#     curr.close()
#     conn.commit()
#     conn.close()
#
#
# def create_row(row, csv_name):
#     res_row = []
#     row_id = ""
#     hash_id = ""
#     if csv_name == "us_campsites.csv":
#         for i in CAMP_ROW_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return False
#             if i == 3:
#                 hash_id = hash(element)
#                 row_id += element + str(hash_id)
#             res_row.append(element)
#         res_row.append(row_id)
#     elif csv_name == "National-Park-Database-DFE.csv":
#         for i in PARKS_ROW_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return False
#             res_row.append(element)
#         longitude, latitude = uniform(-124, -67), uniform(25, 49)
#         res_row.append(longitude)
#         res_row.append(latitude)
#         hash_id = str(row[23]) + str(row[24])
#         row_id += "park_" + str(hash(hash_id))
#         res_row.append(row_id)
#     elif csv_name == "airbnb_all.csv":
#         for i in AIRBNB_ROW_COLUMNS:
#             element = row[i]
#             if element == "":
#                 return False
#             if i == 11 or i == 12:
#                 temp = str(element)
#                 hash_id += temp
#             res_row.append(element)
#
#         row_id += "airbnb_" + str(hash(hash_id))
#         res_row.append(row_id)
#     elif csv_name == "cities_extended.csv":
#         for i in row:
#             res_row.append(i)
#         hash_id = str(row[2]) + str(row[3])
#         row_id += "city_" + str(hash(hash_id))
#         res_row.append(row_id)
#     elif csv_name == "states.csv":
#         for i in row:
#             res_row.append(i)
#     else:
#         return
#     return res_row
#
#
# # -----------------------------------------------------------------------------
#
# app = Flask(__name__)
# api = Api(app)
#
# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = "Aa123456"
# app.config['MYSQL_DB'] = "plan_trip"
# mysql = MySQL(app)
#
#
# def abort_if_username_exist(my_class, username):
#     # create connection to db to check if username in db.
#     cur = mysql.connection.cursor()
#     my_query = "SELECT * FROM " + str(my_class) + " WHERE username = %s"
#     cur.execute(my_query, (username,))
#     data = cur.fetchall()
#     cur.close()
#     if len(data) != 0:
#         abort(409, message="Username already exists... Pick different a user name.")
#
#
# def abort_if_username_doesnt_exist(table_name, value_name, username, method):
#     # create connection to db to check if username in db.
#     cur = mysql.connection.cursor()
#     my_query = "SELECT * FROM " + str(table_name) + " WHERE " + str(value_name) + " = %s"
#     cur.execute(my_query, (username,))
#     data = cur.fetchall()
#     if len(data) == 0:
#         cur.close()
#         abort(404, message="Could not find that user.")
#     elif method == 'delete':
#         cur.close()
#         return
#     else:
#         row_headers = [x[0] for x in cur.description]  # this will extract row headers
#         json_data = []
#         for result in data:
#             json_data.append(dict(zip(row_headers, result)))
#         cur.close()
#         json.dumps(json_data, use_decimal=True)
#         return json_data
#
#
# class Username(Resource):
#
#     # Add new user.
#     # @app.route('/add_user', methods=['POST'])
#     def post(self, username):
#         data = request.get_json()
#         param = []
#         for i in data:
#             param.append(data[i])
#         abort_if_username_exist('users', username)
#         cur = mysql.connection.cursor()
#         my_query = 'INSERT INTO users VALUES(%s,%s,%s)'
#         # param = (username, password, email)
#         cur.execute(my_query, param)
#         mysql.connection.commit()
#         mysql.connection.close()
#         return 201
#         # return username, 204
#
#     def get(self, username):
#         user = abort_if_username_doesnt_exist("users", 'username',  username, 'get')
#         return user
#
#     def delete(self, username):
#         user = abort_if_username_doesnt_exist('users', username, 'delete')
#         cur = mysql.connection.cursor()
#         my_query = "DELETE FROM users WHERE username = %s"
#         cur.execute(my_query, (username,))
#         mysql.connection.commit()
#         mysql.connection.close()
#         # delete the user.
#         return 204
#         # return '',204
#
#
# class Airbnb(Resource):
#
#     # Add new user.
#     # @app.route('/add_user', methods=['POST'])
#     def post(self, airbnb_id):
#         data = request.get_json()
#         param = []
#         for i in data:
#             param.append(data[i])
#         abort_if_username_exist('airbnb', airbnb_id)
#         cur = mysql.connection.cursor()
#         my_query = 'INSERT INTO airbnb VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#         # param = (username, password, email)
#         cur.execute(my_query, param)
#         mysql.connection.commit()
#         mysql.connection.close()
#         return 201
#         # return username, 204
#
#     def get(self, airbnb_id):
#         user = abort_if_username_doesnt_exist('airbnb', 'airbnb_id', airbnb_id, 'get')
#         return user
#
#     def delete(self, airbnb_id):
#         user = abort_if_username_doesnt_exist('airbnb', airbnb_id, 'delete')
#         cur = mysql.connection.cursor()
#         my_query = "DELETE FROM airbnb WHERE airbnb_id = %s"
#         cur.execute(my_query, (airbnb_id,))
#         mysql.connection.commit()
#         mysql.connection.close()
#         # delete the user.
#         return 204
#         # return '',204
#
#
# class Parks(Resource):
#
#     # Add new user.
#     # @app.route('/add_user', methods=['POST'])
#     def post(self, park_id):
#         data = request.get_json()
#         param = []
#         for i in data:
#             param.append(data[i])
#         abort_if_username_exist('parks', park_id)
#         cur = mysql.connection.cursor()
#         my_query = 'INSERT INTO parks VALUES(%s,%s,%s,%s,%s,%s,%s)'
#         # param = (username, password, email)
#         cur.execute(my_query, param)
#         mysql.connection.commit()
#         mysql.connection.close()
#         return 201
#         # return username, 204
#
#     def get(self, park_id):
#         user = abort_if_username_doesnt_exist('parks', park_id, 'get')
#         return user
#
#     def delete(self, park_id):
#         user = abort_if_username_doesnt_exist('parks', park_id, 'delete')
#         cur = mysql.connection.cursor()
#         my_query = "DELETE FROM parks WHERE park_id = %s"
#         cur.execute(my_query, (park_id,))
#         mysql.connection.commit()
#         mysql.connection.close()
#         # delete the user.
#         return 204
#         # return '',204
#
#
# class Campsites(Resource):
#
#     # Add new user.
#     # @app.route('/add_user', methods=['POST'])
#     def post(self, campsite_id):
#         data = request.get_json()
#         param = []
#         for i in data:
#             param.append(data[i])
#         abort_if_username_exist('campsites', campsite_id)
#         cur = mysql.connection.cursor()
#         my_query = 'INSERT INTO campsites VALUES(%s,%s,%s,%s,%s,%s,%s)'
#         # param = (username, password, email)
#         cur.execute(my_query, param)
#         mysql.connection.commit()
#         mysql.connection.close()
#         return 201
#         # return username, 204
#
#     def get(self, campsite_id):
#         user = abort_if_username_doesnt_exist('campsites', campsite_id, 'get')
#         return user
#
#     def delete(self, campsite_id):
#         user = abort_if_username_doesnt_exist('campsites', campsite_id, 'delete')
#         cur = mysql.connection.cursor()
#         my_query = "DELETE FROM campsites WHERE park_id = %s"
#         cur.execute(my_query, (campsite_id,))
#         mysql.connection.commit()
#         mysql.connection.close()
#         # delete the user.
#         return 204
#         # return '',204
#
#
# class Cities(Resource):
#
#     # Add new user.
#     # @app.route('/add_user', methods=['POST'])
#     def post(self, city_id):
#         data = request.get_json()
#         param = []
#         for i in data:
#             param.append(data[i])
#         abort_if_username_exist('cities', city_id)
#         cur = mysql.connection.cursor()
#         my_query = 'INSERT INTO cities VALUES(%s,%s,%s,%s,%s,%s)'
#         # param = (username, password, email)
#         cur.execute(my_query, param)
#         mysql.connection.commit()
#         mysql.connection.close()
#         return 201
#         # return username, 204
#
#     def get(self, city_id):
#         user = abort_if_username_doesnt_exist('cities', city_id, 'get')
#         return user
#
#     def delete(self, city_id):
#         user = abort_if_username_doesnt_exist('cities', city_id, 'delete')
#         cur = mysql.connection.cursor()
#         my_query = "DELETE FROM campsites WHERE park_id = %s"
#         cur.execute(my_query, (city_id,))
#         mysql.connection.commit()
#         mysql.connection.close()
#         # delete the user.
#         return 204
#         # return '',204
#
#
# class Tracks(Resource):
#
#     def get(self, track_id):
#         cur = mysql.connection.cursor()
#         my_query = "SELECT name, latitude, longitude "\
#                    "from plan_trip.campsites "\
#                    "union "\
#                    "select name, latitude, longitude "\
#                    "from plan_trip.parks "\
#                    "union "\
#                    "select name, latitude, longitude " \
#                    "from plan_trip.airbnb "\
#                    "order by name "
#         cur.execute(my_query)
#         data = cur.fetchall()
#         row_headers = [x[0] for x in cur.description]  # this will extract row headers
#         json_data = []
#         for result in data:
#             json_data.append(dict(zip(row_headers, result)))
#         cur.close()
#         return json.dumps(json_data)
#
#
# api.add_resource(Username, "/users/<string:username>")
# api.add_resource(Airbnb, "/airbnb/<string:airbnb_id>")
# api.add_resource(Parks, "/parks/<string:park_id>")
# api.add_resource(Campsites, "/campsites/<string:campsite_id>")
# api.add_resource(Cities, "/cities/<string:city_id>")
# api.add_resource(Tracks, "/tracks/<string:track_id>")
# if __name__ == "__main__":
#     # main()
#     app.run(debug=True)
