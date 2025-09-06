from flask import jsonify,request
from app.model.role_model import Role
from app.utils.success_response import success_response
from app.utils.error_response import error_response
from app import db

def get_role():
    try:
        roles = Role.query.all()
        role_list = [
            {
                "id": role.id,
                "name": role.name,
                "created_at": role.created_at.strftime("%Y-%m-%d %H:%M:%S")
            } for role in roles
        ]
        return success_response(data=role_list)
    except Exception as e:
        return error_response(message=str(e))


def create_role():
    try:
        # get data from request

        data = request.get_json()
        name = data.get('name')

        # get role list from db
        role_list = Role.query.all()

        # check role exist in db
        for roles in role_list:
            if roles.name == name:
                return error_response(message='Role already exists')
        
        
        new_role = Role(name=name)

        # commit name to add db
        db.session.add(new_role)
        db.session.commit()

        # return success message
        return success_response(message='Role Created Successfully')
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def delete_role():
    try:
        data = request.get_json()
        id = data.get('id')
        role = Role.query.get(id)
        if not role:
            return error_response(message='Role Not Found')
        db.session.delete(role)
        db.session.commit()
        return success_response(message='Role Deleted Successfull')
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

def update_role():
    try:
        data = request.get_json()
        id = data.get('id')
        name=data.get('name')
        role = Role.query.get(id)
        if not role:
            return error_response(message='Role not found')
        role.name = name  # Update the role's name
        db.session.commit()

        return success_response(message='Role updated successfully')
    
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),500)
    

