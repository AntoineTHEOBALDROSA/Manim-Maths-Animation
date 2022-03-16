from inspect import iscode
from manim import *


class Graphing(Scene):
    def construct(self):
        # Change background
        self.camera.background_color = WHITE

        # ValueTracker
        t = ValueTracker(1.2)
        #t1 = ValueTracker(1/t2.get_value())

        # Text
        tex1 = MathTex(r'\text{Prenez deux tangeantes à la courbe : } T_a \text{ et } T_{\frac{1}{a}}').set_color(
            BLACK).to_edge(UP)

        tex2 = Tex("Considerons le triangle formé par ", "l'axe des ordonnées ",
                   " et les", " deux tangeantes").scale(0.8).set_color(BLACK).to_edge(UP)
        tex2[-1].set_color(GREEN_B)

        tex3 = MathTex(r"\text{Etudions l'aire de ce triangle quand } a \text{ tend vers }+\infty").scale(
            0.9).set_color(BLACK).to_edge(UP)

        tex4 = MathTex(r"\text{Tout d'abord, écrivons les équations de ces tangeantes}").scale(
            0.9).set_color(BLACK).to_edge(UP)

        tex5 = MathTex(r"Cherchons maintenant les points d'intersection des tangeantes avec l'axe des ordonnées").scale(
            0.8).set_color(BLACK).to_edge(UP)

        fonction = MathTex(
            r"f(x)=\frac{1}{x} \quad \Rightarrow \quad f'(x)=-\frac{1}{x^2}").scale(0.8).set_color(BLACK)

        T_a = MathTex("T_a : y =").set_color(BLACK).scale(
            0.8).shift(UP).to_edge(LEFT, buff=1.35)

        exprs_str = [
            r"f'(a) (x-a) + f(a)",
            r"-\frac{1}{a^2} (x-a) + \frac{1}{a}",
            r"-\frac{x}{a^2} + \frac{1}{a}+\frac{1}{a}",
            r"-\frac{x}{a^2} + \frac{2}{a}",
        ]
        exprs = VGroup(*[MathTex(expr).set_color(BLACK).scale(0.8).next_to(T_a)
                       for expr in exprs_str])

        T_1a = MathTex(r"T_\frac{1}{a} : y =").scale(0.8).set_color(
            BLACK).shift(UP*-1).to_edge(LEFT, buff=1.35)

        exprs_str2 = [
            r"f'\left(\frac{1}{a}\right)\left(x-\frac{1}{a}\right)+f\left(\frac{1}{a}\right)",
            r"-\frac{1}{\frac{1}{a^2}}\left(x-\frac{1}{a}\right)+\frac{1}{\frac{1}{a}}",
            r"-a^2\left(x-\frac{1}{a}\right) + a",
            r"-a^2x + 2a",
        ]
        exprs2 = VGroup(*[MathTex(expr).set_color(BLACK).scale(0.8).next_to(T_1a)
                        for expr in exprs_str2])

        ax = (Axes(x_range=[0, 5, 1], y_range=[0, 3, 1], x_length=7,
              y_length=5).to_edge(DOWN).add_coordinates()).set_color(BLACK)

        labels = ax.get_axis_labels(
            x_label="x", y_label="f(x)").set_color(BLACK)

        parab = ax.get_graph(lambda x: x**(-1), x_range=[0.125, 5], color=BLUE)

        func_label = MathTex(r"y=\frac{1}{x}").scale(
            0.6).next_to(ax, RIGHT, buff=1).set_color(BLACK)

        tangeante1 = always_redraw(lambda: ax.get_secant_slope_group(x=1/t.get_value(
        ), graph=parab, dx=0.01, secant_line_color=GREEN_B, secant_line_length=20))

        tangeante2 = always_redraw(lambda: ax.get_secant_slope_group(x=t.get_value(
        ), graph=parab, dx=0.01, secant_line_color=GREEN_B, secant_line_length=20))

        # t
        pt1 = always_redraw(lambda: Dot().set_color(TEAL_E).move_to(
            ax.c2p(t.get_value(), parab.underlying_function(t.get_value()))))

        # 1/t
        pt2 = always_redraw(lambda: Dot().set_color(TEAL_E).move_to(
            ax.c2p(1/t.get_value(), parab.underlying_function(1/t.get_value()))))

        # label_t1 = always_redraw(lambda: MathTex(r"T_{\frac{1}{a}}").set_color(
        #     TEAL_E).scale(0.6).next_to(tangeante1, RIGHT, buff=0))

        # label_t2 = always_redraw(lambda: MathTex(r"T_{a}").set_color(
        #     TEAL_E).scale(0.6).next_to(tangeante2, RIGHT, buff=-0.85))

        ordonnee = ax.get_x_axis()

        point_tri_1 = always_redraw(lambda: Dot().set_color(PURPLE_C).move_to(
            ax.c2p(((2*(t.get_value()))*((t.get_value())**2-1)
                    )/((t.get_value())**4-1), ((2*(t.get_value()))*((t.get_value())**2-1)
                                               )/((t.get_value())**4-1))))
        # Point Gauche
        point_tri_2 = always_redraw(lambda: Dot().set_color(PURPLE_C).move_to(
            ax.c2p(2*t.get_value(), 0)))
        # Point Droite
        point_tri_3 = always_redraw(lambda: Dot().set_color(PURPLE_C).move_to(
            ax.c2p(2/(t.get_value()), 0)))

        # position_list_triangle = [
        #     [ax.c2p(pt_hauteur, pt_hauteur)],
        #     [ax.c2p(pt_Ta, 0)],
        #     [ax.c2p(pt_1a, 0)]
        # ]
        triangle = always_redraw(lambda: Polygon(ax.c2p(((2*(t.get_value()))*((t.get_value())**2-1)
                                                         )/((t.get_value())**4-1), ((2*(t.get_value()))*((t.get_value())**2-1)
                                                                                    )/((t.get_value())**4-1)), ax.c2p(
            2*t.get_value(), 0), ax.c2p(2/(t.get_value()), 0), fill_color=PURPLE_C, fill_opacity=0.5).set_color(PURPLE_C))

        self.play(DrawBorderThenFill(ax), run_time=2)
        self.wait(2)
        self.play(Write(VGroup(labels, parab, func_label)), run_time=3)
        self.wait(2)
        self.play(Write(tex1), run_time=1.5)
        self.wait()
        self.play(Create(VGroup(tangeante1, tangeante2, pt1,
                  pt2)), run_time=2.5)
        self.wait(2)
        # self.play(t.animate.set_value(2), run_time=4)
        # self.wait(3)
        self.play(FadeOut(tex1))
        self.play(Write(tex2), run_time=3.5)
        self.play(ordonnee.animate.set_color(RED_D),
                  tex2[1].animate.set_color(RED_D), run_time=3)
        self.play(FadeIn(VGroup(point_tri_1, point_tri_2, point_tri_3)))
        self.play(DrawBorderThenFill(triangle), run_time=2.5)
        self.wait()
        self.play(FadeOut(tex2))
        self.play(Write(tex3), run_time=2)
        self.wait(2)
        self.play(t.animate.set_value(3), run_time=3)
        self.wait(2)
        self.play(FadeOut(labels, parab, pt1, pt2, point_tri_1,
                  point_tri_2, point_tri_3, func_label, ax, tangeante1, tangeante2, triangle), run_time=2)
        self.play(TransformMatchingTex(tex3, tex4), run_time=2)
        self.wait(2)
        self.play(Write(fonction), FadeOut(tex4), run_time=3)
        self.play(fonction.animate.to_edge(UP))
        self.wait()
        self.play(Write(VGroup(T_a, T_1a)))
        self.wait()
        self.play(Write(VGroup(exprs[0], exprs2[0])), run_time=6)
        self.wait()
        self.play(ReplacementTransform(exprs[0], exprs[1]), ReplacementTransform(
            exprs2[0], exprs2[1]), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(exprs[1], exprs[2]), ReplacementTransform(
            exprs2[1], exprs2[2]), FadeOut(fonction), run_time=3)
        self.wait(3)
        self.play(ReplacementTransform(exprs[2], exprs[3]), ReplacementTransform(
            exprs2[2], exprs2[3]), run_time=3)
        self.wait(2)
        self.play(FadeOut())

        self.play(Write(tex5),FadeIn)
