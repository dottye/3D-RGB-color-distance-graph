# 3D-RGB-color-distance-graph
3D visualization of RGB color distance. Uses R, G, B values in range (0, 255) as x, y, z values. 

By utilizing tkinter's colorchooser, users can easily pick as many colors as they would like to see graphed.
Colorchooser also allows for easy use of both the hex color and RGB color, as colorchooser.askcolor() returns 
a list of two items: a 3-tuple of RGB values in float, and a string of the hex color code. 
Both values are used to help the users visualize color distance in RGB colorspace. 

First, the colors chosen show up on the main tkinter GUI as colored labels along with the integer RGB values. 
The int RGB values are appended to three separate r_vals[], g_vals[], and b_vals[] lists, and hex values are also 
appended to the hex_colors[] list. 

Next, the matplotlib and its Axes3D are used to graph r_vals[], g_vals[], and b_vals[] in a 3D scatterplot using the associated hex_colors[] list as the points' colors in the graph. The 3D graph is displayed once the user finishes choosing the colors they would like to see graphed and clicks the 'Draw 3D Graph' button. 
