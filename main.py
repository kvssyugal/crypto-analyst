import os
import time
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

# Load API keys from .env
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

search_tool = SerperDevTool()

llm = LLM(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.2
)


news_fetcher = Agent(
    role="Crypto News Fetcher",
    goal="Find the latest news about {coin}",
    backstory="You are a crypto journalist. Be brief and concise.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=2
)

sentiment_analyzer = Agent(
    role="Sentiment Analyzer",
    goal="Score the sentiment of {coin} news from 1-10",
    backstory="You are a financial analyst. Be brief.",
    llm=llm,
    verbose=True,
    max_iter=2
)

price_researcher = Agent(
    role="Price Researcher",
    goal="Find current price of {coin}",
    backstory="You are a crypto trader. Be brief.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iter=2
)

report_writer = Agent(
    role="Report Writer",
    goal="Write a short analyst report for {coin}",
    backstory="You write brief financial reports.",
    llm=llm,
    verbose=True,
    max_iter=2
)

task1 = Task(
    description="Find 3 recent news headlines about {coin} cryptocurrency.",
    expected_output="3 news headlines with one line summary each.",
    agent=news_fetcher
)

task2 = Task(
    description="Score the sentiment for {coin} from 1-10 based on the news. One paragraph max.",
    expected_output="Score X/10 and one sentence reason.",
    agent=sentiment_analyzer
)

task3 = Task(
    description="Find current price of {coin} in USD.",
    expected_output="Current price and 7 day change.",
    agent=price_researcher
)

task4 = Task(
    description="Write a 5 line report for {coin} covering price, sentiment, and recommendation.",
    expected_output="Short report: Price, Sentiment, News summary, Recommendation.",
    agent=report_writer
)

crew = Crew(
    agents=[news_fetcher, sentiment_analyzer, price_researcher, report_writer],
    tasks=[task1, task2, task3, task4],
    process=Process.sequential,
    verbose=True
)

coin = input("Enter a coin to analyze (e.g. Bitcoin, Ethereum): ")

print("\n⏳ Running agents... this may take ~30 seconds due to rate limits\n")
time.sleep(5)

result = crew.kickoff(inputs={"coin": coin})
print("\n\n========== FINAL REPORT ==========")
print(result)