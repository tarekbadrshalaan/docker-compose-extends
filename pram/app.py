import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--project_name', action='append',
                    help='<Required> Set flag', required=True)

args = parser.parse_args()


print(args.project_name)


res = " -f " + " -f ".join(["ali", "hassa", "sara"])
print(res)
