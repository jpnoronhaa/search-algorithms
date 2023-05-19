import json
import random

ascending = list(range(0, 10**3))
descending = list(range(10**3 - 1, -1, -1))
random_order = random.sample(range(0, 10**3), 10**3)

data = {
    "ascending": ascending,
    "descending": descending,
    "random_order": random_order
}

with open("numbers-10-3.json", "w") as file:
    json.dump(data, file)