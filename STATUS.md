# Assistant IA PME — État du projet

Dernière mise à jour : 13 septembre 2026

## État général

Le projet dispose d'une première chaîne fonctionnelle permettant à Python d'envoyer un prompt à un LLM local exécuté par Ollama et de récupérer sa réponse. La couche LLM a été séparée en une interface abstraite et une implémentation spécifique à Ollama.

La connexion réelle au modèle a été vérifiée avec succès.

## Environnement

* Système principal de développement : Windows 10
* Terminal : Git Bash / MSYS2
* Python : 3.14.3
* Environnement virtuel : `.venv`
* Projet : `assistant-ia`
* Emplacement : `~/dev/projects/assistant-ia`

## LLM local

* Moteur : Ollama
* API : `http://localhost:11434/api/generate`
* Modèle : `qwen3:0.6b`

Test direct réalisé :

```text
Réponds uniquement par : OK
→ OK
```

## Code actuel

### `src/config.py`

Contient actuellement la configuration de connexion à Ollama :

* URL de l'API
* nom du modèle

### `src/assistant_ia/llm/`

Contient :

* `LLMInterface`, interface abstraite qui définit `ask(prompt) -> str` ;
* `OllamaLLM`, implémentation de cette interface pour Ollama ;
* communication HTTP avec l'API Ollama
* gestion de l'erreur de connexion à Ollama

`src/llm.py` existe encore et contient l'ancienne API `LLMClient` ainsi que la fonction de raccourci `ask()`. L'audit ne relève aucune importation de `src.llm`, `LLMClient` ou de cette fonction en dehors de ce module. Il est donc conservé provisoirement, sans être utilisé par le test actuel, jusqu'à une décision explicite de suppression.

### Tests

`tests/test_ollama.py` vérifie actuellement :

* qu'une requête réelle au LLM retourne une chaîne non vide ;
* que cette requête passe par une instance de `OllamaLLM`.

Il n'existe actuellement pas de test automatisé de configuration de l'URL ou du modèle, ni de test unitaire isolé d'Ollama.

## Tests

Dernier test exécuté :

```text
python -m pytest

1 passed
```

Le test présent utilise réellement Ollama. La dernière exécution a réussi ; pytest a toutefois émis un avertissement de création de cache `.pytest_cache`, sans échec de test.

## Étape actuelle

**Étape 2 — Interface LLM**

Sous-étape actuelle :

**2.2 — Renforcement et tests de l'interface**

Prochaines actions :

1. compléter les tests ;
2. stabiliser le contrat de `LLMInterface` ;
3. définir les paramètres de génération nécessaires ;
4. améliorer la gestion des erreurs ;
5. préparer l'utilisation du LLM par les prochaines étapes du projet.

## Points restant à traiter

* L'ancien module `src/llm.py` reste à traiter après vérification complémentaire de son absence d'utilisateurs ; il ne doit pas être supprimé sans décision explicite.
* L'extraction PDF n'a pas encore commencé.
* Le RAG n'a pas encore été implémenté.
