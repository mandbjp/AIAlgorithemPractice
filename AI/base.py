#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Base(object):
    def __init__(self, ttt, t):
        self.t = t
        self.ttt = ttt
        self.order_count = 0
        self.order_time = 0

    def play(self):
        raise Exception("Override this!")


