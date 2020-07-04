# -*- coding: utf-8 -*-
from .menu_generator import MenuGenerator
from chicken.view.output import Output
from chicken.view.input import Input
from .user_select_generator import UserSelectGenerator
from .payment_generator import PaymentGenerator
from .order_generator import OrderGenerator


class ChickenController:
    def __call__(self, *args, **kwargs):
        print("init menu")

        mg = MenuGenerator()
        mg.menu_generator()

        op = Output()
        # op.menu(mg.get_display())

        usg = UserSelectGenerator()
        pg = PaymentGenerator()
        og = OrderGenerator()
        ip = Input()

        input_number = -1
        while input_number != 0:
            input_number = ip.user_select(usg.default_display())

            if input_number == 1:
                print(usg.menu_choice_message)
                print(op.menu(mg.get_display()))
                select_menu = ip.menu_select()
                select_count = ip.menu_count()
                og.set_order(mg.get_menu(select_menu), select_count)
                print(og.get_orders())
            elif input_number == 2:
                if len(og.get_orders()) < 1:
                    print("선택한 상품이 없습니다.")
                    continue
                print(usg.payment_choice_message)
                print(pg.get_display())
                select_payment = ip.payment_select()
                payed = pg.pay(og.get_orders(), select_payment)
                op.payment(og.get_orders(), payed)
                og.clear_order()
            else:
                raise Exception(self.error_not_select)

