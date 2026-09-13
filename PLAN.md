# Assistant IA PME — Plan

## Objectif

Construire progressivement un démonstrateur d'assistant IA privé destiné aux PME, capable à terme d'utiliser les documents de l'entreprise pour répondre aux questions avec des sources.

Le projet privilégie :

* l'exécution locale lorsque c'est possible ;
* la confidentialité des documents ;
* une architecture simple et modulaire ;
* des composants facilement remplaçables ;
* des tests à chaque étape.

## Progression

### Étape 1 — LLM local

**Statut : ✅ terminée**

* [x] Environnement Python local
* [x] Environnement virtuel `.venv`
* [x] Ollama fonctionnel
* [x] Modèle local `qwen3:0.6b`
* [x] Communication avec l'API Ollama
* [x] Premier test automatisé

### Étape 2 — Interface LLM

**Statut : 🔄 en cours**

* [x] Première fonction `ask()`
* [x] Définition de l'interface abstraite `LLMInterface`
* [x] Implémentation `OllamaLLM` de cette interface
* [x] Connexion configurable à Ollama
* [x] Modèle configurable
* [x] Test d'intégration avec `OllamaLLM`
* [x] Migration du test existant vers `OllamaLLM`
* [x] Stabiliser le contrat `LLMInterface.ask(prompt) -> str`
* [x] Ajouter le paramètre de génération `temperature`
* [x] Ajouter une limite de réponse avec `max_tokens`
* [ ] Évaluer les autres paramètres utiles de génération
* [ ] Améliorer la gestion des erreurs
* [ ] Finaliser les tests (dont tests unitaires sans dépendre d'Ollama)

### Étape 3 — Extraction PDF

**Statut : ⏳ à venir**

* [ ] Choix de la bibliothèque PDF
* [ ] Extraction du texte
* [ ] Gestion des documents contenant plusieurs pages
* [ ] Tests sur des documents réels

### Étape 4 — Recherche classique

**Statut : ⏳ à venir**

* [ ] Découpage du texte
* [ ] Indexation
* [ ] Recherche par mots-clés
* [ ] Tests de pertinence

### Étape 5 — Embeddings

**Statut : ⏳ à venir**

* [ ] Choix du modèle d'embeddings
* [ ] Génération des vecteurs
* [ ] Stockage
* [ ] Recherche sémantique

### Étape 6 — RAG

**Statut : ⏳ à venir**

* [ ] Recherche des passages pertinents
* [ ] Construction du contexte
* [ ] Envoi au LLM
* [ ] Réponse basée sur les documents

### Étape 7 — Réponse + sources

**Statut : ⏳ à venir**

* [ ] Génération d'une réponse
* [ ] Références aux documents utilisés
* [ ] Gestion des réponses insuffisamment documentées

### Étape 8 — Interface Web

**Statut : ⏳ à venir**

* [ ] Interface utilisateur
* [ ] Envoi de questions
* [ ] Affichage des réponses
* [ ] Affichage des sources

### Étape 9 — Stabilisation

**Statut : ⏳ à venir**

* [ ] Tests
* [ ] Gestion des erreurs
* [ ] Configuration
* [ ] Documentation
* [ ] Nettoyage du code

### Étape 10 — Démonstration client

**Statut : ⏳ à venir**

* [ ] Préparer un jeu de documents de démonstration
* [ ] Préparer des questions représentatives
* [ ] Démontrer le fonctionnement du RAG
* [ ] Présenter les avantages et limites
