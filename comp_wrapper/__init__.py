import os
from .cmd_parser import composite_options
from .granule_fetch import fetch_granules
from .gamma_manager import run_rtc_gamma
from .composite_manager import run_make_composite


def run():
    granules = fetch_granules()
    if composite_options.granule_count > len(granules):
        composite_options.granule_count = len(granules)
    print("Using {granule_count} granules".format(
        granule_count=composite_options.granule_count
        ))
    granules = granules[0:composite_options.granule_count]
    download_location = run_rtc_gamma(granules)
    run_make_composite("{cwd}/{download_location}".format(
        cwd=os.getcwd(),
        download_location=download_location
    ))


def test_run_composite():
    download_location = "2021-05-23T11:03:26.348173_min:[150.1, 65.0]_max:[150.2, 65.5]_granules:2"
    run_make_composite("{cwd}/{download_location}".format(
        cwd=os.getcwd(),
        download_location=download_location
    ))
