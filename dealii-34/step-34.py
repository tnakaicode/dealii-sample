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
from src.Plot3D import Plot3DSurf

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

    obj = Plot3DSurf()
    obj.create_tempdir(flag=opt.flg)
    num = opt.num
    ext = "_{:03d}.vtk".format(num)
    dt1 = meshio.read('./sol/2d_boundary_solution' + ext)
    dt2 = meshio.read('./sol/3d_boundary_solution' + ext)
    print(dt1.points.shape)
    print(dt1.point_data.keys())
    print(obj.tempname)
    #obj.contourf_tri(dt1.points[:, 0], dt1.points[:, 1], dt1.points[:, 2])
    obj.contourf_tri_facecolor(
        dt1.points[:, 0], dt1.points[:, 1], dt1.points[:, 2], dt1.point_data["alpha"])
    obj.SavePng(obj.tempname + "_2d.png")
    obj.contourf_tri_facecolor(
        dt2.points[:, 0], dt2.points[:, 1], dt2.points[:, 2], dt2.point_data["alpha"])
    obj.SavePng(obj.tempname + "_3d.png")
    
