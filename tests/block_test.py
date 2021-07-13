import math
import unittest
from core.blokus import pentagon

class TestBlock(unittest.TestCase):
    
    def setUp(self) -> None:
            sum_interior_angles = (5-2)*math.pi
            pent_angle = ((sum_interior_angles)/5)/2
            r=1.0
            ND = r * math.cos(pent_angle)
            ON = r * math.sin(pent_angle)
            BC = 2 * ND
            FC = BC * math.sin(pent_angle)
            BF = BC * math.cos(pent_angle)
            FO = r -  BF

            A = (-FC,FO)
            B = (0.0, r)
            C = (FC, FO)
            D = (ND, -ON)
            E = (-ND, -ON)
            self.pentagon = [A,B,C,D,E]


    def test_pentagon(self):
        p = pentagon(1.0)
        self.assertEqual(p[0], self.pentagon[0], msg="pent[0] should be eq")

