from app.model.user_model import User
from flask import request
from app import db
from app.utils.success_response import success_response
from app.utils.error_response import error_response
from app.model.role_model import Role

def fetchUser(data):

    roles = Role.query.all()
    role_dict = {r.id: r for r in roles}
    user_list = [
        {
            "name":user.name,
            "email":user.email,
            "role_id":user.role_id,
            "approve":user.approve,
            "role": role_dict[user.role_id].name if user.role_id in role_dict else None,
            "id":user.id
        }for user in data
    ]
    return user_list

def approval_list():
    try:
        users = User.query.filter_by(approve = False).all()
        user_list = fetchUser(users)
        return success_response(message='Approval list fetch successfully',data=user_list)
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def accept_approve():
    try: 
        data = request.get_json()
        id = data.get('id')
        user = User.query.get(id)
        if not user:
            return error_response(message='User Not Found')
        user.approve = True
        db.session.commit()

        

        users = User.query.filter_by(approve=False).all()
        user_list = fetchUser(users)
        return success_response(message='User Accepted Successfully', data=user_list)
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def reject_approve():
    try:
        data = request.get_json()
        id = data.get('id')

        user = User.query.get(id)
        if not user:
            return error_response(message='User not found')
        
        user.id = id

        if user.approve == True:
            return error_response(message=user.name + " Accepted you can't reject")
        
        db.session.delete(user)
        db.session.commit()
        users = User.query.filter_by(approve=False).all()
        user_list = fetchUser(users)
        return success_response(message='User Rejected Successfully', data=user_list)


    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)



