import pygame

class MecaJoy():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Initialize joystick
        pygame.joystick.init()
        # Check if joystick is connected
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count == 0:
            print("Joystick not found")
        else:
            # Get joystick instance
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
    
    def check_driver(self):
        return self.joystick_count > 0

    def check_plugged(self):
        return self.joystick_count > 0
    
    def get_info(self):
        if self.joystick_count > 0:
            # Get joystick axes positions
            axes = [self.joystick.get_axis(i) for i in range(self.joystick.get_numaxes())]
            # Get joystick button states
            buttons = [self.joystick.get_button(i) for i in range(self.joystick.get_numbuttons())]
            # Combine axes and button data
            data = axes + buttons
            return data
        else:
            return None
