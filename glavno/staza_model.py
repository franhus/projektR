import os
import json

class Staza:
    def __init__(self, putanja):
        with open(putanja, "r") as f:
            podaci = json.load(f)
        
        self.linija = podaci.get("linija")
        self.vanjske = podaci.get("vanjske")
        self.unutarnje = podaci.get("unutarnje")

