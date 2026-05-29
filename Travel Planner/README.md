# AI-Based Travel Planner

## Overview

This project implements an **AI-Based Travel Planner** in Python. It uses predefined knowledge bases containing tourist attractions, food recommendations, hotel information, and transportation costs to generate personalized travel itineraries and estimate trip expenses based on user preferences.


## Features

- Accepts destination, interest category, budget type, and trip duration as user input.
- Reuses domain knowledge bases for tourist attractions, food recommendations, and hotels.
- Generates a personalized day-wise travel itinerary.
- Recommends local food specialties for each day.
- Suggests hotels based on the selected budget category.
- Calculates an estimated total trip cost.
- Supports multiple destinations and travel interests.


## How It Works

The travel planner uses several knowledge bases:

### Tourist Places Knowledge Base
Stores attractions categorized by destination and interest.

### Food Knowledge Base
Stores popular local dishes for each destination.

### Hotel Knowledge Base
Stores hotel recommendations based on budget categories.

### Transport Cost Knowledge Base
Stores transportation costs for each destination.

### Workflow

1. Accepts user preferences.
2. Retrieves matching tourist attractions.
3. Selects suitable hotel recommendations.
4. Suggests local foods.
5. Generates a day-wise itinerary.
6. Estimates the total travel cost.


## Input Format

1. Enter the destination.
2. Enter the interest category.
3. Enter the budget type.
4. Enter the number of travel days.

### Example Input

```text
Enter destination: Hyderabad
Enter interest (History/Nature/Beaches/Adventure): History
Enter budget type (Budget/Medium/Luxury): Medium
Enter number of days: 3
```


## Example Output

```text
===== AI TRAVEL PLAN =====

Destination: Hyderabad
Interest: History
Hotel: Hotel XYZ
Days: 3

Itinerary:
Day 1 -> Visit: Charminar | Food: Hyderabadi Biryani
Day 2 -> Visit: Golconda Fort | Food: Haleem
Day 3 -> Visit: Salar Jung Museum | Food: Double Ka Meetha

Estimated Cost: ₹ 11500
```


## Applications

This implementation demonstrates fundamental concepts of:

- Artificial Intelligence Based Recommendation Systems
- Knowledge-Based Systems
- Travel and Tourism Planning
- Personalized Itinerary Generation
- Cost Estimation and Budget Planning
- Decision Support Systems

## Advantages

- Simple and easy to understand implementation.
- Generates personalized travel plans.
- Reuses existing knowledge bases effectively.
- Provides food, accommodation, and sightseeing recommendations.
- Estimates travel expenses automatically.
- Can be extended with additional destinations, hotels, and attractions.



## Conclusion

The AI-Based Travel Planner is a simple knowledge-based recommendation system that assists users in planning trips according to their interests, budget, and travel duration. By combining tourist attractions, food suggestions, accommodation options, and cost estimation, it provides a personalized travel experience and demonstrates the practical application of AI techniques in tourism planning.
