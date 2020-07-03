# -*- coding: utf-8 -*-
class Output:
    def racing_grade(self, cars):
        print("=====================")
        for car in cars:
            print("{} : {}".format(car.name, car.distance))
        print("=====================")

    def correct_round_count(self, strike_count, ball_count):
        print("=====================")
        print("{} strike {} ball".format(strike_count, ball_count))
        print("=====================")

    def winner_announce(self, cars):
        print("=====================")
        print("우승 자동차")
        print("거리 : {}".format(cars[0].distance))
        for car in cars:
            print("{}".format(car.name))
        print("=====================")
