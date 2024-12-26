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

        # Max speed
        machinePointer.speed(10)

        # No cutting!
        machinePointer.penup()

        # Machine movement
        machinePointer.goto(x_coord, y_coord)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by gcodeParser#linInterpolateExpr.
    def visitLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):
        x_coord = int(ctx.x_cord.text)
        y_coord = int(ctx.y_cord.text)

        if hasattr(ctx, 'speed') and ctx.speed:
            speed = int(ctx.speed.text)
            machinePointer.speed(speed)

        if hasattr(ctx, 'color') and ctx.color:
            color = ctx.color.text
            machinePointer.color(color)

        # Set to cut
        machinePointer.pendown()

        # Machine movement
        machinePointer.goto(x_coord, y_coord)

        return self.visitChildren(ctx)

    # G02
    # Visit a parse tree produced by gcodeParser#circularClockwiseInterpolateExpr.
    def visitCircularClockwiseInterpolateExpr(self, ctx:gcodeParser.CircularClockwiseInterpolateExprContext):
        degrees = int(ctx.degrees.text)
        machinePointer.right(degrees)
        return self.visitChildren(ctx)

    # G03
    # Visit a parse tree produced by gcodeParser#drawarcExpr.
    def visitDrawarcExpr(self, ctx:gcodeParser.DrawarcExprContext):
        if not hasattr(ctx, 'radius') or ctx.radius is None:
            raise ValueError("Must specify radius with 'R'<radius> with the G03 command.")
        if not hasattr(ctx, 'degrees') or ctx.degrees is None:
            raise ValueError("Mandatory parameter 'degrees' is missing in the G03 command.")

        degrees = int(ctx.degrees.text)
        radius = int(ctx.radius.text) * 50  # Scale radius for better visualization

        # Optional parameters: speed and color
        if hasattr(ctx, 'speed') and ctx.speed:
            speed = int(ctx.speed.text)
            machinePointer.speed(speed)

        if hasattr(ctx, 'color') and ctx.color:
            color = ctx.color.text
            machinePointer.color(color)

        # Ensure pen is down before drawing
        if not machinePointer.isdown():
            machinePointer.pendown()

        # Draw arc with the specified radius and degrees
        machinePointer.circle(radius, degrees)

        return self.visitChildren(ctx)

del gcodeParser