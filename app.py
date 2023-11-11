from flask import Flask,jsonify , request

app = Flask(__name__)

stores = [
    {
            "name": "My Store",
            "items": [
                {
                    "name": "Chair",
                    "price": 175.50
                }
            ]
        },
        {
            "name": "My Store Two",
            "items": [
                {
                    "name": "Chair",
                    "price": 75.0
                }
            ]
        }

]

#400 -BAD rEQUEST
#404 -PAGE NOT FOUND/tHE REQUESTED url WAS NOT FOUND
#201 - Created success status

@app.route('/',methods=['GET'])
def home_page():
    return 'Hello this home page'


@app.route('/store',methods=['GET'])
def get_stores():
    # return stores
    return jsonify({'stores':stores})

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store , 201




@app.route('/store/<string:store_name>')
def method_name(store_name):
    #this is alwys passing bcoz because Flask's routing system automatically converts the <string:store_name> parameter to a string, 
    # even if a number is provided in the URL. This is why your isinstance(store_name, str) check always passes.
    # if not isinstance(store_name, str):
    #     return jsonify({'message': 'Store name must be a string'}), 400

    # if not store_name.isalpha():
    #     return jsonify({'message': 'Store name must be a string and contain no numbers'}), 400
    
    for store in stores:
        if store['name'] == store_name:
            return jsonify(store)
        
    return jsonify({'message':'Store not found'})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"], "price":request_data["price"]}
            store["items"].append(new_item)
            return new_item , 201
    
    return {"messgae":"Store not found"} , 404

@app.route('/store/<string:store_name>/item',methods=['GET'])
def get_item(store_name):
    for store in stores:
        if store["name"] == store_name:
            return  {"items":store["items"]}
        
    return {"messgae":"Store not found"} , 404

if __name__=='__main__':
    app.run(debug=True)