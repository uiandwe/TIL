# -*- coding: utf-8 -*-


class Winner:

    def final_medal(self, cars):
        d = {}
        max_distinct = 0
        for car in cars:
            if car.distance in d.keys():
                d[car.distance].append(car)
            else:
                max_distinct = max(max_distinct, car.distance)
                d[car.distance] = [car]

        return d[max_distinct]
