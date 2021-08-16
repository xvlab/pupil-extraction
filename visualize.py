import matplotlib.pyplot as plt
import json

filename = "Thy1-GCaMP6s-M5-k-0624-2.json"
with open(filename) as file:
    square = json.load(file)

print(type(square))
print(square.keys())
# plt.plot(square.keys(), square.items())
# plt.show()
