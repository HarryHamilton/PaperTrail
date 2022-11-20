from flask import Blueprint, render_template
from data.main_query import MainQuery
from src.index.forms import DataForm
from src.models import Individual, AccountSite, LinkSite
import json

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
        # query = MainQuery(new_individual).query()
        # bing_results = query["bing_results"]
        # sherlock_results = query["sherlock_results"]
        # beenpwned_results = query["beenpwned_results"]
        # with open("sherlock_results.json", "w") as f:
        #     f.write(json.dumps(sherlock_results))
        #
        # with open("bing_results.json", "w") as f:
        #     f.write(json.dumps(bing_results))
        #
        # with open("beenpwned_results.json", "w") as f:
        #     f.write(json.dumps(beenpwned_results))
        #

        bing_results = json.loads("bing_results.json")
        sherlock_results = json.loads("sherlock_results.json")
        beenpwned_results= json.loads("beenpwned_results.json")
        account_sites = []

        for user in sherlock_results:
            for url in user["urls"]:
                pwned = False
                for account in beenpwned_results:
                    for site in account:
                        if site["id"] == url["id"]:
                            pwned = True
                account_sites.append(AccountSite(user["user"], url["url"], pwned=pwned))

        print(account_sites)

        linked_sites = []
        for page in bing_results["webPages"]["value"]:
            linked_sites.append(LinkSite(page["url"], page["name"], page["snippet"]))


        print(linked_sites)



    return render_template('index.html', form=form)
