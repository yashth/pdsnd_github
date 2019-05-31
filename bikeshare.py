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
    while True:
        city = input('Enter the city(chicago/new york city/washington): ')
        
        if city.lower() == 'chicago' or city.lower() == 'new york city' or city.lower() == 'washington':
            break
        else:
            print('Please enter city from following only : chicago,new york city,washington')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month between january and june: ')
        
        if month.lower() == 'january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may' or month.lower() == 'june':
            break
        else:
            print('Please enter month between january and june')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of week: ')
        
        if day.lower() == 'monday' or day.lower() == 'tuesday' or day.lower() == 'wednesday' or day.lower() == 'thursday' or day.lower() == 'friday' or day.lower() == 'saturday' or day.lower() == 'sunday':
            break
        else:
            print('Please enter the day of week')

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month :',common_month)
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of Week :',common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Hour :',common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if 'Start Station' in df.columns:
        common_start_station = df['Start Station'].mode()[0]
        print('Most Commonly used Start Station: ',common_start_station)
    else:
        print('There are no Start Station specified')
    # TO DO: display most commonly used end station
    if 'End Station' in df.columns:
        common_end_station = df['End Station'].mode()[0]
        print('\nMost Commonly used End Station: ',common_end_station)
    else:
        print('There is no End Station specified')
    # TO DO: display most frequent combination of start station and end station trip
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        df['start_end_station'] ='From '+df['Start Station']+' to '+df['End Station']
        common_start_end_station = df['start_end_station'].mode()[0]
        print('\nMost frequent combination of start station and end station trip: ',common_start_end_station)
    else:
        print('There is no Start Station or End Station specified')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    if 'Trip Duration' in df.columns:
        total_travel_time = np.sum(df['Trip Duration'])
        print('Total travel time: ',total_travel_time)
        # TO DO: display mean travel time
        mean_travel_time = np.mean(df['Trip Duration'])
        print('Mean travel time: ',mean_travel_time)
    else:
        print('There is no Trip Duration specified')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
        user_types_counts = df['User Type'].value_counts()
        print('Counts of User Types: ',user_types_counts)

    # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('Counts of Gender: ',gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_birth = df['Birth Year'].min()
        print('Earliest Birth Year: ',earliest_year_birth)
        most_recent_year_birth = df['Birth Year'].max()
        print('Most Recent Year: ',most_recent_year_birth)
        common_year_birth = df['Birth Year'].mode()[0]
        print('Common Birth Year: ',common_year_birth)
    else:
        print('There is no Birth Year specified')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    counter=5
    query = input('\nDo you want to view the first 5 raw data? yes:no ')
    if query.lower() == 'yes':
        print(df.head(5))
    else:
        return
    while True:
        more_query = input('\nDo you want to view next 5 raw data? yes:no ')
        if more_query.lower() == 'yes':
            print(df.iloc[counter:counter+5])
            if counter<=len(df.index):
                counter+=5
            else:
                print('You have reached the end of data')
                break
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
