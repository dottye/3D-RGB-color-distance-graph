from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import colorchooser


def choose_color(root, rgb_colors, hex_colors):
    """
    colorchooser.askcolor() returns a python list of two items:
    a triplet (3-tuple) of rgb vals, and a string with the hex color.
    This function takes the list and assigns the tuple and string to
    individual variables.
    """

    color = colorchooser.askcolor()  # get the list: [(r, g, b), #hexcolor]
    rgb_float = color[0]
    hex = color[1]

    # truncate the floating point decimals by converting to ints.
    # reassign them to a new list since tuples cannot be modified.
    rgb_int = []
    for i in range(3):
        rounded = int(rgb_float[i])
        rgb_int.append(rounded)

    # append the list of rgb int vals to the whole list of rgb_colors
    # append the hex color to the whole list of hex_colors
    rgb_colors.append(rgb_int)
    hex_colors.append(hex)

    # set the text of the label to be the tuple and hex color
    # set the bg of label using hex color
    # and append it to the root window
    cp_text = tk.StringVar()
    label_cp = tk.Label(root, textvariable=cp_text)

    cp_text.set(rgb_int)
    label_cp.config(bg=hex)
    label_cp.pack(fill='x')


def draw_graph(rgb_colors, hex_colors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    r_vals = []
    g_vals = []
    b_vals = []
    for i in range(len(rgb_colors)):
        r_vals.append(rgb_colors[i][0])
        g_vals.append(rgb_colors[i][1])
        b_vals.append(rgb_colors[i][2])

    ax.scatter(r_vals, g_vals, b_vals, c=hex_colors)
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.set_zlim(0, 255)
    ax.set_xlabel('R-values')
    ax.set_ylabel('G-values')
    ax.set_zlabel('B-values')

    plt.show()

def main():
    rgb_colors = []
    hex_colors = []

    root = tk.Tk()
    root.title("3D Color Graph")
    root.minsize(100, 200)

    color_btn = tk.Button(root, text="Pick a color", width=20, pady=5, command=lambda: choose_color(root, rgb_colors, hex_colors))
    graph_btn = tk.Button(root, text="Draw 3D graph", width=20, pady=5, command=lambda: draw_graph(rgb_colors, hex_colors))

    color_btn.pack()
    graph_btn.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
