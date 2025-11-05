# Import the main modules of expyriment
from expyriment import design, control, stimuli

exp = design.Experiment(name = "Two squares")
control.initialize(exp)

rect_red = stimuli.Rectangle(size = (50,50), colour=(255, 0, 0), position = (-100, 0))
rect_green = stimuli.Rectangle(size = (50,50), colour=(0, 255, 0), position = (100, 0))

# Start running the experiment
control.start(subject_id=1)

rect_red .present(clear=True, update=False)
rect_green.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

control.end()