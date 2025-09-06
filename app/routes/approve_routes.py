from flask import Blueprint
from app.controller import approve_controller


approve_bp = Blueprint('approve_bp',__name__)

approve_bp.route("/list", methods=["POST"])(approve_controller.approval_list)
approve_bp.route('/accept',methods=['POST'])(approve_controller.accept_approve)
approve_bp.route('/reject',methods=['POST'])(approve_controller.reject_approve)
