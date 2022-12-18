import os
import DLRetrieve
import Hyperlink

directory = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(directory):
    if file.endswith('.xlsx'):
        target = file
        break

InputArray = Hyperlink.GetValues(file)

Dictionary = DLRetrieve.DLStore(InputArray)

Hyperlink.Assign(Dictionary, InputArray, file)
DLRetrieve.DriverQuit()