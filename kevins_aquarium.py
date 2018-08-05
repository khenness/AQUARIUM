# Here is a good library I could use http://www.nongnu.org/pygsear/ for games


#Actually no I will use pygame with the arcade library


"""
Bounce balls on the screen.
Spawn a new ball for each mouse-click.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.bouncing_balls


Zooming notes:
https://www.gamedev.net/forums/topic/594055-zooming-onto-an-arbitrary-point/

"""

import arcade
import random

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0


def make_ball(x,y):
    """
    Function to make a new, random ball.
    """
    ball = Ball()

    # Size of the ball
    ball.size = random.randrange(10, 30)

    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = x #random.randrange(ball.size, SCREEN_WIDTH - ball.size)
    ball.y = y #random.randrange(ball.size, SCREEN_HEIGHT - ball.size)

    # Speed and direction of rectangle
    ball.change_x = 0 #random.randrange(-2, 3)
    ball.change_y = 0 #random.randrange(-2, 3)

    # Color
    ball.color = (random.randrange(256), random.randrange(256), random.randrange(256))

    return ball


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

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)

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
        #arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)
        #arcade.draw_text(output, 10, 60, arcade.color.WHITE, 14)



    def update(self, delta_time):
        """ Movement and game logic """
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.size:
                ball.change_x *= -1

            if ball.y < ball.size:
                ball.change_y *= -1

            if ball.x > SCREEN_WIDTH - ball.size:
                ball.change_x *= -1

            if ball.y > SCREEN_HEIGHT - ball.size:
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



def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
