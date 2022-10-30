# import turtle
import prettyTables
# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.speed(0.5)
#
#
# my_screen = turtle.Screen()
# my_screen.exitonclick()

table = prettyTables.Table()
table.add_column("Pokemon_Name", ["Khan"])
table.add_column("Type", ["Water"])
table.add_row(["osama", "fire"])
print(table)
