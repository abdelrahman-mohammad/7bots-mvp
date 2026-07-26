from agents.agent import create_agent


def main():
    agent = create_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": "Hello, are you working?"}]})
    print(result["messages"][-1].text)


if __name__ == "__main__":
    main()
