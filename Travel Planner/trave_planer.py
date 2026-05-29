
# ----------------------------
# Knowledge Bases
# ----------------------------

tourist_places = {
    "Hyderabad": {
        "History": ["Charminar", "Golconda Fort", "Salar Jung Museum"],
        "Nature": ["Hussain Sagar Lake", "KBR National Park"]
    },
    "Goa": {
        "Beaches": ["Baga Beach", "Calangute Beach", "Anjuna Beach"],
        "Adventure": ["Scuba Diving", "Parasailing"]
    }
}

food_kb = {
    "Hyderabad": ["Hyderabadi Biryani", "Haleem", "Double Ka Meetha"],
    "Goa": ["Fish Curry", "Bebinca", "Prawn Balchão"]
}

hotel_kb = {
    "Hyderabad": {
        "Budget": ("Hotel ABC", 1500),
        "Medium": ("Hotel XYZ", 3000),
        "Luxury": ("Hotel Grand", 7000)
    },
    "Goa": {
        "Budget": ("Beach Inn", 2000),
        "Medium": ("Sea View Resort", 4000),
        "Luxury": ("Goa Palace", 8000)
    }
}

transport_cost = {
    "Hyderabad": 1000,
    "Goa": 1500
}

# ----------------------------
# AI Travel Planner
# ----------------------------

def generate_plan(destination, interest, budget_type, days):
    
    if destination not in tourist_places:
        return "Destination not available."

    itinerary = []

    # Tourist recommendations
    places = tourist_places[destination].get(interest, [])

    # Food recommendations
    foods = food_kb.get(destination, [])

    # Hotel recommendation
    hotel_name, hotel_cost = hotel_kb[destination][budget_type]

    # Cost estimation
    total_cost = (
        hotel_cost * days +
        transport_cost[destination] +
        (500 * days)     
    )

    # Generate itinerary
    for day in range(1, days + 1):
        place = places[(day - 1) % len(places)] if places else "Free Exploration"
        food = foods[(day - 1) % len(foods)] if foods else "Local Food"

        itinerary.append({
            "Day": day,
            "Place": place,
            "Food": food
        })

    # Output
    print("\n===== AI TRAVEL PLAN =====")
    print("Destination:", destination)
    print("Interest:", interest)
    print("Hotel:", hotel_name)
    print("Days:", days)

    print("\nItinerary:")
    for item in itinerary:
        print(
            f"Day {item['Day']} -> "
            f"Visit: {item['Place']} | "
            f"Food: {item['Food']}"
        )

    print("\nEstimated Cost: ₹", total_cost)


# ----------------------------
# User Input
# ----------------------------

destination = input("Enter destination: ")
interest = input("Enter interest (History/Nature/Beaches/Adventure): ")
budget = input("Enter budget type (Budget/Medium/Luxury): ")
days = int(input("Enter number of days: "))

generate_plan(destination, interest, budget, days)
