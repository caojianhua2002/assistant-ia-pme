import json
import urllib.error
import urllib.request

from src.config import OLLAMA_MODEL, OLLAMA_URL

from .errors import (
    LLMConnectionError,
    LLMRequestError,
    LLMResponseError,
    LLMValidationError,
)
from .interface import LLMInterface


class OllamaLLM(LLMInterface):
    """Fournisseur Ollama qui respecte le contrat :class:`LLMInterface`."""

    def __init__(
        self,
        url: str = OLLAMA_URL,
        model: str = OLLAMA_MODEL,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ):
        self._validate_configuration(url, model, temperature, max_tokens)
        self.url = url
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def ask(self, prompt: str) -> str:
        """Envoie ``prompt`` à Ollama et retourne sa réponse textuelle."""

        if not isinstance(prompt, str) or not prompt.strip():
            raise LLMValidationError(
                "Le prompt doit être une chaîne de caractères non vide."
            )

        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        options = {}
        if self.temperature is not None:
            options["temperature"] = self.temperature
        if self.max_tokens is not None:
            options["num_predict"] = self.max_tokens
        if options:
            data["options"] = options

        request = urllib.request.Request(
            self.url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        try:
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raise LLMRequestError(
                f"Ollama a retourné l'erreur HTTP {exc.code}."
            ) from exc
        except urllib.error.URLError as exc:
            raise LLMConnectionError(
                f"Impossible de contacter Ollama : {exc}"
            ) from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise LLMResponseError(
                "La réponse d'Ollama n'est pas un JSON valide."
            ) from exc

        try:
            text = result["response"]
        except (KeyError, TypeError) as exc:
            raise LLMResponseError(
                "La réponse d'Ollama ne contient pas de texte."
            ) from exc

        if not isinstance(text, str):
            raise LLMResponseError(
                "La réponse d'Ollama n'est pas un texte."
            )

        return text

    @staticmethod
    def _validate_configuration(
        url: str,
        model: str,
        temperature: float | None,
        max_tokens: int | None,
    ) -> None:
        if not isinstance(url, str) or not url.strip():
            raise LLMValidationError("L'URL Ollama doit être non vide.")
        if not isinstance(model, str) or not model.strip():
            raise LLMValidationError("Le modèle Ollama doit être non vide.")
        if temperature is not None and (
            isinstance(temperature, bool)
            or not isinstance(temperature, (int, float))
        ):
            raise LLMValidationError(
                "La température doit être un nombre ou None."
            )
        if max_tokens is not None and (
            isinstance(max_tokens, bool)
            or not isinstance(max_tokens, int)
            or max_tokens <= 0
        ):
            raise LLMValidationError(
                "max_tokens doit être un entier strictement positif ou None."
            )
