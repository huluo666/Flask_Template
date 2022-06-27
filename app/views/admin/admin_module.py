from flask import Blueprint

admin_blu = Blueprint('admin', __name__)

@admin_blu.route("/admin")
def admin_index():
    return "admin"