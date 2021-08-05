#Utility functions for composite_wrapper
from .cmd_parser import composite_options
from .log import logger
from decimal import Decimal


def check_longitude_validity(min_longitude, max_longitude):
    lon_lower_bound = Decimal('-180')
    lon_upper_bound = Decimal('180')
    if min_longitude > max_longitude:
        raise Exception("minimum longitude must be less than maximum longitude")
    if min_longitude < lon_lower_bound or min_longitude > lon_upper_bound:
        raise Exception("minimum longitude is not a valid value for longitude")
    if max_longitude < lon_lower_bound or max_longitude > lon_upper_bound:
        raise Exception("maximum longitude is not a valid value for longitude")


def check_latitude_validity(min_latitude, max_latitude):
    lat_lower_bound = Decimal('-90')
    lat_upper_bound = Decimal('90')
    if min_latitude > max_latitude:
        raise Exception("minimum latitude must be less than maximum latitude")
    if min_latitude < lat_lower_bound or min_latitude > lat_upper_bound:
        raise Exception("minimum latitude is not a valid value for latitude")
    if max_latitude < lat_lower_bound or max_latitude > lat_upper_bound:
        raise Exception("maximum latitude is not a valid value for latitude")


def check_bounding_box_validity():
    lon_lat_min = composite_options.lon_lat_minimum
    lon_lat_max = composite_options.lon_lat_maximum
    check_longitude_validity(min_longitude=lon_lat_min[0], max_longitude=lon_lat_max[0])
    check_latitude_validity(min_latitude=lon_lat_min[1], max_latitude=lon_lat_max[1])
    logger.debug("Bounding box is valid")
