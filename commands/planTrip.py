import datetime
from func.Speak import speak


def get_user_input():
    print("Welcome to the Weekend Trip Planner!")
    print("Where would you like to go for your weekend trip? ")
    destination = input()
    print("Enter the start date of your trip (YYYY-MM-DD): ")
    start_date = input()
    print("Enter the end date of your trip (YYYY-MM-DD): ")
    end_date = input()

    print("What activities are you interested in? (Enter numbers separated by commas)")
    print("1. Sightseeing")
    print("2. Hiking")
    print("3. Beach")
    print("4. Shopping")
    print("5. Dining")
    print("6. Adventure Sports")
    print("7. Relaxation")
    print("Your choices: ")
    activities = input()

    return destination, start_date, end_date, activities.split(',')


def get_activities():
    return {
        '1': ['Visit the local museum', 'City tour', 'Visit historical landmarks'],
        '2': ['Mountain hike', 'Forest trail', 'Visit a national park'],
        '3': ['Relax on the beach', 'Beach volleyball', 'Snorkeling'],
        '4': ['Visit a shopping mall', 'Explore local markets', 'Visit boutique stores'],
        '5': ['Fine dining at a local restaurant', 'Street food tour', 'Visit a winery'],
        '6': ['Bungee jumping', 'Zip-lining', 'White-water rafting'],
        '7': ['Spa day', 'Yoga session', 'Relax by the pool']
    }


def plan_trip(destination, start_date, end_date, activities):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    trip_duration = (end_date - start_date).days + 1

    activity_options = get_activities()

    selected_activities = [activity_options[activity.strip()] for activity in activities if
                           activity.strip() in activity_options]

    itinerary = []
    day = start_date
    for i in range(trip_duration):
        daily_activities = []
        for activity_list in selected_activities:
            daily_activities.append(activity_list[i % len(activity_list)])

        daily_plan = {
            'date': day.strftime('%Y-%m-%d'),
            'activities': daily_activities
        }
        itinerary.append(daily_plan)
        day += datetime.timedelta(days=1)

    return itinerary


def print_itinerary(destination, itinerary):
    print(f"\nYour weekend trip to {destination} is planned as follows:")
    speak(f"\nYour weekend trip to {destination} is planned as follows:")
    for day_plan in itinerary:
        print(f"\nDate: {day_plan['date']}")
        print("Activities:")
        for activity in day_plan['activities']:
            print(f" - {activity}")


def Tripmain():
    destination, start_date, end_date, activities = get_user_input()
    itinerary = plan_trip(destination, start_date, end_date, activities)
    print_itinerary(destination, itinerary)



