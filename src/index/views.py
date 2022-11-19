from flask import Blueprint, render_template

from src.index.forms import DataForm
from src.models import Individual

index_blueprint = Blueprint('index', __name__, template_folder='templates')

@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        usernames = [username.strip() for username in form.usernames.data.split(",")]
        name = form.name.data
        organisations = [organisation.strip() for organisation in form.organisations.data.split(",")]
        domains = [domain.strip() for domain in form.domains.data.split(",")]
        new_individual = Individual(
            usernames=usernames,
            name=name,
            organisations=organisations,
            domains=domains
        )
        print(new_individual.__dict__)
    return render_template('base.html', form=form)
