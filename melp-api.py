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
        id_value = str(json_data['id'])
        rating = str(json_data['rating'])
        name = str(json_data['name'])
        site = str(json_data['site'])
        email = str(json_data['email'])
        phone = str(json_data['phone'])
        street = str(json_data['street'])
        city = str(json_data['city'])
        state = str(json_data['state'])
        lat = str(json_data['lat'])
        lng = str(json_data['lng'])
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
        id_value = str(json_data['id'])
        rating = str(json_data['rating'])
        name = str(json_data['name'])
        site = str(json_data['site'])
        email = str(json_data['email'])
        phone = str(json_data['phone'])
        street = str(json_data['street'])
        city = str(json_data['city'])
        state = str(json_data['state'])
        lat = str(json_data['lat'])
        lng = str(json_data['lng'])
        conn.execute("update restaurantes set id='"+id_value+"', rating='"+rating+"', name='"+name+"', site='"+site+"' , email='"+email+"' , phone='"+phone+"' , street='"+street+"' , city='"+city+"' , state='"+state+"' , lat='"+lat+"' , lng='"+lng+"' where id='%s'"%identification)
        return "It updated correctly"    
       
api.add_resource(Manage_All, '/restaurantes')
api.add_resource(Manage_By_ID, '/restaurantes/id=<string:identification>')

if __name__ == '__main__':
    app.run(debug=True)