from deepagents import create_deep_agent

from agents.filesystem import create_backend
from agents.models import get_model


def create_agent():
    return create_deep_agent(
        model=get_model(),
        backend=create_backend(),
        skills=["/skills"],
    )
