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

Le code métier ne doit pas dépendre directement de l'API HTTP d'Ollama.

---

## 2026-09-13 — Création de `LLMClient`

### Décision

La communication avec le LLM a d'abord été encapsulée dans `src/llm.py`, via la classe `LLMClient`.

### Raisons

L'application devait pouvoir évoluer sans que le code métier dépende directement de l'API HTTP d'Ollama.

Cette première interface permettait éventuellement de remplacer ou d'ajouter un autre moteur LLM ultérieurement.

### Conséquence historique

Le reste de l'application devait utiliser `LLMClient` plutôt que construire directement des requêtes HTTP vers Ollama.

### État actuel

Cette première encapsulation a été remplacée pour le nouveau code par l'interface `LLMInterface` et son implémentation `OllamaLLM`. Le fichier `src/llm.py` est toujours présent, mais aucune référence à `LLMClient`, `src.llm` ou à sa fonction `ask()` n'a été trouvée en dehors de ce fichier. Il est conservé provisoirement ; sa suppression reste une décision à prendre après vérification complémentaire.

---

## 2026-09-13 — Conservation de `ask()`

### Décision historique

La fonction `ask(prompt)` a été conservée dans `src/llm.py` comme raccourci vers `LLMClient().ask(prompt)`.

### Raisons

* conserver une interface simple ;
* éviter de casser les tests et le code déjà développé ;
* permettre une transition progressive vers `LLMClient`.

### État actuel

La fonction existe encore dans le module historique, mais aucun autre fichier du dépôt ne la référence. Le test actuel utilise `OllamaLLM().ask(...)`. La pertinence de conserver ce raccourci devra être réévaluée en même temps que le sort de `src/llm.py`.

---

## 2026-09-13 — Interface LLM indépendante du fournisseur

### Décision

Le contrat LLM est désormais défini par `LLMInterface` dans `src/assistant_ia/llm/interface.py`. Sa méthode publique est stabilisée à `ask(prompt: str) -> str`. `OllamaLLM`, dans `src/assistant_ia/llm/ollama.py`, implémente ce contrat et délègue les appels au service Ollama.

### Conséquence

Les futurs consommateurs du LLM doivent programmer contre `LLMInterface`. `OllamaLLM` est le fournisseur concret actuel.

---

## 2026-09-13 — Premier paramètre de génération

### Décision

`OllamaLLM` accepte un paramètre optionnel `temperature`. Il est transmis dans les options de la requête Ollama uniquement lorsqu'il est renseigné.

### Conséquence

La signature de `ask(prompt: str) -> str` reste inchangée. La configuration du comportement de génération relève du fournisseur concret, et l'absence de `temperature` conserve le comportement par défaut d'Ollama.

### Complément

Le fournisseur accepte aussi `max_tokens`, transmis à Ollama comme `num_predict`, afin de limiter la longueur maximale de la réponse.

---

## 2026-09-13 — Erreurs LLM explicites

### Décision

Les erreurs provenant d'Ollama sont traduites en exceptions du projet : `LLMConnectionError`, `LLMRequestError` et `LLMResponseError`. Elles héritent toutes de `LLMError`.

### Conséquence

Le reste de l'application peut gérer les échecs sans dépendre directement des exceptions HTTP de Python ou du format de réponse d'Ollama.

---

## 2026-09-13 — Validation avant appel à Ollama

### Décision

`OllamaLLM` valide sa configuration à la construction et valide le prompt avant d'envoyer une requête. Les données invalides lèvent `LLMValidationError`.

### Conséquence

Un prompt vide, une URL ou un modèle vide, une température non numérique et une valeur de `max_tokens` non positive sont détectés localement, sans appel HTTP.
