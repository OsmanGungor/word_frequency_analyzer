import argparse
import logging
from .analyzer import process_file
from .utils import setup_logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file path', required=True)
    parser.add_argument('-o', '--output', help='Output file path', required=True)
    parser.add_argument('-w', '--word', help='Word to count in the text', required=True)

    args = parser.parse_args()
    setup_logging()
    logger_cli = logging.getLogger(__name__)
    logger_cli.info(f"Provided arguments are word: {args.word} input: {args.input} output: {args.output}")

    try:
        process_file(args.word, args.input, args.output)
    except Exception as e:
        logger_cli.error(f"An error occurred: {e}")
