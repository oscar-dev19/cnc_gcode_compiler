# Generated from gcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gcodeParser import gcodeParser
else:
    from gcodeParser import gcodeParser

# This class defines a complete generic visitor for a parse tree produced by gcodeParser.
import turtle
tutu = turtle.Turtle()
class gcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gcodeParser#start.
    def visitStart(self, ctx:gcodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:gcodeParser.DrawlineExprContext):
        target_x    = int(ctx.x_cord.text)
        target_y    = int(ctx.y_cord.text)
        cur_pos     = tutu.pos()

        tutu.pendown()
        if target_x > cur_pos[0]:
            tutu.right( target_x - cur_pos[0])
        else:
            tutu.left( cur_pos[0] - target_x)

        if target_y > cur_pos[1]:
            tutu.forward( target_y - cur_pos[1])
        else:
            tutu.backward( cur_pos[1] - target_y)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#linInterpolateExpr.
    def visitLinInterpolateExpr(self, ctx:gcodeParser.LinInterpolateExprContext):

        x_cord = int(ctx.x_cord.text)
        y_cord = int(ctx.y_cord.text)
        tutu.penup();
        tutu.goto(x_cord,y_cord)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#circularClockwiseInterpolateExpr.
    def visitCircularClockwiseInterpolateExpr(self, ctx:gcodeParser.CircularClockwiseInterpolateExprContext):

        degrees = int(ctx.degrees.text)
        tutu.right(degrees)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gcodeParser#drawarcExpr.
    def visitDrawarcExpr(self, ctx:gcodeParser.DrawarcExprContext):
        
        tutu.pendown()
        radius = int(ctx.radius.text)
        degrees = int(ctx.degrees.text)
        tutu.circle(radius,degrees)

        return self.visitChildren(ctx)



del gcodeParser
