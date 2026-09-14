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

Le paramètre optionnel `seed` est transmis tel quel à Ollama. Il permet de rendre les essais plus reproductibles à paramètres et prompt identiques.

Les erreurs exposées au reste du projet sont `LLMConnectionError` (service injoignable), `LLMRequestError` (erreur HTTP renvoyée par Ollama), `LLMResponseError` (réponse invalide) et `LLMValidationError` (entrée ou configuration invalide). Elles héritent toutes de `LLMError`.

### Tests

La suite de tests vérifie actuellement :

* qu'une requête réelle au LLM retourne une chaîne non vide ;
* que cette requête passe par une instance de `OllamaLLM`.
* que `LLMInterface` impose la méthode `ask()` et que `OllamaLLM` respecte ce contrat sans nécessiter de service Ollama.
* que les options `temperature`, `max_tokens` et `seed` configurées sont bien envoyées dans la requête HTTP vers Ollama, sans contacter le service.
* que les erreurs de connexion, HTTP et de réponse sont traduites en erreurs LLM explicites, sans contacter le service.
* qu'un prompt vide, ainsi qu'une configuration ou des paramètres invalides, sont refusés avant l'appel à Ollama.

Les tests unitaires vérifient aussi que l'URL, le modèle et les options fournis au constructeur sont conservés, ainsi que le contenu de la requête HTTP simulée.

## Tests

Dernier test exécuté :

```text
python -m pytest -v

16 passed
```

Un test appelle réellement Ollama ; les autres sont unitaires et n'appellent pas le service. La dernière exécution a réussi ; pytest a toutefois émis un avertissement de création de cache `.pytest_cache`, sans échec de test.

## Extraction PDF

L'étape 3 est terminée. La bibliothèque locale `pypdf` (version `6.18.1`) est
déclarée dans `requirements.txt`. `PDFExtractor` extrait le texte de chaque
page d'un fichier PDF et retourne des `PDFPage` contenant le chemin du
document, le numéro de page (à partir de 1) et le texte. Une page sans texte
est conservée afin de ne pas perdre les références de source.

Les erreurs de chemin absent, d'extension non-PDF et de lecture de PDF sont
exposées comme `PDFExtractionError`. Les tests génèrent un vrai PDF à deux
pages avec du texte extractible et vérifient le texte ainsi que les métadonnées
de source.

## Étape actuelle

**Étape 4 — Recherche classique**

Prochaines actions :

1. définir le découpage des pages en passages ;
2. indexer les passages ;
3. rechercher par mots-clés ;
4. vérifier la pertinence avec le scénario Martin.

## Points restant à traiter

* La recherche classique n'est pas encore implémentée.
* Les embeddings n'ont pas encore été implémentés.
* Le RAG n'a pas encore été implémenté.
