from floodsystem.geo import stations_by_distance, rivers_by_station_number, stations_within_radius
from floodsystem.stationdata import build_station_list

def test_1B():

    stations = build_station_list()

    assert len(stations_by_distance(stations,p=(52.2053, 0.1218))) > 0
    assert stations_by_distance(stations,p=(52.2053, 0.1218))[0][0] == 'Cambridge Jesus Lock'
    assert stations_by_distance(stations,p=(52.2053, 0.1218))[-1:][0][0] == 'Penberth'

def test_1C():

    stations = build_station_list()

    assert sorted(stations_within_radius(stations, (52.2053, 0.1218), 10)) == stations_within_radius(stations, (52.2053, 0.1218), 10)

def test_1D():

    stations

def test_1E():

    stations = build_station_list()

    assert type(rivers_by_station_number(stations,N=9)) == list #testing that a list is the output
    assert rivers_by_station_number(stations,N=9)[0][0] == 'River Thames' #verifying that River Thames is the closest river

test_1B()
test_1C()
test_1E()