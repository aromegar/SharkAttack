
# SharkAttack

![](https://st.depositphotos.com/2196544/2323/i/950/depositphotos_23239198-stock-photo-cartoon-smiling-baby-shark.jpg)

## Analyzing a data-set with pandas to identify patterns in shark attacks

With this analysis, we try to identify wich are the most repeated patterns when a shark has attacked a human person.

A lot of individual events have been registered since 18th century with the development of navigation around the oceans. In modern times, scientific societies have tried to standarize the registers throu an universal questionary where information like place, time, activity, shark specie or victims' personal details have been stored. Despite that, there are still a lot of unstandarized answers in those questionaries.

Our task as data analysts is to clean data through all those singularities, and aggregate information to extract all kinds of conclusions.

## Goal

We need to clean the data with an array (pun intended) of techniques, and store this data in a clean data-set. Then, we will have to set three aprioristic hypotheses and confirm or discard them via data exploratory analysis. This conclusions should be shown graphically with the most appropiate charts.

## what is in this repo

In this repository you will find:

 - A readmi.md file with information about the project (this document).
 
 - A jupyter notebook called "Cleaning_Data_Sharks" with the methods for the data cleaning. As an output, it exports a csv file with the clean data ready to be further analysed.
 
 - A second jupyter notebook called "Visualizing_Sharks" with the DEA methods and charts used to confirm or discard the conclusions.
 
 - A "src" folder with a "cleaning_functions.py" file inside, where functions called in the Cleaning_data_Sharks jn are.
 
 - A gitignore file with internal stuff not for public sight.
 
## libraries

In this project we have used the following libraries:

 - pandas   https://pandas.pydata.org/docs/
 
 - numpy   https://numpy.org/doc/stable/
 
 - plotly   https://plotly.com/python/
 
 - seaborn   https://seaborn.pydata.org/
 
 - our own "cleaning_functions.py"
    
    
# summary

We confirm our three hypothesis with the exploration of the data we have previously cleaned:

   - Sharks attacks are registered primarily in the summer, when most people dive in the sea for swimming or surfing.
   - South Pacific ocean (Australia and Micronesia majorly) and the Caribbean are the most dangerous seas.
   - The white shark is by far responsible of the majority of attacks.

Have a good reading and enjoy the water!


