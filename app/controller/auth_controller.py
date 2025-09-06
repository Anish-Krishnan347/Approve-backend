from flask import request
from app.model.user_model import User
from app import db
from app.utils.success_response import success_response
from app.utils.error_response import error_response

def auth_login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter(User.email == email).first()
        if not user:
            return error_response(message='Please check you email',status_code=200)
        
        if user.approve == False:
            return error_response(message='Admin approval is pending please contact your admin',status_code=200)
        
        if user.status == 'inactive':
            return error_response(message='User account is inactive, Please contact you HR',status_code=200)
        
        if user.password != password:
            return error_response(message='Invalid credential, check your email or password',status_code=200)
        
        user_data = {
            "id":user.id,
            "role_id":user.id,
            "name":user.name,
            "email":user.email
        }
        
        return success_response(message='Auth login successfull',data=user_data)
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)