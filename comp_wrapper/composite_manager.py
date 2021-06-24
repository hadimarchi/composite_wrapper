from zipfile import ZipFile
from pathlib import Path
from asf_tools.composite import make_composite
from .cmd_parser import composite_options
from .log import logger


def collect_polarized_products(products_path, polarization):
    products = list(products_path.glob("**/*{polarization}.tif".format(
        polarization=polarization)
        ))
    products = [str(product) for product in products]
    logger.info("{polarization} type products created".format(polarization=polarization))
    logger.info(products)
    logger.info("type of products is {type}".format(type=type(products)))
    logger.info("type of product is {type}".format(type=type(products[0])))
    return products


def unzip_rtc_products(location):
    logger.info(composite_options.polarization)
    products_path = Path(location)
    zipped_products = list(products_path.glob('**/*.zip'))
    for zipped_product in zipped_products:
        with ZipFile(zipped_product, 'r') as zipObj:
            zipObj.extractall("{location}".format(location=location))
    unzipped_products = {"vv_products": collect_polarized_products(products_path, "VV") if "vv" in composite_options.polarization else [],
                         "vh_products": collect_polarized_products(products_path, "VH") if "vh" in composite_options.polarization else []}
    return unzipped_products


def run_make_composite(location):
    unzipped_products = unzip_rtc_products(location)
    print(unzipped_products["vv_products"])
    print(unzipped_products["vh_products"])
    if unzipped_products["vv_products"] != []:
        make_composite("{location}/VV-composite".format(location=location),
                       unzipped_products["vv_products"])
    if unzipped_products["vh_products"] != []:
        make_composite("{location}/VH-composite".format(location=location),
                       unzipped_products["vh_products"])
