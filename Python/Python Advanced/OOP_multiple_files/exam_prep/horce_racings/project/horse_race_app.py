from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    # add horse
    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in HorseRaceApp.VALID_HORSES:
            return

        if self.find_horse(horse_name) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        else:
            horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    # add jockey
    def add_jockey(self, jockey_name: str, age: int):
        if self.find_jockey(jockey_name) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    # add race
    def create_horse_race(self, race_type: str):
        if self.find_race(race_type) is not None:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey(jockey_name)
        horse = self.find_horse(horse_type, "taken")
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horse_type not in HorseRaceApp.VALID_HORSES or horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.find_jockey(jockey_name)
        race = self.find_race(race_type)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_race(race_type)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner, highest_speed = self.find_winner(race)

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def find_winner(self, race):
        highest_speed = 0
        for player in race.jockeys:
            if player.horse.speed > highest_speed:
                highest_speed = player.horse.speed
                winner = player

        return winner, highest_speed

    def find_race(self, race_type):
        try:
            race = next(filter(lambda r: race_type == r.race_type, self.horse_races))
        except StopIteration:
            return None

        return race

    def find_jockey(self, jockey_name):
        try:
            jockey = next(filter(lambda j: jockey_name == j.name, self.jockeys))
        except StopIteration:
            return None

        return jockey

    def find_horse(self, horse_name, custom_filter=""):
        if custom_filter == "taken":
            try:
                horse = next(
                    filter(lambda h: (horse_name == h.__class__.__name__ and h.is_taken is False),
                           reversed(self.horses)))
            except StopIteration:
                return None

            return horse

        try:
            horse = next(filter(lambda h: horse_name == h.name, self.horses))
        except StopIteration:
            return None

        return horse
