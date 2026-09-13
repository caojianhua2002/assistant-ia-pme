# Journal du développement

## 2026-09-13

### Étape 1 — LLM local

L'environnement Python local du projet est opérationnel.

Configuration vérifiée :

```text
Python 3.14.3
Environnement virtuel : .venv
Ollama : fonctionnel
Modèle : qwen3:0.6b
```

La communication avec l'API Ollama fonctionne.

Un test réel a été effectué avec :

```text
Réponds uniquement par : OK
```

Réponse obtenue :

```text
OK
```

Le test automatisé initial a également réussi :

```text
1 passed
```

### Étape 2 — Interface LLM

Une première classe `LLMClient` a été ajoutée dans `src/llm.py`.

Elle permet de centraliser la communication avec Ollama et de rendre l'URL et le modèle configurables.

La fonction historique `ask()` a été conservée comme raccourci.

Un test direct avec :

```python
LLMClient().ask(...)
```

a retourné correctement :

```text
OK
```

Cette première version a ensuite été remplacée pour le nouveau code par `LLMInterface` et `OllamaLLM`, situés dans `src/assistant_ia/llm/`. Le test d'intégration actuel instancie `OllamaLLM` puis appelle sa méthode `ask()`.

Après audit de l'absence de référence à l'ancien module `src/llm.py`, à `LLMClient` et à la fonction de raccourci `ask()`, ce module a été supprimé. L'historique de cette première API reste conservé dans ce journal et dans les décisions d'architecture.

Le contrat a été stabilisé : `LLMInterface` définit `ask(prompt: str) -> str`, et `OllamaLLM` l'implémente. Des tests unitaires vérifient ce contrat, l'implémentation et la conservation de la configuration sans contacter Ollama.

### Étape 2 — Premier paramètre de génération

Un premier paramètre de génération, `temperature`, a été ajouté au constructeur de `OllamaLLM`. Lorsqu'il est défini, il est transmis à Ollama dans les options de la requête ; lorsqu'il est absent, le comportement par défaut d'Ollama est préservé.

Un test unitaire vérifie le contenu de la requête HTTP avec un service Ollama simulé.

Une limite facultative de longueur, `max_tokens`, a ensuite été ajoutée. Elle est transmise sous le nom `num_predict` attendu par l'API Ollama.

Un paramètre `seed` a été ajouté pour faciliter la répétition d'une démonstration avec les mêmes conditions de génération.

### Étape 2 — Erreurs LLM explicites

Les erreurs de connexion, les réponses HTTP en erreur et les réponses invalides sont désormais traduites en exceptions du projet. Les tests unitaires simulent ces trois situations sans appeler Ollama.

### Étape 2 — Validation des entrées

La configuration et le prompt sont vérifiés avant tout appel réseau. Une donnée invalide lève `LLMValidationError`, et les tests unitaires confirment que ces cas n'essaient pas de contacter Ollama.

### Fin de l'étape 2 — Interface LLM

L'interface `LLMInterface`, le fournisseur `OllamaLLM`, les paramètres utiles au démonstrateur, la gestion des erreurs et les tests sont en place. Les paramètres supplémentaires sont volontairement différés jusqu'à l'apparition d'un besoin concret.

### Documentation

Les fichiers suivants ont été mis à jour pour refléter l'état réel du projet :

* `PLAN.md`
* `README.md`
* `STATUS.md`
* `docs/decisions.md`
* `docs/journal.md`

### Prochaine étape

Commencer l'étape 3 : extraction des documents PDF.

### Étape 3 — Extraction PDF

La bibliothèque locale `pypdf` a été retenue et déclarée dans
`requirements.txt`. Le nouveau composant `PDFExtractor` lit un PDF et retourne
une entrée `PDFPage` par page : chemin du document, numéro de page humain (à
partir de 1) et texte extrait.

Un test crée un véritable PDF de deux pages, contenant le délai de paiement du
client Martin, puis vérifie l'extraction du texte et des futures métadonnées de
source. Des tests couvrent également un document absent et une extension non
PDF. Les PDF numérisés sans couche texte ne sont pas encore traités par OCR.

### Prochaine étape

Commencer l'étape 4 : découper et indexer les pages, puis mettre en place une
recherche par mots-clés.
