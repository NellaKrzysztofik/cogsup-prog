# Import the main modules of expyriment
from expyriment import design, control, stimuli

exp = design.Experiment(name = "Rectangle")
control.initialize(exp)

fixation = stimuli.FixCross()
rect = stimuli.Rectangle(size = (50,50), colour=(0, 0, 255))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross and rect
rect.present(clear=True, update=False)
fixation.present(clear=False, update=True)

# Leave it on-screen for 5000 ms
exp.clock.wait(5000)

# leave rect
rect.present(clear=True, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

control.end()