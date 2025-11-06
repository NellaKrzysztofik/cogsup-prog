from expyriment import design, control, stimuli

exp = design.Experiment(name = "display edges")

control.initialize(exp)

screen_w, screen_h = exp.screen.size
hx, hy = screen_w// 2, screen_h// 2

side = 0.05 * screen_w
offset = (side // 2) + 1

top_left_square = stimuli.Rectangle(size = (side,side),colour=(255, 0, 0), position = (-hx + offset,  hy - offset), line_width = 1)
top_right_square = stimuli.Rectangle(size = (side,side),colour=(255, 0, 0), position = ( hx - offset,  hy - offset), line_width = 1)
bottom_left_square = stimuli.Rectangle(size = (side,side), colour=(255, 0, 0), position = (-hx + offset, -hy + offset), line_width = 1)
bottom_right_square = stimuli.Rectangle(size = (side,side), colour=(255, 0, 0), position = ( hx - offset, -hy + offset), line_width = 1)

control.start(subject_id=1)

top_left_square.present(clear=True, update=False)
top_right_square.present(clear=False, update=False)
bottom_left_square.present(clear=False, update=False)
bottom_right_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()