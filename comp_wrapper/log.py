import logging
from .cmd_parser import composite_options

log_level = logging.INFO if composite_options.verbose else logging.WARNING
logging.basicConfig(level=log_level, format='%(asctime)s  %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
