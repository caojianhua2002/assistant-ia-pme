class LLMError(RuntimeError):
    """Erreur de base pour les fournisseurs de LLM."""


class LLMConnectionError(LLMError):
    """Impossible de joindre le fournisseur de LLM."""


class LLMRequestError(LLMError):
    """Le fournisseur a rejeté la requête avec une erreur HTTP."""


class LLMResponseError(LLMError):
    """Le fournisseur a renvoyé une réponse inexploitable."""
