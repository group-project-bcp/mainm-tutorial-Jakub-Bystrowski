from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
        self.play(circle.animate.flip())

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait(5)
        self.play(left_square.animate.shift(3 * LEFT),right_square.animate.shift(1*RIGHT),run_time=5)

class Fun(Scene):
    def construct(self):
        c = Circle(2, color=RED, fill_opacity=0.5)
        self.play(DrawBorderThenFill(c))
        self.play(c.animate.shift(10 * LEFT))
        self.play(c.animate.shift(20 * RIGHT))
        self.play(c.animate.shift(10 * LEFT))
        self.play(c.animate.flip(),run_time=0.5)
        hello = Text("HELLO").shift(0.5 * UP)
        world = Text("World!!").shift(0.5*DOWN)
        self.play(Write(hello))
        self.play(Write(world))
        self.wait(1)
        for n in range(4):
            if n % 2 == 0:
             self.play(c.animate.flip(UP), hello.animate.flip(UP), world.animate.flip(UP), run_time=0.7)
            else:
                self.play(c.animate.flip(DOWN), hello.animate.flip(DOWN), world.animate.flip(DOWN), run_time=0.7)
        self.wait(4)
