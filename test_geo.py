from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_1B():

    stations = build_station_list

    assert len(stations_by_distance(stations,p=(52.2053, 0.1218))) > 0
    assert stations_by_distance(stations,p=(52.2053, 0.1218))[0,0] == 'Cambridge Jesus Lock'
    assert stations_by_distance(stations,p=(52.2053, 0.1218))[-1:,0] == 'Penberth'
