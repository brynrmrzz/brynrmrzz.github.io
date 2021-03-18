
# Just figured I would try importing a different modules since I had been unsuccseful in the past
from parsed_data import *
#Grab plotly 
import plotly.graph_objects as go
# This may or may not be necessarry depending on if you want to render the image or just show it in html
##import os


# Since I was testing the modules, and these are functions I have to call them first or else our go.figure object won't be able to actually obtain the list values
our_x_axis = render_years()
our_y_axis= render_total()

# I honestly I just copy and pasted this from plotly's docs
fig = go.Figure(data=[go.Bar(
    x= our_x_axis,
    y= our_y_axis,
    #except for this, this was  my touch
    marker_color='rgb(163, 88, 88)',
)])
# I still have not found how to properly update these values in our original call to fig so I updated the layout for the time being 
fig.update_layout(
    title_text='Total populations of lives in custody',
    paper_bgcolor="rgb(245, 245, 245)",
    plot_bgcolor = "rgb(227, 227, 227)",
    font=dict(
        family="Helvetica",
        size=18,
        color="black"
        ))


## You can use this in case you want to render the images, you can do this in PNG as well

#if not os.path.exists("graphapp/images/images"):
#     os.mkdir("graphapp/images")
#fig.write_image("images/fig1.jpeg")

## Otherwise this will render our graph interactively in html. 
fig.show()


