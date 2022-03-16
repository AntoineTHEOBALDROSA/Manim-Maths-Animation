from manim import *


class Trigo(Scene):

    def construct(self):

        self.camera.background_color = WHITE

        initialisation = MathTex(
            r"\text{Soit }z\text{ un nombre complexe non-nul de la forme :}").set_color(BLACK).to_edge(UP)
        a_ib = MathTex(r'z = a + ib').set_color(BLACK)
        a_b_real = MathTex(r"(a;b)\in\mathbb{R}^2").scale(
            0.9).set_color(BLACK).next_to(a_ib, DOWN*1.5).set_opacity(0.75)
        forme_trigo_initialisation = MathTex(
            r"\text{On appelle forme trigonométrique de } z \text{ le nombre complexe : }").set_color(BLACK).to_edge(UP)
        forme_trigo = MathTex(
            r"z = \left|z\right|(\cos\theta+i\sin\theta)").set_color(BLACK).shift(UP)
        systeme = MathTex(
            r"\text{Avec }\theta\text{ qui vérifie}\begin{cases}\cos\theta=\frac{a}{\left|z\right|} \\\sin\theta=\frac{b}{\left|z\right|}\end{cases}").scale(
                0.8).set_color(BLACK).next_to(forme_trigo, DOWN).shift(DOWN)

        
        module = MathTex(
            r"\text{Et le module de }z\text{ noté }\left|z\right|\text{ tel que :}\\\left|z\right|=\sqrt{a^2+b^2}").set_color(BLACK).scale(0.8).next_to(systeme, DOWN).shift(DOWN*0.5)
        demontrons = MathTex(r"\text{Démontrons ce résultat :}").set_color(BLACK).to_edge(UP)

        demo_str = [
            r"z = \frac{\left|z\right|(a+ib)}{\left|z\right|}",
            r"z= \left|z\right|\cdot\left(\frac{a}{\left|z\right|}+i\frac{b}{\left|z\right|}\right)",
            r"z= \left|z\right|\cdot\left(\cos\theta + i\sin\theta\right)"
        ]

        demo = VGroup(*[MathTex(expr).set_color(BLACK).scale(0.8) for expr in demo_str])

        self.wait()
        self.play(Write(initialisation), run_time=2)
        self.wait(0.5)
        self.play(Write(a_ib), run_time=2)
        self.play(FadeIn(a_b_real))
        self.wait(3)
        self.play(FadeOut(VGroup(a_b_real, a_ib, initialisation)), run_time=2)
        self.play(Write(forme_trigo_initialisation), run_time=3)
        self.wait(0.5)
        self.play(Write(forme_trigo), run_time=2)
        self.wait(4)
        self.play(FadeIn(VGroup(systeme, module)))
        self.wait(5)
        self.play(FadeOut(VGroup(systeme, module, forme_trigo_initialisation)), forme_trigo.animate.shift(DOWN), Write(demontrons))
        self.wait(2)
        self.play(ReplacementTransform(forme_trigo,a_ib),FadeOut(demontrons),run_time=2)
        self.wait()
        self.play(ReplacementTransform(a_ib,demo[0]),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(demo[0],demo[1]),run_time=3)

        systeme2 = MathTex(
            r"\text{D'après }\begin{cases}\cos\theta=\frac{a}{\left|z\right|} \\\sin\theta=\frac{b}{\left|z\right|}\end{cases}").scale(
                0.7).set_color(BLACK).next_to(demo[1], DOWN).shift(DOWN)

        self.wait(2)
        self.play(Write(systeme2))
        self.wait(2)
        self.play(ReplacementTransform(demo[1],demo[2]),run_time=3)
        self.play(FadeOut(systeme2))
        self.wait(2)

        cadre = SurroundingRectangle(demo[2],buff=.2)

        self.play(Create(cadre))
        self.play(VGroup(cadre,demo[2]).animate.scale(1.35),run_time=5)
        self.play(FadeOut(cadre,demo[2]),run_time=2)
        self.wait()

