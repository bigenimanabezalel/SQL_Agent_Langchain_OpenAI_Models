
# Natural Language to SQL AI Agent

## Overview

This project builds an **SQL AI Agent capable of converting natural language questions into SQL queries**, executing those queries on a **PostgreSQL database**, and returning answers derived directly from the data stored into database tables.

The system allows users to interact with structured databases using plain English instead of writing SQL manually.

Example:

User Question: what is the profit per category of product?

## Resources needed

- We use OPENAI model (for this project , we used 'gpt-4o')
- Connect to Postgres database 
- from langchain.agents import create_agent
- from langchain_openai import ChatOpenAI
- from langchain_community.utilities import SQLDatabase

## Key Features

- Natural language → SQL query conversion
- Automatic SQL execution on PostgreSQL
- AI-powered query reasoning with LangChain
- Integration with OpenAI API for query generation
- Supports complex analytical questions
- Returns structured results for downstream analytics or visualization

## Technologies Used

. Python
. LangChain
. OpenAI API
. PostgreSQL
. SQLAlchemy
. Pandas

## Architecture Overview

User Query (Natural Language)
        ↓
LangChain Agent
        ↓
OpenAI Model (LLM)
        ↓
SQL Query Generation
        ↓
PostgreSQL Execution
        ↓
Results and query executed