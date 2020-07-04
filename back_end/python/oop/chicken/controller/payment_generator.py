# -*- coding: utf-8 -*-
from chicken.domain.payment import Payment
from chicken.domain.count_discount import CountDiscount
from chicken.domain.cash_discount import CashDiscount


class PaymentGenerator(Payment):

    default_display_list = ["1. 상품선택", "2. 결제하기", "0. 종료"]
    error_not_select = "잘못 선택 하였습니다."

    payment_message = "주문한 메뉴 리스트"
    payment_choice_message = "결제를 선택해 주세요."

    def default_display(self):
        return self.default_display_list

    def pay(self, orders, select_payment):
        for order in orders:
            if order.count >= 10:
                order.set_discount(CountDiscount())
            if select_payment == 2:
                order.set_discount(CashDiscount())
        self.set_orders(orders)
        self.cal_total_amount()
        return self.get_total_amount()
