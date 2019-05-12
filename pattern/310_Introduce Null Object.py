# -*- coding: utf-8 -*-
# null 검사를 널 객체에 위임

import abc


class Customer:
    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return self.name

    @abc.abstractmethod
    def isNull(self):
        return False

    @abc.abstractmethod
    def getPlan(self):
        return self.nullPlan()

    def nullPlan(self):
        print("customer")
        return True


class NullCustomer(Customer):

    def isNull(self):
        return True

    def getPlan(self):
        return self.nullPlan()

    def nullPlan(self):
        print("nullCustomer")
        return False


class Order():
    def __init__(self, customer=None):
        if customer:
            self.customer = Customer(customer)
        else:
            self.customer = None


class BillingPlan():
    def basic(self):
        print("billingPlan")
        return False


if __name__ == '__main__':

    # 기존 방법
    order = Order()
    if order.customer is not None:
        plan = BillingPlan.basic()
    else:
        nc = NullCustomer()
        plan = nc.getPlan()

    # null 패턴
    order = Order()
    customer = order.customer if order.customer != None else NullCustomer()
    plan = customer.getPlan()

    order = Order("주문")
    customer = order.customer if order.customer != None else NullCustomer()
    plan = customer.getPlan()


