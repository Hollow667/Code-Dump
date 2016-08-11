
import kivy
kivy.require("1.0.6")

from kivy.app import App
from kivy.uix.widget import Widget
from random import randint

class Battle(Widget):
    def roll(self):
        while True:
            player_sk = self.sk_player.value + randint(1,6)
            monster_sk = self.sk_monster.value + randint(1,6)
            if player_sk != monster_sk: break
        return player_sk  > monster_sk

    def attack(self):
        if self.roll():
            self.hp_monster.value -= 2
            if self.hp_monster.value < 0 : self.hp_monster.value=0
        else:
            self.hp_player.value -= 2
            if self.hp_player.value < 0 : self.hp_player.value=0

    def battle(self):
        while self.hp_player.value > 0 and self.hp_monster.value >0:
            self.attack()

class BattleApp(App):
    def build(self):
        return Battle()



if __name__ == "__main__":
    BattleApp().run()