from flask import Blueprint
from app.controller import auth_controller

auth_bp = Blueprint('auth_bp',__name__)

auth_bp.route('/login',methods=['POST'])(auth_controller.auth_login)