from flask import Flask, jsonify, request, make_response
from flask_restful import Api,Resource, reqparse,abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import json


# my advance api
# my advance api 135

USER_DATA = {
    "admin": "SecretPwd"
}



app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.bd'
db = SQLAlchemy(app)

class ContactModel(db.Model):
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    email = db.Column(db.String(100), unique = True,nullable = False)
    name = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Contact(email = {email}, name = {name}, phone = {phone})"

# db.create_all()


contact_put_args = reqparse.RequestParser()
contact_put_args.add_argument("email", type=str, help="email of person is required", required = True)
contact_put_args.add_argument("name", type=str, help="name of person is required", required = True)
contact_put_args.add_argument("phone", type=int, help="phone of person is required", required = True)


contact_update_args = reqparse.RequestParser()
contact_update_args.add_argument("email", type=str, help="email of person is required")
contact_update_args.add_argument("name", type=str, help="name of person is required")
contact_update_args.add_argument("phone", type=int, help="phone of person is required")


resource_field = {
    'id' : fields.Integer,
    'email' : fields.String,
    'name' : fields.String,
    'phone' : fields.Integer
}


def pagination(result):
    res = {}
    res['pages'] = result.pages
    res['previous'] = result.prev_num
    res['page'] = result.page
    res['next'] = result.next_num
    res['per_page'] = result.per_page
    res['total'] = result.total
    res['items'] = None
    item = []
    for con in result.items:
        temp = {}
        Odic = serialized(con)
        temp['id'] = Odic['id']
        temp['email'] = Odic['email']
        temp['name'] = Odic['name']
        temp['phone'] = Odic['phone']

        item.append(temp)
    res['items'] = item
    return res


@marshal_with(resource_field)
def serialized(result):
    return result


@auth.verify_password
def verify(username, password):
    if not (username and password):
        abort(404, message = "authentication required")
    if USER_DATA.get(username) == password:
        return True
    abort(404, message = "username or Password Mismatched")


class Contact(Resource):

    
    @auth.login_required
    def get(self):
        email = request.args.get('email',None)
        name = request.args.get('name',None)
        page = request.args.get('page', 1, type=int)

        if email and name:
            result = ContactModel.query.filter_by(email = email,name = name).first()
            if not result:
                abort(409, message = "contact doesnt exists...")
            return serialized(result)
        elif email:
            result = ContactModel.query.filter_by(email = email).first()
            if not result:
                abort(409, message = "contact doesnt exists......")
            return serialized(result)
        elif name:
            results = ContactModel.query.filter_by(name = name).paginate(page = page, per_page = 10)
            res = pagination(results)
            return res
        else:
            results = ContactModel.query.paginate(page = page, per_page = 10)
            res = pagination(results)
            return res


    @auth.login_required
    @marshal_with(resource_field)
    def put(self):
        args = contact_put_args.parse_args()
    
        result = ContactModel.query.filter_by(email = args['email']).first()
        if result:
            abort(409, message = "email already taken...")
        contact = ContactModel(email = args['email'],name = args['name'],phone = args['phone'])
        db.session.add(contact)
        db.session.commit()
        return contact, 201


    @auth.login_required
    @marshal_with(resource_field)
    def patch(self,email):
        args = contact_update_args.parse_args()
        print(args)
        result = ContactModel.query.filter_by(email = email).first()
        if not result:
            abort("404",message = "contact doesnt exists,cannot updated...")
        
        if args['email']:
            result2 = ContactModel.query.filter_by(email = args['email']).first()
            if result2:
                abort("409",message = "email already taken...")
            result.email = args['email']
        if args['name']:
            result.name = args['name']
        if args['phone']:
            result.phone = args['name']
        
        db.session.commit()

        return result

    @auth.login_required
    def delete(self,email):
        result = ContactModel.query.filter_by(email = email).first()
        if not result:
            abort(409, message = "Contact doesnt exists,cannot delete")
        db.session.delete(result)
        db.session.commit()

        return {"message" : "successfully deleted contact"}





api.add_resource(Contact,  "/contact/", "/contact/<string:email>")


if __name__ == "__main__":
    app.run(debug=True)