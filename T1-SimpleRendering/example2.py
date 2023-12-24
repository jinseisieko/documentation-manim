from manim import *


class Scene_(Scene):
    def construct(self):
        self.camera.frame_rate = 60
        self.camera.background_color = BLACK

        square = Square(fill_opacity=0.5, color=BLUE)

        self.play(FadeIn(square), run_time=2)  # slow emergence (color development)
        self.wait()
