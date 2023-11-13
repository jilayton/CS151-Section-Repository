"""
Program to animate a Pacman character.
"""

from pgl import GWindow, GArc, GOval, GLine, GRect, GState

GW_WIDTH = 900
GW_HEIGHT = 400
PACMAN_RADIUS = 50
PILL_RADIUS = 10
PACMAN_SPEED = 10.86677
MOUTH_SPEED = 100
PACMAN_MOUTHSIZE = 45


def pacman():
    """Draws and animates a pacman across the screen"""

    def setup_scene():
        """
        Creates the scene, including the background, the corridor walls, and
        the yellow pills.

        Returns the background object for later comparisons to ensure that the
        background is not removed.
        """
        midx, midy = GW_WIDTH / 2, GW_HEIGHT / 2
        # Creating the background
        bg = GRect(GW_WIDTH,GW_HEIGHT)
        bg.set_filled(True)
        bg.set_color("black")
        gw.add(bg)
        # Creating the corridor walls
        for shift in range(-1, 2, 2):
            line = GLine(
                0,
                midy + shift * PACMAN_RADIUS * 1.25,
                GW_WIDTH,
                midy + shift * PACMAN_RADIUS * 1.25,
            )
            line.set_color("blue")
            line.set_line_width(10)
            gw.add(line)
        # Creating the pills
        y = GW_HEIGHT / 2 - PILL_RADIUS
        for x in range(20, GW_WIDTH, 100):
            if x < midx - PACMAN_RADIUS or x > midx + PACMAN_RADIUS:
                pill = GOval(x, y, 2 * PILL_RADIUS, 2 * PILL_RADIUS)
                pill.set_filled(True)
                pill.set_color("yellow")
                gw.add(pill)
        return bg
    
    
    
    def char_pacman():
        #MAKES PACMAN CHARACTER DEPICTION
        midx, midy = GW_WIDTH / 2, GW_HEIGHT / 2
        gs.char = GArc(midx - PACMAN_RADIUS, midy - PACMAN_RADIUS, PACMAN_RADIUS*2, PACMAN_RADIUS*2, PACMAN_MOUTHSIZE, PACMAN_MOUTHSIZE*6)
        gs.char.set_fill_color("yellow")
        gs.char.set_filled(True)
        gw.add(gs.char)

    def HALFmouth_close():
        gs.char.set_start_angle(PACMAN_MOUTHSIZE/2)
        gs.char.set_sweep_angle(PACMAN_MOUTHSIZE*6.5)
        
    def FULLmouth_close():
        gs.char.set_start_angle(0)
        gs.char.set_sweep_angle(360)
        
    def mouth_open():
        gs.char.set_start_angle(PACMAN_MOUTHSIZE)
        gs.char.set_sweep_angle(PACMAN_MOUTHSIZE*6)


    def eat():
        object = gw.get_element_at(gs.char.get_x() + PACMAN_RADIUS + (PACMAN_RADIUS/2) * gw.x, gs.char.get_y() + PACMAN_RADIUS)
        if object != bg and object != gs.char:
            gw.remove(object)


    def step():
        gs.char.move(PACMAN_SPEED*gw.x, 0)
        if not (gs.char.get_x()+(PACMAN_RADIUS*2)) <= (GW_WIDTH) or not gs.char.get_x() >= (0):
            gw.x *= -1
            gs.char.set_start_angle(gs.char.get_start_angle()+180)
        
#gw.set_interval(mouth_move, MOUTH_SPEED*4)
        
        
# if (gs.char.get_x()+(PACMAN_RADIUS*2)) != (GW_WIDTH):
    """    gw.set_timeout(HALFmouth_close, MOUTH_SPEED/4)
        gw.set_timeout(FULLmouth_close, MOUTH_SPEED/2)
        gw.set_timeout(HALFmouth_close, MOUTH_SPEED)
        gw.set_timeout(mouth_open, MOUTH_SPEED/(2/3))
        
    
        def mouth_move():
            gw.set_timeout(HALFmouth_close, MOUTH_SPEED/4)
            gw.set_timeout(FULLmouth_close, MOUTH_SPEED/2)
            gw.set_timeout(HALFmouth_close, MOUTH_SPEED)
            gw.set_timeout(mouth_open, MOUTH_SPEED/(2/3))
            

        def HALFmouth_close():
            gs.char.set_start_angle(PACMAN_MOUTHSIZE/2)
            gs.char.set_sweep_angle(PACMAN_MOUTHSIZE*6.5)
            
        def FULLmouth_close():
            gs.char.set_start_angle(0)
            gs.char.set_sweep_angle(360)
            
        def mouth_open():
            gs.char.set_start_angle(PACMAN_MOUTHSIZE)
            gs.char.set_sweep_angle(PACMAN_MOUTHSIZE*6)
            """

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    bg = setup_scene()
    gs = GState()
    gw.x = 1
    char_pacman()
    gw.set_interval(step, 20)
if __name__ == "__main__":
    pacman()