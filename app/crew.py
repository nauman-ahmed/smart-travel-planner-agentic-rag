from crewai import Agent, Task, Crew, Process, LLM


def build_travel_crew(destination, days, budget, style, rag_context, weather_info, currency_info):
    """
    Builds and runs a CrewAI workflow for the Smart Travel Planner.
    """

    llm = LLM(
        model="ollama/llama3.1:8b",
        base_url="http://localhost:11434",
        temperature=0.3,
    )

    destination_researcher = Agent(
        role="Destination Researcher",
        goal=(
            "Analyze destination knowledge and extract the most useful travel information "
            "for the user's trip."
        ),
        backstory=(
            "You are an expert travel researcher. You specialize in understanding destinations, "
            "local attractions, transport, safety, food, culture, and practical travel tips."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    budget_analyst = Agent(
        role="Budget Analyst",
        goal=(
            "Create a realistic budget breakdown based on destination, trip duration, "
            "travel style, and available budget."
        ),
        backstory=(
            "You are a travel budget expert. You estimate accommodation, food, transport, "
            "activities, emergency buffer, and daily spending limits."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    itinerary_planner = Agent(
        role="Itinerary Planner",
        goal=(
            "Create a clear, practical, day-by-day itinerary using destination research "
            "and budget analysis."
        ),
        backstory=(
            "You are a professional itinerary designer. You create realistic travel plans "
            "that balance sightseeing, rest, transport time, budget, and user preferences."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    research_task = Task(
        description=f"""
        Research the destination using the provided local RAG context.

        Destination: {destination}
        Travel style: {style}
        Number of days: {days}

        Local RAG context:
        {rag_context}

        Weather information:
        {weather_info}

        Your job:
        - Summarize the destination
        - Identify top attractions
        - Mention food/culture highlights
        - Mention transport tips
        - Mention weather-related advice
        """,
        expected_output=(
            "A structured destination research summary with attractions, culture, transport, "
            "weather notes, and practical travel advice."
        ),
        agent=destination_researcher,
    )

    budget_task = Task(
        description=f"""
        Create a travel budget estimate.

        Destination: {destination}
        Days: {days}
        Total budget: {budget} EUR
        Travel style: {style}

        Currency information:
        {currency_info}

        Use the research result from the previous task.

        Your job:
        - Estimate accommodation cost
        - Estimate food cost
        - Estimate local transport cost
        - Estimate activity/sightseeing cost
        - Add emergency buffer
        - Decide whether the budget is realistic
        """,
        expected_output=(
            "A budget breakdown table with estimated costs, daily spending guidance, "
            "and a short feasibility conclusion."
        ),
        agent=budget_analyst,
        context=[research_task],
    )

    itinerary_task = Task(
        description=f"""
        Build the final travel plan.

        Destination: {destination}
        Days: {days}
        Budget: {budget} EUR
        Travel style: {style}

        Use the destination research and budget analysis from previous tasks.

        Your job:
        - Create a day-by-day itinerary
        - Include morning, afternoon, and evening activities
        - Keep the plan realistic
        - Respect the travel style and budget
        - Add final travel tips
        """,
        expected_output=(
            "A complete day-by-day itinerary with budget-aware recommendations and final tips."
        ),
        agent=itinerary_planner,
        context=[research_task, budget_task],
    )

    crew = Crew(
        agents=[
            destination_researcher,
            budget_analyst,
            itinerary_planner,
        ],
        tasks=[
            research_task,
            budget_task,
            itinerary_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    return result