from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    
    list = []

    for station in stations:
        try:    
            if station.relative_water_level() > 10:
                pass
            elif station.relative_water_level() > tol:
                list += [(station.name,station.relative_water_level())]
            else:
                pass
        except:
            pass

    return sorted_by_key(list,1,reverse=True)


def stations_highest_rel_level(stations, N):

    list = []

    for station in stations:
        try:    
            if station.relative_water_level() > 10:
                pass
            else:
                list += [(station.name,station.relative_water_level())]
        except:
            pass

    return sorted_by_key(list,1,reverse=True)[:N]

