############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', False, True, 'muskmelon')
    muskmelon.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'crenshaw')
    crenshaw.add_pairing('prosciutto')

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True,
                                        'yellow_watermelon')
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print("{} pairs with ".format(melon_type.name.capitalize()))
        for pairing in melon_type.pairings:
            print("- {}".format(pairing))

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon_type in melon_types:
        melon_dict[melon.code] = melon_type
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, field_three, harvester):
        super().__init__()
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_three = field_three
        self.harvester = harvester

    def is_sellable(self, shape_rating, color_rating, field_three):

        if shape_rating > 5 and color_rating > 5 and not field_three:
            return True


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_objects = []

    melon1 = Melon()
    return melon_objects

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon_object in melon_objects:
        if melon_object.is_sellable():
            print(melon_object "- )


# melon_list = make_melon_types()

# print(make_melon_type_lookup(melon_list))