# -*- coding: utf-8 -*-


class UserSelectGenerator:

    default_display_list = ["1. 상품선택", "2. 결제하기", "0. 종료"]
    error_not_select = "잘못 선택 하였습니다."

    menu_choice_message = "메뉴를 선택해 주세요."
    payment_choice_message = "결제를 선택해 주세요."

    def default_display(self):
        return self.default_display_list

