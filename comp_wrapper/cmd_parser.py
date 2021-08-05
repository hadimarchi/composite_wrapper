from argparse import ArgumentParser
from decimal import Decimal

composite_options_parser = ArgumentParser()

composite_options_parser.add_argument('--username', type=str, help="earthdata username")
composite_options_parser.add_argument('--password', type=str, help="earthdata password")
composite_options_parser.add_argument('--granule_count', type=int, default=10, help="number of granules from bounding box to process and create composite with")
composite_options_parser.add_argument('--lon_lat_minimum', type=Decimal, nargs="+", help="coordinate to define lower left corner of bounding box")
composite_options_parser.add_argument('--lon_lat_maximum', type=Decimal, nargs="+", help="coordinate to define upper right corner of bounding box")
composite_options_parser.add_argument('--polarization', type=str, choices=["vv", "vh", "vv+vh"], default="vv+vh", help="polarization of granules")
composite_options_parser.add_argument('--start_date', type=str, help="start date for granule search in the format yyyy-mm-dd")
composite_options_parser.add_argument('--end_date', type=str, help="end date for granule search in the format yyyy-mm-dd")
composite_options_parser.add_argument('--verbose', action='store_true', help="if this flag is added the logging level will be set at INFO")
composite_options_parser.add_argument('--debug', action='store_true', help="if this flag is added the logging level will be set at DEBUG. This supercedes the verbose option")
composite_options_parser.add_argument('--cleanup', action='store_true', help="if this flag is added the granules used for the composite will be deleted after the composite is made")
composite_options = composite_options_parser.parse_args()
