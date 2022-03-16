from manim import *
import math

from numpy.core.multiarray import dot


class Convergent(Scene):

    def construct(self):

        def is_dot_in_intervall(dot_val):
            if abs(a-dot_val) < epsilon.get_value():
                return True
            else:
                return False

        def dot_updater(dot):
            if is_dot_in_intervall(dot.val) == True:
                dot.set_color(GREEN)
            else:
                dot.set_color(RED)

        self.camera.background_color = WHITE

        ax = (Axes(x_range=[0, 21, 4], y_range=[0.5, 3, 1], x_length=10,
              y_length=5).to_edge(DOWN)).set_color(BLACK)

        # serie = MathTex(r"u_n=\frac{(-1)^n}{n}+2").scale(0.7).next_to(ax, direction=RIGHT,buff=0.25)

        a = 2  # ordonnée de alpha
        alpha = MathTex(r"\alpha").scale(0.9).move_to(
            ax.c2p(-0.8, a)).set_color(BLACK)
        dash = DashedLine(start=ax.c2p(0, 2), end=ax.c2p(
            21, 2), dash_length=0.2, dashed_ratio=0.7).set_color(BLACK)

        epsilon = ValueTracker(0.2)  # ordonnée de epsilon
        epsilon2 = ValueTracker(-0.2)  # ordonnée de epsilon2

        epsilon_pos = always_redraw(lambda: MathTex(
            r"\alpha + \varepsilon").set_color(BLACK).scale(0.8).move_to(ax.c2p(-1.2, epsilon.get_value()+a)))
        dash_pos = always_redraw(lambda: DashedLine(start=ax.c2p(0, epsilon.get_value()+a), end=ax.c2p(
            21, epsilon.get_value()+a)).set_color(BLACK))

        epsilon_neg = always_redraw(lambda: MathTex(
            r"\alpha - \varepsilon").set_color(BLACK).scale(0.8).move_to(ax.c2p(-1.2, epsilon2.get_value()+a)))
        dash_neg = always_redraw(lambda: DashedLine(start=ax.c2p(0, epsilon2.get_value()+a), end=ax.c2p(
            21, epsilon2.get_value()+a)).set_color(BLACK))

        labels = ax.get_axis_labels(
            x_label="n", y_label="u_n").set_color(BLACK)

        dots = [(i, ((((-1)**(i))/i)+2)) for i in range(1, 21)]
        real_dots = [Dot(point=ax.c2p(j+1, dots[j][1])).set_color(BLACK).set(val=dots[j][1])
                     for j in range(len(dots))]
        # real_dots = [Dot(point=ax.c2p(dots[j][0], dots[j][1])).set(val=dots[j][1]) for j in range(1, 21)]

        eq1 = MathTex(r"\forall \varepsilon > 0").set_color(BLACK)
        eq2 = MathTex(r"\exists N \in \mathbb{N}").set_color(BLACK)
        eq3 = MathTex(r":\forall n \geq N").set_color(BLACK)
        eq4 = MathTex(r"|x_n - \alpha| < \varepsilon").set_color(BLACK)
        eqGroup = VGroup(eq1, eq2, eq3, eq4).arrange()
        eqGroup.align_on_border(UP)

        n = 4
        N = always_redraw(lambda: MathTex(
            r"N").set_color(BLACK).move_to(ax.c2p(n, 0.3)))
        dash_N = always_redraw(lambda: DashedLine(start=ax.c2p(n, 0.5), end=ax.c2p(
            n, 3)).set_color(BLACK))

        # rec_coords = [ax.c2p(0, epsilon.get_value()+a),
        #               ax.c2p(21, epsilon.get_value()+a),
        #               ax.c2p(21, epsilon2.get_value()+a),
        #               ax.c2p(0, epsilon2.get_value()+a)]

        rec_coords = [ax.c2p(0, 2.3),
                      ax.c2p(21, 2.3),
                      ax.c2p(21, 1.7),
                      ax.c2p(0, 1.7)]

        shaded_rect = Polygon(*rec_coords, stroke_width=0,
                              fill_color=GOLD_D, fill_opacity=0.4)

        #### MAIN ####
        self.play(Create(VGroup(ax, labels)), run_time=2)

        # for elt in dots:
        #     self.play(Create(Dot().set_color(BLACK).move_to(
        #         ax.c2p(elt[0], elt[1]))), run_time=0.05)

        for elt in real_dots:
            self.play(Write(elt), run_time=1.5/len(dots))

        self.wait()

        self.play(Write(VGroup(dash, alpha)), run_time=1)
        self.wait(2)
        self.play(Write(VGroup(epsilon_pos, dash_pos,
                  epsilon_neg, dash_neg)), run_time=2)

        self.wait(1)

        self.play(Write(eq1), run_time=1.5)
        self.play(epsilon.animate.set_value(0.5),
                  epsilon2.animate.set_value(-0.5))
        self.play(epsilon.animate.set_value(0.3),
                  epsilon2.animate.set_value(-0.3))
        self.wait()
        self.play(Write(eq2), run_time=1.5)
        self.wait(0.5)
        self.play(Create(VGroup(N, dash_N)))
        self.wait()
        self.play(Write(eq3), run_time=1.5)
        self.play(*[dot.animate.add_updater(dot_updater)
                  for dot in real_dots], eq3.animate.set_color(GREEN))
        for dot in real_dots:
            dot.remove_updater(dot_updater)
            dot.add_updater(dot_updater)

        self.wait(1.5)
        self.play(Write(eq4), eq3.animate.set_color(BLACK), run_time=2)
        self.play(eq4.animate.set_color(GOLD_D),
                  Create(shaded_rect), run_time=2)
        self.wait(2)

        n = 8

        self.play(FadeOut(VGroup(dash_N, N, shaded_rect)),
                  eq4.animate.set_color(BLACK))
        self.wait(4)

        for elt in real_dots:
            self.remove(elt)
            self.wait(0.05)
        self.play(FadeOut(VGroup(labels, ax, alpha, dash, epsilon_pos,
                  epsilon_neg, dash_neg, dash_pos)), run_time=3)

        self.play(eqGroup.animate.arrange(center=True))
        self.play(eqGroup.animate.scale(1.2), run_time=2)
        self.wait(4)

        # self.play(epsilon.animate.set_value(0.13),
        #           epsilon2.animate.set_value(-0.13))

        # self.wait()
        # self.play(Write(VGroup(N, dash_N)))
        # self.wait(2)

        # self.play(FadeOut(VGroup(dash_N, N)))
        # n=2
        # self.wait(1)
        # self.play(epsilon.animate.set_value(0.6),
        #           epsilon2.animate.set_value(-0.6))

        # self.wait()
        # self.play(Write(VGroup(N, dash_N)))
        # self.wait(4)
