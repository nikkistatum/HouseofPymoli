
# Dependencies and Setup
import pandas as pd
import numpy as np


# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)


#total number of players
totalplayers = len(purchase_data["SN"].unique())
totalplayers

#Run basic calculations to obtain number of unique items, average price,number of purchases,total revenue

#unique items
uniqueitems = len(purchase_data["Item ID"].unique())
uniqueitems

#number of purchases
numberpurchases = len(purchase_data["Purchase ID"].unique())
numberpurchases

#Total Revenue
totalrevenue = purchase_data["Price"].sum()
totalrevenue

#Average Price
averageprice = purchase_data["Price"].mean()
averageprice

#summary table
summarytable = pd.DataFrame({"Unique Item": [uniqueitems],
                            "Number of Purchases": [numberpurchases],
                            "Average Price": [averageprice],
                            "Total Revenue": [totalrevenue]})
summarytable.head()

summarytable.style.format({"Average Price": "${:.2f}", "Total Revenue": "${:.2f}"})


#Percentage and Count of Male Players
#Percentage and Count of Female Players
#Percentage and Count of Other / Non-Disclosed

allcount = purchase_data["SN"].count()
allcount

#male data
malecount = purchase_data[purchase_data["Gender"] == "Male"]["SN"].count()
malecount

#percentmale
percentmale = malecount / totalplayers * 100
percentmale = percentmale.round(2)
percentmale

#female count
femalecount = purchase_data[purchase_data["Gender"] == "Female"]["SN"].count()
femalecount 

#percentfemale
femalepercent = femalecount / totalplayers * 100
femalepercent = femalepercent.round(2)
femalepercent.round(2)
femalepercent

othercount = allcount - femalecount - malecount
othercount

otherpercent = othercount / totalplayers * 100
otherpercent.round(2)
otherpercent
#Now create the dataframe table

gendertable = pd.DataFrame({"Gender": ["Male", "Female", "Other / Non-Disclosed"], "Percentage of Players": 
                            [percentmale, femalepercent, otherpercent],
                                        "Total Count": [malecount, femalecount, othercount]}, columns = 
                                        ["Gender", "Percentage of Players", "Total Count"])
                                        


gendertable.style.format({"Percentage of Players": "{:.2f}%"})


#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
#Create a summary data frame to hold the results
#Sort the total purchase value column in descending order
#Display the summary data frame

#figure out the math
genderpurchasetotal = purchase_data.groupby(["Gender"]).sum()["Price"]
genderpurchasetotal = genderpurchasetotal.round(2)
genderpurchasetotal


genderaverage = purchase_data.groupby(["Gender"]).mean()["Price"]
genderaverage = genderaverage.round(2)
genderaverage

gendercounts = purchase_data.groupby(["Gender"]).count()["Price"]
gendercounts

perperson = genderpurchasetotal / gendercounts 
perperson =perperson.round(2)
perperson

#create the table
genderpurchasetable = pd.DataFrame({"Purchase Count": gendercounts, 
                                   "Average Purchase Price": genderaverage, "Total Purchase Value": genderpurchasetotal,
                                   "Avg Purchase Total Per Person": perperson})
                                   
                                  
   

                                        
genderpurchasetable
genderpurchasetable.style.format({"Average Purchase Price": "${:.2f}", "Avg Purchase Total Per Person": "${:.2f}",
                                 "Total Purchase Value": "${:.2f}"})


#Establish bins for ages
#Categorize the existing players using the age bins. Hint: use pd.cut()
#Calculate the numbers and percentages by age group
#Create a summary data frame to hold the results
#Optional: round the percentage column to two decimal points
#Display Age Demographics Table

#binning

age_bins = [0, 9.90, 14.90, 19.90, 24.9, 29.9, 34.90, 39.90, 9999999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", ">40"]


playerdemographic = pd.cut(purchase_data["Age"], age_bins, labels=group_names)
playerdemographic

#calculations
agedemocount =playerdemographic.value_counts()
agedemocount = agedemocount.round(2)
 
agepercent = agedemocount / totalplayers *100
agepercent =agepercent.round(2)
agepercent

#create table
agedemotable = pd.DataFrame({"Total Count": agedemocount, "Percentage of Players": agepercent})


agedemotable = agedemotable.sort_index()
agedemotable

agedemotable.style.format({"Percentage of Players": "{:.2f}%"})

#Bin the purchase_data data frame by age
#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
#Create a summary data frame to hold the results
#Optional: give the displayed data cleaner formatting
#Display the summary data frame


# Bin the Purchasing Data
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)
# Run basic calculations
analysistot = purchase_data.groupby(["Age Ranges"]).sum()["Price"]
analysistot

analysisavg = purchase_data.groupby(["Age Ranges"]).mean()["Price"]
analysisavg

analysiscounts = purchase_data.groupby(["Age Ranges"]).count()["Price"]
analysiscounts

#Average Purchase Total per Person 


analysisperperson = analysistot / analysiscounts 
analysisperperson = analysisperperson.round(2)
analysisperperson

#create DataFrame table
analysistable = pd.DataFrame({"Purchase Count": analysiscounts, "Average Purchase Price": analysisavg,
                             "Total Purchase Value": analysistot, "Average Purchase Per Person": analysisperperson})

#cleaner format
analysistable.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}",
                           "Average Purchase Per Person": "${:.2f}"})






#Run basic calculations to obtain the results 
#Purchase Count
#Average Purchase Price
#Total Purchase Value

#Sort the total purchase value column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame

topcount = purchase_data.groupby(["SN"]).count()["Price"]
topcount.head()

topavgcount = purchase_data.groupby(["SN"]).mean()["Price"]
topavgcount.head()

toptotalvalue = purchase_data.groupby(["SN"]).sum()["Price"]
toptotalvalue.head()

topspenders = pd.DataFrame({"Purchase Count": topcount, "Average Purchase Price": topavgcount,
                           "Total Purchase Value": toptotalvalue})


topspenders.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})
topspenders.sort_values("Total Purchase Value", ascending=False).head()

#Most Popular Items
#Retrieve the Item ID, Item Name, and Item Price columns
#Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
#Create a summary data frame to hold the results
#Sort the purchase count column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame


#Purchase Count
#Item Price
#Total Purchase Value

mostpopcount = purchase_data.groupby(["Item ID", "Item Name"]).count()["Price"]
mostpopcount

mostpoptot = purchase_data.groupby(["Item ID", "Item Name"]).sum()["Price"]
mostpoptot

mostpopprice = purchase_data.groupby(["Item ID", "Item Name"]).mean()["Price"]
mostpopprice

mostpopdf = pd.DataFrame({"Purchase Count": mostpopcount, "Item Price": mostpopprice, "Total Purchase Value": mostpoptot})
mostpopdf.sort_values("Purchase Count", ascending=False).head()


mostpopdf.style.format({"Item Price": "${:.2f}",
                       "Total Purchase Value": "${:.2f}"})


#sort Total purchase value by descending
mostpopdf.sort_values("Total Purchase Value", ascending=False).head()
mostpopdf.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})

#3 Take Aways
#1. Based on the Most Popular, Thorn, Satchel of Dark Souls had the most in counts however Putrid Fan had the highest dollar
#   amount due to the cost of $4.08 vs $1.33. Putrid only needed 4 sales and it made almost half of what the highest count made.
#2. The age bracket of 20-24 doubled the amount of spend compared to the other age categories. Age group 40 and over had the lowest
#   amount of dollars spent. This is a segment that I would not recommend advertising to. I would look to grow the 15-19 segment.
#3  Males were the largest amount of purchasers an had the highest amount of dollars spent but were the lowest when it came to 
#   dollars spent per person. They followed females and the other classifications. 
