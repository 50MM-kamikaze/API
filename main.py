from flask import Flask, request , jsonify 

app = Flask(__name__)


@app.route("/")
def home():
    return "home"

@app.route("/get_user/<user_id>") # lets say user_id is 876 , them we can take a value after the /get_user/876
def get_user(user_id): # this is how we make a get route 
    user_data = {
        "user_id" : user_id,
        "name" : "Samhith",
        "email" : "samhith.wgl.in@gmail.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200


@app.route("/create_user" , methods = ["POST"]) #unlike a get_user methods need to be mentioned 
def create_user():
    data = request.get_json()
    return jsonify(data) , 201

         

if __name__ == "__main__":
    app.run(debug=True)
    
    #end