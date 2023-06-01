import json
import random
import os

try:
    os.makedirs("files")
    print("A pasta foi criada com sucesso.")
except FileExistsError:
    print("A pasta já existe.")
    

def  generate1000():

    # Generating numbers in ascending order
    ascending = list(range(0, 10**3))

    # Generating numbers in descending order
    descending = list(range(10**3 -1, -1, -1))

    # Generating numbers in random order
    random_order = random.sample(range(0, 10**3), 10**3)

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-10-3.json", "w") as file:
        json.dump(data, file)

def generate10000():
    # Generating numbers in ascending order
    ascending = list(range(0, 10**4))

    # Generating numbers in descending order
    descending = list(range(10**4 -1, -1, -1))

    # Generating numbers in random order
    random_order = random.sample(range(0, 10**4), 10**4)

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-10-4.json", "w") as file:
        json.dump(data, file)

def generate100000():
    # Generating numbers in ascending order
    ascending = list(range(0, 10**5))

    # Generating numbers in descending order
    descending = list(range(10**5 -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 10**5), 10**5)

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-10-5.json", "w") as file:
        json.dump(data, file)
def generate200000():
    # Generating numbers in ascending order
    ascending = list(range(0, 2*(10**5)))

    # Generating numbers in descending order
    descending = list(range(2*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 2*(10**5)), 2*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-2*10-5.json", "w") as file:
        json.dump(data, file)
def generate300000():
    # Generating numbers in ascending order
    ascending = list(range(0, 3*(10**5)))

    # Generating numbers in descending order
    descending = list(range(3*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 3*(10**5)), 3*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-3*10-5.json", "w") as file:
        json.dump(data, file)

def generate400000():
    # Generating numbers in ascending order
    ascending = list(range(0, 4*(10**5)))

    # Generating numbers in descending order
    descending = list(range(4*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 4*(10**5)), 4*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-4*10-5.json", "w") as file:
        json.dump(data, file)
def generate500000():
    # Generating numbers in ascending order
    ascending = list(range(0, 5*(10**5)))

    # Generating numbers in descending order
    descending = list(range(5*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 5*(10**5)), 5*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-5*10-5.json", "w") as file:
        json.dump(data, file)

def generate600000():
    # Generating numbers in ascending order
    ascending = list(range(0, 6*(10**5)))

    # Generating numbers in descending order
    descending = list(range(6*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 6*(10**5)), 6*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-6*10-5.json", "w") as file:
        json.dump(data, file)
def generate700000():
    # Generating numbers in ascending order
    ascending = list(range(0, 7*(10**5)))

    # Generating numbers in descending order
    descending = list(range(7*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 7*(10**5)), 7*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-7*10-5.json", "w") as file:
        json.dump(data, file)
def generate800000():
    # Generating numbers in ascending order
    ascending = list(range(0, 8*(10**5)))

    # Generating numbers in descending order
    descending = list(range(8*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 8*(10**5)), 8*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-8*10-5.json", "w") as file:
        json.dump(data, file)
def generate900000():
    # Generating numbers in ascending order
    ascending = list(range(0, 9*(10**5)))

    # Generating numbers in descending order
    descending = list(range(9*(10**5) -1, -1, -1))
    # Generating numbers in random order
    random_order = random.sample(range(0, 9*(10**5)), 9*(10**5))

    # Creating a dictionary with the three lists of numbers
    data = {
        "ascending": ascending,
        "descending": descending,
        "random_order": random_order
    }

    # Saving the data to a JSON file
    with open("files/numbers-9*10-5.json", "w") as file:
        json.dump(data, file)
# def generate1000000():
#     # Generating numbers in ascending order
#     ascending = list(range(0, 10**6))

#     # Generating numbers in descending order
#     descending = list(range(10**6 -1, -1, -1))

#     # Generating numbers in random order
#     random_order = random.sample(range(0, 10**6), 10**6)

#     # Creating a dictionary with the three lists of numbers
#     data = {
#         "ascending": ascending,
#         "descending": descending,
#         "random_order": random_order
#     }

#     # Saving the data to a JSON file
#     with open("files/numbers-10-6.json", "w") as file:
#         json.dump(data, file)


generate1000()
generate10000()
generate100000()
generate200000()
generate300000()
generate400000()
generate500000()
generate600000()
generate700000()
generate800000()
generate900000()

