import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
arcade.start_render()
def main():
    #tic-tac-toe board
    arcade.draw_line(200, 50, 200, 550, arcade.color.YELLOW, 5)
    arcade.draw_line(400, 50, 400, 550, arcade.color.GREEN, 5)

    arcade.draw_line(50, 200, 550, 200, arcade.color.NEON_FUCHSIA, 5)
    arcade.draw_line(50, 400, 550, 400, arcade.color.FRENCH_SKY_BLUE, 5)
    #X's
    arcade.draw_line(60, 540, 180, 410, arcade.color.BRILLIANT_LAVENDER, 3)
    arcade.draw_line(60, 410, 180, 540, arcade.color.BRILLIANT_LAVENDER, 3)

    arcade.draw_line(50, 50, 175, 175, arcade.color.BRILLIANT_LAVENDER, 3)
    arcade.draw_line(50, 175, 175, 50, arcade.color.BRILLIANT_LAVENDER, 3)
    #O's
    arcade.draw_circle_outline(300, 300, 75, arcade.csscolor.ORANGE, 3)

    arcade.draw_circle_outline(485, 485, 75, arcade.csscolor.ORANGE, 3)

    arcade.draw_circle_outline(300, 110, 75, arcade.csscolor.ORANGE, 3)

main()
arcade.finish_render()
arcade.run()