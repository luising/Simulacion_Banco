"""Clase gui Text."""
import pygame


class Text:
    """Clase para formato de texto."""

    def __init__(self, superficie, FontName=None, FontSize=30):
        """Instancia."""
        pygame.font.init()
        self.font = pygame.font.Font(FontName, FontSize)
        self.size = FontSize
        self.v = superficie
        self.amarillo = (255, 255, 0)
        self.black = (0, 0, 0)

    def render(self, surface, text, color, pos):
        """parametros."""
        text = str(text)
        x, y = pos
        for i in text.split("\r"):
            surface.blit(self.font.render(i, 1, color), (x, y))
            y += self.size

    def write(self, m, pos, c=(0, 0, 0)):
        """Ecribir en pantalla."""
        self.render(self.v, m, c, pos)
