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
 LLMInterface
       ▲
       │
  OllamaLLM
       │
       ▼
     Ollama
       │
       ▼
   qwen3:0.6b
```

`LLMInterface` définit le contrat commun des fournisseurs de LLM. `OllamaLLM` en est l'implémentation actuelle et réalise les requêtes HTTP vers Ollama. Le code appelant peut donc dépendre de l'interface plutôt que d'un moteur précis.

Cette séparation permet de faire évoluer le moteur LLM sans modifier le contrat utilisé par le reste de l'application.

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
from src.assistant_ia.llm import OllamaLLM

llm = OllamaLLM()

response = llm.ask("Réponds uniquement par : OK")

print(response)
```

Pour définir le premier paramètre de génération disponible, on le passe au fournisseur concret :

```python
llm = OllamaLLM(temperature=0.2)
```

Si `temperature` n'est pas renseignée, Ollama conserve son comportement par défaut.

On peut aussi limiter la longueur de la réponse :

```python
llm = OllamaLLM(max_tokens=64)
```

Cette option est transmise à Ollama sous le nom `num_predict`.

L'ancien module `src/llm.py` est encore présent de manière transitoire, avec `LLMClient` et sa fonction `ask()`. Il n'est plus référencé par les tests ni par le nouveau package ; il est conservé jusqu'à vérification et décision explicite de suppression.

## Structure

```text
assistant-ia/
├── docs/
│   ├── decisions.md
│   └── journal.md
├── src/
│   ├── config.py
│   ├── llm.py                  # ancienne API, conservée temporairement
│   └── assistant_ia/
│       └── llm/
│           ├── __init__.py
│           ├── interface.py
│           └── ollama.py
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
