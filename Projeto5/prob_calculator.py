import copy
import random

class Hat:
    def __init__(self, **balls):
        balls = dict(balls)
        self.contents = []
        for ball in balls:
            for i in range(balls[ball]):
                self.contents.append(ball)
        self.copia=self.contents.copy()

    def draw(self, number):
        self.contents=self.copia.copy()
        if len(self.contents) < number:
            return self.contents
        
        drawn_balls = []
        contents = self.contents
        
        for i in range(number):
            ball = random.choice(contents)
            drawn_balls.append(ball)
            contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    c = 0
    for i in range(num_experiments):
        retiradas = hat.draw(num_balls_drawn)
        retiradas_dict = {}
        for bola in retiradas:
            retiradas_dict[bola] = retiradas_dict.get(bola, 0) + 1

        quantidade_correta = True
        for cor, quantidade in expected_balls.items():
            if retiradas_dict.get(cor, 0) < quantidade:
                quantidade_correta = False
                break

        if quantidade_correta:
            c += 1

    probabilidade = c / num_experiments
    return probabilidade