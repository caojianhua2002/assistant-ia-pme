from abc import ABC, abstractmethod


class LLMInterface(ABC):
    """Interface commune pour les fournisseurs de LLM."""

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Envoie un prompt au LLM et retourne sa réponse."""
        raise NotImplementedError