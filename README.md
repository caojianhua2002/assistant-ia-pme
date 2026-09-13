# Assistant IA PME

Démonstrateur d'assistant IA privé destiné aux PME.

L'objectif est de construire progressivement un système capable d'interroger des documents d'entreprise et de produire des réponses basées sur leur contenu.

## Principes

Le projet privilégie :

* le traitement local des données ;
* la confidentialité des documents ;
* une architecture modulaire ;
* des composants simples et remplaçables ;
* des tests automatisés ;
* une progression par étapes.

## Architecture actuelle

```text
Question utilisateur
       │
       ▼
   LLMClient
       │
       ▼
     Ollama
       │
       ▼
   qwen3:0.6b
```

L'application ne communique donc pas directement avec le modèle : `LLMClient` constitue l'interface entre le code du projet et Ollama.

Cette séparation permettra de faire évoluer ultérieurement le moteur LLM sans modifier le reste de l'application.

## Environnement de développement

Le projet utilise actuellement :

* Windows 10
* Git Bash / MSYS2
* Python 3.14.3
* environnement virtuel Python `.venv`
* Ollama
* modèle `qwen3:0.6b`
* pytest

## Installation de l'environnement

Depuis le répertoire du projet :

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Vérification :

```bash
python --version
```

## Tests

Les tests sont exécutés avec :

```bash
pytest -q
```

## Utilisation actuelle

Exemple d'utilisation directe :

```python
from src.llm import LLMClient

client = LLMClient()

response = client.ask("Réponds uniquement par : OK")

print(response)
```

Un raccourci compatible est également disponible :

```python
from src.llm import ask

response = ask("Réponds uniquement par : OK")
```

## Structure

```text
assistant-ia/
├── docs/
│   ├── decisions.md
│   └── journal.md
├── src/
│   ├── config.py
│   └── llm.py
├── tests/
│   ├── __init__.py
│   └── test_ollama.py
├── .venv/
├── PLAN.md
├── README.md
└── STATUS.md
```

## Progression

Le projet est développé par étapes.

Voir `PLAN.md` pour le plan général et `STATUS.md` pour l'état actuel.

## Documentation

* `PLAN.md` — plan de développement
* `STATUS.md` — état actuel
* `docs/decisions.md` — décisions d'architecture
* `docs/journal.md` — journal du développement
