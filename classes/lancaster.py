import argparse

# create the parser (defining what command line arguments are expected)
parser = argparse.ArgumentParser()

# add an argument called "name", which will require a --name flag followed by the input to be used
parser.add_argument("--name", help="Enter your name")
parser.add_argument("--age", help="Enter your age", type=int)  # convert to integer
parser.add_argument("--occupation", help="Enter your occupation", default=None)  # default to None if not provided

# parse the command line arguments
args = parser.parse_args()

# use the arguments
print(f"{args.name} is {args.age} years old")
if args.occupation is not None:
    print(f"{args.name} is a {args.occupation}")