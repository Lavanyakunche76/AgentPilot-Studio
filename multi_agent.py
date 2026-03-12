import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    client = OpenAIChatCompletionClient(
        model="llama-3.1-8b-instant",
        api_key="YOUR_GROQ_API_KEY",
        base_url="https://api.groq.com/openai/v1",
        model_capabilities={
            "json_output": False,
            "vision": False,
            "function_calling": True,
        }
    )
    agent1 = AssistantAgent("Teacher", model_client=client)
    agent2 = AssistantAgent("Student", model_client=client)
    team = RoundRobinGroupChat([agent1, agent2], max_turns=4)
    await Console(team.run_stream(task="Explain what is Artificial Intelligence"))
    await client.close()

asyncio.run(main())