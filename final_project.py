# Final Project ENDG 233
# PRATHAM NITIN BHAWALKAR - 30143647
# MASROOR AHMAD POSH - 30156171

# A TERMINAL BASED PROGRAM WHICH SHOWS DIFFERENT STATISTICS OF A COUNTRY






import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



country_data = pd.read_csv('Country_Data.csv')                          # panadas is used to read data from the Country_Data.csv file and it is assigned to variable country_data
country_data = country_data.to_numpy()                                  # data coverted to array form

population_data = pd.read_csv('Population_Data.csv')                    # panadas is used to read the data from Population_Data.csv file and it is assigned to variable population_data
population_data=population_data.to_numpy()                              # data coverted to array form

threatened_species = pd.read_csv('Threatened_Species.csv')              # panadas is used to read the data from Threatened_Species.csv file and it is assigned to variable threatened_species     
threatened_species = threatened_species.to_numpy()                      # data coverted to array form


class Area_Data:
    
    """
    
    A class used to create a Area_Data object.

    Arguments:
        country (str): country name provided by the user
        km (int): calculated area

    
    """    
    def __init__(self, country, km):
        self.country = country 
        self.km = km

    def print_area(self):

        """
        
        A function that prints the country name and area

        Arguments: None
        
        Output: prints ths country name and the area of the country

        """

        print("Country: {}, Area: {} Km".format(self.country,self.km))  # print statement

    
  




def Country_check(country_name):
  '''
  This function checks whether the country name provided by the user exists or not

  Argument:
  country_name - str() country name provided by the user

  Result:
  Returns the checked country name enterd by the user

  '''
  name_country = " "                                               # empty string name_country creted
  flag = 1                                                         # flag variable assigned value one 
  while(flag == 1):                                                # while loop creted
      for i in country_data :                                      # for loop to accees each element in array country_name
          if(country_name == i[0]):                                # if statement with condition of country name in array equals to user inpuuted country name
              name_country = name_country + country_name           # variable name_country assigned value of country_name
              flag = 0                                             # flag value updated to zero
              return name_country                                  # name_country returned

      print("Your entered country does not exist. please enter the country name again")  # print statement
      country_name = input("Please enter a new country name: ")                          # user prompt to input country name again if the country name entered by the user before does not exist 
      country_name=country_name.title()                                                  # country_name coverted to title case

def un_region_check(country_name):
  '''
  Prints the UN Region of the user given country

  Arguments:
  country_name - (str) country name enterd by the user

  Result:
  Prints the UN region of the user entered country

  '''

  for i in country_data:                                         # for loop to access each element of country_data
      if i[0] == country_name:                                   # if statement with condition of country name in array equals to user given country name
          print("UN region of",country_name,"is",i[1])           # print statement
            
def un_sub_check(country_name):
    '''
  Prints the UN Sub Region of the user given country

  Arguments:
  country_name - (str) country name enterd by the user

  Result:
  Prints the UN Sub region of the user entered country

  '''
    for i in country_data:                                        # for loop to access each element of country_data
        if i[0] == country_name:                                  # if statement with condition of country name in array equals to user given country name
            print("UN sub-region of",country_name,"is",i[2])      # print statement

def sqkm_region(country_name):
  '''
  Prints the Area of the user given country

  Arguments:
  country_name - (str) country name enterd by the user

  Result:
  Prints the area of the user entered country

  '''
  
  for i in country_data:                                         # for loop to access each element of country_data
    if i[0] == country_name:                                     # if statement with condition of country name in array equals to user inputed country name
        return i[3]                                              # returns area



def display_all_results(country_name):
  '''
  This function displays all results

  Arguments:
  country_name - (str) country name enterd by the user

  Result:
  Prints the Area user entered country

  '''
  for i in country_data:                                                    # for loop to access each element of country_data
      if(i[0] == country_name):                                             # if statement with condition of country name in array equals to user inputed country name
        print("Country name"," ","Region"," ","Subregion","     ","Area")   # print statement
        print(country_name,"        ",i[1],"   ",i[2]," ",i[3])             # print statement

def population_year (country_name):
  '''
  This function displays the population of the user entered country for the user given year

  Argument:
  country_name - country name entered by the user

  Result:
  returns the population

  '''

  year=int(input("Please enter a year between 2000 and 2020 for which you want population : "))         # user is asked to input the year 
  while(True):                                                                                          # while loop creted
  
    for i in population_data:                                                                           # for loop to access each element of country_data
      if(i[0] == country_name):                                                                         # if statement with condition of country name in array equals to user inputed country name
       
        if(year >= 2000 and year <= 2020):                                                              # if statement with condition that year entered by the user is between 2000 and 2020
       
          return(i[year - 2000 + 1])                                                                    # returns population of the user entered country and year
    print("invalid year")                                                                               # print statement
    year=int(input("Please enter a year between 2000 and 2020 for which you want population again: "))  # user is asked to input the year again if the year entered before is not between 2000 and 2020

def population_change(country_name):

  '''
  This function displays the population change of the user entered country for the user given year

  Argument:
  country_name - country name entered by the user

  Result:
  returns the population change

  '''

  first_year = int(input("Enter the first year: "))            # User prompted to input first year
  second_year = int(input("Enter the second year: "))          # User prompted to input second year
  while(True):                                                 # while loop created
    for i in population_data:                                  # for loop to access each element of country_data
      if(i[0] == country_name):                                # if statement with condition of country name in array equals to user inputed country name       
        if(first_year >= 2000 and first_year <= 2020 and second_year >= 2000 and second_year <= 2020):  #  if statement with condition that years entered by the user is between 2000 and 2020
          return(i[second_year - 2000 + 1] - i[first_year - 2000 + 1])                                  # returns population of the user entered country and years
    print("invalid year")                                      # print statement
    first_year = int(input("Starting year: "))                 # User prompted to input first year
    second_year = int(input("Ending year: "))                  # User prompted to input second year

def population_density(country_name):
  '''
  This function displays the population density of the user entered country for the user given year

  Argument:
  country_name - country name entered by the user

  Result:
  returns the population density

  '''
  population = population_year (country_name)   # function population_year(country_name) is called and country_name is passsed as parameter to it
  sqkm = sqkm_region(country_name)              # function sqkm_region(country_name) is called and country_name is passsed as parameter to it
  return(population/sqkm)                       # population density is returned



def populationgrpaph(country_name):
  '''
  this function plots the graph of population between the user specified years for a user given country

  Arguments:
  country_name - country name given by the user

  Output:
  plots the graph 
  '''
   

  year1=int(input("Please enter the starting year between 2000 and 2020: "))  # user is prompted to input the starting year
  year2=int(input("Please enter the ending year between 2000 and 2020: "))     # user is prompted to input the ending year
                                                             
  

  while(True):                                                                # while loop created
    for i in population_data:                                                 # for loop to access every element of population_data array
      if(i[0 ]== country_name):                                               # if statement to check whether the country name exists in the array population_data or not
        if(year1 >= 2000 and year1 <= 2020 or (year2 >= 2000 and year2 <= 2020)):     # if statement to check whether the years provided by the user are between 2000 and 2020
        
          if(year2 < year1):                                                  # if statement to check if the starting year is greater than ending year
            values = []                                                       # empty list values created
            value = 0                                                         # variable value assigned value 0
            population = []                                                   # empty list population created
            year = []                                                         # empty list year created
            for k in range(year1 - year2 + 1):                                # for loop created         
              population.append((int(i[year1 - 2000 + 1])) / 1000000)         # population list appended 
              year.append(year1)                                              # years list appended
              values.append(value)                                            # values list appended
              value = value + 1                                               # value variable incremented by one            
              year1 = year1-1                                                 # year1 variable decremented by one
            plt.plot(population,"r--",label="Population")                     # plot
            plt.legend(shadow=True)                                           # legend provided
            plt.xticks(values,year)                                           # x ticks provided           
            plt.xlabel("Year")                                                # x-axis labelled
            plt.ylabel("Number of people in millions")                        # y-axis labelled
            plt.title("Population")                                           # title provided
            plt.show()                                                        # plot displayed
            return()                                                     
        
          else:                                                               # else statement
             values = []                                                      # empty list values created
             year = []                                                        # empty list year created
             population = []                                                  # empty list population created
             value = 0                                                        # variable value assigned value 0
             for k in range(year2 - year1 + 1):                               # for loop created   
              population.append(int(i[year1 - 2000 + 1] / 1000000))           # population list appended
              year.append(year1)                                              # years list appended
              year1 = year1+1                                                 # year1 variable incremented by one
              values.append(value)                                            # values list appended
              value = value + 1                                               # variable value incremented by one
             plt.plot(population,"r--",label="Population")                    # plot
             plt.legend(shadow=True)                                          # legend provided
             plt.xticks(values,year)                                          # x-ticks provided
             plt.xlabel("Year")                                               # x axis labelled
             plt.ylabel("Number of people in millions")                       # y axis labeled
             plt.title("Population")                                          # title provided
             plt.show()                                                       # plot displayed
             return()
              

    print("Invalid year")                                                              # print statement
    year1=int(input("Please Enter the starting year between 2000 and 2020 again: "))   # user prompted to input year again if the year provided earlier does not exist in the array population_data
    year2=int(input("Please Enter the ending year between 2000 and 2020 again: "))     # user prompted to input year again if the year provided earlier does not exist in the array population_data


    

def max_min_avg(country_name):
  '''
  this function prints the maximum , minimum, mean and median of population

  Arguments:
  country_name - country name entered by the user

  Output:
  prints the maximum, minimum, mean and median of population

  '''


  for i in population_data:                      # for loop to access each element of country_data

    if(i[0] == country_name):                    # if statement with condition of country name in array equals to user inputed country name
      print(" ")                                 # print statement
      print("Country name"," "," Maximum Population"," ","Minimum Population"," ","Mean population"," ","Median population")    # print statement
      print(country_name,"         ",np.amax(i[1:]),"             ",int(np.amin(i[1:])),"           ",int(np.mean(i[1:])),"            ",int(np.median(i[1:])))   # print statement
      return()



def thretened_species(country_name):
  '''
  this function prints the thretened species data and plots a bar graph for it

  Arguments:
  country_name - country name entered by the user

  Output:
  prints the thretened species data and plots a bar graph for it

  '''

  while(True):                                                                 # while loop created
  
    for i in threatened_species:                                               # for loop to access each element of threatened_species
      thretened_specie = []                                                    # empty list thretened_specie created
      if(i[0] == country_name):                                                # if statement with condition of country name in array equals to user inputed country name
        print("Countryname"," ","Plants"," ""Fish"," ","Birds"," ","Mammals")  # print statement

        print(country_name,"       ",i[1],"    ",i[2],"    ",i[3],"   ",i[4])  # print statement
        thretened_specie.append(i[1])                                          # empty list thretened_specie appended       
        thretened_specie.append(i[2])                                          # empty list thretened_specie appended      
        thretened_specie.append(i[3])                                          # empty list thretened_specie appended      
        thretened_specie.append(i[4])                                          # empty list thretened_specie appended      
    
        plt.bar([1,2,3,4],thretened_specie,color=['green', 'blue', 'yellow', 'orange'])   # bar graph plotted
        plt.xticks([1,2,3,4],["Plants","Fish","Bird","Mammal"])                           # x ticks added
        plt.xlabel("Thretened species")                                                   # label added to x axis 
        plt.ylabel("Number")                                                              # label added to y axis 
        plt.title("Number of thretened species")                                          # titile added
      
        plt.show()                                                                        # plot displayed
        return()

def plant_count(country_name):
  '''
  This function prints the number of thretened plants of the user given country

  Arguments:
  country_name - (str) country name given by the user

  Output:
  prints the number of thretened plants of the user given country name
  '''
  while(True):                                                                    # while loop created   
    for i in threatened_species:                                                  # for loop to access each element of threatened_species   
      if(i[0] == country_name):                                                   # if statement with condition of country name in array equals to user inputed country name
        print("The number of endangered Plants in ",country_name,"is: ",i[1])     # print statement
        return()


def fish_count(country_name):
  '''
  This function prints the number of thretened fish of the user given country

  Arguments:
  country_name - (str) country name given by the user

  Output:
  prints the number of thretened fish of the user given country name
  '''
  while(True):                                                                 # while loop created    
    for i in threatened_species:                                               # for loop to access each element of threatened_species   
      if(i[0] == country_name):                                                # if statement with condition of country name in array equals to user inputed country name
        print("The number of endangered Fish in ",country_name,"is: ",i[2])    # print statement
    return()
def bird_count(country_name):
  '''
  This function prints the number of thretened birds of the user given country

  Arguments:
  country_name - (str) country name given by the user

  Output:
  prints the number of thretened birds of the user given country name
  '''
  while(True):                                                                 # while loop created    
    for i in threatened_species:                                               # for loop to access each element of threatened_species   
      if(i[0] == country_name):                                                # if statement with condition of country name in array equals to user inputed country name
        print("The number of endangered birds in ",country_name,"is: ",i[3])   # print statement
    return()

def mammal_count(country_name):
  '''
  This function prints the number of thretened mammals of the user given country

  Arguments:
  country_name - (str) country name given by the user

  Output:
  prints the number of thretened mammals of the user given country name
  '''
  while(True):                                                                 # while loop created
    for i in threatened_species:                                               # for loop to access each element of threatened_species
      if(i[0] == country_name):                                                # if statement with condition of country name in array equals to user inputed country name
        print("The number of endangered mammals in ",country_name,"is: ",i[4]) # print statement
    return()

def min_max_mean_thretened_species(country_name):

  '''
  this function prints the maximum , minimum and mean of thretened species

  Arguments:
  country_name - country name entered by the user

  Output:
  prints the maximum, minimum and mean thretened species

  '''


  for i in threatened_species:                      # for loop to access each element of threatened_species:  

    if(i[0] == country_name):                    # if statement with condition of country name in array equals to user inputed country name
      print(" ")                                 # print statement
      print("Country name"," "," Maximum number of thretened species"," ","Minimum number of thretened species"," ","Mean number of thretened species")    # print statement
      print(country_name,"           ",np.amax(i[1:]),"                                      ",int(np.amin(i[1:])),"                                  ",int(np.mean(i[1:])))         # print statement

def all_details(country_name):
  '''
  this function prints all the details

  Arguments:
  country_name - country name entered by the user

  Output:
  prints all the details

  '''

  display_all_results(country_name)                      # function display_all_results(country_name) is called and country_name is passed as parametr to it
  max_min_avg(country_name)                              # function max_min_avg(country_name)   is called and country_name is passed as parametr to it
  print("")                                              # print statement
  while(True):                                           # while loop created

    for i in threatened_species:                         # for loop to access each element of threatened_species
    
      if(i[0] == country_name):                          # if statement with condition of country name in array equals to user inpuuted country name
        print("Countryname"," ","Plants"," ""Fish"," ","Birds"," ","Mammals") # print statement
        print(country_name,"       ",i[1],"    ",i[2],"    ",i[3],"   ",i[4]) # print statement
        return()

def main():
  '''
  this function prints the menu for the user to select whcih function to execute

  Arguments:
  country_name - country name entered by the user

  Output:
  prints the details user asks for by calling function

  '''

  print('-' * 45, end = '')                                                   # print statement
  print(' Welcome to the Country Statistics Program ',end="")                 # print statement
  print('-' * 45)                                                             # print statement
  print(' ')                                                                  # print statement

  country_name = input("Please enter the country name: ")                     # user is prompted to enter the country name
  country_name = country_name.title()                                         # country_name coverted to title case
  countryname = Country_check(country_name)                                   # function Country_check(country_name) is called and country_name is passed as parameter to it
  print("")                                                                   # print statement
  title_main_menu = '----- Main Menu -----'                                   # assigns a string for the title menu
  center_align_main_menu = title_main_menu.center(130)                        # aligns the string at center
  print(center_align_main_menu)                                               # prints the title of the main menu
  menu = "\nSelect 1 for Geographical details of country\nSelect 2 for Popoulation\nSelect 3 for Threatened species \nSelect 4 to display all details of the country \nSelect 5 to quit" # menu is assigned string
  print(menu)                                                                # print statement
  user_input = 2                                                             # variable user_input is given value 2 just to enter the loop
  
  while user_input != 5:                                                     # while loop created

    
      user_input = int(input("Enter your choice: "))                         # user is prompted to enter the user_input
      if user_input == 1:                                                    # if statement which will execute if the user_input is 1
          print("")                                                          # print statement
          print('-' * 45, end='')                                            # print statement
          print(' Geographical Data  ',end="")                               # print statement
          print('-' * 45)                                                    # print statement
          print(" ")                                                         # print statement
          menu1 = "\nSelect 1 to display UN-region\nSelect 2 to display UN-SUB REGION\nSelect 3 to display SQKM area of the region\nSelect 4 to display all details\nSelect 5 to Return to the main menu" # variable menu1 assigned string
          print(menu1)                                                       # print statement
          user_input1 = int(input("\nEnter your Choice: "))                  # user is prompted to enter the user_input1
          while(user_input1!= 5):                                            # while loop created           
            if user_input1 == 1:                                             # if statement which will execute if the user_input1 is 1
                un_region_check(country_name)                                # function un_region_check(country_name) and country_name is passed as parameter to it
                print(menu1)                                                 # print statement
                user_input1 = int(input("\nEnter your choice: "))            # user is prompted to enter the user_input1
            elif user_input1 == 2:                                           # if statement which will execute if the user_input1 is 1
                un_sub_check(country_name)                                   # function un_sub_check(country_name) and country_name is passed as parameter to it
                print(menu1)                                                 # print statement
                user_input1 = int(input("\nEnter your choice: "))            # user is prompted to enter the user_input1
            elif user_input1 == 3:                                           # if statement which will execute if the user_input1 is 1
                
                km=sqkm_region(country_name)                                 # function sqkm_region(country_name) and country_name is passed as parameter to it and value is stored in variable km
                area1=Area_Data(country_name,km)                             # area1 is creted by passing country_name and km to the class Area_Data
                Area_Data.print_area(area1)                                  # class function is called and asrea1 is paseed to it
                user_input1 = int(input("\nEnter your choice: "))            # user is prompted to enter the user_input1
            elif user_input1 == 4:                                           # if statement which will execute if the user_input1 is 1
                display_all_results(country_name)                            # function display_all_results(country_name) and country_name is passed as parameter to it
                print(menu1)                                                 # print statement
                user_input1 = int(input("\nEnter your choice: "))            # user is prompted to enter the user_input1
            else:
              print("invalid input")
              print(menu1)                                                 # print statement
              user_input1 = int(input("\nEnter your choice: "))            # user is prompted to enter the user_input1
       
          else:                                                              # else statement
            print(center_align_main_menu)                                    # print statement
            print(menu)                                                      # print statement

          
      elif user_input == 2:                                                  # if statement which will execute if the user_input is 1
          print("")                                                          # print statement
          print('-' * 45, end = '')                                          # print statement
          print(' Population statistics  ',end="")                           # print statement

          print('-' * 45)                                                    # print statement
          print(" ")                                                         # print statement
          menu2 = "\nSelect 1 to display population of the country\nSelect 2 to display population change in two years\nSelect 3 to display population density for the year\nSelect 4 to display graph for population between two years\nSelect 5 to dislpay max,min,mean and median of population\nSelect 6 to return to the main menu" # variable menu2 assigned value
          print(menu2)                                                       # print statement
          user_input2 = int(input("\nEnter your Choice: "))                  # user is prompted to enter the user_input2
          while(user_input2!=6):                                             # while loop created
            if user_input2 == 1:                                                                            # if statement which will execute if the user_input2 is 1
              print("Population of",country_name,"in the given year was",population_year(country_name))     # function population_year(country_name) and country_name is passed as parameter to it
              print(menu2)                                                   # print statement
              user_input2 = int(input("\nEnter your choice: "))              # user is prompted to enter the user_input2
            elif user_input2 == 2:                                           # if statement which will execute if the user_input2 is 2
              print("Population change of",country_name,"between given two years is",population_change(country_name))  # function population_change(country_name) and country_name is passed as parameter to it
              print(menu2)                                                  # print statement
              user_input2 = int(input("\nEnter your choice: "))             # user is prompted to enter the user_input2
            elif user_input2 == 3:                                          # if statement which will execute if the user_input2 is 3
              density_of_population = population_density(country_name)      # function population_density(country_name) and country_name is passed as parameter to it and stored in the variable density_of_population
              print("Population density of",countryname,"in the given year is",'{:.2f}'.format(density_of_population))  # print statement
              print(menu2)                                                  # print statement
              user_input2 = int(input("\nEnter your choice: "))             # user is prompted to enter the user_input2
            elif user_input2 == 4:                                          # if statement which will execute if the user_input2 is 4
              populationgrpaph(country_name)                                # function populationgrpaph(country_name) and country_name is passed as parameter to it
              print(menu2)                                                  # print statement
              user_input2 = int(input("\nEnter your choice: "))             # user is prompted to enter the user_input2        
            elif user_input2 == 5:                                          # if statement which will execute if the user_input2 is 6
              max_min_avg(country_name)                                     # function max_min_avg(country_name) and country_name is passed as parameter to it
              print(menu2)                                                  # print statement
              user_input2 = int(input("\nEnter your choice: "))             # user is prompted to enter the user_input2
            elif user_input2 == 6:  
              break
            else:                                                            # else statement
               print("invalid input")                                        # print statement
               print(menu2)                                                  # print statement
               user_input2 = int(input("\nEnter your choice: "))             # user is prompted to enter the user_input2
          else:                                                             # else statement
            print(center_align_main_menu)                                   # print statement
            print(menu)                                                     # print statement
 
      elif user_input == 3:                                                 # if statement which will execute if the user_input is 3
        print("")                                                           # print statement
        print('-' * 45, end='')                                             # print statement
        print(' Thretened species  ',end="")                                # print statement
        print('-' * 45)                                                     # print statement
        print(" ")                                                          # print statement
        menu3 = "\nSelect 1 to display thretened plants\nSelect 2 to display thretened fish\nSelect 3 to display thretened birds\nSelect 4 to display thretened mammals\nSelect 5 to dislpay all details with bar graph\nSelect 6 to display minimum, maximum and mean value of thretened species\nSelect 7 to return to the main menu" # variable menu3 assigned value
        print(menu3)                                                        # print statement
        user_input3 = int(input("\nEnter your Choice: "))                   # user is prompted to enter the user_input3
        while(user_input3 != 7):                                            # while loop created
          if(user_input3 == 1):                                             # if statement which will execute if the user_input3 is 1
            plant_count(country_name)                                       # function plant_count(country_name) is called and country_name is passed as parameter to it 
            print(menu3)                                                    # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
          elif(user_input3 == 2):                                           # if statement which will execute if the user_input3 is 2
            fish_count(country_name)                                        # function fish_count(country_name) is called and country_name is passed as parameter to it 
            print(menu3)                                                    # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
          elif(user_input3 == 3):                                           # if statement which will execute if the user_input3 is 3
            bird_count(country_name)                                        # function bird_count(country_name) is called and country_name is passed as parameter to it 
            print(menu3)                                                    # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
          elif(user_input3 == 4):                                           # if statement which will execute if the user_input3 is 4
            mammal_count(country_name)                                      # function mammal_count(country_name) is called and country_name is passed as parameter to it 
            print(menu3)                                                    # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
          elif(user_input3 == 5):                                           # if statement which will execute if the user_input3 is 5
            thretened_species(country_name)                                 # function thretened_species(country_name) is called and country_name is passed as parameter to it 
            print(menu3)                                                    # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
          elif(user_input3 == 6):                                           # if statement which will execute if the user_input3 is 6
            min_max_mean_thretened_species(country_name)                    # function min_max_mean_thretened_species(country_name)   is called and country_name is passed as parameter to it 
            print(menu3)                                                    # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
          else:                                                             # else statement
            print("invalid input")
            print(center_align_main_menu)                                   # print statement
            print(menu3)                                                     # print statement
            user_input3 = int(input("\nEnter your Choice: "))               # user is prompted to enter the user_input3
        else:                                                               # else statement
          print(center_align_main_menu)                                     # print statement
          print(menu)                                                       # print statement
   
      elif user_input == 4:                                                 # if statement which will execute if the user_input is 4
        print("")                                                           # print statement
        print('-' * 45, end='')                                             # print statement
        print(' All details  ',end="")                                      # print statement

        print('-' * 45)                                                     # print statement
        print(" ")                                                          # print statement
        
        all_details(country_name)                                           # function all_details(country_name) and country_name is passed as parameter to it
        print(center_align_main_menu)                                       # print statement
        print(menu)                                                         # print statement
   
      elif user_input == 5:
        print(" ")                                                                                 # print statement
        print("---------------------------------------------------------------------------------") # print statement
        print("Thank you for using this program")                                                  # print statement
        break
     
      else:                                                                 # else statement
        print("Invalid input")                                              # print statement
        print(center_align_main_menu)                                       # print statement
        print(menu)                                                         # print statement

  

if __name__ == '__main__':
  
  main() # calls the function main