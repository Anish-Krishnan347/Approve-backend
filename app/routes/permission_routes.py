from flask import Blueprint
from app.controller import permission_controller 

permission_bp = Blueprint('permission_bp',__name__)
permission_bp.route('/apply',methods=["POST"])(permission_controller.apply_permission)
permission_bp.route('/list',methods=['POST'])(permission_controller.list_permission)
permission_bp.route('/approve_list',methods=['POST'])(permission_controller.list_permission_approve)
permission_bp.route('/action',methods=['POST'])(permission_controller.action_permission)
