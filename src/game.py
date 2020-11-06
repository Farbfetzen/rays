import pygame

from src.constants import *
from src import resources
from src.scenes import SCENES


class Game:
    def __init__(self):
        pygame.init()
        self.main_display = pygame.display.set_mode(MAIN_DISPLAY_SIZE)
        self.small_display = pygame.Surface(SMALL_DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        resources.load_all()
        self.running = True
        self.scene = SCENES["main game"](self)
        self.scene.start()
        self.persistent_scene_data = {}
        self.dev_overlay_visible = True

    def run(self):
        while self.running:
            # delta time of previous tick in seconds.
            # Protect against hiccups (e.g. from moving the pygame window)
            # by setting an upper limit to dt.
            dt = min(self.clock.tick(FPS) / 1000, DT_LIMIT)

            for event in pygame.event.get():
                # TODO: Check if event is mousemotion or mousebuttondown and
                #  rescale it before passing it to the scene.
                self.scene.process_event(event)
            self.scene.update(dt)
            self.scene.draw()
            pygame.transform.scale(
                self.small_display,
                MAIN_DISPLAY_SIZE,
                self.main_display
            )
            if self.dev_overlay_visible:
                self.scene.dev_overlay.update()
                self.scene.dev_overlay.draw()
            pygame.display.flip()

            if self.scene.is_done:
                self.change_scene()

    def change_scene(self):
        next_scene_name = self.persistent_scene_data["next_scene_name"]
        if not next_scene_name:
            self.quit()
        self.scene = SCENES[next_scene_name]
        self.scene.start()

    def quit(self):
        # TODO: If there are unsaved changes, ask if they should be
        #  saved, discarded or if the exit should be canceled. That
        #  popup will be its own scene. And that one may then exit the game.
        self.running = False
