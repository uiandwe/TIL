# -*- coding: utf-8 -*-
import abc


class Weapon:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def doAttack(self):
        raise NotImplementedError("doAttack")


class Knife(Weapon):
    def doAttack(self):
        print("attack knife!!")

class Sword(Weapon):
    def doAttack(self):
        print("Attack Sword!!")

class Character(object):
    def __init__(self, weapon):
        super(Character, self).__init__()
        self.weapon = weapon

    def setWeapon(self, weapon):
        self.weapon = weapon

    def doAttack(self):
        self.weapon.doAttack()

c = Character(Knife())
c.doAttack()
c.setWeapon(Sword())
c.doAttack()
