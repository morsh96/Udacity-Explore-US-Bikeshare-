import time
from typing import Counter
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hey! Wanna explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington).
    city = input( ' Plz choose a city [chicago, new york city, washington]>>> ' ).lower()
    while city not in CITY_DATA:
        print('You entered invalid city!')
        city = input( ' Plz choose a city [chicago, new york city, washington]>>>' ).lower()

    #get user input for month (all, january, february, ... , june)
    months = [ 'january', 'february', 'march', 'april', 'may', 'june', 'all' ]
    month = input( 'Plz choose a month of the first 6 months of a year or all>>>').lower()

    while month not in months:
        print ('Invalid month!')
        month = input( 'Plz choose a month of the first 6 months of a year or all>>>').lower()
    
    #get user input for day of week (all, monday, tuesday, ... sunday)
    days = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday', 'all' ]
    day = input( 'Plz choose a day or all >>>').lower()

    while day not in days:
        print ('Invalid day')
        day = input( 'Plz choose a day or all >>>').lower()
    
        print('-'*55)
    return city, month, day


def load_data(city, month, day):
  
    df = pd.read_csv(CITY_DATA[city])

    df['Start_Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start_Time'].dt.month
    df['day_of_week'] = df['Start_Time'].dt.day_name()

    if month != all:
    
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    months = [ 'january', 'February', 'March', 'April', 'May', 'June' ]
    common_month = df['month'].mode()[0]
    print('Most common month: ', months[common_month-1] )

    #display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is: ', common_day)

    #display the most common start hour
    df['hour'] = df['Start_Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*55)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    common_start_station =  df['Start Station'].mode()[0]
    print ( 'Most common start station is: ' , common_start_station )
    
    #display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ( 'Most common end station is: ' , common_end_station )

    #display most frequent combination of start station and end station trip
    route = df['End Station']+ ' to ' + df['End Station']
    common_route = route.mode()[0]
    print ('Most frequent start and end stations is: ', common_route)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*55)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    trip = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    total_time = trip.sum()
    days = total_time.days
    hours = total_time.seconds / 60*60
    minutes = total_time.seconds % 60*60 / 60
    seconds = minutes = total_time.seconds % 60*60 % 60
    print( 'Total travel time of the trip is: ' , days , 'days  ' , hours , 'hours  ' , minutes , 'minutes  ' , seconds , 'seconds.')

    #display mean travel time
    average_time = trip.mean()
    days = average_time.days
    hours = average_time.seconds / 60*60
    minutes = average_time.seconds % 60*60 / 60
    seconds = average_time.seconds % 60*60 % 60
    print('Mean travel time of the trip is: ', '{} days {} hours {} minutes {} seconds'.format(days, hours, minutes, seconds) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*55)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_stats = df['User Type'].value_counts()
    print( 'Users numbers based on user type: \n', user_stats )
    #Display counts of gender
    
    if 'Gender' not in df.columns:
        print ('Gender not in this data set')
    else:
        user_gender = df['Gender'].value_counts()
        print('Users numbers based on gender: \n', user_gender )

    #Display earliest, most recent, and most common year of birth
    early_birth = df['Birth Year'].fillna(0).min()
    print ('Earlist birth year is: ', early_birth)
    recent_birth = df['Birth Year'].fillna(0).max()
    print ('Recent birth year is: ', recent_birth)
    common_birth = df['Birth Year'].fillna(0).mode()[0]
    print ('Common birth year is: ', common_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*55)


def display_raw_data(df): 
    q1 = input( "Would you like to view raw data? yes or no?" ).lower()
    if q1 == 'yes':
        start = 0
        while True:
            print(df.iloc[start:start+5])
            start += 5
            q2 = input("Wanna see more raw data? ").lower()
            if q2 != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



