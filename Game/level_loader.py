import json
from .bird import Bird


def load_level(level, game):
    game.birds = []
    game.rocks = []
    game.slingshot.shot = False
    load_map(level, game)


def load_map(level, game):
    if level > 1:
        level = 1
    path = f"Game/Assets/levels/level_{level}.json"
    with open(path, "r") as f:
        data = json.load(f)

    for key, obj in data.items():
        obj_type = obj.get("type")
        x = obj.get("x")
        y = obj.get("y")
        distance = obj.get("distance")
        speed = obj.get("speed")

        if obj_type == "bird":
            game.birds.append(Bird(x, y, distance, speed, 1, 0.5))
