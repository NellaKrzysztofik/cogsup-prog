from expyriment import design, control, stimuli, misc
import random
import math

FPS  = 60
MSPF = 1000 / FPS

def to_frames(t_ms):
    return math.ceil(t_ms / MSPF)

def to_time(num_frames):
    return num_frames * MSPF

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(stims):
    clk = misc.Clock()
    t0 = clk.time
    last = len(stims) - 1
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == last))
    return clk.time - t0  

def present_for(stims, num_frames):
    if num_frames <= 0:
        return
    target_ms = to_time(num_frames)
    dt = timed_draw(stims)
    clk = misc.Clock()
    clk.wait(max(0, target_ms - dt))

""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemented correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()