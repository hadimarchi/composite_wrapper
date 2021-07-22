import logging
from .cmd_parser import composite_options

log_level = logging.WARNING
if composite_options.debug:
    log_level = logging.DEBUG
elif composite_options.verbose:
    log_level = logging.INFO

logging.basicConfig(level=log_level, format='%(asctime)s  %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
