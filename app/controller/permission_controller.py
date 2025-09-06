from app import db
from app.model.user_model import User
from app.model.role_model import Role
from flask import request
from app.utils.error_response import error_response
from app.utils.success_response import success_response
from datetime import datetime
from app.model.permission_model import Permission


def findUser(id):
    user = User.query.get(id)
    role = Role.query.get(user.role_id)
    data = {"name": user.name, "role": role.name}
    return data


def filterPermissionList():
    data = Permission.query.filter_by(status="Pending").all()

    returnData = [
        {
            "name": findUser(permission.user_id)["name"],
            "to": permission.to,
            "from_": permission.from_,
            "reason": permission.reason,
            "description": permission.description,
            "role": findUser(permission.user_id)["role"],
            "status": permission.status,
            "id": permission.id,
        }
        for permission in data
    ]
    return returnData


def apply_permission():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        reason = data.get("reason")
        to = data.get("to")
        from_ = data.get("from_")
        description = data.get("description")
        to_date = datetime.strptime(to, "%Y-%m-%d").date()
        from_date = datetime.strptime(from_, "%Y-%m-%d").date()

        user = User.query.filter(User.id == user_id).first()
        if not user:
            return error_response(message="User Not Found")

        all_data = Permission(
            user_id=user_id,
            reason=reason,
            to=to_date,
            from_=from_date,
            description=description,
        )

        db.session.add(all_data)
        db.session.commit()
        return success_response(message="Permission send to the admin")

    except Exception as e:
        db.session.rollback()
        return error_response(str(e), 500)


def list_permission():
    try:
        user_data = request.get_json()
        user_id = user_data.get("id")
        permissions = Permission.query.filter_by(user_id=user_id).all()

        permission_list = [
            {
                "name": findUser(permission.user_id)["name"],
                "to": permission.to,
                "from_": permission.from_,
                "reason": permission.reason,
                "description": permission.description,
                "role": findUser(permission.user_id)["role"],
                "status": permission.status,
            }
            for permission in permissions
        ]
        
        return success_response(data=permission_list)
    except Exception as e:
        db.commit.rollback()
        return error_response(str(e))


def list_permission_approve():
    try:
        list = filterPermissionList()
        return success_response(data=list)
    except Exception as e:
        db.commit.rollback()
        return error_response(str(e), 500)


def action_permission():
    try:
        data = request.get_json()
        id = data.get("id")
        action = data.get("action")

        permission_data = Permission.query.get(id)
        permission_data.status = action
        db.session.commit()

        message = (
            "Permission accepted" if action == "Approved" else "Permission rejected"
        )

        list = filterPermissionList()
        return success_response(message=message, data=list)

    except Exception as e:
        db.commit.rollback()
        return error_response(str(e), 500)
