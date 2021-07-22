from hyp3_sdk import HyP3, Batch, Job
from .cmd_parser import composite_options
from datetime import datetime
from .log import logger


def run_rtc_gamma(granules):
    hyp3 = HyP3(username=composite_options.username, password=composite_options.password)
    logger.info("Running Gamma")
    logger.debug("preparing gamma jobs")
    rtc_gamma_jobs = [hyp3.prepare_rtc_job(granule=granule, include_scattering_area=True) for granule in granules]
    logger.debug("jobs prepared")
    logger.info(rtc_gamma_jobs)
    rtc_gamma_batch = hyp3.submit_prepared_jobs(rtc_gamma_jobs)
    logger.debug("jobs submitted")
    rtc_gamma_batch = hyp3.watch(rtc_gamma_batch)
    logger.info("Gamma done")
    logger.info("Downloading Gamma products")
    download_location = "{now}_min:{lon_lat_min}_max:{lon_lat_max}_granules:{granule_count}".format(
        now=datetime.now().isoformat(),
        lon_lat_min=composite_options.lon_lat_minimum,
        lon_lat_max=composite_options.lon_lat_maximum,
        granule_count=len(granules)
    )
    rtc_gamma_batch.download_files(location=download_location)
    logger.info("Gamma products downloaded")
    logger.info("Download location is {location}".format(location=download_location))
    return download_location
