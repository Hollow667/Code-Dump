
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty,ListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line
from kivy.modules.touchring import*

class BouncyBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class BallBounce(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def start_ball(self):
        self.ball.center = self.center
        self.ball.velocity = 0, 0

    def update(self, dt):
        self.ball.move()

        #bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        #bounce ball off left or right
        if (self.ball.x < self.x) or (self.ball.x > self.width):
            self.ball.velocity_x *= -1

    def on_touch_move(self, touch):
        if touch.x > self.ball.x - 10 and touch.x < self.ball.x:
            self.ball.velocity_x += 5
        if touch.x < self.ball.x + 10 and touch.x > self.ball.x:
            self.ball.velocity_x -= 5
        if touch.y > self.ball.y - 10 and touch.y < self.ball.y:
            self.ball.velocity_y += 5
        if touch.y < self.ball.y + 10 and touch.y > self.ball.y:
            self.ball.velocity_y -= 5

    def slowdown(self, dt):
        #Slows down ball gradually
        if self.ball.velocity_x > 0:
            self.ball.velocity_x -= 1
        if self.ball.velocity_x < 0:
            self.ball.velocity_x += 1
        if self.ball.velocity_y > 0:
            self.ball.velocity_y -= 1
        if self.ball.velocity_y < 0:
            self.ball.velocity_y += 1


class BounceApp(App):
    def build(self):
        game = BallBounce()
        game.start_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_interval(game.slowdown, 10.0 / 60.0)
        return game


if __name__ == '__main__':
    BounceApp().run()

