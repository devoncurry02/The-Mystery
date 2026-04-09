from tkinter import font
import pygame
from story_data import Story

print("NOTE: This game is meant to be played on a 1536x1024 screen or bigger. If you are playing on a smaller screen, it may not be playable.")

def main():
    pygame.init()
    display_info = pygame.display.Info()
    width = display_info.current_w
    height = display_info.current_h
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The Case of the Stolen Gem")
    current_card = Story["card1"]
    current_image = current_card["image"]
    current_text = current_card["text"]
    index = 0
    list_text = True
    requested_image = pygame.image.load(current_image)
    requested_box = requested_image.get_rect()
    requested_box.center = (width // 2, height // 2)

    font = pygame.font.SysFont(None, 72) #Font style and size

    clock = pygame.time.Clock()

    while True:
        hitboxes = []
        for box in current_card["hitboxes"]:
            rectangle = pygame.Rect(
                requested_box.left + box["x"],
                requested_box.top + box["y"],
                box["width"],
                box["height"]
            )
            hitboxes.append((rectangle, box))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game closed.")
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if list_text:
                    index += 1
                    if index >= len(current_text):
                        list_text = False
                        index = 0
                else:
                    for rectangle, box in hitboxes:
                        if rectangle.collidepoint(event.pos):
                            current_card = Story[box["next_card"]]
                            current_image = current_card["image"]
                            requested_image = pygame.image.load(current_image)
                            requested_box = requested_image.get_rect()
                            requested_box.center = (width // 2, height // 2)
                            current_text = current_card["text"]

                            list_text = True
                            index = 0

        screen.fill((0, 0, 0))
        screen.blit(requested_image, requested_box)

        if list_text:
            text_box = pygame.Rect(
                requested_box.left + 15, requested_box.top + 15, requested_box.width - 30, 210
            )
            background_surface = pygame.Surface((text_box.width, text_box.height), pygame.SRCALPHA)
            pygame.draw.rect(background_surface, (0, 0, 60, 230), background_surface.get_rect()) #Text box color/transparency
            screen.blit(background_surface, text_box.topleft)
            pygame.draw.rect(screen, (0, 0, 40), text_box, 5) #Text box border color and thickness
            for i, line in enumerate(current_text[index]):
                text_surface = font.render(line, True, (255, 255, 255)) #Font color
                screen.blit(text_surface, (text_box.left + 20, text_box.top + 20 + (i * 60)))

        #for rectangle, _ in hitboxes: # <-- Outlines hitboxes, can be used to see where they are.
            #pygame.draw.rect(screen, (255, 0, 0), rectangle, 2)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()