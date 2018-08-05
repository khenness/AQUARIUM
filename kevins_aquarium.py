# Here is a good library I could use http://www.nongnu.org/pygsear/ for games


#Actually no I will use pygame with the arcade library


"""
Bounce balls on the screen.
Spawn a new ball for each mouse-click.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.bouncing_balls


Zooming notes:
https://www.gamedev.net/forums/topic/594055-zooming-onto-an-arbitrary-point/

2d transformations lecture: https://www.youtube.com/watch?v=DD70ZIDjL7g

"""

import arcade
import random
import numpy as np


# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def compute_radius_image(radius, zoomvalue):
    pass


def translate(x, y, a, b):
    # x and y are the point to be translated, a and b are the translations in the x direction and y direction
    # video time 13.45
    m1 = np.array([[1, 0, a],
                   [0, 1, b],
                   [0, 0, 1]])
    m2 = np.array([[x],
                   [y],
                   [1]])

    return (np.dot(m1, m2))


def scale_point(x, y, s, t):
    m1 = np.array([[s, 0, 0],
                   [0, t, 0],
                   [0, 0, 1]])
    m2 = np.array([[x],
                   [y],
                   [1]])

    return (np.dot(m1, m2))




def compute_point_image(x,y,m1):
    m2 = np.array([[x],
                   [y],
                   [1]])
    return (np.dot(m1, m2))





class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0

        my_matrix = []


        self.world_x = 0
        self.world_y = 0


        self.change_x = 0
        self.change_y = 0
        self.radius = 0

    def get_x_image(self):
        #todo multiply x by my_matrix
        return self.x

    def get_y_image(self):
        #todo multiply y by my_matrix
        return self.x

def make_ball(x,y):
    """
    Function to make a new, random ball.
    """
    ball = Ball()

    # Size of the ball
    ball.radius = random.randrange(10, 30)

    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = x #random.randrange(ball.radius, SCREEN_WIDTH - ball.radius)
    ball.y = y #random.randrange(ball.radius, SCREEN_HEIGHT - ball.radius)

    # Speed and direction of rectangle
    ball.change_x = 0 #random.randrange(-2, 3)
    ball.change_y = 0 #random.randrange(-2, 3)

    # Color
    ball.color = (random.randrange(256), random.randrange(256), random.randrange(256))

    return ball



def get_2d_matrix_string(m):
    returnVal = ""
    for i in range(len(m)):
        returnVal.append(*m[i])
    return returnVal

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Kevin's Aquarium!")
        self.ball_list = []
        ball = make_ball(300,300)
        self.ball_list.append(ball)
        self.xpos = 0
        self.ypos = 0
        self.mouse_dx = 0
        self.mouse_dy = 0
        self.zoomLevel = 0

        self.my_matrix = [[1,0,0],
                             [0,1,0],
                             [0,0,1]]







    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        for ball in self.ball_list:
            myTuple = compute_point_image(ball.x, ball.y, self.my_matrix)

            arcade.draw_circle_filled(myTuple[0], myTuple[1], ball.radius, ball.color)

        # Put the text on the screen.
        output = "Balls: {}".format(len(self.ball_list))
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        output = "Mouse X Pos: {}".format(self.xpos)
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)
        output = "Mouse Y Pos: {}".format(self.ypos)
        arcade.draw_text(output, 10, 60, arcade.color.WHITE, 14)
        output = "Mouse dx: {}".format(self.mouse_dx)
        arcade.draw_text(output, 10, 80, arcade.color.WHITE, 14)
        output = "Mouse dy: {}".format(self.mouse_dy)
        arcade.draw_text(output, 10, 100, arcade.color.WHITE, 14)
        output = "Zoom Level: {}".format(self.zoomLevel)
        arcade.draw_text(output, 10, 120, arcade.color.WHITE, 14)
        output = "my_matrix: \n{}".format(np.matrix((self.my_matrix)))
        arcade.draw_text(output, 10, 220, arcade.color.WHITE, 14)


        #arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)
        #arcade.draw_text(output, 10, 60, arcade.color.WHITE, 14)



    def update(self, delta_time):
        """ Movement and game logic """


        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.radius:
                ball.change_x *= -1

            if ball.y < ball.radius:
                ball.change_y *= -1

            if ball.x > SCREEN_WIDTH - ball.radius:
                ball.change_x *= -1

            if ball.y > SCREEN_HEIGHT - ball.radius:
                ball.change_y *= -1


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        ball = make_ball(x,y)
        self.ball_list.append(ball)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.xpos = x
        self.ypos = y
        self.mouse_dx = dx
        self.mouse_dy = dy

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP or arcade.M. MOUSE_BUTTON_LEFT: # key.:
            self.zoomLevel+=1
        elif key == arcade.key.DOWN:
            self.zoomLevel-=1

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        """ User moves the scroll wheel. """
        #if scroll_x != 0:
        self.zoomLevel -= scroll_x
        #if scroll_y != 0:
        self.zoomLevel += scroll_y

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        #if key == arcade.key.UP or key == arcade.key.DOWN:
        #    self.player.delta_y = 0
        #elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
        #    self.player.delta_x = 0




def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
