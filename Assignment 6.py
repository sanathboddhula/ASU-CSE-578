
# coding: utf-8

# # Assignment 6: Hierarchical Clustering
# 
# ### Assignment Description
# 
# As in your previous assignments, the administrators of the Dino Fun World theme park have asked you, one of their data analysts, to perform a data analysis task in order to help them administer the park. In this case, your task builds upon one of the tasks the administrators previously asked you to perform. In a prior task, you were asked to find the distance between a set of visitor trajectories using a simple edit distance algorithm and report the distances. For this task, you must construct and display a dendrogram of those distances. Again, the administrators of the park have provided a database which contains the information needed.
# 
# This assignment consists of only one task, which is to generate a dendrogram. Create this dendrogram using the trajectories of the visitors with the IDs: 165316, 1835254, 296394, 404385, and 448990. When performing clustering over the trajectories to inform the dendrogram, use an average distance over all points in the cluster.
# 
# **Hint:**  Use “%matplotlib inline” to display the graph on the Jupyter Notebook(To allow the grader to identify the PartID, add the cell magic after the Graded Cell and PartID comments.).
# ### Directions
# 
# The database provided by the park administration is formatted to be readable by any SQL database library. The course staff recommends the sqlite3 library. The database contains three tables, named 'checkin', 'attractions', and 'sequences'. The database file is named 'dinofunworld.db' and is available in the read only directory of the Jupyter Notebook environment (i.e., readonly/dinofunworld.db). It can also be accessed by selecting File > Open > readonly/dinofunworld.db.
# 
# The information contained in each of these tables is listed below:
# 
# `checkin`:
#     - The check-in data for all visitors for the day in the park. The data includes two types of check-ins: inferred and actual checkins.
#     - Fields: visitorID, timestamp, attraction, duration, type
# `attraction`:
#     - The attractions in the park by their corresponding AttractionID, Name, Region, Category, and type. Regions are from the VAST Challenge map such as Coaster Alley, Tundra Land, etc. Categories include Thrill rides, Kiddie Rides, etc. Type is broken into Outdoor Coaster, Other Ride, Carousel, etc.
#     - Fields: AttractionID, Name, Region, Category, type
# `sequences`:
#     - The check-in sequences of visitors. These sequences list the position of each visitor to the park. If the visitor has not entered the part yet, the sequence has a value of 0 for that time interval. If the visitor is in the park, the sequence lists are the most visited.
#     - Fields: visitorID, sequence
#     
# Using the data provided, create the dendrogram. (Note: If you are unsure of how to create a dendrogram, please refer to the "Jupyter Notebook Demonstration: Dendrograms" video provided in the Jupyter Notebook Assignment 6 section.)
# 
# ### Submission Directions for Assignment Deliverables
# 
# This assignment will be auto-graded. We recommend that you use Jupyter Notebook in your browser to complete and submit this assignment. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment in the cell's display area. The display area should contain only your answer with no extraneous information, or else the answer may not be picked up correctly.
# 
# Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed. (Graded Cell and PartID comments must be in the same line for proper execution of code.)
# 
# Please execute each cell in Jupyter Notebook before submitting.
# 
# **NOTE:**  For each question, be sure to add your code in the exact cell that has the comment ```"# Graded Cell, PartID:______"```. If you add extra cells or split your code up into multiple cells, ensure you are displaying your output in the cell containing the comment with regard to each question.
# 
# 
# **NOTE:**  If you lose the partId that is mentioned in the first line of each cell with regard to each question, use the syntax described below to add it.
# * Question 1: # Graded Cell, PartID : RLU7S 
# 

# ### Question 1:
# Create and display a dendrogram of the trajectories of the 5 visitors specified above. The clustering algorithm used to create the dendrogram should use the average distance between points in a cluster.

# In[5]:


# Graded Cell, PartID:RLU7S
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import sqlite3
db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
#165316, 1835254, 296394, 404385, and 448990
c.execute('Select visitorID, sequence from sequences where visitorID in (165316, 1835254, 296394, 404385, 448990)')
seq_all = c.fetchall()
seq_df = pd.DataFrame.from_records(seq_all, columns = ['visitors', 'sequences'])
seq_df['seq_list'] = seq_df['sequences'].apply(lambda s: [int(x) for x in s.split("-")])

x = np.matrix(seq_df['seq_list'].values.tolist())
links = linkage(x, 'centroid')

dendrogram(links, labels = seq_df['visitors'].values.tolist())
plt.show()


