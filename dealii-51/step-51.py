import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import vtk
import meshio
import argparse

sys.path.append(os.path.join("../"))
from base import plot2d

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--num", dest="num", default=3, type=int)
    parser.add_argument("--flg", dest="flg", default=1, type=int)
    parser.add_argument("--pxyz", dest="pxyz",
                      default=[0.0, 0.0, 0.0], type=float, nargs=3)
    opt = parser.parse_args()
    print(opt, argvs)

    obj = plot2d()
    obj.create_tempdir(flag=opt.flg)
    num = opt.num
    ext = "-{:03d}.vtk".format(num)
    dt1 = meshio.read('./sol/solution-adaptive-face-q1' + ext)
    dt2 = meshio.read('./sol/solution-adaptive-q1' + ext)
    dt3 = meshio.read('./sol/solution-global-face-q1' + ext)
    dt4 = meshio.read('./sol/solution-global-q1' + ext)
    print(dt1.points.shape)
    obj.contourf_tri(dt1.points[:, 0], dt1.points[:, 1], dt1.points[:, 2])
    obj.contourf_tri(dt2.points[:, 0], dt2.points[:, 1], dt2.points[:, 2])
    obj.contourf_tri(dt3.points[:, 0], dt3.points[:, 1], dt3.points[:, 2])
    obj.contourf_tri(dt4.points[:, 0], dt4.points[:, 1], dt4.points[:, 2])
