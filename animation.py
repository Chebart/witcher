'''
Created on 14 июн. 2020 г.

@author: Артем
'''

# Класс анимации
# Animation class
class Animation():
    def __init__(self, sprites, time=100):
        self.sprites = sprites
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
    def update(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites):
                self.frame = 0
    def get_sprite(self):
        return self.sprites[self.frame]