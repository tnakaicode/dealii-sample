import numpy
import matplotlib.pyplot as plt
import vtk

# The source file
file_name = "./sol/solution-129.vtu"

# Read the source file.
reader = vtk.vtkXMLUnstructuredGridReader()
reader.SetFileName(file_name)
reader.Update()  # Needed because of GetScalarRange
output = reader.GetOutput()
potential = output.GetPointData().GetArray("potential")
print(output)
print(output.GetPointData().GetArray(0))
#gridreader = vtk.vtkXMLPUnstructuredGridReader()
# gridreader.SetFileName('whatever.pvtu')
# gridreader.Update()
#vtkOut = gridreader.GetOutput()
#vtkOut = gridreader.GetOutput()
#vtkData = vtkOut.GetPoints().GetData()
# coords = numpy.array([vtkData.GetTuple3(x)
#                      for x in range(vtkData.GetNumberOfTuples())])
vtkData = output.GetPoints().GetData()
coords = numpy.array([vtkData.GetTuple3(x)
                      for x in range(vtkData.GetNumberOfTuples())])


plt.triplot(coords[:, 0], coords[:, 1])
plt.gcf().set_size_inches(16, 8)
plt.gca().set_aspect('equal')
plt.savefig('meshPython1.png', bbox_inches='tight')
plt.gca().set_xlim((5e5, 3e6))
plt.gca().set_ylim((6e5, 1e6))
plt.savefig('meshPython2.png', bbox_inches='tight')
