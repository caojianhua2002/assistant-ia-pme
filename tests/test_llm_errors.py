import json
import urllib.error
from unittest.mock import MagicMock, patch

import pytest

from src.assistant_ia.llm import (
    LLMConnectionError,
    LLMRequestError,
    LLMResponseError,
    OllamaLLM,
)


def test_ask_raises_connection_error_when_ollama_is_unreachable():
    with patch(
        "src.assistant_ia.llm.ollama.urllib.request.urlopen",
        side_effect=urllib.error.URLError("connection refused"),
    ):
        with pytest.raises(LLMConnectionError, match="Impossible de contacter"):
            OllamaLLM().ask("Bonjour")


def test_ask_raises_request_error_when_ollama_returns_http_error():
    http_error = urllib.error.HTTPError(
        url="http://localhost:11434/api/generate",
        code=500,
        msg="Internal Server Error",
        hdrs=None,
        fp=None,
    )

    with patch(
        "src.assistant_ia.llm.ollama.urllib.request.urlopen",
        side_effect=http_error,
    ):
        with pytest.raises(LLMRequestError, match="HTTP 500"):
            OllamaLLM().ask("Bonjour")


def test_ask_raises_response_error_when_response_has_no_text():
    response = MagicMock()
    response.__enter__.return_value.read.return_value = json.dumps(
        {"model": "test-model"}
    ).encode("utf-8")

    with patch(
        "src.assistant_ia.llm.ollama.urllib.request.urlopen",
        return_value=response,
    ):
        with pytest.raises(LLMResponseError, match="ne contient pas de texte"):
            OllamaLLM().ask("Bonjour")


def test_ask_raises_response_error_when_response_is_not_json():
    response = MagicMock()
    response.__enter__.return_value.read.return_value = b"not-json"

    with patch(
        "src.assistant_ia.llm.ollama.urllib.request.urlopen",
        return_value=response,
    ):
        with pytest.raises(LLMResponseError, match="n'est pas un JSON valide"):
            OllamaLLM().ask("Bonjour")
