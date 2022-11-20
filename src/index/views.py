from flask import Blueprint, render_template, send_from_directory
from data.main_query import MainQuery
from src.index.forms import DataForm
from src.models import Individual, AccountSite, LinkSite
import json
import string

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
        query = MainQuery(new_individual).query()
        bing_results = query["bing_results"]
        sherlock_results = query["sherlock_results"]
        beenpwned_results = query["beenpwned_results"]
        # with open("sherlock_results.json", "w") as f:
        #     f.write(json.dumps(sherlock_results))
        #
        # with open("bing_results.json", "w") as f:
        #     f.write(json.dumps(bing_results))
        #
        # with open("beenpwned_results.json", "w") as f:
        #     f.write(json.dumps(beenpwned_results))


        # with open("bing_results.json", "r") as bing, open("sherlock_results.json") as sherlock, open("beenpwned_results.json") as beenpwned:
        #     bing_results = json.loads(bing.read())
        #     sherlock_results = json.loads(sherlock.read())
        #     beenpwned_results= json.loads(beenpwned.read())

        account_sites = []

        for user in sherlock_results:
            for url in user["urls"]:
                pwned = False
                breach_date = None
                pwn_description = None
                for account in beenpwned_results:
                    for site in account:
                        if site["id"] == url["id"]:
                            pwned = True
                            breach_date = site["breach_date"]
                            pwn_description = site["description"]
                account_sites.append(AccountSite(user["user"], url["url"], pwned=pwned, breach_date=breach_date, pwn_description=pwn_description))

        print(account_sites)

        linked_sites = []
        for page in bing_results["webPages"]["value"]:
            linked_sites.append(LinkSite(page["url"], page["name"], page["snippet"]))

        grouped_list = {}
        for site in linked_sites:
            dom = site.extracted_domain.domain + site.extracted_domain.suffix
            if dom not in grouped_list.keys():
                grouped_list[dom] = [site]
            else:
                grouped_list[dom].append(site)


        return render_template("data.html", account_sites=account_sites, str=str, string=string, grouped_list=grouped_list)



    return render_template('index.html', form=form)

@index_blueprint.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")