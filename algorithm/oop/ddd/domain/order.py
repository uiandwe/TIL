from enum import Enum
from functools import reduce


class Order:
    __slots__ = ["state", "shipping_info", "order_lines", "total_amounts"]

    def __init__(self, order_lines):
        self.state = None
        self.shipping_info = None
        self.order_lines = []
        self.total_amounts = None
        # order_lines의 총 합 계산
        self._set_order_lines(order_lines)

    # 대기 중 일때만 배송 정보 변경 가능
    def change_shipping_info(self, new_shipping_info):
        if not self.is_shipping_change_able():
            raise AssertionError("can't change shipping in "+self.state)
        self.shipping_info = new_shipping_info

    def is_shipping_change_able(self):
        return self.state == OrderState.PAYMENT_WAITING or self.state == OrderState.PREPARING

    def _set_order_lines(self, order_lines):
        self._verify_at_least_one_or_more_order_lines(order_lines)
        self.order_lines = order_lines
        self._calculate_total_amounts()

    def _verify_at_least_one_or_more_order_lines(self, order_lines):
        if order_lines is None or len(order_lines) <= 0:
            raise AssertionError("no order lines")

    def _calculate_total_amounts(self):
        self.total_amounts = Money(sum(reduce(lambda x: x.price in self.order_lines)))


class OrderState(Enum):
    PAYMENT_WAITING : 0
    PREPARING : 1
    SHIPPED : 2
    DELIVERING : 3
    DELIVERY_COMPLETED : 4


class OrderLine:
    __slots__ = ["product", "price", "quantity", "amounts"]

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.amounts = self._calculateAmounts()

    def _calculateAmounts(self):
        return self.price * self.quantity


class Money:
    def __init__(self, price):
        self.price = price