from src.models import Individual
from query import BingQuery
import json
individual = Individual(["LukeBriggsDev"], "Luke Briggs", ["Newcastle University"], ["lukebriggs.dev"])

query = BingQuery(individual)
with open("response.json", "w") as f:
    response = query.query()
    print(response)
    f.write(json.dumps(response))
