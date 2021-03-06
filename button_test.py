import button
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))

    b1 = button.Button()
    b2 = button.Button()

    b2.set_position(100, 200)
    b2.set_size(500, 200)
    b2.set_color((200, 100, 0))
    b2.set_visible(False)
    b2.set_text("hello", (100, 0, 0), 100, bold=True)
    b2.set_icon("fortest/example1.png")
    b2.set_iconSize(100, 100)
    b2.set_layout_left()

    print( (100, 250) in b2 )

    working = True

    while working:
        screen.fill((150, 150, 150))
        b1.draw(screen)
        b2.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: working = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos in b1:
                    b1.set_active(False)
                    b2.set_active()
                    b2.set_visible()
                    print("b1 pressed")
                if event.pos in b2:
                    b2.set_active(False)
                    b1.set_active()
                    print("b2 pressed")


    pygame.quit()

if __name__ == "__main__":
    main()
