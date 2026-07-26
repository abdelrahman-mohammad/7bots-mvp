from agents.agent import create_agent
from agents.subagents import SUBAGENTS

NAMES = ", ".join(subagent["name"] for subagent in SUBAGENTS)
PROMPT = f"Call each of these subagents once with the task tool: {NAMES}. Then report what each one returned."


def main():
    agent = create_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": PROMPT}]})
    print(result["messages"][-1].text)


if __name__ == "__main__":
    main()
