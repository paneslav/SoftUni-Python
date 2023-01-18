from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_results = {
            'success': 0,
            'fail': 0
        }

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut_type not in Astronaut.VALID_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        if astronaut:
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)

        self.astronaut_repository.astronauts.append(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)

        if planet:
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = [item for item in items.split(', ')]

        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts = self.__choose_astros()

        return self.__start_mission(astronauts, planet)

    def report(self):
        result = [f"{self.mission_results['success']} successful missions!",
                  f"{self.mission_results['fail']} missions were not completed!", "Astronauts' info:"]
        astros = [str(astro) for astro in self.astronaut_repository.astronauts]
        result.extend(astros)

        return "\n".join(result)

    def __choose_astros(self):
        eligible_astros = []

        for astro in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen):
            if len(eligible_astros) == 5:
                break
            if astro.oxygen < 30:
                continue

            eligible_astros.append(astro)

        if len(eligible_astros) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        return eligible_astros

    def __start_mission(self, astronauts, planet):
        participants = 0

        for astro in astronauts:
            if not planet.items:
                break

            participants += 1

            while astro.oxygen > 0 and planet.items:
                astro.backpack.append(planet.items.pop())
                astro.breathe()

        if planet.items:
            self.mission_results['fail'] += 1
            return "Mission is not completed."

        self.mission_results['success'] += 1
        return f"Planet: {planet.name} was explored. {participants} astronauts participated in collecting items."


# station = SpaceStation()
# print(station.add_astronaut("Biologist", "Ivan"))
# print(station.add_astronaut("Geodesist", "Pesho"))
# print(station.add_astronaut("Geodesist", "Traqn"))
# print(station.add_astronaut("Biologist", "Kosta"))
# print(station.astronaut_repository.astronauts)
# print(station.add_planet("Venera", "Kol, Greda, Topka, Zub, Nz"))
# print(station.send_on_mission("Venera"))
# print(station.report())
# station.recharge_oxygen()
# [print(astro.oxygen) for astro in station.astronaut_repository.astronauts]
# print(station.retire_astronaut("Ivan"))
# print(station.report())
# station.retire_astronaut("Gencho")