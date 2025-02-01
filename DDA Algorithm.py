# Import necessary library
from matplotlib import pyplot as plt

def dda(x0, y0, x1, y1):
    dx = abs(x1 - x0)  # Calculate change in x
    dy = abs(y1 - y0)  # Calculate change in y
    max_steps = max(dx, dy)  # Maximum steps needed

    xincrement = dx / max_steps if max_steps != 0 else 0
    yincrement = dy / max_steps if max_steps != 0 else 0

    x = float(x0)
    y = float(y0)

    xcoordinates = []
    ycoordinates = []

    for _ in range(max_steps + 1):  # Ensure the last point is plotted
        xcoordinates.append(round(x))  # Round to nearest pixel
        ycoordinates.append(round(y))
        print(f"x: {round(x)}, y: {round(y)}")  # Print coordinates
        
        x += xincrement
        y += yincrement

    # Plot the line
    plt.plot(xcoordinates, ycoordinates, marker='o', color="red", linestyle="-")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("DDA Line Drawing Algorithm")
    plt.grid()
    plt.show()

# Take user input for coordinates
print("Input first point coordinate:")
x0 = int(input("x0: "))
y0 = int(input("y0: "))

print("Input second point coordinate:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))

# Call the function
dda(x0, y0, x1, y1)
