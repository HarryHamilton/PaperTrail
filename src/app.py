from flask import render_template, redirect, url_for, Blueprint, send_file

app_blueprint = Blueprint('app', __name__, template_folder='templates')
