import pyglet
from pyglet import shapes
from pyglet.graphics import Batch
import os
import sys
import time

def resource_path(relative_path):
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

window = pyglet.window.Window(500,500,"meow :3 v0.2")    
batch = pyglet.graphics.Batch()
player = pyglet.media.Player()

background_image = pyglet.image.load(resource_path('images/background.png'))
background_sprite = pyglet.sprite.Sprite(background_image,-5,0, batch=batch)
background_sprite.scale = 0.5


music_sound = pyglet.media.load(resource_path('sounds/music.mp3'), streaming=False)




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

        catAnim_sprite.opacity = 0





to_store = pyglet.image.load(resource_path('images/to_store.png'))
to_store_sprite = pyglet.sprite.Sprite(to_store,440,10, batch=batch)




        


#para que funcione pon en cmd: pyinstaller --onefile --add-data "images/*;images/" --add-data "sounds/*;sounds/" --noconsole mewah.py

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()  

