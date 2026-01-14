# StockPicker Crew

Welcome to the StockPicker Crew project, powered by [crewAI](https://crewai.com). This AI-powered system helps you pick the best stocks from any sector through comprehensive market research and analysis. The multi-agent system leverages advanced memory capabilities and web research to provide intelligent stock recommendations with detailed analysis and insights.

![Stock_picker](https://github.com/user-attachments/assets/bff61db6-3efe-427a-9765-1bd9736df0d0)


## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Creating a New Project

If you want to create a new crewAI project from scratch, you can use the following command:

```bash
crewai create crew <project_name>
```

This command will automatically generate the complete project structure with all necessary files and folders.

### Customizing

**Add your API keys into the `.env` file:**
- `OPENAI_API_KEY` - Your OpenAI API key (or configure your desired LLM)
- `SERPER_API_KEY` - Your Serper API key for web search capabilities (get it from [serper.dev](https://serper.dev))

**Configuration:**
- Modify [src/stock_picker/config/agents.yaml](src/stock_picker/config/agents.yaml) to define your agents
- Modify [src/stock_picker/config/tasks.yaml](src/stock_picker/config/tasks.yaml) to define your tasks
- Modify [src/stock_picker/crew.py](src/stock_picker/crew.py) to add your own logic, tools and specific args
- Modify [src/stock_picker/main.py](src/stock_picker/main.py) to specify the sector you want to analyze

**To select your desired sector:**
Open [src/main.py](src/main.py) and specify the sector you're interested in (e.g., Technology, Healthcare, Finance, etc.). The AI agents will research and analyze stocks from that sector.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the stock_picker Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Memory Features

This project leverages advanced memory capabilities to provide intelligent, context-aware stock recommendations:
- **LongTermMemory** - Retains historical market trends and past analyses
- **ShortTermMemory** - Manages current research session data and immediate insights
- **EntityMemory** - Tracks companies, stocks, and market entities across sessions

These memory features enable the AI agents to learn from previous analyses and provide more informed recommendations over time.

## Output

The stock analysis results are saved in the `output/` directory:
- `decision.md` - Final stock recommendations with detailed analysis
- `research_report.json` - Comprehensive research data in JSON format
- `trending_companies_<sector>.json` - Trending companies information for the selected sector

## How It Works

This project uses **SerperDevTool** for web search capabilities to gather the latest market data, stock performance metrics, and financial news. The AI agents collaborate to:
1. Research stocks in your specified sector
2. Analyze market trends and company performance
3. Evaluate financial metrics and growth potential
4. Generate comprehensive reports with stock recommendations
5. Save the analysis to the `output/` directory

Simply specify the sector you're interested in within [src/main.py](src/main.py), and the system will handle the rest!

## Understanding Your Crew

The stock_picker Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the StockPicker Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
