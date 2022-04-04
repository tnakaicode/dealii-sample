import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import argparse
from linecache import getline, clearcache

sys.path.append(os.path.join("./"))
from src.base_occ import dispocc

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

from OCC.Core.gp import gp_Pnt, gp_Vec, gp_Dir

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--inp", dest="inp", default="./dealii-33/slide.inp")
    parser.add_argument("--pxyz", dest="pxyz",
                      default=[0.0, 0.0, 0.0], type=float, nargs=3)
    opt = parser.parse_args()
    print(opt, argvs)

    obj = dispocc()
    data = open(opt.inp, "r").readlines()
    n0, n1, i0, i1, i2 = [int(v) for v in data[0].split()]
    for idx, xyz in enumerate(data[1:n0 + 1]):
        n, x, y, z = [float(v) for v in xyz.split()]
        pnt = gp_Pnt(x, y, z)
        obj.display.DisplayShape(pnt)
        print(idx, n)
    obj.ShowOCC()
