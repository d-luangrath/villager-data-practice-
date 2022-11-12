"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    unique_species = set()
    
    f = open(filename)
    for line in f:
        species = line.rstrip().split("|")[1]
        unique_species.add(species)
    f.close()

    print(unique_species)
    return unique_species

all_species("villagers.csv")


def get_villagers_by_species(filename, search_string="every"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
   
    f = open(filename)
    for line in f:
        name, species = line.rstrip().split("|")[:2]

        if search_string in ("every", species):
            villagers.append(name)
    f.close()
    
    print(sorted(villagers))
    return sorted(villagers)

get_villagers_by_species('villagers.csv', search_string="every")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = []
    nature = []
    education =[]
    music = []
    fashion = []
    play = []

    f = open(filename)
    for line in f:

        name, _, _, hobby, _ = line.rstrip().split("|")
        # hobby = line.rstrip().split("|")[3]
        # name = line.rstrip().split("|")[0]
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)
    f.close()

    '''returing out sorted names by hobby'''
    return[
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]

print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    f = open(filename)
    for line in f:
        data_tuple = tuple(line.rstrip().split("|"))
        all_data.append(data_tuple)

        '''Another way to write the above code, but nested'''
        # all_data.append(tuple(line.rstrip().split("|")))
    f.close()

    print(all_data)
    return all_data

print(all_data("villagers.csv"))



def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    f = open(filename)
    for name, _, _, _, motto in all_data(filename):
        if name == villager_name:
            f.close()

            return motto

print(find_motto("villagers.csv", "name"))

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    
    same_personality = set()
    wanted_personality = None
    for villager_info in all_data(filename):
        name, _, personality = villager_info[:3]
        if name == villager_name:
         wanted_personality = personality
         break

    if wanted_personality:
        for villager_info in all_data(filename):
            name, _, personality = villager_info[:3]
            if personality == wanted_personality:
                same_personality.add(name)

    return same_personality
    
result = find_likeminded_villagers("villagers.csv", "Wendy")

print(sorted(result))
print(len(result))
