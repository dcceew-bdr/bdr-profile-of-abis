from pathlib import Path
from rdflib import Graph

VALIDATORS_DIR = Path(__file__).parent
validators = [
    Path(VALIDATORS_DIR / "core.ttl"),
    Path(VALIDATORS_DIR / "dr.ttl"),
    Path(VALIDATORS_DIR / "proj.ttl"),
    "https://ausbigg.github.io/abis/validators/abis.ttl",
]

g = Graph()

for validator in validators:
    g.parse(validator)
    print(len(g))

g.serialize(destination=VALIDATORS_DIR / "validator.ttl", format="longturtle")