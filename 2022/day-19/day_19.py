import re

with open('day-19/sample.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

class Robot:
    def __init__(self, name: str, ore_cost: int, clay_cost = 0, obsidian_cost = 0):
        self.name = name.lower()
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.counter = 0

    def create(self):
        self.counter += 1

    def check_cost(self, ore_price, clay_price = 0, obsidian_price = 0):
        if self.name == 'obsidian':
            return self.check_obsidian_cost(ore_price, clay_price)

        if self.name == 'geode':
            return self.check_geode_cost(ore_price, obsidian_price)

        return ore_price >= self.ore_cost

    def check_obsidian_cost(self, ore_price, clay_price):
        if ore_price >= self.ore_cost and clay_price >= self.clay_cost:
            return True
        return False

    def check_geode_cost(self, ore_price, obsidian_price):
        if ore_price >= self.ore_cost and obsidian_price >= self.obsidian_cost:
            return True
        return False

class Blueprint:
    def __init__(self, blueprint_id: int, ore_rbt: int, clay_rbt: int, obsidian_rbt: list, geode_rbt: list):
        self.blueprint_id = blueprint_id
        self.ore_rbt = Robot('ore', ore_rbt)
        self.clay_rbt = Robot('clay', clay_rbt)
        self.obsidian_rbt = Robot('obsidian', ore_cost=obsidian_rbt[0], clay_cost=obsidian_rbt[1])
        self.geode_rbt = Robot('geode', ore_cost=geode_rbt[0], obsidian_cost=geode_rbt[1])
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        # start off with one ore robot at initialize
        self.ore_rbt.create()

blueprints = {}

for line in data:
    blue_id = int(re.findall('Blueprint (\d+):', line)[0])
    ore_robot = int(re.findall('Each ore robot costs (\d+) ore\.', line)[0])
    clay_robot = int(re.findall('Each clay robot costs (\d+) ore\.', line)[0])
    obsidian_robot = list(map(int, re.findall('Each obsidian robot costs (\d+) ore and (\d+) clay\.', line)[0]))
    geode_robot = list(map(int, re.findall('Each geode robot costs (\d+) ore and (\d+) obsidian\.', line)[0]))

    blueprints[blue_id] = Blueprint(blue_id, ore_robot, clay_robot, obsidian_robot, geode_robot)

# print(blueprints)

for min in range(1,25):
    for key, blueprint in blueprints.items():
