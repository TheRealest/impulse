### IMPORTANT EVENTS:
## JOYAXISMOTION -- joy, axis, value
## JOYBUTTONUP -- joy, button
## JOYBUTTONDOWN -- joy, button

import pygame
import error
import signal

# Set this to True to print every button press
VERBOSE_CONTROLLER_DEBUG = False
# Set this to True to print every access of the controller state
VERBOSE_CONTROLLER_ACCESS = False
# Number of 'positions' for each of positive/negative of each axis
NUM_BUCKETS = 3

BUTTON = {
    'A': 11,
    'B': 12,
    'X': 13,
    'Y': 14,

    'LB': 8,
    'RB': 9,

    'LS': 6,
    'RS': 7,

    'UP': 0,
    'DOWN': 1,
    'LEFT': 2,
    'RIGHT': 3,

    'BACK': 5,
    'START': 4,
    'HOME': 10
}

AXIS = {
    'LEFT-X': 0,
    'LEFT-Y': 1,

    'RIGHT-X': 2,
    'RIGHT-Y': 3,

    'LEFT-TRIGGER': 4,
    'RIGHT-TRIGGER': 5,
}

pygame.joystick.init()
button_state, button_read = {}, {}
for b in BUTTON.values():
    button_state[b], button_read[b] = False, False
axis_state = {}
for a in AXIS.values():
    axis_state[a] = 0
axis_state[AXIS['LEFT-TRIGGER']] = -1
axis_state[AXIS['RIGHT-TRIGGER']] = -1

if pygame.joystick.get_count() == 0:
    raise error.ControllerError('No controllers connected')
JS = pygame.joystick.Joystick(0)
if JS.get_name() != 'Wireless 360 Controller':
    raise error.ControllerError('Controller is not Xbox 360 controller')
JS.init()


def get_button_name(num):
    for b, n in BUTTON.items():
        if n == num:
            return b


def get_axis_name(num):
    for a, n in AXIS.items():
        if n == num:
            return a


def button_pressed(button):
    if VERBOSE_CONTROLLER_DEBUG:
        print '%s button pressed' % (get_button_name(button))
    button_state[button] = True


def button_released(button):
    if VERBOSE_CONTROLLER_DEBUG:
        read_status = '' if button_read[button] else 'not '
        print '%s button released, was %sread' % (get_button_name(button), read_status)
    button_state[button], button_read[button] = False, False


def axis_changed(axis, value):
    if VERBOSE_CONTROLLER_DEBUG:
        print '%s axis changed value to %.3f' % (get_axis_name(axis), value)
    axis_state[axis] = value


def read_button(button_str):
    if VERBOSE_CONTROLLER_ACCESS:
        if button_state[BUTTON[button_str]]:
            read_status = 'pressed, but read' if button_read[BUTTON[button_str]] else 'pressed and not yet read'
        else:
            read_status = 'released'
        print 'Read button %s, it was %s' % (button_str, read_status)
    if button_state[BUTTON[button_str]] & (not button_read[BUTTON[button_str]]):
        button_read[BUTTON[button_str]] = True
        return True
    else:
        return False


def peek_button(button_str):
    if VERBOSE_CONTROLLER_ACCESS:
        read_status = 'pressed' if button_state[BUTTON[button_str]] else 'released'
        print 'Peeked at button %s, it was %s' % (button_str, read_status)
    return button_state[BUTTON[button_str]]


def get_axis(axis_str):
    if VERBOSE_CONTROLLER_ACCESS:
        print 'Got %s axis with value %.3f' % (axis_str, axis_state[AXIS[axis_str]])
    return axis_state[AXIS[axis_str]]


def get_axes():
    axes = dict((a, get_axis(a)) for a in AXIS)
    if VERBOSE_CONTROLLER_ACCESS:
        print 'Got axes: ' + str(axes)
    return axes


def get_discrete_axis(axis, buckets=NUM_BUCKETS, zero_tolerance=0.15):
    raw_value = get_axis(axis)
    if raw_value >= 0:
        sign = 1
    else:
        sign = -1
    abs_value = abs(raw_value)

    bucket_size = (1 - zero_tolerance) / buckets
    cutoff = zero_tolerance
    for i in range(buckets):
        if abs_value < cutoff:
            return i * sign
        cutoff += bucket_size
    return buckets * sign


signal.subscribe('buttonpressed', button_pressed)
signal.subscribe('buttonreleased', button_released)
signal.subscribe('axischanged', axis_changed)
