from agents.agent import create_agent

QUESTIONS = [
    ("Which layer does Driver belong to?", "Motivation"),
    ("Which layer does ValueStream belong to?", "Strategy"),
    ("Which layer does BusinessRole belong to?", "Business"),
    ("Which layer does ApplicationInterface belong to?", "Application"),
    ("Which layer does SystemSoftware belong to?", "Technology"),
    ("Is Realization from BusinessProcess to Node permitted?", "No"),
    ("Is Access from ApplicationComponent to DataObject permitted?", "Yes"),
    ("Is Assignment from Node to Artifact permitted?", "Yes"),
    ("Is Serving from ApplicationService to BusinessProcess permitted?", "Yes"),
    ("Is Influence from Driver to Goal permitted?", "Yes"),
    ("Is Composition from DataObject to ApplicationComponent permitted?", "No"),
    ("Is BusinessComponent a valid element type?", "No"),
]


def main():
    agent = create_agent()

    for question, expected in QUESTIONS:
        prompt = question + " Answer in one word. No formatting."
        result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
        print(question)
        print(f"  expected: {expected}")
        print(f"  answer:   {result['messages'][-1].text}\n")


if __name__ == "__main__":
    main()
