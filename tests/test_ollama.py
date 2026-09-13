from src.assistant_ia.llm import OllamaLLM


def test_ask_returns_response():
    llm = OllamaLLM()

    response = llm.ask(
        "Réponds en une phrase : qu'est-ce qu'une PME ?"
    )

    assert isinstance(response, str)
    assert response.strip()