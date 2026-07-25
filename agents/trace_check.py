from deepagents import create_deep_agent

from agents.models import get_model


def main() -> None:
    agent = create_deep_agent(model=get_model())
    result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
