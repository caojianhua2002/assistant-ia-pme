import json
import urllib.error
import urllib.request

from src.config import OLLAMA_MODEL, OLLAMA_URL

from .interface import LLMInterface


class OllamaLLM(LLMInterface):
    """Fournisseur Ollama qui respecte le contrat :class:`LLMInterface`."""

    def __init__(
        self,
        url: str = OLLAMA_URL,
        model: str = OLLAMA_MODEL,
        temperature: float | None = None,
    ):
        self.url = url
        self.model = model
        self.temperature = temperature

    def ask(self, prompt: str) -> str:
        """Envoie ``prompt`` à Ollama et retourne sa réponse textuelle."""

        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        if self.temperature is not None:
            data["options"] = {"temperature": self.temperature}

        request = urllib.request.Request(
            self.url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        try:
            with urllib.request.urlopen(request) as response:
                result = json.loads(
                    response.read().decode("utf-8")
                )
        except urllib.error.URLError as exc:
            raise RuntimeError(
                f"Impossible de contacter Ollama : {exc}"
            ) from exc

        return result["response"]
