from manim import *


class Scene_(Scene):  # The class for creating the Scene
    def construct(self):
        self.camera.frame_rate = 60  # fps
        self.camera.background_color = BLACK  # background color

        square = Square(fill_opacity=0.5, color=BLUE)  # Blue Square with semi-transparent background

        self.play(Write(square), run_time=2)  # Outline drawing   run_time=2 - playback time
        self.wait()
