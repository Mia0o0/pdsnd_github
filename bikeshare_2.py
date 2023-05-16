import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
   
    while True:
        city=input('would you like to see data for Chicago, New York, or Washinton? ')
        city = city.lower()
        if city.lower() in ('chicago','new york','washington'):
            break
        print('please select cities from Chicago, New York, or Washington')
        
    
    while True:
        month=input('would you like to see data from month of all, January, February,...,June ')
        month = month.lower()
        if month.lower() in ('all','january','february','march','april','may','june'):
            break
        print('please select monthes from all, January, February,...,June')

    
    while True:
        try:
            day=int(input('which day would you like to see, please type your response as an integer (eg: 1=Sunday) '))
            assert 0 < day < 8
            break
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer between 1 and 7")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    # load data file into a dataframeNone
    df = pd.read_csv(CITY_DATA[city])
   # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
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
       df = df[df['day_of_week']  == day]   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)
    
    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day_of_week)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station) 
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station) 

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'],sep=',',na_rep='-')
    popular_trip = df['trip'].mode()[0]
    print('Most commonly start station and end station trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if 'Trip Duration' in df.columns.values:
        print('total travel time:', df['Trip Duration'].sum())

    # display mean travel time
        print('total travel time:', df['Trip Duration'].mean())

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('No Trip data for this city')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if "User Type" in df.columns.values:
        print('counts of user types', df['User Type'].nunique())
    else:
        print("No user types data for this city")

    # Display counts of gender
    if "Gender" in df.columns.values:
        print('counts of gender', df['Gender'].nunique())
    else:
        print("No gender data for this city")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns.values:
        print('cearliest year of birth', df['Birth Year'].min())
        print('most recent year of birth', df['Birth Year'].max())  
        popular_Birth_Year = df['Birth Year'].mode()[0]
        print('most common year of birth', popular_Birth_Year) 
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("No Birth Year data for this city")

def rawdata(df):
    """Displays raw data for users."""
    showrow = 0    
    while True:
        datashow = input('would you like to see the raw data? ')
        if datashow.lower() != 'yes':
            break
        else:
            showdata = df.head(showrow*5+5).iloc[showrow*5:]
            print(showdata)
            showrow += 1

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
