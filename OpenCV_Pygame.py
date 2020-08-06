import pygame
from pygame.locals import KEYDOWN, K_ESCAPE
import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0)
# Native Resolution:
W = cap.get(cv.CAP_PROP_FRAME_WIDTH)
H = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
size = int(W), int(H)

pygame.init()
pygame.display.set_caption("OpenCV + PyGame")
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    screen.fill([123, 123, 123])
    # OpenCV :
    ret, frame = cap.read()
    dim = (int(W/2), int(H/2))
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
    frame = np.rot90(frame)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = cv.flip(frame, 0)

    # PYGAME:
    surfArray = pygame.surfarray.make_surface(frame)
    surfArray2 = pygame.transform.flip(surfArray, True, False)
    surfArray3 = pygame.transform.flip(surfArray, False, True)
    surfArray4 = pygame.transform.flip(surfArray, True, True)
    screen.blit(surfArray, (0, 0))
    screen.blit(surfArray2, (W/2, 0))
    screen.blit(surfArray3, (0, H/2))
    screen.blit(surfArray4, (W/2, H/2))
    pygame.display.update()

cap.release()
cv.destroyAllWindows()
