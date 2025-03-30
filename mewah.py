import pyglet,os,sys,time
from pyglet import shapes
from pyglet.graphics import Batch
from pyglet.gl import *



def resource_path(relative_path):
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = pyglet.window.Window(500,500,"meow :3 v0.2")    
batch = pyglet.graphics.Batch()
player = pyglet.media.Player()



counter = 0






background_image = pyglet.image.load(resource_path('images/background.png'))
background_sprite = pyglet.sprite.Sprite(background_image,-5,0, batch=batch)
background_sprite.scale = 0.5


music_sound = pyglet.media.load(resource_path('sounds/music.mp3'), streaming=False)

ui_open = pyglet.media.load(resource_path('sounds/ui_open.mp3'), streaming=False)
ui_close = pyglet.media.load(resource_path('sounds/ui_close.mp3'), streaming=False)


cat_image = pyglet.image.load(resource_path('images/cat.png'))
cat_sprite = pyglet.sprite.Sprite(cat_image,150,150, batch=batch)
cat_sprite.scale = 0.5
cat_sprite.opacity = 0



catAnim_image = pyglet.image.load(resource_path('images/catAnim.gif'))
catAnim_sprite = pyglet.sprite.Sprite(catAnim_image,120,120, batch=batch)
catAnim_sprite.scale = 1.5
catAnim_sprite.opacity = 255

tut_click_image = pyglet.image.load(resource_path('images/tut_click.png'))
tut_click_sprite = pyglet.sprite.Sprite(tut_click_image,172,300, batch=batch)




button_width = 200
button_height = 200


buttonx = 160
buttony = 160


button = shapes.Rectangle(buttonx, buttony, button_width, button_height, color=(50, 225, 30), batch=batch)


button.opacity = 0


music_sound.play()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if buttonx <= x <= buttonx + button_width and buttony <= y <= buttony + button_height:
        
        wah_sound = pyglet.media.load(resource_path('sounds/wah.mp3'), streaming=False)
        wah_sound.play()
        
        tut_click_sprite.opacity = 0
        cat_sprite.opacity = 255

        global counter
        counter += 1
        print(f"Cat clicked {counter} times")
        

        catAnim_sprite.opacity = 0

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.L:

        window.set_size(850, 500)
        ui_open.play()


@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.L:
        window.set_size(500, 500)
        ui_close.play()



achivements_menu_image = pyglet.image.load(resource_path('images/achivement_menu.png'))
achivements_menu_sprite = pyglet.sprite.Sprite(achivements_menu_image,488,0, batch=batch)


achivement_1 = pyglet.image.load(resource_path('images/the_beginning.png'))
achivement_1_sprite = pyglet.sprite.Sprite(achivement_1,600,350, batch=batch)

well_made = pyglet.image.load(resource_path('images/completed.png'))
well_made_sprite = pyglet.sprite.Sprite(well_made,763,420, batch=batch)

# ejemplo de como se hacen funciones en gameloop

def update_well_made_opacity(dt):
    if counter > 0:
        well_made_sprite.opacity = 255
    else:
        well_made_sprite.opacity = 0

pyglet.clock.schedule_interval(update_well_made_opacity, 0.1)



#para que funcione pon en cmd: pyinstaller --onefile --add-data "images/*;images/" --add-data "sounds/*;sounds/" --noconsole mewah.py

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()


