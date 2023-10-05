from pico2d import *

# Game object class here



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
def reset_world():
    global running
    running = True

def update_world():
    pass

def render_world():
    clear_canvas()
    update_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events() # 핸들과 업데이트가 일종의 게임 로직
    update_world()
    render_world()
    delay(0.05)


# finalization code

close_canvas()
