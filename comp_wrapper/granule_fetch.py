from datetime import date
import json
import requests
from .cmd_parser import composite_options
from .log import logger
from .util import check_bounding_box_validity


def fetch_granules():
    check_bounding_box_validity()
    fetch_url = build_fetch_url()
    logger.info("Searching for granules")
    granules = requests.get(fetch_url).json()[0]
    granule_names = get_granule_names(granules)

    if granule_names == []:
        raise Exception("No granules found")
    logger.info("Found {granule_count} granules".format(granule_count=len(granule_names)))
    return granule_names


def build_fetch_url():
    base_url = "https://api.daac.asf.alaska.edu/services/search/param?"

    fetch_url_bbox = get_fetch_url_bbox()

    fetch_url_date_range = get_fetch_url_date_range()

    fetch_url_polarization = get_fetch_url_polarization()

    fetch_url = "{base_url}{bbox}{date_range}{polarization}&platform=S1&processingLevel=GRD_HD&output=JSON".format(
        base_url=base_url,
        bbox=fetch_url_bbox,
        date_range=fetch_url_date_range,
        polarization=fetch_url_polarization
        )
    logger.debug("Fetch url is {fetch_url}".format(fetch_url=fetch_url))
    return fetch_url


def get_fetch_url_bbox():
    min_bbox_bound = composite_options.lon_lat_minimum
    max_bbox_bound = composite_options.lon_lat_maximum

    fetch_url_bbox = "bbox={min_lon},{min_lat},{max_lon},{max_lat}&".format(
        min_lon=min_bbox_bound[0],
        min_lat=min_bbox_bound[1],
        max_lon=max_bbox_bound[0],
        max_lat=max_bbox_bound[1]
        )
    return fetch_url_bbox


def get_fetch_url_date_range():
    fetch_url_date_range = "start={start_date}T00:00:00UTC&end={end_date}T00:00:00&".format(
        start_date=composite_options.start_date if composite_options.start_date is not None else "2014-06-15",
        end_date=composite_options.end_date if composite_options.end_date is not None else str(date.today())
        )
    return fetch_url_date_range


def get_fetch_url_polarization():
    fetch_url_polarization = "polarization={polarization}".format(
        polarization=composite_options.polarization.upper()
    ).replace("+", "%2B")
    return fetch_url_polarization


def get_granule_names(granule_list):
    granule_names = []
    logger.debug("Example granule has keys of {granule_keys}".format(granule_keys=granule_list[0].keys()))
    for granule in granule_list:
        name = granule["granuleName"]
        logger.info("Acquired granule {name}".format(name=name))
        granule_names.append(name)

    return granule_names
