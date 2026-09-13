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

Une classe `LLMClient` a été ajoutée dans `src/llm.py`.

Elle permet de centraliser la communication avec Ollama et de rendre l'URL et le modèle configurables.

La fonction historique `ask()` est conservée comme raccourci.

Un test direct avec :

```python
LLMClient().ask(...)
```

a retourné correctement :

```text
OK
```

Les tests actuels ont ensuite été complétés pour vérifier également la configuration du client.

Résultat attendu :

```text
2 passed
```

### Documentation

Les fichiers suivants ont été mis à jour pour refléter l'état réel du projet :

* `PLAN.md`
* `README.md`
* `STATUS.md`
* `docs/decisions.md`
* `docs/journal.md`

### Prochaine étape

Continuer l'étape 2 :

* renforcer les tests ;
* stabiliser l'interface `LLMClient` ;
* définir les paramètres utiles du LLM ;
* améliorer la gestion des erreurs ;

avant de commencer l'extraction des documents PDF.
