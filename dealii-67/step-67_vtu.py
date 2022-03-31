import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
import vtk
import argparse

sys.path.append(os.path.join("../"))
from base import plot2d

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default="./")
    parser.add_argument("--pxyz", dest="pxyz",
                      default=[0.0, 0.0, 0.0], type="float", nargs=3)
    opt = parser.parse_args()
    print(opt, argvs)

    gridreader = vtk.vtkXMLPUnstructuredGridReader()
    gridreader.SetFileName('./sol/solution_003.vtu')
    gridreader.Update()
    vtkOut = gridreader.GetOutput()
    vtkData = vtkOut.GetPoints().GetData()
    coords = np.array([vtkData.GetTuple3(x)
                       for x in range(vtkData.GetNumberOfTuples())])

    obj = plot2d()
    obj.axs.triplot(coords[:, 0], coords[:, 1])
    obj.SavePng()
