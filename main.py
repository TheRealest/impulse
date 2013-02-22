import pygame
from lib import pygcurse

from src.util import signal
from src.util.hud import hud

from src import ship

from src.ring.impulse import Impulse

WIDTH, HEIGHT, TITLE = 80, 40, 'Impulse'

win = pygcurse.PygcurseWindow(WIDTH, HEIGHT, TITLE)
win.autoupdate = False
win.font = pygame.font.SysFont('couriernew', 14, bold=True)

pygame.event.set_allowed(None)
pygame.event.set_allowed([
    pygame.JOYAXISMOTION,
    pygame.JOYBUTTONUP,
    pygame.JOYBUTTONDOWN
])
hud = hud.HUD(win, 24, 1)

this_ship = ship.generate_ship(win, 10, 12)

signal.subscribe('update', hud.update)
signal.subscribe('update', this_ship.update)
signal.subscribe('update', win.update)

while True:
    signal.emit('update')

    for e in pygame.event.get():
        if e.type == pygame.JOYBUTTONDOWN:
            signal.emit('buttonpressed', e.button)
        if e.type == pygame.JOYBUTTONUP:
            signal.emit('buttonreleased', e.button)
        elif e.type == pygame.JOYAXISMOTION:
            signal.emit('axischanged', e.axis, e.value)
