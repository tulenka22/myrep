import time
from tkinter import PhotoImage, Tk, Canvas

class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def collided_left(coords1, coords2):
    return coords1.x1 < coords2.x2 and coords1.x2 > coords2.x1 and coords1.y1 < coords2.y2 and coords1.y2 > coords2.y1

class Game:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.sprites = []
        self.running = True
        self.canvas_height = 600
        self.canvas_width = 800

    def mainloop(self):
        while self.running:
            for sprite in self.sprites:
                sprite.move()
            self.root.update()
            time.sleep(0.01)

class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates

class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        super().__init__(game)
        self.image = game.canvas.create_image(x, y,
                image=photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)

class StickFigureSprite(Sprite):
    def __init__(self, game):
        super().__init__(game)
        # Здесь добавьте код для создания изображения персонажа и его начальных координат.
        
    def move(self):
       # Здесь добавьте логику движения персонажа.
       for sprite in self.game.sprites:
           if isinstance(sprite, DoorSprite) and collided_left(self.coords(), sprite.coords()):
               sprite.open_door()  # Открыть дверь при столкновении.
               print("Вы победили!")  # Сообщение о победе.
               sprite.endgame=True   # Отметить дверь как конечную.
               break

class DoorSprite(Sprite):
    def __init__(self, game, photo_image_closed, photo_image_open, x, y, width, height):
        super().__init__(game)
        self.photo_image_closed = photo_image_closed
        self.photo_image_open = photo_image_open
        self.image = game.canvas.create_image(x, y,
                image=self.photo_image_closed, anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
    
    def open_door(self):
        # Изменить изображение двери на открытое.
        if not self.endgame:  # Проверка на то что дверь еще не открыта.
            self.game.canvas.itemconfig(self.image, image=self.photo_image_open)
            print("Дверь открыта!")

class MovingPlatformSprite(PlatformSprite):
    def __init__(self, game, photo_image, x_start, y_start, width, height):
        super().__init__(game, photo_image,x_start,y_start,width,height)
        self.direction = 1  # 1 для движения вправо; -1 для движения влево
        self.speed = 2

    def move(self):
        if (self.coordinates.x1 <= 0 and self.direction == -1) or (self.coordinates.x2 >= self.game.canvas_width and self.direction == 1):
            # Изменить направление при достижении края канваса
            self.direction *= -1
        
        dx = self.direction * self.speed
        
        # Обновление координат платформы
        new_x1 = self.coordinates.x1 + dx
        new_x2 = new_x1 + (self.coordinates.x2 - self.coordinates.x1)
        
        # Обновление координат и перемещение изображения на канвасе
        if new_x1 >= 0 and new_x2 <= self.game.canvas_width: 
            # Проверка на выход за границы канваса
            for i in range(len(self.game.sprites)):
                if isinstance(self.game.sprites[i], MovingPlatformSprite) and (self.game.sprites[i] == self): 
                    continue 
                else:
                    continue 
            
            # Перемещение платформы на канвасе
            for i in range(len(self.game.sprites)):
                if isinstance(self.game.sprites[i], MovingPlatformSprite) and (self.game.sprites[i] == self): 
                    continue 
                else:
                    continue 

            # Обновление координат платформы
            old_coords=self.coordinates 
            old_coords.x1=new_x1 
            old_coords.x2=new_x2 

# Инициализация игры и спрайтов...
g = Game()

# Создание платформ...
platform_img = PhotoImage(file="fon_and_plat/2плат.png")
platform_sprite_1 = PlatformSprite(g,
                                    platform_img,
                                    100,
                                    500,
                                    200,
                                    20)
g.sprites.append(platform_sprite_1)

# Создание движущихся платформ...
moving_platform_img = PhotoImage(file="fon_and_plat/2плат.png")
moving_platform_sprite_1 = MovingPlatformSprite(g,
                                                moving_platform_img,
                                                0,
                                                300,
                                                100,
                                                10)
g.sprites.append(moving_platform_sprite_1)

# Создание двери с изображениями закрытой и открытой...
door_closed_img = PhotoImage(file="fon_and_plat/close.png")
door_open_img = PhotoImage(file="fon_and_plat/open.png")
door_sprite_1 = DoorSprite(g,
                            door_closed_img,
                            door_open_img,
                            45,
                            30,
                            40,
                            35)
g.sprites.append(door_sprite_1)

# Создание персонажа...
stick_figure_sprite_1 = StickFigureSprite(g)
g.sprites.append(stick_figure_sprite_1)

g.mainloop()
