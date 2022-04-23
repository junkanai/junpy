import pygame

class Box:
    def __init__(self):
        self._is_active = True
        self._is_visible = True
        self.set(0, 0, 200, 50)
        self._color = (255, 255, 255)

    def set(self, x, y, w, h):
        self._x, self._y, self._w, self._h = x, y, w, h
        self._update()

    def set_position(self, x, y):
        self._x, self._y = x, y
        self._update()

    def set_size(self, w, h):
        self._w, self._h = w, h
        self._update()

    def set_color(self, c):
        self._color = c

    def set_active(self, b=True):
        self._is_active = b

    def set_visible(self, b=True):
        self._is_visible = b

    def _update(self):
        self._box = pygame.Rect(self._x, self._y, self._w, self._h)

    def draw(self, screen):
        if self._is_visible: pygame.draw.rect(screen, self._color, self._box)

    def is_in(self, pos):
        if not self._is_active: return False
        if not (self._x < pos[0] <= self._x + self._w): return False
        if not (self._y < pos[1] <= self._y + self._h): return False
        return True

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def w(self): return self._w

    @property
    def h(self): return self._h

    @property
    def color(self): return self._color

class Button:
    pass

