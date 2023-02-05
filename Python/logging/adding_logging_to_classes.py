import logging

class PlanetarySystem():
    """The class that builds a planetary system"""
    def __init__(self, name: str, star_name: str):
        """Creates a planetary system with name, name of the star and an empty dict to 
        place new planets on.
        
        :param name: Name of the solar system
        :type name: str
        :param star_name: Name of the star in the middle of the solar system.
        :type star_name: str
        """
        self.system_name = name
        self.star_name = star_name
        self.system = {}

        logging.info(f"Planetary system {name} was created. All planets orbit {star_name}")

    def add_planet(self, name: str, period: float):
        """Adds a planet to the planetary system"""
        if isinstance(period, int):
            period = float(period)

            logging.warning(
                f"""The period passed for planet "{name}" was an int, so it was coherced to a float."""
            )

        if not isinstance(period, float):
            logging.error(
                f"""Value for the 'period' was not a float for planet {name}. User passed: {period} with type {type(period)}"""
                )
            raise TypeError("""The value you passed for the "period" parameter is not a float.""")

        dist = self.distance_planet_to_star(period=period)
        self.system[name] = Planet(name, period, dist)

        logging.info(f"Planet {name} with a period of {period} years and a distance of {dist} AU was created")

    @staticmethod
    def distance_planet_to_star(period: float) -> float:
        """Method to calculate distance from a star to a planet using the time it takes 
        the planet (in years) to orbit the star.

        :param period: Time (in years) that it takes the planet to orbit the star
        :type period: float
        :return: The distance in astronomical units (AU) from the star to the planet.
        :rtype: float
        """
        return (period ** 2) ** (1/3)

class Planet():
    """The class that builds a planet"""

    def __init__(self, name: str, period: float, dist_to_star: float):
        """Creates a new planet
        
        :param name: Name of the planet
        :type name: str
        :param period: Time it takes the planet to orbit the star in years
        :type period: float
        :param dist_to_star: Distance to the center star
        :type dist_to_star: str
        """
        self.name = name
        self.period = period
        self.dist_to_star = dist_to_star


if __name__ == '__main__':
    logging.basicConfig(
        filename="Logging/planetary_logs.log",
        format="%(asctime)s | %(levelname)s | %(message)s",
        level=logging.INFO
    )
    SolarSystem = PlanetarySystem("Solar System", "Sun")

    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
    periods = [0.241, 0.616, 1, 1.882, 11.871, 29.477]

    for planet, period in zip(planets, periods):
        SolarSystem.add_planet(planet, period)