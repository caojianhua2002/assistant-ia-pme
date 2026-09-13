from abc import ABC, abstractmethod


class LLMInterface(ABC):
    """Contrat commun des fournisseurs de modèles de langage.

    Les consommateurs de LLM dépendent de cette interface plutôt que d'un
    fournisseur concret. Chaque implémentation doit transformer un prompt en
    réponse textuelle.
    """

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Retourne la réponse textuelle du fournisseur pour ``prompt``.

        Args:
            prompt: La question ou l'instruction à envoyer au modèle.

        Returns:
            La réponse produite par le modèle.
        """
        raise NotImplementedError
