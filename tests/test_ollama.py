from src.llm import ask


def test_ask_returns_response():
    response = ask(
        "Réponds en une phrase : qu'est-ce qu'une PME ?"
    )

    assert isinstance(response, str)
    assert response.strip()
