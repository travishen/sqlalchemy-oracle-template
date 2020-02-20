import json
import argparse
from app import settings
from app.database import utils


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['init', 'describe'], default='describe',
                        help='Command line argument.')
    parser.add_argument('--db', choices=settings.DATABASES.keys(), default='default',
                        help='Database declared from settings.')
    parser.add_argument('--table', type=str, default=None, help='Table name.')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    if args.action == 'init':
        confirm_msg = (
            f"Do you want to drop tables in {args.db} database before recreate them? (y/n)"
        )
        drop = input(confirm_msg).lower() == "y"
        utils.init_database(args.db, drop)
        print('OK')
    if args.action == 'describe':
        if args.table:
            result = utils.describe_table(args.table, args.db)
            json_result = json.dumps(result, indent=4, default=str)
            print(json_result)


if __name__ == '__main__':
    main()
