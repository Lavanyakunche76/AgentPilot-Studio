@"

<a name="readme-top"></a>



<div align="center">

<img src="https://microsoft.github.io/autogen/0.2/img/ag.svg" alt="AgentPilot Studio Logo" width="100">



\# AgentPilot Studio



A multi-agent AI application built with Microsoft AutoGen and Groq API.



\[!\[Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python\&logoColor=white)](https://python.org)

\[!\[AutoGen](https://img.shields.io/badge/Framework-AutoGen-orange)](https://github.com/microsoft/autogen)

\[!\[Groq](https://img.shields.io/badge/API-Groq-green)](https://groq.com)

\[!\[License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)



</div>



\## What is AgentPilot Studio?



\*\*AgentPilot Studio\*\* is a multi-agent AI project powered by Microsoft AutoGen framework and Groq free API. It enables intelligent agents to work together autonomously to solve tasks.



\## Setup

\- \*\*Model:\*\* llama-3.1-8b-instant

\- \*\*API:\*\* Groq (Free)

\- \*\*Framework:\*\* AutoGen v0.7.5

\- \*\*Python:\*\* 3.10+



\## Installation

pip install autogen-agentchat autogen-ext autogenstudio



\## Files

\- agent.py - Single agent demo (asks a question to AI)

\- multi\_agent.py - Multi agent team (Teacher + Student agents)



\## How to Run

python agent.py

python multi\_agent.py



\## AutoGen Studio (No-Code GUI)

python -m autogenstudio.cli ui --port 8080



Then open: http://127.0.0.1:8080



\## Built By

Lavanya Kunche - AgentPilot Studio Project

"@ | Out-File -FilePath README.md -Encoding utf8

