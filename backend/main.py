from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from adapters.api.routes import bp
import os

load_dotenv()

app=Flask(__name__)
CORS(app, supports_credentials=True, origins="http://localhost:5173/*")

app.config["POSTGRESQL_URL"]=os.getenv("POSTGRESQL_URL")
app.config["SALT"]=os.getenv("SALT")
app.config["SECRET"]=os.getenv("SECRET")
app.config["PORT"]=os.getenv("PORT")

port=os.getenv("PORT") or 5000

# Routes
app.register_blueprint(bp)

if __name__=="__main__":
    app.run(debug=True, port=port)