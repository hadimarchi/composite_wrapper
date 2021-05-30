from zipfile import ZipFile
from pathlib import Path
from asf_tools.composite import make_composite


def unzip_rtc_products(location):
    products_path = Path(location)
    zipped_products = list(products_path.glob('**/*.zip'))
    for zipped_product in zipped_products:
        with ZipFile(zipped_product, 'r') as zipObj:
            zipObj.extractall("{location}".format(location=location))
    unzipped_products = list(products_path.glob("*/*VH.tif"))
    unzipped_products = [str(unzipped_product) for unzipped_product in unzipped_products]
    return unzipped_products


def run_make_composite(location):
    unzipped_products = unzip_rtc_products(location)
    make_composite("{location}/VH-composite".format(location=location),
                   unzipped_products)
