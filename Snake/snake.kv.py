#:kivy 1.9.1

<SnakeGame>:
    ball: pong_ball

    Apple:
        id: pong_ball
        center: self.parent.center

<Apple>:
    size: 10,10
    canvas:
        Color:
            rgb: 1,0,0
        Ellipse:
            pos: self.pos
            size: self.size

<PongPaddle>:
    size: 25, 200
    canvas:
        Rectangle:
            pos:self.pos
            size:self.size
