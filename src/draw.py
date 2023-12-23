import cv2
import numpy as np

# CONSTANTS
WINDOW_NAME = "Draw a digit"
WINDOW_SIZE = 256
ENTER_ASCII = 13
WHITE_COLOR = (255, 255, 255)
LINE_WIDTH = 5

# GLOBALS
img = np.zeros((WINDOW_SIZE, WINDOW_SIZE, 1), np.uint8)
prev_x = None
prev_y = None
mouse_pressed = False


def draw_line(event, curr_x, curr_y, flags, param):
    global prev_x, prev_y, mouse_pressed

    # proceed based on event
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        prev_x = curr_x
        prev_y = curr_y

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        cv2.line(img, (prev_x,prev_y), (curr_x, curr_y),
                 color=WHITE_COLOR, thickness=LINE_WIDTH)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv2.line(img, (prev_x,prev_y), (curr_x, curr_y),
                     color=WHITE_COLOR, thickness=LINE_WIDTH)
            prev_x = curr_x
            prev_y = curr_y


def draw():
    # loop until closed
    while cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) > 0:
        # show window
        cv2.imshow(WINDOW_NAME, img)

        # break loop when escape key is pressed
        if cv2.waitKey(1) == ENTER_ASCII:
            break

    # close windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # set callback function and draw
    cv2.namedWindow(WINDOW_NAME)
    cv2.setMouseCallback(WINDOW_NAME, draw_line)
    draw()
