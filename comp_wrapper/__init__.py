import os
from .cmd_parser import composite_options
from .granule_fetch import fetch_granules
from .gamma_manager import run_rtc_gamma
from .composite_manager import run_make_composite
from .log import logger
from .cleanup import cleanup_gamma_products


def run():
    granules = fetch_granules()
    if composite_options.granule_count > len(granules):
        composite_options.granule_count = len(granules)
        logger.warning("Found fewer granules than requested")
    logger.info("Using {granule_count} granules".format(
        granule_count=composite_options.granule_count
        ))
    granules = granules[0:composite_options.granule_count]
    logger.info("Using granules {granules}".format(granules=granules))
    download_location = run_rtc_gamma(granules)
    run_make_composite("{cwd}/{download_location}".format(
        cwd=os.getcwd(),
        download_location=download_location
    ))
    if composite_options.cleanup:
        logger.info("Removing gamma products")
        cleanup_gamma_products(download_location)
