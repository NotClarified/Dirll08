from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):  # self 자세한 설명 생략, 생성이된 객체를 가리키는 변수
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass  # 더미함수를 넣어서 world의 update가 한번에 진행될 수 있도록 더미 코드 작성


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Large_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 750), 599
        self.image = load_image('ball41x41.png')
        self.frame = 0

    def update(self):
        self.y -= random.randint(5, 30)
        if self.y < 71 or self.y == 71:
            self.y = 71

    def draw(self):
        self.image.clip_draw(self.frame, 0, 100, 100, self.x, self.y, 41, 41)


class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 750), 599
        self.image = load_image('ball21x21.png')
        self.frame = 0

    def update(self):
        self.y -= random.randint(5, 30)
        if self.y < 61 or self.y == 61:
            self.y = 61

    def draw(self):
        self.image.clip_draw(self.frame, 0, 100, 100, self.x, self.y, 21, 21)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global large_ball, small_ball
    global world
    running = True
    world = []

    grass = Grass()  # grass 객체 변수, Grass() 클래스
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    large_ball_int = random.randint(1, 19)
    small_ball_int = 20 - large_ball_int
    large_ball = [Large_Ball() for j in range(large_ball_int)]
    small_ball = [Small_Ball() for k in range(small_ball_int)]
    world += large_ball
    world += small_ball


def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
# initialization code
reset_world()

# game main loop code
while running:
    handle_events()  # 핸들과 업데이트가 일종의 게임 로직
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
