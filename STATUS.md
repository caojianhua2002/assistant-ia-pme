# Assistant IA PME — État du projet

Dernière mise à jour : 13 septembre 2026

## État général

Le projet dispose maintenant d'une première chaîne fonctionnelle permettant à Python d'envoyer un prompt à un LLM local exécuté par Ollama et de récupérer sa réponse.

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

### `src/llm.py`

Contient :

* `LLMClient`
* méthode `LLMClient.ask()`
* fonction `ask()` conservée comme raccourci
* communication HTTP avec l'API Ollama
* gestion de l'erreur de connexion à Ollama

### Tests

`tests/test_ollama.py` vérifie actuellement :

* qu'une requête réelle au LLM retourne une chaîne non vide ;
* que `LLMClient` accepte une URL et un modèle configurables.

## Tests

Dernier test exécuté :

```text
pytest -q

2 passed
```

Le premier test utilise réellement Ollama.

## Étape actuelle

**Étape 2 — Interface LLM**

Sous-étape actuelle :

**2.2 — Renforcement et tests de l'interface**

Prochaines actions :

1. compléter les tests ;
2. stabiliser l'API de `LLMClient` ;
3. définir les paramètres de génération nécessaires ;
4. améliorer la gestion des erreurs ;
5. préparer l'utilisation du LLM par les prochaines étapes du projet.

## Points restant à traiter

* Le dépôt Git du projet n'est pas encore correctement identifié dans ce répertoire.
* La documentation vient d'être remise à jour pour correspondre à l'état réel du projet.
* L'extraction PDF n'a pas encore commencé.
* Le RAG n'a pas encore été implémenté.
