from flask import Blueprint, request,jsonify, make_response
from use_cases.AuthService import AuthService
from domain.exceptions import *

bp= Blueprint("users",__name__)

@bp.route("/api/register", methods=["POST"])
def register():
    if request.method=="POST":
            
            data=request.get_json()
            
            username=data["username"]
            passwd= data["passwd"]

            if not username or not passwd:
                return jsonify({"error":"Fields are empty"}), 400

            register_user=AuthService()
            try:
                register_user.register(username,passwd)
                return jsonify({"message":"Register successfully"}), 200
            except EmptyFields as e:
                return jsonify({"error":e.message}), 400
            except InvalidUsername as e:
                return jsonify({"error":e.message}), 400
            except InvalidPassword as e:
                return jsonify({"error":e.message}), 400
            except UnavailableUsername as e :
                return jsonify({"error":e.message}), 400
            except Exception:
                return jsonify({"error":"Internal server error"}), 500
            
            

@bp.route("/api/login", methods=["POST"])
def login():
    if request.method=="POST":
        
        data=request.get_json()
        username=data["username"]
        passwd= data["passwd"]
            
        if not username or not passwd:
            return jsonify({"error":"Fields are empty"}), 400
            
        login_user=AuthService()

        try:
            jwt,csrf_token=login_user.login(username, passwd)

            res=make_response(jsonify({"message":"Login successfully"}))

            # secure is False because I don't use HTTPS, Lax is for development
            res.set_cookie("token", jwt, httponly=True, samesite="Lax", secure=False)

            res.headers["X-CSRF"]=csrf_token

            return res, 200
        
        except EmptyFields as e:
            return jsonify({"error":e.message}), 400
        except WrongLogin as e:
            return jsonify({"error":e.message}), 400
        except Exception:
            return jsonify({"error":"Internal server error"}), 500
            
        

# Check cookie          
@bp.route("/api/validate", methods=["GET","POST"])
def validate():
    try:
        token=request.cookies.get("token")
        validation_token=AuthService()
        auth=validation_token.validate(token)
        return jsonify({"message":"OK", "auth": auth}), 200
    except InvalidToken as e:
        return jsonify({"error":e.message}), 400
    except:
        return jsonify({"error":"Internal server error"}), 500


# Delete cookie
@bp.route("/api/logout", methods=["GET"])
def logout():
    try:
        res=make_response(jsonify({"message":"Logout successfully"}))
        res.delete_cookie("token")
        return res, 200

    except:
        return jsonify({"error":"Can't logout"}), 400