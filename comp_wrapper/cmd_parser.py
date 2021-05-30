from argparse import ArgumentParser

composite_options_parser = ArgumentParser()

composite_options_parser.add_argument('--username', type=str, help="earthdata username")
composite_options_parser.add_argument('--password', type=str, help="earthdata password")
composite_options_parser.add_argument('--granule_count', type=int, default=10, help="number of granules from bounding box to process and create composite with")
composite_options_parser.add_argument('--lon_lat_minimum', type=float, nargs="+", help="coordinate to define lower left corner of bounding box")
composite_options_parser.add_argument('--lon_lat_maximum', type=float, nargs="+", help="coordinate to define upper right corner of bounding box")
composite_options_parser.add_argument('--polarization', type=str, choices=["vv", "vh", "vv+vh"], default="vv+vh", help="polarization of granules")
composite_options_parser.add_argument('--cleanup', type=str, choices=["y", "n"], default="n", help="remove original granules")
composite_options_parser.add_argument('--start_date', type=str, help="start date for granule search in the format yyyy-mm-dd")
composite_options_parser.add_argument('--end_date', type=str, help="end date for granule search in the format yyyy-mm-dd")

composite_options = composite_options_parser.parse_args()
