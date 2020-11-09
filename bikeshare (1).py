import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()
    while city not in CITY_DATA:
        print('Sorry that is not a valid input. Please try again.')
        city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month_responses = ['jan','feb','mar','apr','may','jun','all']
    month = input('Which month would you like to view data for? Please enter: Jan, Feb, Mar, Apr, May, Jun, or All.\n').lower()
    while month not in valid_month_responses:
        print('Sorry that is not a valid input. Please Try again.')
        month = input('Which month would you like to view data for? Please enter: Jan, Feb, Mar, Apr, May, Jun, or All.\n').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day_responses = ['mon','tue','wed','thu','fri','sat','sun', 'all']
    day = input('Which day would you like to view data for? Please enter: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All.\n').lower()
    while day not in valid_day_responses:
        print('Sorry that is not a valid input. Please Try again.')
        day = input('Which day would you like to view data for? Please enter: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All.\n').lower()
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=MONTHS[df['month'].mode()[0]-1]

    print("The most common month:", most_common_month)


    # TO DO: display the most common day of week
    most_common_day_of_week = df['day of week'].mode()[0]

    print("the most common day of week:", most_common_day_of_week) 


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    
    print("the most common Start Hour:", most_common_start_hour)
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most popular start station is {}".format(common_start))
          

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most popular end station is {}".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip=df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most popular trip from start to end is: \n {}".format(popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
         gender = df['Gender'].value_counts()
         print("counts of gender = ",gender)
    else:
         print("not available information .")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_year = df['Birth_Year'].min()
        print("Earliest year is ",earliest_year)
        recent_year = df['Birth_Year'].max()
        print('Recent year is ',recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('The most common year is',common_year)
    else:
        print("not available information .") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index1 = 0
    index2 = 5
    while True:
        view_data = input('Would you like to view 5 rows of data?\nEnter yes or no.').lower()
        if view_data == 'yes':
            print(df.iloc[index1:index2])
            index1 += 5
            index2 += 5
        
        else:
        
            break


    
def main(): 
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)     
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    
if __name__ == "__main__":
	main()
           
