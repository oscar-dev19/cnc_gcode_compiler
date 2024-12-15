# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.
import turtle
machinePointer = turtle.Turtle()

class gcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcodeParser#start.
    def visitStart(self, ctx:gcodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#fastPositionExpr.
    def visitFastPositionExpr(self, ctx:gcodeParser.FastPositionExprContext):
        
        x_coord = int(ctx.x_cord.text)
        y_coord = int(ctx.y_cord.text)

        #max speed
        machinePointer.speed(10)

        #no cutting!
        machinePointer.penup()

        #machine movement.
        machinePointer.goto(x_coord,y_coord)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#linInterpolateExpr.
    def visitLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):
        
        x_coord = int(ctx.x_cord.text)
        y_coord = int(ctx.y_cord.text)

        if ctx.speed:
            speed = int(ctx.speed.text)
            machinePointer.speed(speed)

        if ctx.color:
            color = ctx.color.text
            machinePointer.color(color)


        #set to cut
        machinePointer.pendown()

        #machine movement
        machinePointer.goto(x_coord,y_coord)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#circularClockwiseInterpolateExpr.
    def visitCircularClockwiseInterpolateExpr(self, ctx:gcodeParser.CircularClockwiseInterpolateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawarcExpr.
    def visitDrawarcExpr(self, ctx:gcodeParser.DrawarcExprContext):
        return self.visitChildren(ctx)



del gcodeParser
