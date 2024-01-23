from manim import *

class SinGraph(Scene):
    def construct(self):
        e = ValueTracker(0.01)

        plane = PolarPlane(radius_max=3).add_coordinates()
        graph1 = always_redraw(lambda:
                               ParametricFunction(lambda t: plane.polar_to_point(2 * np.sin(3 * t), t),
                                                  t_range=[0, e.get_value()], color=GREEN)
                               )
        dot1 = always_redraw(lambda: Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end()))

        title = MathTex("f(\\theta) = 2sin(3\\theta)", color=GREEN).next_to(plane, UP, buff=0.2)

        self.play(LaggedStart(
            Write(plane), Write(title),
            run_time=3, lag_ratio=0.5)
        )
        self.add(graph1, dot1)
        self.play(e.animate.set_value(PI), run_time=10, rate_func=linear)
        self.wait()
