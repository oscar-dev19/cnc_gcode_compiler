from antlr4 import * 
from gcodeLexer import gcodeLexer
from gcodeParser import gcodeParser
from gcodeVisitor import gcodeVisitor
import time
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Parse a G-code file using ANTLR.")
    parser.add_argument('file', type=str, help="Path to the G-code file")
    args = parser.parse_args()

    # Load the file specified by the user
    lexer = gcodeLexer(FileStream(args.file))
    token_stream = CommonTokenStream(lexer)
    parser = gcodeParser(token_stream)
    visitor = gcodeVisitor()

    # Parse and visit the file
    while True: 
        tree = parser.start()
        if tree.expr() == None:
            break
        print(tree.toStringTree(recog=parser))
        visitor.visit(tree)

    time.sleep(2)

if __name__ == '__main__':
    main()

