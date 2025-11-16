from expyriment import design, control, stimuli
from expyriment.misc.constants import (
    C_WHITE, C_BLACK,
    K_SPACE, K_1, K_2, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE
)

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)
control.start(subject_id=1)

# data logging header
exp.data_variable_names = ["eye", "key", "radius", "x", "y"]

INSTRUCTION_TEMPLATE = (
    "While looking at the cross with your {eye_closed} eye closed, adjust the circle's "
    "position (ARROWS) and size (1 smaller, 2 larger) until you can no longer see it.\n\n"
    "When the circle becomes invisible, press SPACE."
)

def make_instructions(eye: str) -> stimuli.TextScreen:
    # eye: "left" or "right" — the eye to cover
    eye = eye.lower()
    eye_closed = "left" if eye == "left" else "right"
    scr = stimuli.TextScreen(
        "Instructions",
        INSTRUCTION_TEMPLATE.format(eye_closed=eye_closed)
    )
    scr.preload()
    return scr

# tuning
SIZE_STEP   = 5      # px change in radius per press
POS_STEP    = 5      # px move per press
MIN_RADIUS  = 5
MAX_RADIUS  = 300
FIX_OFFSET  = 300    # px from center for fixation

KEYS = [K_SPACE, K_1, K_2, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE]

def draw(stims):
    last = len(stims) - 1
    for i, s in enumerate(stims):
        s.present(clear=(i == 0), update=(i == last))

def make_circle(r, pos=(0, 0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

def run_trial(eye: str, radius: int = 75):
    eye = eye.lower()
    assert eye in ("left", "right"), "eye must be 'left' or 'right'"

    make_instructions(eye).present()
    exp.keyboard.wait() 

    if eye == "left":
        fixation_pos = (+FIX_OFFSET, 0)
        circle_pos   = (-150, 0)
    else: 
        fixation_pos = (-FIX_OFFSET, 0)
        circle_pos   = (+150, 0)

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_pos)
    fixation.preload()
    circle = make_circle(radius, circle_pos)

    adjusting = True
    while adjusting:
        draw([fixation, circle])

        key, _ = exp.keyboard.wait(KEYS)

        if key == K_SPACE:
            adjusting = False
            break
        if key == K_ESCAPE:
            break

        x, y = circle.position
        if key == K_1:
            radius = max(MIN_RADIUS, radius - SIZE_STEP)
        elif key == K_2:
            radius = min(MAX_RADIUS, radius + SIZE_STEP)
        elif key == K_LEFT:
            x -= POS_STEP
        elif key == K_RIGHT:
            x += POS_STEP
        elif key == K_DOWN:
            y -= POS_STEP
        elif key == K_UP:
            y += POS_STEP

        circle = make_circle(radius, (x, y))

        exp.data.add([eye, key, radius, x, y])

    stimuli.TextLine("Saved. Press SPACE to continue.").present(clear=True)
    exp.keyboard.wait(K_SPACE)

# Example: run for both eyes
run_trial("left")
run_trial("right")

control.end()
