"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    x,y,z,*rest = each_wagons_id
    *agg_list, = z, *missing_wagons, *rest, x, y
    return agg_list


def add_missing_stops(route, **kwargs):
    # route.update(dict(kwargs.items()))
    return {**route, "stops": list(kwargs.values()) }


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    a, b, c = zip(*wagons_rows)
    return [list(a),list(b), list(c)]
