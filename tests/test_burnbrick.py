"""
Unit test for slcore/brick.py, slcore/tools/burnbrick.py.
"""
from unittest import TestCase
from slcore.tools.burnbrick import burn_brick
from slcore.brick import Brick

import os


class TestBurnBrick(TestCase):
    def test_burn_brick_cpu(self):
        b = Brick('cpu', ['arm,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/cpuparameters.yaml'
        ))

    def test_burn_brick_intc(self):
        b = Brick('intc', ['intc,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/intcparameters.yaml'
        ))

    def test_burn_brick_ram(self):
        b = Brick('ram', ['ram,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/ramparameters.yaml'
        ))

    def test_burn_brick_timer(self):
        b = Brick('timer', ['timer,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/timerparameters.yaml'
        ))

    def test_burn_brick_flash(self):
        b = Brick('flash', ['flash,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/flashparameters.yaml'
        ))

    def test_burn_brick_mmio(self):
        b = Brick('mmio', ['mmio,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/mmioparameters.yaml'
        ))

    def test_burn_brick_serial(self):
        b = Brick('serial', ['serial,generic'])
        burn_brick(b, os.path.join(
            os.path.dirname(__file__),
            'brickparameters/serialparameters.yaml'
        ))
