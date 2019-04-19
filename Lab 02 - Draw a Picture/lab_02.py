import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.WHITE)
arcade.start_render()

# Sunset

arcade.draw_lrtb_rectangle_filled(0, 599, 250, 0, arcade.csscolor.PINK)
arcade.draw_lrtb_rectangle_filled(0, 599, 400, 250, arcade.csscolor.DEEP_PINK)
arcade.draw_lrtb_rectangle_filled(0, 599, 500, 400, arcade.csscolor.VIOLET)
arcade.draw_lrtb_rectangle_filled(0, 599, 600, 500, arcade.csscolor.MEDIUM_PURPLE)

# ground

arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.csscolor.BLACK)

# Lighthouse

arcade.draw_polygon_filled(((150, 350), (135, 150), (215, 150), (200, 350)), arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(150, 200, 350, 150, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(150, 153.5, 376, 350, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(196.5, 200, 376, 350, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(150, 200, 379.5, 376, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(184, 187.5, 376, 350, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(166, 169.5, 376, 350, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(148.1, 378, 201.9, 378, 175, 420, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(173, 350, 180, 350, 176.5, 357, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(173, 180, 359.5, 355, arcade.csscolor.BLACK)

arcade.finish_render()
arcade.run()