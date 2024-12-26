# Generated from gcode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,44,2,0,7,0,2,1,7,1,1,0,1,0,3,0,7,8,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,3,1,25,8,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,1,1,1,3,1,40,8,1,3,1,
        42,8,1,1,1,0,0,2,0,2,0,0,49,0,6,1,0,0,0,2,41,1,0,0,0,4,7,3,2,1,0,
        5,7,1,0,0,0,6,4,1,0,0,0,6,5,1,0,0,0,7,1,1,0,0,0,8,9,5,1,0,0,9,10,
        5,8,0,0,10,11,5,11,0,0,11,12,5,9,0,0,12,42,5,11,0,0,13,14,5,2,0,
        0,14,15,5,8,0,0,15,16,5,11,0,0,16,17,5,9,0,0,17,20,5,11,0,0,18,19,
        5,7,0,0,19,21,5,11,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,24,1,0,0,0,
        22,23,5,10,0,0,23,25,5,12,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,42,
        1,0,0,0,26,27,5,3,0,0,27,42,5,11,0,0,28,29,5,4,0,0,29,30,5,5,0,0,
        30,31,5,11,0,0,31,32,5,6,0,0,32,35,5,11,0,0,33,34,5,7,0,0,34,36,
        5,11,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,39,1,0,0,0,37,38,5,10,0,
        0,38,40,5,12,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,8,
        1,0,0,0,41,13,1,0,0,0,41,26,1,0,0,0,41,28,1,0,0,0,42,3,1,0,0,0,6,
        6,20,24,35,39,41
    ]

class gcodeParser ( Parser ):

    grammarFileName = "gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G00'", "'G01'", "'G02'", "'G03'", "'R'", 
                     "'D'", "'F'", "'X'", "'Y'", "'Z'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "R", "D", "F", "X", "Y", "Z", "NUMBER", 
                      "COLOR", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    R=5
    D=6
    F=7
    X=8
    Y=9
    Z=10
    NUMBER=11
    COLOR=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(gcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return gcodeParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = gcodeParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FastPositionExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def X(self):
            return self.getToken(gcodeParser.X, 0)
        def Y(self):
            return self.getToken(gcodeParser.Y, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFastPositionExpr" ):
                listener.enterFastPositionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFastPositionExpr" ):
                listener.exitFastPositionExpr(self)


    class CircularClockwiseInterpolateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.degrees = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gcodeParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircularClockwiseInterpolateExpr" ):
                listener.enterCircularClockwiseInterpolateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircularClockwiseInterpolateExpr" ):
                listener.exitCircularClockwiseInterpolateExpr(self)


    class LinInterpolateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.speed = None # Token
            self.color = None # Token
            self.copyFrom(ctx)

        def X(self):
            return self.getToken(gcodeParser.X, 0)
        def Y(self):
            return self.getToken(gcodeParser.Y, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)
        def F(self):
            return self.getToken(gcodeParser.F, 0)
        def Z(self):
            return self.getToken(gcodeParser.Z, 0)
        def COLOR(self):
            return self.getToken(gcodeParser.COLOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinInterpolateExpr" ):
                listener.enterLinInterpolateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinInterpolateExpr" ):
                listener.exitLinInterpolateExpr(self)


    class DrawarcExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gcodeParser.ExprContext
            super().__init__(parser)
            self.radius = None # Token
            self.degrees = None # Token
            self.speed = None # Token
            self.color = None # Token
            self.copyFrom(ctx)

        def R(self):
            return self.getToken(gcodeParser.R, 0)
        def D(self):
            return self.getToken(gcodeParser.D, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gcodeParser.NUMBER)
            else:
                return self.getToken(gcodeParser.NUMBER, i)
        def F(self):
            return self.getToken(gcodeParser.F, 0)
        def Z(self):
            return self.getToken(gcodeParser.Z, 0)
        def COLOR(self):
            return self.getToken(gcodeParser.COLOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawarcExpr" ):
                listener.enterDrawarcExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawarcExpr" ):
                listener.exitDrawarcExpr(self)



    def expr(self):

        localctx = gcodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = gcodeParser.FastPositionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(gcodeParser.T__0)
                self.state = 9
                self.match(gcodeParser.X)
                self.state = 10
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 11
                self.match(gcodeParser.Y)
                self.state = 12
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                pass
            elif token in [2]:
                localctx = gcodeParser.LinInterpolateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(gcodeParser.T__1)
                self.state = 14
                self.match(gcodeParser.X)
                self.state = 15
                localctx.x_cord = self.match(gcodeParser.NUMBER)
                self.state = 16
                self.match(gcodeParser.Y)
                self.state = 17
                localctx.y_cord = self.match(gcodeParser.NUMBER)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 18
                    self.match(gcodeParser.F)
                    self.state = 19
                    localctx.speed = self.match(gcodeParser.NUMBER)


                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 22
                    self.match(gcodeParser.Z)
                    self.state = 23
                    localctx.color = self.match(gcodeParser.COLOR)


                pass
            elif token in [3]:
                localctx = gcodeParser.CircularClockwiseInterpolateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(gcodeParser.T__2)
                self.state = 27
                localctx.degrees = self.match(gcodeParser.NUMBER)
                pass
            elif token in [4]:
                localctx = gcodeParser.DrawarcExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(gcodeParser.T__3)
                self.state = 29
                self.match(gcodeParser.R)
                self.state = 30
                localctx.radius = self.match(gcodeParser.NUMBER)
                self.state = 31
                self.match(gcodeParser.D)
                self.state = 32
                localctx.degrees = self.match(gcodeParser.NUMBER)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 33
                    self.match(gcodeParser.F)
                    self.state = 34
                    localctx.speed = self.match(gcodeParser.NUMBER)


                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 37
                    self.match(gcodeParser.Z)
                    self.state = 38
                    localctx.color = self.match(gcodeParser.COLOR)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





