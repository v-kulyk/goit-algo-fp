import turtle


def draw_pythagoras_tree(branch_length: float, t_cursor: turtle.Turtle, angle: int, recursion_level: int):
    if recursion_level == 0:
        return
    else:
        t_cursor.forward(branch_length)
        t_cursor.right(angle)
        draw_pythagoras_tree(branch_length * 0.7, t_cursor, angle, recursion_level - 1)
        t_cursor.left(angle * 2)
        draw_pythagoras_tree(branch_length * 0.7, t_cursor, angle, recursion_level - 1)
        t_cursor.right(angle)
        t_cursor.backward(branch_length)



if __name__ == "__main__":
    recursion_level = int(input("Enter the recursion level for the Pythagorean tree: "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("green")
    t.width(2)
    t.speed(0)
    t.left(90)

    draw_pythagoras_tree(100, t, 45, recursion_level)
    screen.exitonclick()
