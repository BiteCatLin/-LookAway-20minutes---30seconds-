# This is a simple program that will notify you
#   every 20 minutes to take a 30-second break,
#   which is, to look away from your computer
# Notes: The tuples used in the program are constructed
#        based on the coordinates' system as specified in the
#        pygame package. Please refer to https://www.pygame.org/docs/
#        for more details;
#        Some numbers appear to be magic numbers in this program, such as
#        'move'. These numbers are obtained by testing the outcomes/effects
#        of the timer to best perform the function and effect of this program


# Necessary packages
import sys
import time as t
import numpy as np
import pygame as pg
from pygame.locals import *
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


# terminate() will terminate the entire program
def terminate():
    pg.quit()
    sys.exit()

# highlight() will highlight the button when the mouse is over it
def highlight():
    mousex, mousey = event.pos
    if (mousex in range(0, WIDTH)) and (mousey in range(0, HEIGHT)):
        # Over the pause or start button
        if mousex in range(pauseRect[0], pauseRect[0] + pauseRect[2]) and \
                mousey in range(pauseRect[1], pauseRect[1] + pauseRect[3]):
            points = ((pauseRect[0], pauseRect[1]),
                      (pauseRect[0] + pauseRect[2] - 1, pauseRect[1]),
                      (pauseRect[0] + pauseRect[2] - 1, pauseRect[1] + pauseRect[3] - 1),
                      (pauseRect[0], pauseRect[1] + pauseRect[3] - 1))
            pg.draw.polygon(WINDOW, BLUE, points, 2)

        # Over the reset button
        elif mousex in range(resetRect[0], resetRect[0] + resetRect[2]) and \
                mousey in range(resetRect[1], resetRect[1] + resetRect[3]):
            points = ((resetRect[0], resetRect[1]),
                      (resetRect[0] + resetRect[2] - 1, resetRect[1]),
                      (resetRect[0] + resetRect[2] - 1, resetRect[1] + resetRect[3] - 1),
                      (resetRect[0], resetRect[1] + resetRect[3] - 1))
            pg.draw.polygon(WINDOW, BLUE, points, 2)

        # Over the end button
        elif mousex in range(endRect[0], endRect[0] + endRect[2]) and \
                mousey in range(endRect[1], endRect[1] + endRect[3]):
            points = ((endRect[0], endRect[1]),
                      (endRect[0] + endRect[2] - 1, endRect[1]),
                      (endRect[0] + endRect[2] - 1, endRect[1] + endRect[3] - 1),
                      (endRect[0], endRect[1] + endRect[3] - 1))
            pg.draw.polygon(WINDOW, BLUE, points, 2)
    pg.display.update()

# resetTimer() will reset the timer
def resetTimer():
    global status
    global begin
    global theta
    global restLength
    if status == 0:
        # The background colour
        WINDOW.fill(OLDLACE)

        # Play the notification sound
        continueNotify = pg.mixer.Sound("continue.mp3")
        continueNotify.play()

        # Reset the timer's status
        begin = t.time() + 1
        theta = - np.pi / 2

    elif status == 1:
        # Play the notification sound
        pauseNotify = pg.mixer.Sound("stop.mp3")
        pauseNotify.play()

        # Reset the timer's status
        begin = t.time() + 1
        restLength = 30

# click() will response to the mouse click
def click():
    global isPause
    global begin
    global now
    global interval
    mousex, mousey = event.pos
    if (mousex in range(0, WIDTH)) and (mousey in range(0, HEIGHT)):
        # Over the pause or start button
        if mousex in range(pauseRect[0], pauseRect[0] + pauseRect[2]) and \
                mousey in range(pauseRect[1], pauseRect[1] + pauseRect[3]):
            points = ((pauseRect[0], pauseRect[1]),
                      (pauseRect[0] + pauseRect[2] - 1, pauseRect[1]),
                      (pauseRect[0] + pauseRect[2] - 1, pauseRect[1] + pauseRect[3] - 1),
                      (pauseRect[0], pauseRect[1] + pauseRect[3] - 1))
            pg.draw.polygon(WINDOW, RED, points, 2)
            pg.display.update()
            pg.time.wait(oneSecond // 2)
            if not isPause:
                isPause = True
            elif isPause:
                now = t.time()
                begin = now - interval
                interval = 0
                isPause = False

        # Over the reset button
        elif mousex in range(resetRect[0], resetRect[0] + resetRect[2]) and \
                mousey in range(resetRect[1], resetRect[1] + resetRect[3]):
            points = ((resetRect[0], resetRect[1]),
                      (resetRect[0] + resetRect[2] - 1, resetRect[1]),
                      (resetRect[0] + resetRect[2] - 1, resetRect[1] + resetRect[3] - 1),
                      (resetRect[0], resetRect[1] + resetRect[3] - 1))
            if not isPause:
                pg.draw.polygon(WINDOW, RED, points, 2)
                pg.display.update()
                pg.time.wait(oneSecond // 2)
                resetTimer()
            elif isPause:
                pg.draw.polygon(WINDOW, BLUE, points, 2)
                pg.display.update()
                pg.time.wait(oneSecond // 2)

        # Over the end button
        elif mousex in range(endRect[0], endRect[0] + endRect[2]) and \
                mousey in range(endRect[1], endRect[1] + endRect[3]):
            points = ((endRect[0], endRect[1]),
                      (endRect[0] + endRect[2] - 1, endRect[1]),
                      (endRect[0] + endRect[2] - 1, endRect[1] + endRect[3] - 1),
                      (endRect[0], endRect[1] + endRect[3] - 1))
            pg.draw.polygon(WINDOW, RED, points, 2)
            pg.display.update()
            pg.time.wait(oneSecond // 2)
            terminate()


# program initializes
pg.init()

# 1 second in milliseconds:
oneSecond = 1000

# 20 minutes in seconds
twentyMinute = 20 * 60

# countdown represents the countdown
#   that will be shown on the
#   display window
countdown = 0

# begin represents the time when the countdown started
begin = t.time() + 1

# now represents the time at any point after the countdown started
now = 0

# restLength is length of the break
restLength = 30

# interval is the length of the time after
#  the break or the work began
interval = 0

# status indicates whether it is
#   the working time or the break
# Notes: status = 0 => work
#        status = 1 => break
status = 0

# isPause indicates whether the timer is paused
isPause = False

# FPS
FPS = 30
FPSCLOCK = pg.time.Clock()

# Colours in RGB format
OLDLACE = (253, 245, 230)
BLACK = (0, 0, 0)
GREEN = (25, 205, 58)
RED = (235, 51, 48)
# YELLOW = (255, 215, 0)
GOLD = (238, 201, 0)
BLUE = (0, 0, 255)

# Sets up the program display window
WIDTH = 300
HEIGHT = WIDTH + 50
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("休息一下吧, 阿烨")

# Sets up the text size
textSize = 25
timeSize = 35
warnSize = 40
textFont = pg.font.SysFont("calibri", textSize)
timeFont = pg.font.SysFont("arial", timeSize)
warnFont = pg.font.SysFont("arial", warnSize)

# The pause button
textPause = textFont.render("PAUSE", True, BLACK, OLDLACE)
textPauseObj = textPause.get_rect()
textPauseObj.center = (150, 248)
pauseRect = (110, 233, 80, 27)

# The start button
textStart = textFont.render("START", True, BLACK, OLDLACE)
textStartObj = textStart.get_rect()
textStartObj.center = (150, 248)
startRect = (110, 233, 80, 27)

# The reset button
textReset = textFont.render("RESET", True, BLACK, OLDLACE)
textResetObj = textReset.get_rect()
textResetObj.center = (150, 288)
resetRect = (110, 273, 80, 27)

# The end button
textEnd = textFont.render("END", True, BLACK, OLDLACE)
textEndObj = textEnd.get_rect()
textEndObj.center = (150, 325)
endRect = (110, 311, 80, 27)

# The circle
circleCentre = (150, 140)
circleRadius = 70

# Use lines to fill the circle
theta = - np.pi / 2
tinyAdjustment = 1.7453292519943197e-06    # obtained by trying several times
move = np.pi / (pow(1200, 3) / (1440 * 66)) + tinyAdjustment # obtained by trying several times

# The warning
look = warnFont.render("LOOK", True, RED, OLDLACE)
lookObj = look.get_rect()
lookObj.center = (150, 120)
away = warnFont.render("AWAY", True, RED, OLDLACE)
awayObj = away.get_rect()
awayObj.center = (150, 160)

# The warning in gold
goldLook = warnFont.render("LOOK", True, GOLD)
goldLookObj = goldLook.get_rect()
goldLookObj.center = (150, 120)
goldAway = warnFont.render("AWAY", True, GOLD)
goldAwayObj = goldAway.get_rect()
goldAwayObj.center = (150, 160)

# Fill the background for the very first start
WINDOW.fill(OLDLACE)
pg.display.update()

# The 'timer loop'
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            terminate()
        if not event.type == MOUSEMOTION or not event.type == MOUSEBUTTONUP:
            pg.event.pump()
        # When the timer is paused
        if isPause:
            # Save the timer's status
            now = now
            interval = now - begin

            # Refill the bottom half of the window
            bottomHalfRect = (0, HEIGHT - 120, WIDTH, 120)
            pg.draw.rect(WINDOW, OLDLACE, bottomHalfRect)

            # The start button
            WINDOW.blit(textStart, textStartObj)
            pg.draw.rect(WINDOW, BLACK, startRect, 1)

            # The reset button
            WINDOW.blit(textReset, textResetObj)
            pg.draw.rect(WINDOW, BLACK, resetRect, 1)

            # The end button
            WINDOW.blit(textEnd, textEndObj)
            pg.draw.rect(WINDOW, BLACK, endRect, 1)

            # Highlight the buttons
            if event.type == MOUSEMOTION:
                highlight()

            # When the mouse is clicked
            if event.type == MOUSEBUTTONDOWN:
                click()

            pg.display.update()
            continue
        # The working time
        if status == 0:

            # The countdown
            now = t.time()
            countdown = int(twentyMinute - (now - begin))
            timeLeft = divmod(countdown, 60)
            minute = timeLeft[0]
            second = timeLeft[1]
            textCountdown = timeFont.render("%02d:%02d" % (minute, second), True, GREEN, OLDLACE)
            textCountdownObj = textCountdown.get_rect()
            textCountdownObj.center = (150, 45)
            WINDOW.blit(textCountdown, textCountdownObj)
            pg.draw.circle(WINDOW, GREEN, circleCentre, circleRadius, 5)

            # Fill the green circle
            greenLineStart = circleCentre
            greenLineEnd = ((circleRadius - 2) * round(np.cos(theta), 2) + greenLineStart[0],
                            (circleRadius - 2) * round(np.sin(theta), 2) + greenLineStart[1])
            pg.draw.line(WINDOW, GREEN, greenLineStart, greenLineEnd, 2)

            # Refill the bottom half of the window
            bottomHalfRect = (0, HEIGHT - 120, WIDTH, 120)
            pg.draw.rect(WINDOW, OLDLACE, bottomHalfRect)

            # The pause button
            WINDOW.blit(textPause, textPauseObj)
            pg.draw.rect(WINDOW, BLACK, pauseRect, 1)

            # The reset button
            WINDOW.blit(textReset, textResetObj)
            pg.draw.rect(WINDOW, BLACK, resetRect, 1)

            # The end button
            WINDOW.blit(textEnd, textEndObj)
            pg.draw.rect(WINDOW, BLACK, endRect, 1)

            # Highlight the buttons
            if event.type == MOUSEMOTION:
                highlight()

            # When the mouse is clicked
            if event.type == MOUSEBUTTONDOWN:
                click()

            # Fill the circle
            if countdown > -1:
                theta += move

            # When the time is up
            elif countdown <= -1:
                # Play the notification sound
                pauseNotify = pg.mixer.Sound("stop.mp3")
                pauseNotify.play()

                # Change the timer's status
                status = 1
                begin = t.time() + 1
                restLength = 30
                theta = - np.pi / 2

            pg.display.update()
            continue
        # The break time
        elif status == 1:
            # The background colour
            WINDOW.fill(OLDLACE)

            # The countdown
            now = t.time()
            countdown = int(restLength - (now - begin))
            textCountdown = timeFont.render("%s" % countdown, True, RED, OLDLACE)
            textCountdownObj = textCountdown.get_rect()
            textCountdownObj.center = (150, 45)
            WINDOW.blit(textCountdown, textCountdownObj)

            # The circle
            pg.draw.circle(WINDOW, RED, circleCentre, circleRadius, 5)

            if countdown % 2 == 0:
                # The warning
                WINDOW.blit(look, lookObj)
                WINDOW.blit(away, awayObj)

            elif not countdown % 2 == 0:
                # The warning
                WINDOW.blit(goldLook, lookObj)
                WINDOW.blit(goldAway, awayObj)

            # The pause button
            WINDOW.blit(textPause, textPauseObj)
            pg.draw.rect(WINDOW, BLACK, pauseRect, 1)

            # The reset button
            WINDOW.blit(textReset, textResetObj)
            pg.draw.rect(WINDOW, BLACK, resetRect, 1)

            # The end button
            WINDOW.blit(textEnd, textEndObj)
            pg.draw.rect(WINDOW, BLACK, endRect, 1)

            # Highlight the buttons
            if event.type == MOUSEMOTION:
                highlight()

            # When the mouse is clicked
            if event.type == MOUSEBUTTONDOWN:
                click()

            # When the time is up
            if countdown < 0:
                # The background colour
                WINDOW.fill(OLDLACE)

                # The pause button
                WINDOW.blit(textPause, textPauseObj)
                pg.draw.rect(WINDOW, BLACK, pauseRect, 1)

                # The reset button
                WINDOW.blit(textReset, textResetObj)
                pg.draw.rect(WINDOW, BLACK, pauseRect, 1)

                # The end button
                WINDOW.blit(textEnd, textEndObj)
                pg.draw.rect(WINDOW, BLACK, endRect, 1)

                # Play the notification sound
                continueNotify = pg.mixer.Sound("continue.mp3")
                continueNotify.play()

                # Change the timer's status
                status = 0
                begin = t.time() + 1

            pg.display.update()
            continue
    # Add an event to the queue to prevent the
    #  timer from freezing
    if not pg.event.peek():
        pg.event.post(event)
    FPSCLOCK.tick(FPS)






