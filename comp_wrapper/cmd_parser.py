import argparse
from decimal import Decimal
from getpass import getpass


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass()
        setattr(namespace, self.dest, values)


composite_options_parser = argparse.ArgumentParser()

composite_options_parser.add_argument('--username', type=str, help="Earthdata username.")
composite_options_parser.add_argument('--password', action=Password, nargs='?', dest='password', help="Earthdata password. Either use as a flag for secure password entry or followed by your password.")
composite_options_parser.add_argument('--granule_count', type=int, default=10, help="Number of granules from bounding box to process and create composite with")
composite_options_parser.add_argument('--lon_lat_minimum', type=Decimal, nargs="+", help="Coordinate to define lower left corner of bounding box")
composite_options_parser.add_argument('--lon_lat_maximum', type=Decimal, nargs="+", help="Coordinate to define upper right corner of bounding box")
composite_options_parser.add_argument('--polarization', type=str, choices=["vv", "vh", "vv+vh"], default="vv+vh", help="Polarization of granules")
composite_options_parser.add_argument('--start_date', type=str, help="Start date for granule search in the format yyyy-mm-dd")
composite_options_parser.add_argument('--end_date', type=str, help="End date for granule search in the format yyyy-mm-dd")
composite_options_parser.add_argument('--verbose', action='store_true', help="If this flag is added the logging level will be set at INFO")
composite_options_parser.add_argument('--debug', action='store_true', help="If this flag is added the logging level will be set at DEBUG. This supercedes the verbose option")
composite_options_parser.add_argument('--cleanup', action='store_true', help="If this flag is added the granules used for the composite will be deleted after the composite is made")
composite_options = composite_options_parser.parse_args()
