import datetime
from func.Speak import speak


def get_workout_plan():
    workout_plan = {
        "Monday": {
            "Workout": [
                "Warm-up: 10 minutes of jogging",
                "Strength Training: Upper Body - 3 sets of push-ups, pull-ups, and dumbbell presses",
                "Cardio: 20 minutes of running or cycling",
                "Cool-down: 5 minutes of stretching"
            ],
            "Diet": [
                "Breakfast: Oatmeal with fruits and nuts",
                "Lunch: Grilled chicken salad with mixed greens and vinaigrette",
                "Snack: Greek yogurt with honey",
                "Dinner: Baked salmon with quinoa and steamed vegetables"
            ]
        },
        "Tuesday": {
            "Workout": [
                "Warm-up: 10 minutes of brisk walking",
                "Strength Training: Lower Body - 3 sets of squats, lunges, and calf raises",
                "Cardio: 20 minutes of HIIT (High-Intensity Interval Training)",
                "Cool-down: 5 minutes of stretching"
            ],
            "Diet": [
                "Breakfast: Smoothie with spinach, banana, and protein powder",
                "Lunch: Turkey wrap with whole grain tortilla and avocado",
                "Snack: Carrot sticks with hummus",
                "Dinner: Stir-fried tofu with brown rice and mixed vegetables"
            ]
        },
        "Wednesday": {
            "Workout": [
                "Warm-up: 10 minutes of jumping jacks",
                "Strength Training: Core - 3 sets of planks, Russian twists, and leg raises",
                "Cardio: 20 minutes of swimming or rowing",
                "Cool-down: 5 minutes of stretching"
            ],
            "Diet": [
                "Breakfast: Scrambled eggs with spinach and whole grain toast",
                "Lunch: Quinoa salad with chickpeas, tomatoes, and cucumbers",
                "Snack: Apple slices with peanut butter",
                "Dinner: Grilled shrimp with couscous and roasted vegetables"
            ]
        },
        "Thursday": {
            "Workout": [
                "Warm-up: 10 minutes of light jogging",
                "Strength Training: Upper Body - 3 sets of bench presses, shoulder presses, and bicep curls",
                "Cardio: 20 minutes of cycling or elliptical training",
                "Cool-down: 5 minutes of stretching"
            ],
            "Diet": [
                "Breakfast: Greek yogurt with granola and berries",
                "Lunch: Lentil soup with whole grain bread",
                "Snack: Mixed nuts and seeds",
                "Dinner: Grilled chicken with sweet potatoes and green beans"
            ]
        },
        "Friday": {
            "Workout": [
                "Warm-up: 10 minutes of dynamic stretching",
                "Strength Training: Lower Body - 3 sets of deadlifts, leg presses, and hamstring curls",
                "Cardio: 20 minutes of running or stair climbing",
                "Cool-down: 5 minutes of stretching"
            ],
            "Diet": [
                "Breakfast: Smoothie bowl with banana, berries, and almond butter",
                "Lunch: Chicken and avocado salad with mixed greens",
                "Snack: Cottage cheese with pineapple",
                "Dinner: Baked cod with wild rice and asparagus"
            ]
        },
        "Saturday": {
            "Workout": [
                "Warm-up: 10 minutes of yoga or stretching",
                "Strength Training: Full Body - 3 sets of burpees, kettlebell swings, and mountain climbers",
                "Cardio: 20 minutes of hiking or brisk walking",
                "Cool-down: 5 minutes of stretching"
            ],
            "Diet": [
                "Breakfast: Whole grain pancakes with fresh fruit",
                "Lunch: Tuna salad with mixed greens and olive oil",
                "Snack: Protein bar",
                "Dinner: Grilled steak with mashed potatoes and broccoli"
            ]
        },
        "Sunday": {
            "Workout": [
                "Active Rest: Light activities such as walking, stretching, or yoga",
                "Optional: Leisurely activities like a bike ride or a light swim"
            ],
            "Diet": [
                "Breakfast: Avocado toast with poached eggs",
                "Lunch: Vegetable stir-fry with tofu",
                "Snack: Smoothie with kale, apple, and ginger",
                "Dinner: Roasted chicken with mixed vegetables and quinoa"
            ]
        }
    }
    return workout_plan


def get_today_plan(plan):
    today = datetime.datetime.today().strftime('%A')
    return today, plan.get(today, {})


def print_plan(day, activities):
    if not activities:
        print(f"No plan found for {day}.")
        return

    print(f"\n{day}:")
    speak(f"Today is {day}. So your workout plan and diet is given below :")
    print("\nWorkout Plan:")
    for workout in activities["Workout"]:
        print(f"- {workout}")
    print("\nDiet Plan:")
    for meal in activities["Diet"]:
        print(f"- {meal}")


def ExerciseMain():
    print(" 1-Week Workout and Diet Plan :- ")
    plan = get_workout_plan()
    day, today_plan = get_today_plan(plan)
    print_plan(day, today_plan)



