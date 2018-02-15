import sys
import sdl2
import sdl2.ext

#http://ipafont.ipa.go.jp/
#http://ipafont.ipa.go.jp/node26#jp
#https://stackoverflow.com/questions/24709312/pysdl2-renderer-or-window-surface-for-handling-colors-and-text
def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("PySDL2で日本語の描画をする", size=(800, 600))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    fontManager = sdl2.ext.FontManager(font_path='./res/IPAexfont00301/ipaexg.ttf', size=58, color=sdl2.ext.Color(255, 0, 0))
    spriteFactory = sdl2.ext.SpriteFactory(renderer=renderer)
    text = spriteFactory.from_text("PySDL2で日本語の描画をする。",fontmanager=fontManager)
    renderer.copy(text, dstrect= (0,0,text.size[0],text.size[1]))

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        renderer.clear(sdl2.ext.Color(0, 0, 0))
        renderer.copy(text, dstrect=(0, 240, text.size[0], text.size[1]))
        renderer.present()
        window.refresh()

if __name__ == "__main__":
    sys.exit(run())
