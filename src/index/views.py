from flask import Blueprint, render_template, session
from src.index.forms import DataForm
from src.models import Individual
import hashlib

index_blueprint = Blueprint('index', __name__, template_folder='templates')


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        usernames = [username.strip() for username in form.usernames.data.split(",")]
        emails = [email.strip() for email in form.emails.data.split(",")]
        name = form.name.data
        organisations = [organisation.strip() for organisation in form.organisations.data.split(",")]
        domains = [domain.strip() for domain in form.domains.data.split(",")]
        new_individual = Individual(
            usernames=usernames,
            emails=emails,
            name=name,
            organisations=organisations,
            domains=domains
        )
        # TODO: Call function, get ids
        print(new_individual.__dict__)
        response = [{
            'user': 'gwo0d', 'urls': [{
                'url': 'https://discussions.apple.com/profile/gwo0d', 'id': '66fa8b9736ce198067f5adfaf9ff507f'
            }, {
                'url': 'https://www.codecademy.com/profiles/gwo0d', 'id': '11f17d39763bf6ed48dd3955e0ad4e2f'
            }, {
                'url': 'https://www.codewars.com/users/gwo0d', 'id': '7cd1265b478bb5fa0d795659a8b14578'
            }, {
                'url': 'https://www.duolingo.com/profile/gwo0d', 'id': 'c09afd93efeac6ffdb2f47222656d383'
            }, {
                'url': 'https://www.facebook.com/gwo0d', 'id': '174c238a0af8df72532a7a201179b306'
            }, {
                'url': 'https://fortnitetracker.com/profile/all/gwo0d', 'id': '6ca57e902f100081ec629a9995b395ce'
            }, {
                'url': 'https://genius.com/gwo0d', 'id': '70b9b8e806a5f07bd70af974b4debabb'
            }, {
                'url': 'https://www.github.com/gwo0d', 'id': 'dd709a8a615ce2b2807da758cdc9e9a5'
            }
            ]
        }]

    return render_template('index.html', form=form)
