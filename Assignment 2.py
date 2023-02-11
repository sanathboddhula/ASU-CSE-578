
# coding: utf-8

# # Assignment 2: Graphing Dino Fun World
# 
# ### Assignment Description
# 
# Impressed by your previous work, the administrators of Dino Fun World have asked you to create some charts that they can use in their next presentation to upper management. The data used for this assignment will be the same as the data used for the previous assignment.
# 
# The administrators would like you to create four graphs:
# 
# Chart 1: A pie chart depicting visits to thrill ride attractions.
# 
# Chart 2: A bar chart depicting total visits to food stalls.
# 
# * Please query attractions with Category equal to "Food".
# 
# Chart 3: A line chart depicting attendance at the newest ride, Atmosfear over the course of the day.
# 
# * For this question, use data from the table "sequences". You can assume that all activity sequences are aligned by time (i.e., the first node of all sequences occurred at the same time) and are of the same length.
# 
# * You only need to consider the first 16 hours of records in the sequences, which is considered the open hours of the park in one day. Specifically, because an activity sequence from the "sequences" table was updated/recorded every 5 minutes, you need to extract the first 192 items (16h * 60m / 5m = 192).
# 
# * Your data list (which will be printed) must be in the format of tuple list (or list of lists). The first item in tuples is irrelevant, but you can put in some meaningful information. The second item is the count of visits at that moment. For example, your output should look like this (in Python syntax; not relevant to the correct answer): [ (0, 0), (1, 7), (2, 3), …, (190, 4), (191, 5) ].
# 
# Chart 4: A box-and-whisker plot depicting total visits to the park's Kiddie Rides.
# 
# * The to-be-printed, the  data list must be ordered by AttractionID (a field in the table "attraction").
# 
# **Hint:**  Use “%matplotlib inline” to display the graph on the Jupyter Notebook(To allow the grader to identify the PartID, add the cell magic after the Graded Cell and PartID comments.).
# 
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
#     - The attractions in the park by their corresponding AttractionID, Name, Region, Category, and type. Regions are from the VAST Challenge map such as Coaster Alley, Tundra Land, etc. Categories include Thrill rides, Kiddie Rides, etc. Type is broken into Outdoor Coaster, Other Ride, Carousel, etc.
#     - Fields: AttractionID, Name, Region, Category, type
# `sequences`:
#     - The check-in sequences of visitors. These sequences list the position of each visitor to the park every five minutes. If the visitor has not entered the part yet, the sequence has a value of 0 for that time interval. If the visitor is in the park, the sequence lists the attraction they have most recently checked in to until they check in to a new one or leave the park.
#     - Fields: visitorID, sequence
#     
# Using the provided data, create the four visualizations that the administration requested: the pie chart, bar chart, line chart, and box-and-whisker plot.   
# 
# ### Submission Directions for Assignment Deliverables
# 
# This assignment will be auto-graded. We recommend that you use Jupyter Notebook in your browser to complete and submit this assignment. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment with the output of the code in the cell's display area. The display area should contain only your answer to the question with no extraneous information, or else the answer may not be picked up correctly.
# 
# Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed. (Graded Cell and PartID comments must be in the same line for proper execution of code.)
# 
# Please execute each cell in Jupyter Notebook before submitting.
# 
# **NOTE:**  For each question, be sure to add your code in the exact cell that has the comment ```"# Graded Cell, PartID:______"```. If you add extra cells or split your code up into multiple cells, ensure you are adding your output print( ) statement and the chart in the cell containing the comment with regard to each question.
# 
# 
# **NOTE:**  If you lose the partId that is mentioned in the first line of each cell with regard to each question, use the syntax described below to add it.
# * Question 1: # Graded Cell, PartID : gtMqY 
# * Question 2: # Graded Cell, PartID : 9Ocyl
# * Question 3: # Graded Cell, PartID : 0zcEV
# * Question 4: # Graded Cell, PartID : zdzaT

# ### Question 1 : 
# Make a Pie Chart of the visits to Thrill Ride attractions.
# 
# **Note:** For this question, display the pie chart in the notebook and print the data used to create the pie chart as a list of lists (ex: [['Ride 1', 10], ['Ride 2', 100], ...])
# 

# In[3]:


# Graded Cell, PartID: gtMqY
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_filename = 'readonly/dinofunworld.db'
conn = sqlite3.connect(db_filename)
c = conn.cursor()
c.execute("Select attraction.name, count(*) from attraction, checkin where attraction.attractionid = checkin.attraction and lower(attraction.Category) Like '%thrill%' Group by attraction.name Order By count(attraction.name)")

counts = c.fetchall()
rides = pd.DataFrame.from_records(counts, columns = ['Name', 'value'])
plt.pie(rides['value'], labels = rides['Name'], shadow = False)
plt.axis('equal')
plt.show()
print(counts)


# ### Question 2 : 
# Make a bar chart of total visits to food stalls.
# 
# **Note:** For this question, display the bar chart in the notebook and print the data used to create the bar chart as a list of lists (ex: [['Stall 1', 10], ['Stall 2', 50], ...])
# 

# In[4]:


# Graded Cell, PartID: 9Ocyl
c.execute("Select attraction.name, Count(*) from checkin, attraction where checkin.attraction = attraction.attractionid and lower(category) like'%food%' group by attraction.name")
foodStallVisits = c.fetchall()

foodFrame = pd.DataFrame.from_records(foodStallVisits, columns = ['Food Stall', '# Visits'])
plt.bar(range(len(foodFrame['Food Stall'])), foodFrame['Food Stall'])
plt.xticks([])
plt.show()
print(foodStallVisits)


# ### Question 3 : 
# Make a line chart of attendance at Atmosfear every five minutes.
# 
# **Note:** For this question, display the line chart in the notebook and print the data used to create the chart as a list of lists (ex: [['Stall 1', 10], ['Stall 2', 50], ...]) or tuple lists (ex: [('Stall 1, 10),('Stall 2', 50), ...]
# 
# The first item in tuples is irrelevant, but you can put in some meaningful information. The second item is the count of visits at that moment. For example, your output should look like this (in Python syntax; not relevant to the correct answer): [ (0, 0), (1, 7), (2, 3), …, (190, 4), (191, 5) ].

# In[6]:


# Graded Cell, PartID: 0zcEV
#how many visits to atmostfear y 
#required visits for every 5 minutes x 

c.execute("Select attractionId from attraction where attraction.name = 'Atmosfear'")
attractionid = c.fetchall()[0][0] #8

val = [[i, 0] for i in range(192)]

c.execute("Select sequence from sequences")
sequences = c.fetchall()

for x in sequences:
    temp = x[0]
    x = temp.split('-')
    for i in range(192):
        if(x[i] == str(attractionid)):
            val[i][1] += 1

yAxis = [val[i][1] for i in range(192)]
xAxis = [i for i in range(192)]
#take first 192 values in sequence 0 - 0 - 8 - 0  
#create list of lists of size 192 (index, # visitors)
#print(attendanceCount)

#xAxis = list(zip(*attendanceCount))[0]
#yAxis = list(zip(*attendanceCount))[1]

plt.plot(xAxis, yAxis)
plt.show()

print(val)


# ### Question 4: 
# Make a box plot of total visits to rides in the Kiddie Rides category.
# 
# **Note:** For this question, display the box plot in the notebook and print the number of visits to each ride as a list (ex: [3, 4, 5, 6, ...])

# In[7]:


# Graded Cell, PartID: zdzaT
c.execute("Select attraction.name, Count(*) from attraction, checkin where checkin.attraction = attraction.attractionid and lower(category) like '%kiddie rides%' group by attraction.attractionid")
kiddieVisits = c.fetchall()
# visitCount = []
# for i in kiddieVisits:
#     visitCount.append(i[1])
kiddieFrame = pd.DataFrame.from_records(kiddieVisits, columns=['Kiddie Ride', 'Count'])
plt.boxplot(kiddieFrame['Count'])
plt.show()

visitCount = list(zip(*kiddieVisits))[1]
print(list(visitCount))

