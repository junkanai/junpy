import button
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))

    box1 = button.Box()
    box2 = button.Box()

    box2.set_position(100, 200)
    box2.set_size(300, 400)
    box2.set_color((200, 100, 0))
    box2.set_visible(False)

    working = True

    while working:
        screen.fill((150, 150, 150))
        box1.draw(screen)
        box2.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: working = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if box1.is_in(event.pos):
                    box1.set_active(False)
                    box2.set_active()
                    box2.set_visible()
                    print("box1 pressed")
                if box2.is_in(event.pos):
                    box2.set_active(False)
                    box1.set_active()
                    print("box2 pressed")


    pygame.quit()

if __name__ == "__main__":
    main()
