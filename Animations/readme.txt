Today we are going to learn how to create animations in Python, to make our visualizations much more impressive and we can give more information in a visual and impressive way. In this post, you will learn how to create all kinds of animations in Python from simple animations to animated graphics like bar chart races.

How animations work in Python ??

To create our animations we will use the FuncAnimation function inside matplolib. A fundamental aspect to be able to create our animations is to understand that this function does not create whole animations with interpolation, but simply limits itself to creating animations from a series of graphics that we pass to it.

To create animations in Python we will use the animation functions of the matplotlib module. Therefore, creating an animation is very simple and similar to creating graphics with matplotlib. We simply have to create:

fig : it is the object that we will use to paint our graph.
func : it is a function that must return the state of the animation for each frame. Basically what we have to do is create a function that returns all the graphs. Following the example of the line chart animation mentioned above, the function must return, in the first iteration a linechart with the first year, in the second interaction a linechart with the first two years, and so on for all the years.
interval: is the delay in milliseconds between the different frames of the animation.
frames: the number of images on which to base the chart. This will depend on how many “states” the animation has. If we have an animation with data in 5 different states (let’s imagine, 5 years), the number of frames will be 5, while if we have data of 100 years, the number of frames will be 100.
With these arguments, we can create all kinds of animations. Now, this can be somewhat complex (especially the update part), so I would always recommend first creating the graphic that we want and, from that, generating the animation.
