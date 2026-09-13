import json
import urllib.error
import urllib.request

from src.config import OLLAMA_MODEL, OLLAMA_URL


class LLMClient:
    """Client minimal pour communiquer avec Ollama."""

    def __init__(
        self,
        url: str = OLLAMA_URL,
        model: str = OLLAMA_MODEL,
    ):
        self.url = url
        self.model = model

    def ask(self, prompt: str) -> str:
        """Envoie un prompt au LLM et retourne sa réponse."""

        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

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


def ask(prompt: str) -> str:
    """Raccourci compatible avec l'ancienne interface."""

    return LLMClient().ask(prompt)