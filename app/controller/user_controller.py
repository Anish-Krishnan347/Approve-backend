from flask import request
from app.model.user_model import User
from app.utils.error_response import error_response
from app.utils.success_response import success_response
from app import db
from app.model.role_model import Role

def fetchUser():
    users = User.query.all()
    roles = Role.query.all()
    role_dict = {r.id: r for r in roles}
    user_list = [
        {   "id":user.id,
            "name":user.name,
            "email":user.email,
            "password":user.password,
            "status":user.status,
            "approve":user.approve,
            "role_id":user.role_id,
            "role": role_dict[user.role_id].name if user.role_id in role_dict else None
        }for user in users
    ]

    return user_list

def create_user():
    try:
        data = request.get_json()
        name=data.get('name')
        email=data.get('email')
        role_id=data.get('role_id')
        status = 'active' if role_id == 1 else 'inactive'
        approve = True if role_id ==1 else False
        password = data.get('password')

        user_list = User.query.all()

        for user in user_list:
            if user.email == email:
                return error_response(message='This email allocate another user',status_code=200)
            

        new_user = User(name=name,email=email,password=password,role_id=role_id,status=status,approve=approve)
        db.session.add(new_user)
        db.session.commit()

        user_list = fetchUser()
        return success_response(message='User created successfully, Waiting for admin approval',data=user_list)

    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def list_user():
    try:
        user_list = fetchUser()
        return success_response(data=user_list)
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def delete_user():
    try:
        data = request.get_json()
        id = data.get('id')
        user = User.query.get(id)
        if not user:
            return error_response('User Not Found')
        db.session.delete(user)
        db.session.commit()

        user_list = fetchUser()
        return success_response(message='User Deleted Successfully',data=user_list)
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def update_user():
    try:
        data = request.get_json()
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        role_id = data.get('role_id')

        user = User.query.get(id)
        if not user:
            error_response(message='User not found')
            return

        user.name = name
        user.email = email
        user.password = password
        user.role_id = role_id

        db.session.commit()

        user_list = fetchUser()
        return success_response(message='User details updated successfully',data=user_list)

        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def update_status():
    try:
        data = request.get_json()
        id = data.get('id')
        status = data.get('status')

        user = User.query.get(id)  # ✅ Correct usage
        if not user:
            return error_response(message='User not found')

        if status not in ['active', 'inactive']:  # ✅ Optional validation
            return error_response(message='Invalid status value')

        user.status = status
        db.session.commit()

        user_list = fetchUser()
        return success_response(message='User Status updated successfully',data=user_list)

    except Exception as e:
        return error_response(str(e), 500)  # ✅ Return the response


