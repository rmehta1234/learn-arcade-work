import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.CYAN)
arcade.start_render()

def draw_snow():
    arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, arcade.csscolor.WHITE)



def draw_body():
    arcade.draw_circle_filled(300, 250, 100, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300, 400, 70, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300, 500, 40, arcade.csscolor.WHITE)

def draw_eyes():
    arcade.draw_circle_filled(280, 500, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(320, 500, 5, arcade.csscolor.BLACK)

def draw_nose():
    arcade.draw_triangle_filled(290, 495, 310, 495, 320, 480, arcade.csscolor.ORANGE)

def draw_buttons():
    arcade.draw_circle_filled(300, 435, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(300, 405, 5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(300, 375, 5, arcade.csscolor.BLACK)

def draw_hat():
    arcade.draw_rectangle_filled(300, 535, 80, 2, arcade.csscolor.BLACK)
    arcade.draw_polygon_filled(((278, 580),
                                (278, 537),
                                (323, 537),
                                (323, 580)
                                ),
                               arcade.csscolor.BLACK)

def draw_mouth():
    arcade.draw_circle_filled(283, 480, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(288, 477, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(294, 475.5, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(299.5, 475.5, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(304.5, 477, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(309.5, 479.5, 2, arcade.csscolor.BLACK)

draw_snow()

draw_body()

draw_eyes()

draw_nose()

draw_buttons()

draw_hat()

draw_mouth()


arcade.finish_render()
arcade.run()