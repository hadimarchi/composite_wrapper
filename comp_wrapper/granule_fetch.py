from .cmd_parser import composite_options
from datetime import date
import json
import requests


def fetch_granules():
    search_url = build_search_url()
    granules = requests.get(search_url).json()[0]
    granule_names = get_granule_names(granules)

    print("Found {granule_count} granules".format(granule_count=len(granule_names)))
    if granule_names == []:
        raise Exception("No granules")
    return granule_names


def build_search_url():
    min_bbox_bound = composite_options.lon_lat_minimum
    max_bbox_bound = composite_options.lon_lat_maximum

    fetch_url_bbox = "bbox={min_lon},{min_lat},{max_lon},{max_lat}&".format(
        min_lon=min_bbox_bound[0],
        min_lat=min_bbox_bound[1],
        max_lon=max_bbox_bound[0],
        max_lat=max_bbox_bound[1]
        )

    fetch_url_date_range = "start={start_date}T00:00:00UTC&end={end_date}T00:00:00&".format(
        start_date=composite_options.start_date if composite_options.start_date is not None else "2014-06-15",
        end_date=composite_options.end_date if composite_options.end_date is not None else str(date.today())
        )

    fetch_url_polarization = "polarization={polarization}".format(
        polarization=composite_options.polarization.upper()
    ).replace("+", "%2B")

    fetch_url = "https://api.daac.asf.alaska.edu/services/search/param?{bbox}{date_range}{polarization}&platform=S1&processingLevel=GRD_HD&output=JSON".format(
        bbox=fetch_url_bbox,
        date_range=fetch_url_date_range,
        polarization=fetch_url_polarization
        )
    print(fetch_url)
    return fetch_url

def get_granule_names(granule_list):
    granule_names = []
    for granule in granule_list:
        name = granule["granuleName"]
        granule_names.append(name)

    return granule_names
