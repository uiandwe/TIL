# -*- coding: utf-8 -*-
class Input:
    input_car_name_message = "차의 이름을 입력, (콤마로 구분)"
    error_input_not_car_name_length_message = "{}자 이하로 입력해 주세요."

    input_track_count_message = "트랙 횟수를 입력"
    error_input_input_message = '숫자만 입력'

    def input_car_names(self):
        print(self.input_car_name_message)

        try:
            names = input()
            return [name.strip() for name in names.split(",")]
        except Exception as e:
            print(e)
            raise Exception(self.error_input_not_car_name_length_message)

    def input_track_count(self):
        print(self.input_track_count_message)

        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(self.error_input_input_message)
