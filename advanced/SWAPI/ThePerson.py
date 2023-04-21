
class ThePerson:

    def __int__(self):
        self.name = ""
        self.height = 0
        self.mass = 0.0
        self.hair_color = ""
        self.skin_color = ""
        self.eye_color = ""
        self.birth_year = ""
        self.gender = ""
        self.home_world = ""
        self.films = []
        self.species = []
        self.vehicles = []
        self.starships = []

    def load_from_json(self, data=None):
        if data is None:
            data = {}

        self.name = data.get("name", "None")

        if data.get("height", "") == 'unknown':
            self.height = -1
        else:
            self.height = int(data.get("height", "0"))

        if data.get("mass", "") == 'unknown':
            self.mass = -1.0
        else:
            temp_mass = data.get("mass", "0")
            if "," in temp_mass:
                temp_mass = float(temp_mass.replace(",", ""))

            self.mass = float(temp_mass)

        self.hair_color = data.get("hair_color", "None")
        self.skin_color = data.get("skin_color", "None")
        self.eye_color = data.get("eye_color", "None")
        self.birth_year = data.get("birth_year", "")
        self.gender = data.get("gender", "")
        self.home_world = data.get("homeworld", "None")
        self.films = data.get("films", [])
        self.species = data.get("species", [])
        self.vehicles = data.get("vehicles", [])
        self.starships = data.get("starships", [])

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
