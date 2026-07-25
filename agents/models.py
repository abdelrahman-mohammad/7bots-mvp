from langchain.chat_models import init_chat_model

from backend.config import require

MODEL_NAME = "anthropic:claude-haiku-4-5"


def get_model():
    require("ANTHROPIC_API_KEY")
    return init_chat_model(MODEL_NAME)
