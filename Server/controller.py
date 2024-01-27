from Shared import Client
from Shared.Abstract import BaseController, AuthController
from flask import request, jsonify
import jwt
import bcrypt
import os


class Controller(BaseController, AuthController):
    def __init__(self):
        super().__init__()
        self.client = Client()

    def get_user(self, user_id, email):
        try:
            verify_token(request.headers)
            res = self.client.get_request('/user', user_id, email)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        else:
            return res.json(), res.status_code

    def add_user(self):
        try:
            verify_token(request.headers)
            data = request.get_json()
            res = self.client.post_request('/user', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def update_user(self):
        try:
            verify_token(request.headers)
            data = request.get_json()
            res = self.client.update_request('/user', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def delete_user(self):
        try:
            verify_token(request.headers)
            data = request.get_json()
            res = self.client.delete_request('/user', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    # Note requests
    def get_note(self, user_id, note_id):
        try:
            verify_token(request.headers)
            res = self.client.get_request('/note', user_id, note_id)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        else:
            return res.json(), res.status_code

    def add_note(self):
        try:
            verify_token(request.headers)
            data = request.get_json()
            res = self.client.post_request('/note', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def update_note(self):
        try:
            verify_token(request.headers)
            data = request.get_json()
            res = self.client.update_request('/notes', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def delete_note(self):
        try:
            verify_token(request.headers)
            data = request.get_json()
            res = self.client.delete_request('/note', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    # Authentication
    def login(self, email, password):
        try:
            user_id = None
            response = self.client.get_request('/user', user_id, email)
            data = request.get_json()
            hashed_password = data['Password']
            password_verify(password, hashed_password)
            res = generate_token(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        else:
            return jsonify({'token': res, 'User_id': data['User_id']}), 200

    def token(self):
        try:
            verify_token(request.headers)
        except Exception as e:
            return jsonify({"message": str(e)}), 301
        else:
            return jsonify({"message": "Token is valid"}), 200


def password_hash(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def password_verify(input_password, hashed_password):
    if bcrypt.checkpw(input_password, hashed_password):
        return True
    raise Exception('Password is invalid!')


def generate_token(user_data):
    payload = {
        'User_id': user_data['User_id'],
        'Email': user_data['Email'],
        'Username': user_data['Username'],
    }
    jwt_token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
    return jwt_token


def verify_token(header):
    try:
        if 'Authorization' in header:
            auth_header = header.get('Authorization')
            token = auth_header.split(' ')[1]
        else:
            raise Exception('No authorization header')
        token_decoded = jwt.decode(token, os.getenv('SECRET_KEY'), algorithm='HS256')
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Token is Invalid")
    else:
        return token_decoded
