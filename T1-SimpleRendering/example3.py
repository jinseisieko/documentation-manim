from manim import *


class Scene_(Scene):
    def construct(self):
        self.camera.frame_rate = 60
        self.camera.background_color = BLACK

        circle = Circle(color=BLUE, radius=1)
        text = Text("абоба")  # text

        v_group = VGroup()  # Group obj

        v_group.add(circle)  # add
        v_group.add(text)

        v_group.move_to((LEFT * 2))

        self.play(Write(v_group))
        self.wait(0.1)  # wait 0.1 second

        v_group_new = v_group.copy()  # copy group
        v_group_new.color = YELLOW

        self.play(ShowPassingFlash(v_group_new))  # interesting stroke effect
        self.wait()

        self.play(v_group.animate.shift(RIGHT * 6))  # shift
        self.wait()

