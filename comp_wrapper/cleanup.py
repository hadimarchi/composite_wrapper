# For the cleaning of SLC or GRD gamma_products after running composite
from pathlib import Path
from .log import logger


def cleanup_gamma_products(download_location):
    logger.info("Running cleanup of gamma products")
    remove_zipped_gamma_products(download_location)
    remove_unzipped_gamma_products(download_location)
    logger.info("Removed gamma products")


def remove_zipped_gamma_products(download_location):
    logger.debug("Removing zipped gamma products")
    zipped_gamma_products = Path(download_location).rglob("*.zip")
    zipped_gamma_products.unlink()


def remove_unzipped_gamma_products(download_location):
    logger.debug("Removing unzipped gamma product files")
    unzipped_gamma_products_files = Path(download_location).glob("S*/*")
    logger.debug("{file_count} gamma product files will be deleted".format(
        file_count=len(list(unzipped_gamma_products_files)))
        )
    unzipped_gamma_products_files.unlink()

    logger.debug("Removing empty gamma product directories")
    unzipped_gamma_product_directories = Path.glob("S*")
    logger.debug("Found {directory_count} directories or files matching 'S*' pattern to be deleted".format(
        directory_count=len(list(unzipped_gamma_product_directories))
        ))
    for gamma_product_directory in unzipped_gamma_product_directories.iterdir():
        if not gamma_product_directory.is_dir():
            logger.warning("Unexpected file in gammma products path")
        else:
            logger.debug("Removing {gamma_product_directory} directory".format(
                gamma_product_directory=gamma_product_directory
                ))
            gamma_product_directory.rmdir()
