from app.crew import build_travel_crew

rag_context = """
Paris is known for the Eiffel Tower, Louvre Museum, cafes, walkable neighborhoods,
public transport, museums, Seine river walks, and cultural tourism.
"""

weather_info = """
Current weather in Paris: mild temperature, moderate wind. Spring and autumn are comfortable.
"""

currency_info = """
Base currency: EUR. Budget is already in EUR.
"""

result = build_travel_crew(
    destination="Paris",
    days=3,
    budget=600,
    style="Cultural",
    rag_context=rag_context,
    weather_info=weather_info,
    currency_info=currency_info,
)

print(result)