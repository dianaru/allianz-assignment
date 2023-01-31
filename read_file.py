import argparse
import sys

def cli_arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--i','-input', help='foo help')

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()