from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE

exp = design.Experiment(name = "kanizsa square", background_colour = C_GREY)

control.initialize(exp)

control.start(subject_id=1)

screen_w, screen_h = exp.screen.size

side_square = 0.25 * screen_w
radius = 0.25/4 * screen_w

square = stimuli.Rectangle (size = (side_square, side_square), colour = C_GREY, position=(0, 0))
                            
half_side = side_square // 2

circle_top_left = stimuli.Circle(radius = radius, colour = C_BLACK, position = (-half_side,  half_side))
circle_top_right = stimuli.Circle(radius = radius, colour = C_BLACK, position = ( half_side,  half_side))
circle_bottom_left = stimuli.Circle(radius = radius, colour = C_WHITE, position = (-half_side, -half_side))
circle_bottom_right = stimuli.Circle(radius = radius, colour = C_WHITE, position = (half_side, -half_side))

circle_top_left.present(clear=True, update=False)
circle_top_right.present(clear=False, update=False)
circle_bottom_left.present(clear=False, update=False)
circle_bottom_right.present(clear=False, update=False)
square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()