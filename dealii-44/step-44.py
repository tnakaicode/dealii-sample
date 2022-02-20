import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import vtk
import meshio
from vtk import vtkUnstructuredGridReader
from optparse import OptionParser

sys.path.append(os.path.join("../"))
from base import plot2d

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--dir", dest="dir", default="./")
    parser.add_option("--file", dest="file", default="./sol/solution-3d-000.vtu")
    parser.add_option("--pxyz", dest="pxyz",
                      default=[0.0, 0.0, 0.0], type="float", nargs=3)
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    px = np.linspace(-1, 1, 100) * 100 + 50
    py = np.linspace(-1, 1, 200) * 100 - 50
    mesh = np.meshgrid(px, py)

    reader = vtkUnstructuredGridReader()
    reader.SetFileName(opt.file)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()
    #mesh = meshio.read("./sol/solution-3d-0.vtu")
