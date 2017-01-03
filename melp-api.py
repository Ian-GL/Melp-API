#Import all the libraries that are necessary
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#The engine connects to the SQLite
e = create_engine('sqlite:///restaurants.sqlite')
#The database should be in the same folder

app = Flask(__name__)
api = Api(app)

#The classes for the CRUD operations

class Manage_All(Resource):
    def get(self):
        #Connect to the DB
        conn = e.connect()
        #Perform the SQL query
        query = conn.execute("select * from restaurantes")
        all_restaurants = {'Restaurantes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return all_restaurants
    def post(self):
        conn = e.connect()
        #Get the JSON data from the POST method
        json_data = request.get_json(force=True)
        if json_data.get('id'):
            id_value = str(json_data['id'])
        else:
            return "Could not create the row: id is missing"
        if json_data.get('rating'):
            rating = str(json_data['rating'])
        else:
            return "Could not create the row: rating is missing"
        if json_data.get('name'):
            name = str(json_data['name'])
        else:
            return "Could not create the row: name is missing"
        if json_data.get('site'):
            site = str(json_data['site'])
        else:
            return "Could not create the row: site is missing"
        if json_data.get('email'):
            email = str(json_data['email'])
        else:
            return "Could not create the row: email is missing"
        if json_data.get('phone'):
            phone = str(json_data['phone'])
        else:
            return "Could not create the row: phone is missing"
        if json_data.get('street'):
            street = str(json_data['street'])
        else:
            return "Could not create the row: street is missing"
        if json_data.get('city'):
            city = str(json_data['city'])
        else:
            return "Could not create the row: city is missing"
        if json_data.get('state'):
            state = str(json_data['state'])
        else:
            return "Could not create the row: state is missing"
        if json_data.get('lat'):
            lat = str(json_data['lat'])
        else:
            return "Could not create the row: lat is missing"
        if json_data.get('lng'):
            lng = str(json_data['lng'])
        else:
            return "Could not create the row: lng is missing"
        conn.execute("insert into restaurantes (id, rating, name, site, email, phone, street, city, state, lat, lng) VALUES ('"+id_value+"', '"+rating+"', '"+name+"', '"+site+"', '"+email+"', '"+phone+"', '"+street+"', '"+city+"', '"+state+"', '"+lat+"', '"+lng+"')")   
        return "A new row with the values you entered was added to the database with the id "+id_value


class Manage_By_ID(Resource):
    def get(self, identification):
        conn = e.connect()
        query = conn.execute("select * from restaurantes where id='%s'"%identification)
        by_ID = {'Restaurante con el id' : [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return by_ID
    def delete(self, identification):
        conn = e.connect()
        conn.execute("delete from restaurantes where id='%s'"%identification)
        return "The data was sucessfully ereased"
    def put(self, identification):
        conn = e.connect()
        json_data = request.get_json(force=True)
        columns_updated = ""
        if json_data.get('rating'):
            rating = str(json_data['rating'])
            conn.execute("update restaurantes set rating='"+rating+"' where id='%s'"%identification)
            columns_updated = columns_updated + " rating,"
        if json_data.get('name'):
            name = str(json_data['name'])
            conn.execute("update restaurantes set name='"+name+"' where id='%s'"%identification)
            columns_updated = columns_updated + " name,"
        if json_data.get('site'):
            site = str(json_data['site'])
            conn.execute("update restaurantes set site='"+site+"' where id='%s'"%identification)
            columns_updated = columns_updated + " site,"
        if json_data.get('email'):
            email = str(json_data['email'])
            conn.execute("update restaurantes set email='"+email+"' where id='%s'"%identification)
            columns_updated = columns_updated + " email,"
        if json_data.get('phone'):
            phone = str(json_data['phone'])
            conn.execute("update restaurantes set phone='"+phone+"' where id='%s'"%identification)
            columns_updated = columns_updated + " phone,"
        if json_data.get('street'):
            street = str(json_data['street'])
            conn.execute("update restaurantes set street='"+street+"' where id='%s'"%identification)
            columns_updated = columns_updated + " street,"
        if json_data.get('city'):
            city = str(json_data['city'])
            conn.execute("update restaurantes set city='"+city+"' where id='%s'"%identification)
            columns_updated = columns_updated + " city,"
        if json_data.get('state'):
            state = str(json_data['state'])
            conn.execute("update restaurantes set state='"+state+"' where id='%s'"%identification)
            columns_updated = columns_updated + " state,"
        if json_data.get('lat'):
            lat = str(json_data['lat'])
            conn.execute("update restaurantes set lat='"+lat+"' where id='%s'"%identification)
            columns_updated = columns_updated + " lat,"
        if json_data.get('lng'):
            lng = str(json_data['lng'])
            conn.execute("update restaurantes set lng='"+lng+"' where id='%s'"%identification)
            columns_updated = columns_updated + " lng,"
        if json_data.get('id'):
            id_value = str(json_data['id'])
            conn.execute("update restaurantes set id='"+id_value+"' where id='%s'"%identification)
            columns_updated = columns_updated + " id,"
        return "The columns that were updated are:"+columns_updated+"at the id='%s'"%identification 
       
api.add_resource(Manage_All, '/restaurantes')
api.add_resource(Manage_By_ID, '/restaurantes/id=<string:identification>')

if __name__ == '__main__':
    app.run(debug=True)
