
# coding: utf-8

# # Assignment 3: Dino Fun World Analysis
# 
# ### Assignment Description
# 
# The administrators of Dino Fun World, a local amusement park, have asked you, one of their data analysts, to perform three data analysis tasks for their park. These tasks will involve understanding, analyzing, and graphing attendance data for three days of the park's operations that the park has provided for you to use. They have provided the data in the form of a database.
# 
# Part 1: The park's administrators would like your help understanding the different paths visitors take through the park and different rides they visit. In this mission, they have selected five (5) visitors at random whose check-in sequences they would like you to analyze. For now, they would like you to construct a distance matrix for these five visitors. The five visitors have the IDs: 165316, 1835254, 296394, 404385, and 448990.
# 
# Part 2: The park's administrators would like to understand the attendance dynamics at each ride (note that not all attractions are rides). They would like to see the minimum (non-zero) attendance at each ride, the average attendance over the whole day, and the maximum attendance for each ride in a parallel coordinate plot.
# 
# Part 3: In addition to a parallel coordinate plot, the administrators would like to see a scatterplot matrix depicting the minimum, average, and maximum attendance for each ride as above.
# 
# **Hint:** Use “%matplotlib inline” to display the graph on the Jupyter Notebook(To allow the grader to identify the PartID, add the cell magic after the Graded Cell and PartID comments.).
# 
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
#     - The attractions in the park by their corresponding AttractionID, Name, Region, Category, and type. Regions are from the VAST Challenge map such as Coaster Alley, Tundra Land, etc. Categories include Thrill rides, Kiddie Rides, etc. Type is broken into Outdoor Coaster, Other Ride, Carussel, etc.
#     - Fields: AttractionID, Name, Region, Category, type
# `sequences`:
#     - The check-in sequences of visitors. These sequences list the position of each visitor to the park every five minutes. If the visitor has not entered the part yet, the sequence has a value of 0 for that time interval. If the visitor is in the park, the sequence lists the attraction they have most recently checked in to until they check in to a new one or leave the park.
#     - Fields: visitorID, sequence
#     
# Using the data provided, perform the required analyses and create the distance matrix, parallel coordinate plot, and scatterplot matrix.
# 
# 
# ### Submission Directions for Assignment Deliverables
# 
# This assignment will be auto-graded. We recommend that you use Jupyter Notebook in your browser to complete and submit this assignment. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment with the output of the code in the cell's display area. The display area should contain only your answer to the question with no extraneous information or else the answer may not be picked up correctly.
# 
# Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed. (Graded Cell and PartID comments must be in the same line for proper execution of code.)
# 
# Please execute each cell in Jupyter Notebook before submitting.
# 
# **NOTE:**  For each question, be sure to add your code in the exact cell that has the comment ```"# Graded Cell, PartID:______"```. If you add extra cells or split your code up into multiple cells, ensure you are adding your output print( ) statement and the chart in the cell containing the comment with regard to each question.
# 
# 
# **NOTE:**  If you lose the partId that is mentioned in the first line of each cell with regard to each question, use the syntax described below to add it.
# * Question 1: # Graded Cell, PartID : IiXwN 
# * Question 2: # Graded Cell, PartID : 8S2jm
# * Question 3: # Graded Cell, PartID : KHoww
# 

# ### Question 1: 
# Create a distance matrix suitable for use in hierarchical clustering of the checkin sequences of the 5 specified visitors.
# 
# Your distance function should count the number of dissimilarities in the sequences without considering any other factors. The distance matrix should be reported as a dictionary of dictionaries (eg. {1: {2:0, 3:0, 4:0}, 2: {1:0, 3:0, ...}, ...}).
# 

# In[29]:


# Graded Cell, PartID: IiXwN
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
#from pandas.plotting import mosaic

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
#165316, 1835254, 296394, 404385, and 448990
c.execute("Select visitorID, sequence from sequences where visitorID in (165316, 1835254, 296394, 404385, 448990)")
seq = c.fetchall()

seq_df = pd.DataFrame.from_records(seq, columns = ['Visitors', 'Sequence'])
seq_df['sequence_list'] = seq_df['Sequence'].apply(lambda s: s.split("-"))

final_dict = {}
counter = 0
for val in range(5):
        final_dict[seq[val][0]] = {}
        for val2 in range(5):
            counter = 0
            if val != val2:
                for val3 in range(len(seq_df['sequence_list'][0])):
                    if seq_df['sequence_list'][val][val3] != seq_df['sequence_list'][val2][val3]:
                        counter+=1
                final_dict[seq[val][0]][seq[val2][0]] = counter
print(final_dict)


# final_dict = {}
# currSeqVal = []
# #i is visitorid
# #j is sequenceVal
# visitorSet = {165316, 1835254, 296394, 404385, 448990}

# for i in range(5):
#     for j in seq_df['Visitors'][i]:
#         #currSeqVal.append(seq_df['sequence_list'][j])
#         new_dict = {}
#         for x in visitorSet:
#             if x not in new_dict:
#                 new_dict[x] = 0

#         new_dict.remove(seq_df['Visitors'][i])
#         if seq_df['sequence_list'][j] != seq_df['Visitors'][i] and seq_df['sequence_list'][j] in visitorSet:
            
#             #final_dict[visitorId] +=1
#             currSeqVal = []

# return final_dict
        
        
        

#print distance result

### Question 2:  
Create and display a Parallel Coordinate Plot displaying the minimum, average, and maximum attendance for each ride in the park.

For this question, display a Parallel Coordinate Plot in the notebook and print the data used to create a Parallel Coordinate Plot as a dictionary of dictionaries (eg: { 1 : { name : 'Ride1', min : 1, max : 3, avg : 2 }, 2 :{ name : 'Ride2', min : 1, max : 3, avg : 2 } ... })

**Note:** Not all attractions are rides.
# In[31]:


# Graded Cell, PartID: 8S2jm
c.execute("SELECT AttractionID, Name FROM attraction where category LIKE '%ride%'")
rides = c.fetchall()
allAttractions = pd.DataFrame.from_records(rides, columns = ['AttractionId', 'Name'])

c.execute("Select visitorID, sequence from sequences")
seqList = c.fetchall()
seqList_df = pd.DataFrame.from_records(seqList, columns=['visitor', 'sequence'])
seqList_df['sequencesList'] = seqList_df['sequence'].apply(lambda s: s.split("-"))

dictionary = {}
colName = "AttendanceOrder"
for x in range(len(rides)):
    seqList_df[colName] = seqList_df['sequencesList'].apply(lambda val: [1 if int(i) == int(rides[x][0]) else 0 for i in val])
    attendance = np.sum(seqList_df[colName].values.tolist(), axis = 0)
    attendance = attendance[np.nonzero(attendance)]
    maxAttendance = np.max(attendance)
    minAttendance = np.min(attendance)
    avgAttendance = np.mean(attendance)
    rangeDict = {"min": minAttendance, "avg": avgAttendance, "max": maxAttendance}
    dictionary[rides[x][1]] = rangeDict

finalRes = pd.DataFrame.from_dict(dictionary, orient="index")
finalRes = finalRes.reset_index()
finalRes.columns = ['ride' if x=='index' else x for x in finalRes.columns]

pd.plotting.parallel_coordinates(finalRes, 'ride')
plt.show()
print(finalRes)


# ### Question 3:
# Create and display a Scatterplot Matrix displaying the minimum, average, and maximum attendance for each ride in the park.
# 
# **Note:** This is a different view into the same data as the previous part. While you work on these plots, consider the different things that each chart says about the data.

# In[28]:


# Graded Cell, PartID: KHoww
pd.plotting.scatter_matrix(finalRes)
plt.show()
print(finalRes)

