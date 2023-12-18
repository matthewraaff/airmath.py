from .coordinate import Coordinate
from .constants import RADIUS_E

from math import sin, cos, sqrt, atan2, radians

def haversine(coord1: Coordinate, coord2: Coordinate) -> float:

    pointone = (
        radians(coord1.a),
        radians(coord1.b)
        )

    pointtwo = (
        radians(coord2.a),
        radians(coord2.b)
        )

    deltaLat = pointtwo[0] - pointone[0]
    deltaLon = pointtwo[1] - pointone[1]

    a = sin(deltaLat/2) * sin(deltaLat/2) + \
     cos(pointone[0]) * cos(pointtwo[0]) * \
     sin(deltaLon/2) * sin(deltaLon/2)

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return RADIUS_E * c # km