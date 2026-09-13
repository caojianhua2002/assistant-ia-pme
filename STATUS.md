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

Le contrat stabilisé est `ask(prompt: str) -> str` : chaque fournisseur reçoit un prompt textuel et retourne une réponse textuelle. `LLMInterface` reste abstraite ; `OllamaLLM` est l'implémentation concrète actuelle.

`OllamaLLM` accepte aussi un paramètre optionnel `temperature`. Lorsqu'il est renseigné, il est transmis à Ollama dans les options de génération. Lorsqu'il vaut `None` (valeur par défaut), aucune option n'est envoyée et le comportement par défaut d'Ollama est conservé.

`OllamaLLM` accepte également `max_tokens`, qui limite le nombre maximal de tokens générés. Cette option est transmise à l'API Ollama sous son nom `num_predict`. Comme `temperature`, elle reste absente de la requête lorsqu'elle vaut `None`.

Les erreurs exposées au reste du projet sont `LLMConnectionError` (service injoignable), `LLMRequestError` (erreur HTTP renvoyée par Ollama) et `LLMResponseError` (réponse invalide). Elles héritent toutes de `LLMError`.

`src/llm.py` existe encore et contient l'ancienne API `LLMClient` ainsi que la fonction de raccourci `ask()`. L'audit ne relève aucune importation de `src.llm`, `LLMClient` ou de cette fonction en dehors de ce module. Il est donc conservé provisoirement, sans être utilisé par le test actuel, jusqu'à une décision explicite de suppression.

### Tests

`tests/test_ollama.py` vérifie actuellement :

* qu'une requête réelle au LLM retourne une chaîne non vide ;
* que cette requête passe par une instance de `OllamaLLM`.
* que `LLMInterface` impose la méthode `ask()` et que `OllamaLLM` respecte ce contrat sans nécessiter de service Ollama.
* que les options `temperature` et `max_tokens` configurées sont bien envoyées dans la requête HTTP vers Ollama, sans contacter le service.
* que les erreurs de connexion, HTTP et de réponse sont traduites en erreurs LLM explicites, sans contacter le service.

Les tests unitaires vérifient aussi que l'URL et le modèle fournis au constructeur sont conservés. Il n'existe pas encore de test isolé de la requête HTTP vers Ollama.

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
2. évaluer les autres paramètres de génération utiles ;
3. valider les entrées et paramètres du fournisseur ;
4. préparer l'utilisation du LLM par les prochaines étapes du projet.

## Points restant à traiter

* L'ancien module `src/llm.py` reste à traiter après vérification complémentaire de son absence d'utilisateurs ; il ne doit pas être supprimé sans décision explicite.
* L'extraction PDF n'a pas encore commencé.
* Le RAG n'a pas encore été implémenté.
