from enum import Enum

class Order:
    __slots__ = ["state", "shipping_info"]

    def __init__(self):
        self.state = None
        self.shipping_info = None

    # 대기 중 일때만 배송 정보 변경 가능
    def change_shipping_info(self, new_shipping_info):
        if not self.is_shipping_change_able():
            raise AssertionError("can't change shipping in "+self.state)
        self.shipping_info = new_shipping_info

    def is_shipping_change_able(self):
        return self.state == OrderState.PAYMENT_WAITING or self.state == OrderState.PREPARING


class OrderState(Enum):
    PAYMENT_WAITING : 0
    PREPARING : 1
    SHIPPED : 2
    DELIVERING : 3
    DELIVERY_COMPLETED : 4



