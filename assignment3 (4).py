#!/usr/bin/env python
# coding: utf-8

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

# ![title](mushroms.png)

# https://www.instagram.com/p/32J4AFSgh8/

# ### First, lets import Bokeh! In the Jupyer Lab environment, we simply need to pass the following: 

# In[1]:


import bokeh


# ### Then, let's import important python libraries like numpy, pandas, and math. Then, we'll import our first Bokeh libraries!

# In[2]:


import numpy as np
import pandas as pd
from math import pi

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from bokeh.transform import dodge


# ### Now, we'll read in our mushroom data set, clean up our values to  make them more understandable, and pick out just the columns we'll need for our viualizations. 

# In[3]:


df = pd.read_csv("/home/jovyan/work/resources/assignment3/assets/mush.csv")
pd.set_option('display.max_columns', None)
df['class'].replace(to_replace="p",value="poisonous", inplace=True)
df['class'].replace(to_replace="e",value="edible", inplace=True)

df['cap-color'].replace(to_replace="n",value="brown", inplace=True)
df['cap-color'].replace(to_replace="b",value="buff", inplace=True)
df['cap-color'].replace(to_replace="c",value="cinnamon", inplace=True)
df['cap-color'].replace(to_replace="g",value="gray", inplace=True)
df['cap-color'].replace(to_replace="r",value="green", inplace=True)
df['cap-color'].replace(to_replace="p",value="pink", inplace=True)
df['cap-color'].replace(to_replace="u",value="purple", inplace=True)
df['cap-color'].replace(to_replace="e",value="red", inplace=True)
df['cap-color'].replace(to_replace="w",value="white", inplace=True)
df['cap-color'].replace(to_replace="y",value="yellow", inplace=True)

df['cap-shape'].replace(to_replace="b",value="bell", inplace=True)
df['cap-shape'].replace(to_replace="c",value="conical", inplace=True)
df['cap-shape'].replace(to_replace="x",value="convex", inplace=True)
df['cap-shape'].replace(to_replace="f",value="flat", inplace=True)
df['cap-shape'].replace(to_replace="k",value="knobbed", inplace=True)
df['cap-shape'].replace(to_replace="s",value="sunken", inplace=True)

df['cap-surface'].replace(to_replace="f",value="fibrous", inplace=True)
df['cap-surface'].replace(to_replace="g",value="grooves", inplace=True)
df['cap-surface'].replace(to_replace="y",value="scaly", inplace=True)
df['cap-surface'].replace(to_replace="s",value="smooth", inplace=True)
    
df['spore-print-color'].replace(to_replace="k",value="black", inplace=True)
df['spore-print-color'].replace(to_replace="n",value="brown", inplace=True)
df['spore-print-color'].replace(to_replace="b",value="buff", inplace=True)
df['spore-print-color'].replace(to_replace="h",value="chocolate", inplace=True)
df['spore-print-color'].replace(to_replace="r",value="green", inplace=True)
df['spore-print-color'].replace(to_replace="o",value="orange", inplace=True)
df['spore-print-color'].replace(to_replace="u",value="purple", inplace=True)
df['spore-print-color'].replace(to_replace="w",value="white", inplace=True)
df['spore-print-color'].replace(to_replace="y",value="yellow", inplace=True)

df['population'].replace(to_replace="a",value="abundant", inplace=True)
df['population'].replace(to_replace="c",value="clustered", inplace=True)
df['population'].replace(to_replace="n",value="numerous", inplace=True)
df['population'].replace(to_replace="s",value="scattered", inplace=True)
df['population'].replace(to_replace="v",value="several", inplace=True)
df['population'].replace(to_replace="y",value="solitary", inplace=True)

df['habitat'].replace(to_replace="g",value="grasses", inplace=True)
df['habitat'].replace(to_replace="l",value="leaves", inplace=True)
df['habitat'].replace(to_replace="m",value="meadows", inplace=True)
df['habitat'].replace(to_replace="p",value="paths", inplace=True)
df['habitat'].replace(to_replace="u",value="urban", inplace=True)
df['habitat'].replace(to_replace="w",value="waste", inplace=True)
df['habitat'].replace(to_replace="d",value="woods", inplace=True)

df['odor'].replace(to_replace="a",value="almond", inplace=True)
df['odor'].replace(to_replace="l",value="anise", inplace=True)
df['odor'].replace(to_replace="c",value="creosote", inplace=True)
df['odor'].replace(to_replace="y",value="fishy", inplace=True)
df['odor'].replace(to_replace="f",value="foul", inplace=True)
df['odor'].replace(to_replace="m",value="musty", inplace=True)
df['odor'].replace(to_replace="n",value="none", inplace=True)
df['odor'].replace(to_replace="p",value="pungent", inplace=True)
df['odor'].replace(to_replace="s",value="spicy", inplace=True)

df=df.loc[:,['class','cap-shape','cap-surface',"cap-color","odor","bruises","population","spore-print-color","habitat"]]

df.head()


# ### Different from some othe visualization libraries in Python, in order to show any sort of output on the screen we must first specify that was want to actually see the output inside of the Jupyter Notebook environment itself.

# In[4]:


# The figure will be right in the Jupyter Notebook
output_notebook()


# ### Next, lets take a look at how many mushrooms species in the data set are poisonous, and how many aren't. 
# #### Let's clean up the data and create a dataframes of class, frequency, angle needed for the pie chart, and the color we want each class.

# In[5]:


#How many mushrooms in the data set are poisoness and how many are edible 
not_pois, pois = df['class'].value_counts()

#Create a dictionary 
x = {
    'Edible': not_pois,
    'Poisonous': pois}

#Pick colors!
chart_colors = ['#44e5e2', '#e29e44']

#Create a dictionary to be used in making the visualization 
data = pd.Series(x).reset_index(name='value').rename(columns={'index':'class'})

#Get the proper angle of the pie "slice"
data['angle'] = data['value']/data['value'].sum() * 2*pi  
#Add the colors to the dataframe
data['color'] = chart_colors[:len(x)]
data


# #### To easily compare one categorical variable, with only two unique values, we are going to make a simple pie chart.

# In[6]:


# The "figure()" command is used to set the size, title, and whether you want some interactivity or not 
# let's title it p for poisonous! Or Pie! Or Pi!
p = figure(plot_height=500, title="Poisonous Vs Edible Mushrooms", toolbar_location=None,
           tools="hover", tooltips="@class: @value", x_range=(-0.5, 1.0))   #Tools!

# with the "wedge()" command, we are specifying that we want a pie chart, and then specifying the size of the "wedges" 
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='class', source=data)


#Since we are dealing with a pie chart, we don't want any axis, axis labels, or grid lines
p.axis.axis_label=None
p.axis.visible=False 
p.grid.grid_line_color = None

print("Hover Over It!")
#SHOW!
show(p)


# #### Okay... so only slightly over half of the species in the data set are edible... Interesting, but not telling us much yet...
# 

# See the documentation on interactivity here:
#     https://docs.bokeh.org/en/latest/docs/user_guide/tools.html

# ### Now lets, look at the distribution of mushrooms by their cap colors 
# #### Let's clean up the data a little bit by creating a list of cap colors and another list of their corespsonding frequencies, and combining them all into a pandas series. 

# In[7]:


#Lets clean up the data a little bit
cap_color_count = df['cap-color'].value_counts()
m_height = cap_color_count.values.tolist() #Provides numerical values
cap_color_count.axes #Provides row labels
cap_color = cap_color_count.axes[0].tolist() 

#Let's pick colors corresponding to the list
colors=["#82553e","#b8b0ad","red","yellow","#f0eeed","#f0dc82","pink","#e55444","green","purple"]

#Lets tie all that data together in a data frame
datacolor = pd.Series(cap_color_count).reset_index(name='value').rename(columns={'index':'color'})


# ### Let's specify that we want a vertical bar graph to show us frequency of cap color

# In[8]:


#We want a x axis of cap_color, a title, and no interactivity 
p = figure(x_range=cap_color, plot_height=500, title="Cap Colors",
           toolbar_location=None, tools="")

#vbar() specifies it will be a vertical bar chart, with the specified colors from above. As you can see from below, there is no "y" only "top." 
#"top" in this case is actally the "y" variable, a bit confusing at first, but once you know this, its smooth sailing 
p.vbar(x=cap_color, top=cap_color_count, color=colors, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)


# #### So there are A LOT of brown mushrooms.. Can't say I'm suprised. 

# ### Let's dive into nested categories with Bokeh.
# #### I want to be able to see if there are any definitive ways to tell if a mushrooms is edible. So, I'l start by looking at color. Are green mushrooms ALWAYS poisonous? Can you eat all the red ones? Again, I'm going to start by cleaning up the data

# In[9]:


poisonous = [] #Poisonous color cap list
edible = []    #Edible color cap list

# for every color, lets determine how many are poisonous and how many are edible, and create a dictionary with that knowledge
for color in cap_color:
    size = len(df[df['cap-color'] == color].index)
    edibles = len(df[(df['cap-color'] == color) & (df['class'] == 'edible')].index)
    edible.append(edibles)
    poisonous.append(size-edibles)

data = {'color' : cap_color,
        'poisonous'   : poisonous,
        'edible'   : edible}

source = ColumnDataSource(data=data)


# #### In order to create a nested bar chart, we need to specify one figure, but with two different bars for each color - one for poisonous mushrooms and one for edible ones. These will then show up side by side. Again, I'm adding some interactivity to the figure, to get a better idea of exact numbers. 

# In[10]:


TOOLTIPS = [
    ("Edible", "@edible"),
    ("Poisonous", "@poisonous"),
]

p = figure(x_range=cap_color, y_range=(0, 1400), plot_height=500, title="Poisonousness by Color!",
           toolbar_location=None, tools="hover",tooltips=TOOLTIPS)


p.vbar(x=dodge('color', -0.25, range=p.x_range), top='edible', width=0.2, source=source,
       color="#44e5e2", legend_label="Edible")

p.vbar(x=dodge('color',  0.0,  range=p.x_range), top='poisonous', width=0.2, source=source,
       color="#e29e44", legend_label="Poisonous")
show(p)


# #### This still doesn't really tell us much. The only suprising thing is that all the green and purple mushrooms from this data set are _edible_. 

# ### Since color doesn't show us any difinitive patterns, let try it with odor. I've copied the code from above, but modified it in order to show poisonousness by odor. 

# In[11]:


odor_count = df['odor'].value_counts()
m_height = odor_count.values.tolist() #Provides numerical values
odor_count.axes #Provides row labels
odor = odor_count.axes[0].tolist() 

poisonous = [] #Poisonous color cap list
edible = []    #Edible color cap list

#Again, we'll create a dictionary with odor now, and poisonous vs edible samples
for smell in odor:
    size = len(df[df['odor'] == smell].index)
    edibles = len(df[(df['odor'] == smell) & (df['class'] == 'edible')].index)
    edible.append(edibles)
    poisonous.append(size-edibles)

data = {'odor' : odor,
        'poisonous'   : poisonous,
        'edible'   : edible}

source = ColumnDataSource(data=data)
source
TOOLTIPS = [
    ("Edible", "@edible"),
    ("Poisonous", "@poisonous"),
]

#Creating the same figure as above, but with odor
p = figure(x_range=odor, y_range=(0, 3500), plot_height=500, title="Dont Eat The Smelly Ones!",
           toolbar_location=None, tools="hover", tooltips=TOOLTIPS)

p.vbar(x=dodge('odor', -0.25, range=p.x_range), top='edible', width=0.2, source=source,
       color="#44e5e2", legend_label="Edible")

p.vbar(x=dodge('odor',  0.0,  range=p.x_range), top='poisonous', width=0.2, source=source,
       color="#e29e44", legend_label="Poisonous")
show(p)


# #### Only 3.4 % of mushrooms with no smell are poisonous... Would you risk it?
# ### Take some to experment with other variables, using the code above, or code from scratch and create brand new visualizations. Either way, there is so mushroom for more exploration! 

# In[12]:


from zipfile import ZipFile

# create a ZipFile object
zipObj = ZipFile('gonzalez.zip',"w")
# Add multiple files to the zip
zipObj.write('assignment3.ipynb')
zipObj.write('mushroms.png')
zipObj.write('assets/mush.csv')
# close the Zip File
zipObj.close()


# In[ ]:





# In[ ]:





# In[ ]:




