# # Introduction to Visualizing Categorical Data with Bokeh

# ## What is Bokeh?
# #### Bokeh is a open-sourced visulazation library for Python, specificaly know for its interactivity. While any visualization works well for simple charts, Bokeh looks extremely modern, and doesn't have to be modified in order to have a "clean" look. As this is a declaritive language, it is also is extremely user friendly, especially when it comes to interactivity of visuaizations. It also allows users to output visuaizations, not only in the Jupyter Lab environment, but directly to web browsers a well. 
# 
# #### The downfall to Bokeh is that some graph interactions must be written in JavaScript, however for simple visualizations like those found in this tutorial, Java Script knowledge is not necessary.
# 
# #### Since I really wanted to learn an interactive library without spending weeks getting into the specifics, I chose Bokeh. 
# 

# ## The Data 
# #### This dataset contains mushroom samples from 23 species of gilled mushrooms drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Although this data set is quite old, when it comes to mushroom species of North America, not a lot has actually changed. The data included in this data set is all categorical, which lends itself mainly to pie charts and bars charts, both of which are showed below. Can you tell if a mushroom in North America is poisonous just by its color? What about its smell?
# 
# #### As we dive in, I would urge you not to judge the poisonous mushrooms too harshly... they are all fungis!

# ## Pie Charts and Bar Charts
# 
# #### Since we are dealing with _only_ categorical data, specifially frequency of categorical data, our simplest options lie with pie chats and bar charts. Visualizations like line charts, scatteplots, and box plots can only be used with quantitative variables.  
# 
# 

![mushroms (1)](https://user-images.githubusercontent.com/79933773/139507231-4ede9236-1f55-460b-9d1d-35a2a8adc542.png)
# https://www.instagram.com/p/32J4AFSgh8/