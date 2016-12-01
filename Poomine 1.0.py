import pygame

pygame.init()

Screen = pygame.display.set_mode((win_width, win_height))  # teeb akna
pygame.display.set_caption("Hangman")  # aknale pealkiri



gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:

            pass


    pygame.display.update()

    pygame.quit()
    quit()

# Fonts
def text_objects(text, color, size):
    if size == "small":
        text_surface = smallFont.render(text, True, color)
    elif size == "medium":
        text_surface = medFont.render(text, True, color)
    elif size == "large":
        text_surface = largeFont.render(text, True, color)
    return text_surface, text_surface.get_rect()


# Text for button
def text_to_button(msg, color, button_x, button_y, but_width, but_height, size="small"):
    textsurface, textrectangle = text_objects(msg, color, size)
    textrectangle.center = ((button_x + (but_width / 2)), button_y + (but_height / 2))
    Screen.blit(textsurface, textrectangle)


# Text to screen
def message_to_screen(msg, color, y_displace=0, size="small", background=white, x_displace=0):
    textsurface, textrectangle = text_objects(msg, color, size)
    textrectangle.center= (display_width / 2) + x_displace, (display_height / 2) + y_displace
    if background is not None:
        pygame.draw.rect(Screen, white, ((display_width / 2 - textrectangle.width / 2 + x_displace),
                                         (display_height / 2 - textrectangle.height / 2 + y_displace), textrectangle.width, textrectangle.height))
    Screen.blit(textsurface, textrectangle)


# Button info
class Button():
    def __init__(self, rect, col1, col2, button_text, tulemus):
        self.rect = rect
        self.col1 = col1
        self.col2 = col2
        self.button_text = button_text
        self.tulemus = tulemus

    def draw(self):
        if collision(self.rect[0], self.rect[1], self.rect[2],self.rect[3],pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            pygame.draw.rect(Screen, self.col2, self.rect)
        else:
            pygame.draw.rect(Screen, self.col1, self.rect)
        text_to_button(self.button_text, black, self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def mouse_collision(self, mouse_event):
        if collision(self.rect[0], self.rect[1], self.rect[2], self.rect[3], mouse_event.pos[0], mouse_event.pos[1]):
            return self.tulemus
        else:
            return


def handle_buttons(buttons, mouse_event):
    for b in buttons:
        result = b.mouse_collision(mouse_event)
        if result is not None:
            return result


def draw_buttons(buttons):
    for b in buttons:
        b.draw()


def collision(box_x, box_y, box_w, box_h, point_x, point_y):
    if point_x < box_x or point_y < box_y or point_x > box_x+box_w or point_y > box_y + box_h:
        return False
    else:
        return True