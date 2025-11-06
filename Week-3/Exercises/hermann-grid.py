from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE

exp = design.Experiment(name = "hermann grid", background_colour = C_WHITE)

control.initialize(exp)

control.start(subject_id=1)

max_width, max_height = exp.screen.size

n_rows, n_cols = 15, 15

W = n_cols * 50 + (n_cols - 1) * 10    
H = n_rows * 50 + (n_rows - 1) * 10

exp.screen.clear()

for row in range (n_rows):
    for col in range(n_cols):
        pos_x = col * (50 + 10) - (W - 50) // 2 
        pos_y = row * (50 + 10) - (H - 50) // 2 
        
        square = stimuli.Rectangle (size = (50,50) , colour = C_BLACK, position = (pos_x, pos_y))
        square.present(False, False)


exp.screen.update()
exp.keyboard.wait()

control.end()