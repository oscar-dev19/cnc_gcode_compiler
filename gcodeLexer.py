# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,91,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,8,4,8,49,8,8,11,8,12,8,50,1,8,1,8,4,8,55,8,8,11,8,12,8,
        56,3,8,59,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,83,8,9,1,10,4,10,86,8,
        10,11,10,12,10,87,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,1,0,1,3,0,9,10,13,13,32,32,98,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,
        1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,0,7,31,1,0,0,0,9,35,1,0,0,0,11,37,
        1,0,0,0,13,39,1,0,0,0,15,43,1,0,0,0,17,48,1,0,0,0,19,82,1,0,0,0,
        21,85,1,0,0,0,23,24,5,71,0,0,24,25,5,48,0,0,25,26,5,48,0,0,26,2,
        1,0,0,0,27,28,5,88,0,0,28,4,1,0,0,0,29,30,5,89,0,0,30,6,1,0,0,0,
        31,32,5,71,0,0,32,33,5,48,0,0,33,34,5,49,0,0,34,8,1,0,0,0,35,36,
        5,70,0,0,36,10,1,0,0,0,37,38,5,90,0,0,38,12,1,0,0,0,39,40,5,71,0,
        0,40,41,5,48,0,0,41,42,5,50,0,0,42,14,1,0,0,0,43,44,5,71,0,0,44,
        45,5,48,0,0,45,46,5,51,0,0,46,16,1,0,0,0,47,49,2,48,57,0,48,47,1,
        0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,58,1,0,0,0,52,
        54,5,46,0,0,53,55,2,48,57,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,
        0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,52,1,0,0,0,58,59,1,0,0,0,59,
        18,1,0,0,0,60,61,5,98,0,0,61,62,5,108,0,0,62,63,5,117,0,0,63,83,
        5,101,0,0,64,65,5,114,0,0,65,66,5,101,0,0,66,83,5,100,0,0,67,68,
        5,103,0,0,68,69,5,114,0,0,69,70,5,101,0,0,70,71,5,101,0,0,71,83,
        5,110,0,0,72,73,5,121,0,0,73,74,5,101,0,0,74,75,5,108,0,0,75,76,
        5,108,0,0,76,77,5,111,0,0,77,83,5,119,0,0,78,79,5,112,0,0,79,80,
        5,105,0,0,80,81,5,110,0,0,81,83,5,107,0,0,82,60,1,0,0,0,82,64,1,
        0,0,0,82,67,1,0,0,0,82,72,1,0,0,0,82,78,1,0,0,0,83,20,1,0,0,0,84,
        86,7,0,0,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,
        0,88,89,1,0,0,0,89,90,6,10,0,0,90,22,1,0,0,0,6,0,50,56,58,82,87,
        1,6,0,0
    ]

class gcodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NUMBER = 9
    COLOR = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G00'", "'X'", "'Y'", "'G01'", "'F'", "'Z'", "'G02'", "'G03'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "COLOR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "NUMBER", "COLOR", "WS" ]

    grammarFileName = "gcode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

