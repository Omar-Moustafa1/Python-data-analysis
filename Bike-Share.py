# Project 1
# Made by Omar Mostafa

from os import name
import time
from warnings import catch_warnings
import numpy as np
import pandas as panda

def Intro():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
    
    print("Hello! Let's explore some US bikeshare data! ")
    while True:
        city=input("Would you like to see data Chicago, New York, or Washington?\n")
        if city == "Chicago":
            file_name="chicago.csv"
            break
        elif city == "New York":
            file_name="new_york_city.csv"
            break
        elif city == "Washington":
            file_name="washington.csv"
            break
        else :
            print("Wrong city")

    #------------------------Filter the Data-------------------------------------------------#
    
    data_Frame= panda.read_csv(file_name)
    data_Frame['Start Time']=panda.to_datetime(data_Frame['Start Time'])
    
    # extract month, day of week, hour from Start Time to create 3 new columns
    data_Frame['month'] = data_Frame['Start Time'].dt.month
    data_Frame['day_of_week'] = data_Frame['Start Time'].dt.day_name()
    data_Frame['hour'] = data_Frame['Start Time'].dt.hour

    choice=input('Would you like to filter the data by month, day, both, or not at all? type "none" for no time filter.\n')
    
    if choice == 'month':
        month=input('Which month? Jan, Feb, Mar, Apr, May, or June?.\n')
        month = months.index(month) + 1
        filtered_data=data_Frame[data_Frame['month']==month]
    
    elif choice == 'day':
        day=int(input('Which day? Please type your response as an integer (e.g., 1=Sunday).\n'))
        day_name=days[day-1]
        filtered_data=data_Frame[data_Frame['day_of_week']==day_name]
    elif choice == 'both':
        month=input('Which month? Jan, Feb, Mar, Apr, May, or June?.\n')
        month = months.index(month) + 1
        day=int(input('Which day? Please type your response as an integer (e.g., 1=Sunday).\n'))
        day_name=days[day-1]
        data_Frame=data_Frame[data_Frame['month']==month]
        filtered_data=data_Frame[data_Frame['day_of_week']==day_name]

    elif choice == 'none':
        filtered_data = data_Frame

    return [filtered_data,choice]



def Calculate_Statistics(data_Frame,choice):
    
    print("Calculate the statistics ... ")
#--------------------------------------------------------------------------------------------#
    start_time=time.time()
    
    popular_month=data_Frame['month'].mode()[0]
    popular_month_counts = data_Frame['month'].value_counts()
    popular_month_counts=popular_month_counts[popular_month]

    popular_day=data_Frame['day_of_week'].mode()[0]
    popular_day_counts = data_Frame['day_of_week'].value_counts()
    popular_day_counts=popular_day_counts[popular_day]

    popular_hour=data_Frame['hour'].mode()[0]
    popular_hour_counts = data_Frame['hour'].value_counts()
    popular_hour_counts=popular_hour_counts[popular_hour]

    elapsed_time=time.time()-start_time

    print("Calculate the first statistics ... ")
    print("Most popular month : "+str(popular_month)+", Count: "+str(popular_month_counts)+", "+choice)
    print("Most popular day : "+str(popular_day)+", Count: "+str(popular_day_counts)+", "+choice)
    print("Most popular hour : "+str(popular_hour)+", Count: "+str(popular_hour_counts)+", "+choice)
    print("That took : "+str(elapsed_time)+", seconds.")

#--------------------------------------------------------------------------------------------#
    start_time=time.time()
    trip_duration=np.sum(data_Frame['Trip Duration'])
    trip_duration_counts = data_Frame['Trip Duration'].size
    avg_duration=trip_duration/trip_duration_counts
    elapsed_time=time.time()-start_time

    print("Calculate the next statistics ... trip_duration: ")
    print("Total duration: "+str(trip_duration)+", seconds, Count: "+str(trip_duration_counts)+", Avg Duration: "+str(avg_duration)+", "+choice)
    print("That took : "+str(elapsed_time)+", seconds.")

#--------------------------------------------------------------------------------------------#
    start_time=time.time()
    start_station=data_Frame['Start Station'].mode()[0]
    start_station_count=data_Frame['Start Station'].value_counts()[start_station]
    end_station=data_Frame['End Station'].mode()[0]
    end_station_count=data_Frame['End Station'].value_counts()[end_station]
    elapsed_time=time.time()-start_time

    print("Calculate the next statistics ... popular_station: ")
    print("Start Station:"+str(start_station)+", Count:"+str(start_station_count)+" - End Station:"+str(end_station)+", Count:"+str(end_station_count))
    print("That took : "+str(elapsed_time)+", seconds.")

#--------------------------------------------------------------------------------------------#
    start_time=time.time()
    trips_grouped=data_Frame.groupby(['Start Station','End Station'])
    popular_combination_station = trips_grouped.size().sort_values(ascending=False).head(1)
    popular_trip=str(popular_combination_station)
    popular_trip_lines=popular_trip.splitlines()[1]
    line=popular_trip_lines.split(' ')
    popular_trip_count=line[len(line)-1]
    index=popular_trip_lines.index(popular_trip_count)
    popular_trip=popular_trip_lines[0:index:1]
    elapsed_time=time.time()-start_time

    print("Calculating the next statistic...popular_trip")
    print("Trip: ("+popular_trip+"), Count:"+popular_trip_count+", Filter:"+choice+"")
    print("That took : "+str(elapsed_time)+", seconds.")

#--------------------------------------------------------------------------------------------#
    start_time=time.time()
    user_types=data_Frame['User Type'].value_counts()
    subscribers=user_types[0]
    customers=user_types[1]
    elapsed_time=time.time()-start_time

    print("Calculate the next statistics ... user_type: ")
    print("Subscribers: "+str(subscribers)+", Customers: "+str(customers)+", Filter: "+choice)
    print("That took : "+str(elapsed_time)+", seconds.")


    try :
    #--------------------------------------------------------------------------------------------#
        start_time=time.time()
        user_types=data_Frame['Gender'].value_counts()
        male_count=user_types[0]
        female_count=user_types[1]
        elapsed_time=time.time()-start_time

        print("Calculate the next statistics ... gender: ")
        print("Male:"+str(male_count)+", Female:"+str(female_count)+", Filter: "+choice)
        print("That took : "+str(elapsed_time)+", seconds.")

    #--------------------------------------------------------------------------------------------#
        print("Calculating the next statistic...birth_year")
        earlier_year=str(data_Frame['Birth Year'].min())
        print("The earlier year : "+earlier_year)
        recent_year=str(data_Frame['Birth Year'].max())
        print("The recent year : "+recent_year)
        common_year=str(data_Frame['Birth Year'].mode()[0])
        print("The most common year : "+common_year)
        #print("would you like to view individual trip data/type 'yes' or 'no'?")
    except KeyError:
        print("")
        #print("would you like to view individual trip data/type 'yes' or 'no'?")
    

def main():    
    restart=True    
    while restart:
        [filtered_Data,choice]=Intro()
        Calculate_Statistics(filtered_Data,choice)
        while True:
            restart_choice=input("would you like to restart? Type 'yes' or 'no'\n")
            if restart_choice == "yes":
                break
            elif restart_choice == "no":
                restart=False
                break
            else :
                print("Wrong choice !!")

main()

