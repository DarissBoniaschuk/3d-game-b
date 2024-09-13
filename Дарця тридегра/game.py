from direct.showbase.ShowBase import ShowBase
from map import Mapmanager
from hero import Hero
from direct.gui.OnscreenText import OnscreenText

class Game (ShowBase):
    def __init__(self):
        super().__init__()

        self.camera.setPos(10, 0, 0)     
        self.camLens.setFov(90)
        self.land = Mapmanager()
        x,y = self.land.loadland('land.txt')
        self.hero = Hero((x//2,y//2,7), self.land)
        self.skybox()



    def skybox(self):
        self.sky = loader.loadModel('skybox/skybox.egg')
        self.sky.setScale(500)
        self.sky.setBin('background', 1)
        self.sky.setLightOff()
        self.sky.reparentTo(render)








game = Game()
game.run()


