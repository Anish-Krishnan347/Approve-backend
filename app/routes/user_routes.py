from flask import Blueprint
from app.controller import user_controller

user_bp = Blueprint('user_bp',__name__)

user_bp.route("/create",methods=['POST'])(user_controller.create_user)
user_bp.route("/list",methods=['POST'])(user_controller.list_user)
user_bp.route("/delete",methods=['POST'])(user_controller.delete_user)
user_bp.route("/update",methods=['POST'])(user_controller.update_user)
user_bp.route("/status",methods=['POST'])(user_controller.update_status)