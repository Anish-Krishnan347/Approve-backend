from flask import Blueprint
from app.controller import role_controller

role_bp = Blueprint('role_bp', __name__)

role_bp.route("/list", methods=["POST"])(role_controller.get_role)
role_bp.route('/create',methods=['POST'])(role_controller.create_role)
role_bp.route("/delete",methods=['POST'])(role_controller.delete_role)
role_bp.route("/update",methods=['POST'])(role_controller.update_role)