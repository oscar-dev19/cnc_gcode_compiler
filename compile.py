from antlr4 import *
from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser
from gcodeVisitor import gcodeVisitor
import time
import argparse
import os


def compile_gcode(filename):
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return False

    try:
        # Initialize lexer, parser and visitor
        lexer = gcodeLexer(FileStream(filename))
        token_stream = CommonTokenStream(lexer)
        parser = gcodeParser(token_stream)
        visitor = gcodeVisitor()

        # Process the GCode
        while True:
            tree = parser.start()
            if tree.expr() is None:
                break
            print(tree.toStringTree(recog=parser))
            visitor.visit(tree)

        # Wait before closing
        time.sleep(2)
        return True

    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return False


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='GCode compiler for drawing shapes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Add arguments
    parser.add_argument('filename',
                        help='The GCode file to compile and execute')
    parser.add_argument('-d', '--delay',
                        type=float,
                        default=2.0,
                        help='Delay in seconds before closing the drawing window')

    # Parse arguments
    args = parser.parse_args()

    # Run compiler
    success = compile_gcode(args.filename)
    if not success:
        parser.print_help()
        exit(1)


if __name__ == '__main__':
    main()