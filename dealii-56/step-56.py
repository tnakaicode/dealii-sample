import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import vtk
import meshio
from optparse import OptionParser

sys.path.append(os.path.join("../"))
from base import plot2d
from src.Plot3D import Plot3DSurf

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--dir", dest="dir", default="./")
    parser.add_option("--num", dest="num", default=3, type="int")
    parser.add_option("--flg", dest="flg", default=1, type="int")
    parser.add_option("--pxyz", dest="pxyz",
                      default=[0.0, 0.0, 0.0], type="float", nargs=3)
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    obj = plot2d()#Plot3DSurf()
    obj.create_tempdir(flag=opt.flg)
    num = opt.num
    ext = "_{:03d}.vtk".format(num)
    dt0 = meshio.read('./sol/solution-000.vtk')
    dt1 = meshio.read('./sol/solution-001.vtk')
    dt2 = meshio.read('./sol/solution-002.vtk')
    print(dt1.points.shape)
    obj.contourf_tri(dt0.points[:, 0], dt0.points[:, 1], dt0.points[:, 2])
    obj.contourf_tri(dt1.points[:, 0], dt1.points[:, 1], dt1.points[:, 2])
    obj.contourf_tri(dt2.points[:, 0], dt2.points[:, 1], dt2.points[:, 2])
    