from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from typing import List
from crewai_tools import SerperDevTool
# from .tools.push_tool import PushNotificationTool
from crewai.memory import LongTermMemory, ShortTermMemory,EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
# import google.generativeai as genai
# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class TrendingCompany(BaseModel):
    name: str = Field(description="Company name")
    ticker: str = Field(description="The ticker symbol of the company")
    reason: str = Field(description="Reason this company is trending in the news")

class TrendingCompanyList(BaseModel):
	companies: List[TrendingCompany] = Field(description="List of trending companies in the news")

class TrendingCompanyResearch(BaseModel):
	name: str = Field(description="Company name")
	market_position: str = Field(description="Current market position and competitive analysis")
	future_outlook: str = Field(description="Future outlook and growth prospects")
	investment_potential: str = Field(description="Investment potential and suitability for investment")
	
class TrendingCompanyReasearchList(BaseModel):
	research_list: List[TrendingCompanyResearch] = Field(description="Comprehensive research on all trending companies")
	
@CrewBase
class StockPicker():
	agents_config='config/agents.yaml'
	tasks_config='config/tasks.yaml'
	
	@agent
	def trending_company_finder(self) -> Agent:
		"""
		Finds trending companies in the news
		"""
		return Agent(config=self.agents_config['trending_company_finder'], tools=[SerperDevTool()],memory=True)
	
	@agent
	def financial_researcher(self) -> Agent:
		"""
		Researches financial data for trending companies
		"""
		return Agent(config=self.agents_config['financial_researcher'], tools=[SerperDevTool()])
	
	@agent
	def stock_picker(self) -> Agent:
		"""
		Selects the best stocks from the trending companies
		"""
		return Agent(config=self.agents_config['stock_picker'],memory=True)
	
	@task
	def find_trending_companies(self) -> Task:
		"""
		Finds trending companies in the news
		"""
		return Task(
			config=self.tasks_config['find_trending_companies'],
			output_pydantic=TrendingCompanyList,
		)

	@task
	def research_trending_companies(self) -> Task:
		"""
		Researches financial data for trending companies
		"""
		return Task(
			config=self.tasks_config['research_trending_companies'],
			output_pydantic=TrendingCompanyReasearchList,
		)
	
	@task
	def pick_best_company(self) -> Task:
		"""
		Selects the best stocks from the trending companies
		"""
		return Task(
			config=self.tasks_config['pick_best_company'],
		)
	@crew
	def crew(self) -> Crew:
		manager=Agent(config=self.agents_config['manager']
		, allow_delegation=True)
		
		short_term_memory=ShortTermMemory(
			storage=RAGStorage(
				embedder_config={
					"provider":"google-generativeai",
					"config":{"model_name":'models/gemini-embedding-001'}
				},
				type="short_term",
				path="./memory/"
				)
		)	
		long_term_memory=LongTermMemory(
			storage=LTMSQLiteStorage(
				db_path="./memory/long_term_memory_storage.db"
			)
		)
		entity_memory=EntityMemory(
			storage=RAGStorage(
				embedder_config={
					"provider":"google-generativeai",
					"config":{"model_name":"models/gemini-embedding-001"}
				},
				type="entity",
				path="./memory/"
				)
		)	
			
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.hierarchical,
			verbose=True,
			manager_agent=manager,
			memory=True,
			short_term_memory=short_term_memory,
			long_term_memory=long_term_memory,
			entity_memory=entity_memory
		)
	
	
	
	