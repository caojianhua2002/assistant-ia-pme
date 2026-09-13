from src.assistant_ia.llm import LLMInterface, OllamaLLM


def test_llm_interface_is_abstract():
    assert "ask" in LLMInterface.__abstractmethods__


def test_ollama_llm_implements_llm_interface():
    llm = OllamaLLM(
        url="http://example.test/api/generate",
        model="test-model",
    )

    assert isinstance(llm, LLMInterface)
    assert llm.url == "http://example.test/api/generate"
    assert llm.model == "test-model"
    assert llm.temperature is None
