# -*- coding: utf-8 -*-

import random

from view.input_view import InputView
from domain.random_power_generator import RandomPowerGenerator
from domain.racing_track import RacingTrack
from domain.lap_counter import LapCounter
from controller.racing_game import RacingGame


def get_racing_track():
    car_names = InputView.get_car_names()
    random_power_generator = RandomPowerGenerator(random.randrange(1, 10))
    return RacingTrack(car_names, random_power_generator)


def get_lap_count():
    total_lap = InputView.get_total_laps()
    return LapCounter(total_lap)

if __name__ == '__main__':
    racing_track = get_racing_track()
    lap_counter = get_lap_count()
    racing_game = RacingGame(racing_track, lap_counter)
    racing_game()

