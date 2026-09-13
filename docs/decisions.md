# Décisions d'architecture

Ce document conserve les décisions importantes prises pendant le développement du projet.

---

## 2026-09-13 — Utilisation d'un LLM local

### Décision

Le projet utilise initialement un LLM local exécuté avec Ollama.

Le modèle actuellement utilisé est :

```text
qwen3:0.6b
```

### Raisons

* confidentialité des documents d'entreprise ;
* possibilité de fonctionner sans envoyer les données à un service externe ;
* coût de fonctionnement limité ;
* possibilité de tester et développer localement.

### Conséquence

Le projet doit éviter de dépendre directement du moteur Ollama dans son code métier.

---

## 2026-09-13 — Création de `LLMClient`

### Décision

La communication avec le LLM est encapsulée dans `src/llm.py`, via la classe :

```python
LLMClient
```

### Raisons

L'application devra pouvoir évoluer sans que le code métier dépende directement de l'API HTTP d'Ollama.

L'interface permettra éventuellement de remplacer ou d'ajouter un autre moteur LLM ultérieurement.

### Conséquence

Le reste de l'application doit utiliser `LLMClient` plutôt que construire directement des requêtes HTTP vers Ollama.

---

## 2026-09-13 — Conservation de `ask()`

### Décision

La fonction :

```python
ask(prompt)
```

est conservée comme raccourci vers `LLMClient().ask(prompt)`.

### Raisons

* conserver une interface simple ;
* éviter de casser les tests et le code déjà développé ;
* permettre une transition progressive vers `LLMClient`.

Cette fonction pourra être supprimée ultérieurement si elle ne présente plus d'utilité.
