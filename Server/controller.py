from Server.client import DataLayerClient
from flask import request, jsonify
import jwt
import bcrypt
import os


class Controller:
    def __init__(self):
        self.client = DataLayerClient()

    def get_user(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            if data['User_id']:
                res = self.client.get_request('/user/name', data)
            elif data['email']:
                res = self.client.get_request('/user/email', data)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        else:
            return res.json(), res.status_code

    def add_user(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            res = self.client.post_request('/user', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def update_user(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            if data['Username']:
                res = self.client.update_request('/user/name', data)
            elif data['Email']:
                res = self.client.update_request('/user/email', data)
            elif data['Password']:
                res = self.client.update_request('/user/password', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def delete_user(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            res = self.client.delete_request('/user', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    # Note requests
    def get_note(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            if data['User_id']:
                res = self.client.get_request('/note/user_id', data)
            elif data['Note_id']:
                res = self.client.get_request('/note/id', data)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        else:
            return res.json(), res.status_code

    def add_note(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            res = self.client.post_request('/note', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def update_note(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            if data['content']:
                res = self.client.update_request('/notes', data)
            elif data['title']:
                res = self.client.update_request('/notes/title', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    def delete_note(self):
        data = request.get_json()
        try:
            token = data['token']
            self.verify_token(token)
            res = self.client.delete_request('/note', data)
        except Exception as e:
            return jsonify(str(e)), 400
        else:
            return res.json(), res.status_code

    # Authentication
    def login_user(self):
        try:
            if request.get_json()['token']:
                token = request.get_json()['token']
                res = self.verify_token(token)
            else:
                request_data = request.get_json()
                email = request_data.get('email')
                password = request_data.get('password')
                data = self.client.get_request(f'/user/email', email)
                hashed_password = data['Password']
                self.password_verify(password, hashed_password)
                res = self.generate_token(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        else:
            return jsonify(res), 200

    def password_hash(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def password_verify(self, input_password, hashed_password):
        if bcrypt.checkpw(input_password, hashed_password):
            return True
        raise Exception('Password is invalid!')

    def generate_token(self, user_data):
        payload = {
            'User_id': user_data['User_id'],
            'Email': user_data['Email'],
            'Username': user_data['Username'],
        }
        jwt_token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
        return jwt_token

    def verify_token(self, token):
        try:
            token_decoded = jwt.decode(token, os.getenv('SECRET_KEY'), algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Token is Invalid")
        else:
            return token_decoded
