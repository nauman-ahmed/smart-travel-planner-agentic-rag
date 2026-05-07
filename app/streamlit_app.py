import streamlit as st

from rag import search_knowledge
from crew import build_travel_crew


st.set_page_config(
    page_title="Smart Travel Planner",
    page_icon="🧳",
    layout="wide"
)

st.title("🧳 Smart Travel Planner")
st.write("Local Agentic RAG travel planner using Ollama, CrewAI, ChromaDB, and Streamlit.")


# -----------------------------
# Sidebar Inputs
# -----------------------------

st.sidebar.header("Trip Preferences")

destination = st.sidebar.text_input(
    "Destination",
    value="Paris"
)

days = st.sidebar.number_input(
    "Number of days",
    min_value=1,
    max_value=14,
    value=5
)

budget = st.sidebar.number_input(
    "Budget in EUR",
    min_value=100,
    max_value=10000,
    value=800,
    step=50
)

style = st.sidebar.selectbox(
    "Travel style",
    ["Budget", "Cultural", "Family", "Adventure", "Luxury"]
)


# -----------------------------
# Main Preview Section
# -----------------------------

st.subheader("Trip Request")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Destination", destination)
col2.metric("Days", days)
col3.metric("Budget", f"{budget} EUR")
col4.metric("Style", style)


# -----------------------------
# Generate Button
# -----------------------------

if st.button("Generate Travel Plan"):

    if not destination.strip():
        st.error("Please enter a destination.")
        st.stop()

    with st.spinner("Searching local travel knowledge..."):
        rag_result = search_knowledge(
            f"{destination} travel guide attractions food transport"
        )
        rag_context = str(rag_result)

    weather_info = """
    Weather information will be loaded from the local weather pipeline.
    For MVP: use general seasonal advice.
    """

    currency_info = """
    Base currency is EUR. Currency conversion data will be loaded from the local currency pipeline.
    """

    with st.spinner("Running CrewAI travel agents with local Ollama model..."):
        result = build_travel_crew(
            destination=destination,
            days=days,
            budget=budget,
            style=style,
            rag_context=rag_context,
            weather_info=weather_info,
            currency_info=currency_info,
        )

    st.success("Travel plan generated!")

    st.subheader("Generated Travel Plan")
    st.markdown(str(result))


# -----------------------------
# Info Section
# -----------------------------

with st.expander("How this app works"):
    st.write("""
    1. User enters destination, days, budget, and travel style.
    2. App searches local ChromaDB travel knowledge.
    3. CrewAI agents process the request.
    4. Ollama runs the local LLM.
    5. Streamlit displays the final itinerary.
    """)