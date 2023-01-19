import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, frames, pos, group):
        super().__init__(group)

        self.moving = Moving()
        self.moving.x = False
        self.moving.y = False
        self.frames = frames
        self.sheet = pygame.image.load(sheet).convert_alpha()
        self.image = self.get_image(0, 0, 16, 16, 3, 'black')
        self.rect = self.image.get_rect(center=pos)

        self.animations = {'down': [], 'up': [], 'left': [], 'right': [], 'idle': []}
        self.state = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.010
        self.import_animations()

        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_animations(self):
        for index, animation in enumerate(self.animations):
            surf_list = []
            for frame in range(self.frames):
                if animation == 'idle':
                    image = self.get_image(0, 0, 16, 16, 3, 'black')
                else:
                    image = self.get_image(frame, index, 16, 16, 3, 'black')

                surf_list.append(image)

            self.animations[animation] = surf_list

    def get_image(self, frame, colunm, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((colunm * 16), (frame * 16), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.state = 'up'
            self.moving.y = True
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.state = 'down'
            self.moving.y = True
        else:
            self.direction.y = 0
            self.moving.y = False


        if keys[pygame.K_d]:
            self.direction.x = 1
            self.state = 'right'
            self.moving.x = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.state = 'left'
            self.moving.x = True
        else:
            self.direction.x = 0
            self.moving.x = False

    def move(self, delta_time):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.position.x += self.direction.x * self.speed * delta_time
        self.rect.centerx = self.position.x

        self.position.y += self.direction.y * self.speed * delta_time
        self.rect.centery = self.position.y

    def animate(self):
        animation = self.animations[self.state]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        if self.moving.x or self.moving.y:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = animation[0]
        self.rect = self.image.get_rect(center=self.rect.center)


    def update(self, delta_time):
        self.input()
        self.move(delta_time)
        self.animate()

class Moving:
    def __init__(self):
        self.x = False
        self.y = False
