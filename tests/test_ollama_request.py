import json
from unittest.mock import MagicMock, patch

from src.assistant_ia.llm import OllamaLLM


def test_ask_sends_configured_generation_options_to_ollama():
    llm = OllamaLLM(
        model="test-model",
        temperature=0.2,
        max_tokens=64,
        seed=42,
    )
    response = MagicMock()
    response.__enter__.return_value.read.return_value = (
        b'{"response": "Bonjour"}'
    )

    with patch(
        "src.assistant_ia.llm.ollama.urllib.request.urlopen",
        return_value=response,
    ) as urlopen:
        result = llm.ask("Bonjour")

    request = urlopen.call_args.args[0]
    payload = json.loads(request.data.decode("utf-8"))

    assert result == "Bonjour"
    assert payload["model"] == "test-model"
    assert payload["prompt"] == "Bonjour"
    assert payload["stream"] is False
    assert payload["options"] == {
        "temperature": 0.2,
        "num_predict": 64,
        "seed": 42,
    }
