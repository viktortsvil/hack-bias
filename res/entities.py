class Suspect:
    def __init__(self, level, person):
        path = "cases/"
        with open(path + str(level) + "/suspect_" + str(person) + ".txt") as file:
            lines = file.readlines()
            self.name = lines[0]
            self.sex = lines[1]
            self.age = lines[2]
            self.race = lines[3]
            self.record = lines[4]
            self.biography = lines[5]
        self.lineup_path = 'img/characters/lineups/' + str(level) + "/" + str(person) + ".png"
        self.card_path = 'img/characters/photocards/' + str(level) + "/" + str(person) + ".png"
        self.lineup_image = None
