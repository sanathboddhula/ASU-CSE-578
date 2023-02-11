
# coding: utf-8

# # Assignment 5: Geographic Data Analysis
# 
# ### Assignment Description
# 
# In this assignment, you will be using a database of geographic data provided for you in the PySal library to create two plots: a choropleth map and a proportional symbol map. 
# 
# In addition to these two plots, you will compute the value of Moran's I for this data.
# 
# **Hint:** Use “%matplotlib inline” to display the graph on the Jupyter Notebook(To allow the grader to identify the PartID, add the cell magic after the Graded Cell and PartID comments.).
# 
# ### Directions
# 
# The data for this assignment includes the United States' lower 48 states. In addition to the state-by-state data, the dataset contains shape files for each state that you can use to create the choropleth and proportional symbol maps.
# 
# Using the data provided, perform the required analyses and create the requested maps.
# 
# ### Submission Directions for Assignment Deliverables
# 
# This assignment will be auto-graded. We recommend that you use Jupyter Notebook in your browser to complete and submit this assignment. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment in the cell's display area. The display area should contain only your answer with no extraneous information, or else the answer may not be picked up correctly.
# 
# Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed. (Graded Cell and PartID comments must be in the same line for proper execution of code.)
# 
# Please execute each cell in Jupyter Notebook before submitting.
# 
# **NOTE:**  For each question, be sure to add your code in the exact cell that has the comment ```"# Graded Cell, PartID:______"```. If you add extra cells or split your code up into multiple cells, ensure you are adding your output print( ) statement and the chart in the cell containing the comment with regard to each question.
# 
# 
# **NOTE:**  If you lose the partId that is mentioned in the first line of each cell with regard to each question, use the syntax described below to add it.
# * Question 1: # Graded Cell, PartID : CkcsR 
# * Question 2: # Graded Cell, PartID : FqNRm
# * Question 3: # Graded Cell, PartID : CtQYv

# ### Question 1:  
# Using the PySal Data, create a choropleth path of the United States that depicts the per capita income of each US state in 2009.
# 
# **Note:** The PySal and GeoPandas libraries both contain utility functions that may make this task easier.

# In[3]:


# Graded Cell, PartID: CkcsR
import pandas as pd
import geopandas as gpd
import pysal as ps
import matplotlib.pyplot as plt



#usjoin.csv
per_cap = pd.read_csv(ps.examples.get_path('usjoin.csv'))

#us48.hsx
us_df = gpd.read_file(ps.examples.get_path("us48.shx"))

us_df['per_capita'] = list(per_cap["2009"])

plt.rcParams["figure.figsize"] = (30,8)

us_df.plot(column="per_capita")

plt.show()


# ### Question 2:
# Again using the PySal Data, create a proportional symbol map showing a dot at the centroid of each state that is scaled to the per capita income of each US state in 2009.
# 
# **Notes:** The demonstration notebook for this unit contains code that performs a similar task and may be a useful reference for your assignment.
# 
# 

# In[4]:


# Graded Cell, PartID: FqNRm
us_df['cent'] = us_df.centroid
cents = list(us_df['cent'])
fin_df = pd.DataFrame({'y':[cents[i].y for i in range(len(cents))],                    'x':[cents[i].x for i in range(len(cents))],                    'data':list(us_df['per_capita'])})

base = us_df.plot(color = 'white', edgecolor='black')
plt.rcParams["figure.figsize"] = (30,8)
fin_df.plot(kind = 'scatter', x = 'x', y = 'y', s=fin_df['data']*0.01, ax=base)
plt.show()


# ### Question 3:
# Using the same data, compute the value of Moran's I for the per capita income of each US state in 2009 using Rook Continuity. Report the value of I rounded to 4 decimal places (i.e. x.XXXX)
# 
# **Notes:** Again, the PySal and GeoPandas libraries may contain useful utility functions.

# In[11]:


# Graded Cell, PartID: CtQYv
#from pysal.explore import esda
#from pysal.lib import weights,examples
from pysal.weights import Rook

tmp = us_df['per_capita']
weight = Rook.from_shapefile(ps.examples.get_path("us48.shx"))
morans = ps.Moran(tmp, weight, two_tailed=False)
print(round(morans.I, 4))

