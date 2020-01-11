# -*- coding: utf-8 -*-

from oop.coupon.product import Product
from oop.coupon.coupon import Coupon
from oop.coupon.limit_coupon import LimitCoupon

if __name__ == '__main__':
    product = Product(1000)
    coupon = Coupon(500)

    discount_amount = coupon.calculate_discounted_price(product)

    print(discount_amount)

    limit_coupon = LimitCoupon(300, 500)
    discount_amount = limit_coupon.calculate_discounted_price(product)

    print(discount_amount)

    limit_coupon = LimitCoupon(400, 600)
    discount_amount = limit_coupon.calculate_discounted_price(product)

    print(discount_amount)
