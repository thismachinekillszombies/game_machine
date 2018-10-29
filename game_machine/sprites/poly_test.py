from .vector_sprite import VectorSprite
import pygame

class Poly_Test(VectorSprite):
    def __init__(self, co_ords, lines,
                 visible = True, interactive = True,
                 line_colour = (0, 0, 0, 1),
                 line_width = 1,
                 fill_colour = (255, 255, 255, 1)):
        super(Poly_Test, self).__init__(co_ords, visible, interactive,
                                     line_colour, line_width, fill_colour)
        self.lines = lines
        max_x = min_x = lines[0][0]
        max_y = min_y = lines[0][1]
        for line in lines:
            if line[0] > max_x:
                max_x = line[0]
            if line[0] < min_x:
                min_x = line[0]
            if line[1] > max_y:
                max_y = line[1]
            if line[1] < min_y:
                min_y = line[1]
        self.bounding_box = ((-10, 10), (-30, 30))
        self.size = (21, 60)

    def fill_surface(self) :
        super(Poly_Test, self).fill_surface()
        points = [self._screen.to_pygame_coords((x, y), size_ovr = (20, 60)) for (x, y) in self.lines]
        print points
        pygame.draw.polygon(self._surface, self.line_colour,
                            points, self.line_width)
##        if self._fill_colour != None :
##            pygame.draw.circle(self._surface, self._fill_colour, \
##                               (self._radius, self._radius),
##                               self.radius, 0)
##        if self.line_width > 0 :
##            pygame.draw.circle(self._surface, self._line_colour, \
##                               (self._radius, self._radius), \
##                               self._radius, self._line_width)

##    def _draw(self):
##        points = [self._screen.to_pygame_coords((x + self.x, y + self.y)) for (x, y) in self.lines]
##        pygame.draw.aalines(self._screen.pygame_screen, self.line_colour, True,
##                            points, self.line_width)
