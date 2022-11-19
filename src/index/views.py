from flask import Blueprint, render_template, session

index_blueprint = Blueprint('index', __name__, template_folder='templates')

@index_blueprint.route('/')
def index():
    return render_template('base.html')