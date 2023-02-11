
# coding: utf-8

# # Assignment 1: Dino Fun World
# 
# ### Assignment Description
# 
# You, in your role as a data explorer and visualizer, have been asked by the administrators of a small amusement park in your hometown to answer a few questions about their park operations. The dataset that they provided for you to perform the requested analysis includes the movement and communication data captured from the park attendees' apps during one weekend (Friday, Saturday, and Sunday).
# 
# The administrators would like you to answer four relatively simple questions about the park activities on the day in question. These questions all deal with park operations and can be answered using the data provided.
# * **Question 1:** What is the most popular attraction to visit in the park?
# 
# 
# * **Question 2:** What ride (note that not all attractions are rides) has the second longest average visit time?
# 
# 
# * **Question 3:** Which Fast Food offering has the fewest visitors?
# 
# 
# * **Question 4:** Compute the Skyline of number of visits and visit time for the park's ride, and report the rides that appear in the Skyline. (Note: Your answer should be three points, which can be given in any order.)
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
# Using the provided data, answer the four questions that the administrators have asked.
# 
# ### Submission Directions for Assignment Deliverables
# 
# This assignment will be auto-graded. We recommend that you submit this assignment. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment with the output of the code in the cell's display area. The display area should contain only your answer to the question with no extraneous information, or else the answer may not be picked up correctly. 
# 
# Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed. (Graded Cell and PartID comments must be in the same line for proper execution of code.)
# 
# Please execute each cell in Jupyter Notebook before submitting.
# 
# **NOTE:**  For each question, be sure to add your code in the exact cell that has the comment ```"# Graded Cell, PartID:______"```. If you add extra cells or split your code up into multiple cells, ensure you are adding your output print( ) statement in the cell containing the comment with regard to each question.
# 
# 
# **NOTE:**  If you lose the partId that is mentioned in the first line of each cell with regard to each question, use the syntax described below to add it.
# * Question 1: # Graded Cell, PartID : NDnou 
# * Question 2: # Graded Cell, PartID : FXGHp
# * Question 3: # Graded Cell, PartID : KALua
# * Question 4: # Graded Cell, PartID : B0LUP
# 

# ### Question 1: 
# What is the most popular attraction to visit in the park?
# 
# **Note:** Your output should be the name of the attraction.

# In[2]:


# Graded Cell, PartID: NDnou
# your code here


# ### Question 2: 
# 
# What ride (note that not all attractions are rides) has the second longest average visit time?
# 
# **Note:** Your output should be the name of the ride.
# 

# In[4]:


# Graded Cell, PartID: FXGHp
# your code here


# ### Question 3:
# 
# Which Fast Food offering in the park has the fewest visitors?
# 
# **Note:** Your output should be the name of the fast food offering.

# In[5]:


# Graded Cell, PartID: KALua
# your code here


# ### Question 4:
# 
# Compute the Skyline of number of visits and visit time for the park's ride and report the rides that appear in the Skyline. 
# 
# **Note:** Remember that in this case, higher visits is better and lower visit times are better. Your output should be formatted as a list of names of the rides in the Skyline. Your output should be three points, which can be given in any order(example output : ['Ride 1','Ride 2','Ride 3'] )
# 

# In[6]:


# Graded Cell, PartID: B0LUP
# your code here

