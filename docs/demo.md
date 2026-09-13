# Assistant IA PME — Scénario de démonstration

## 1. Entreprise fictive

Le démonstrateur est construit autour d'une PME fictive :

**STP Services**

* Effectif : 25 salariés
* Activité : entreprise de services et de vente de produits
* Données utilisées : documents fictifs ou documents anonymisés servant uniquement à la démonstration.

L'objectif est de reproduire un environnement documentaire réaliste d'une PME.

## 2. Documents de démonstration

La base documentaire pourra contenir notamment :

* catalogue produits ;
* tarifs ;
* conditions générales de vente ;
* procédures SAV ;
* contrats clients ;
* documentation technique ;
* factures ;
* fichiers Excel ;
* autres documents administratifs utiles à la démonstration.

Les fichiers réels ou exemples disponibles seront intégrés progressivement afin de constituer un corpus représentatif.

## 3. Première démonstration — recherche documentaire

### Question

> Quel est le délai de paiement du client Martin ?

### Réponse attendue

> Le délai de paiement du client Martin est de 30 jours fin de mois.

### Sources attendues

* Contrat Martin — page 7
* Conditions générales — article 5

L'objectif est de démontrer que l'assistant :

1. comprend la question ;
2. recherche l'information dans plusieurs documents ;
3. fournit une réponse synthétique ;
4. cite précisément les sources utilisées.

## 4. Deuxième démonstration — données structurées

Une étape ultérieure permettra de connecter l'assistant à des données structurées, notamment les factures et les informations clients.

### Question

> Quels clients ont des factures échues ?

L'assistant devra interroger la base de données et identifier les factures correspondant aux critères d'échéance.

Cette fonction sera distincte de la simple recherche documentaire :

```text
Question
   │
   ▼
Compréhension de la demande
   │
   ▼
Interrogation de la base de données
   │
   ▼
Résultats
   │
   ▼
Réponse à l'utilisateur
```

## 5. Troisième démonstration — préparation d'une action

Une évolution ultérieure permettra de demander :

> Prépare les emails de relance.

L'assistant pourra alors :

1. identifier les clients concernés ;
2. récupérer les informations nécessaires ;
3. préparer un email de relance pour chaque client ;
4. présenter les emails à l'utilisateur ;
5. demander une confirmation explicite avant tout envoi.

### Principe de sécurité

La préparation d'une action et son exécution sont deux opérations distinctes.

```text
Utilisateur
    │
    ▼
"Prépare les emails de relance"
    │
    ▼
Assistant
    │
    ├── recherche les factures
    ├── identifie les clients
    └── prépare les emails
            │
            ▼
       Demande de confirmation
            │
       ┌────┴────┐
       │         │
      Oui       Non
       │         │
       ▼         ▼
    Envoi      Aucun envoi
```

L'assistant ne doit donc pas envoyer automatiquement un email simplement parce que l'utilisateur lui a demandé de le préparer.

## 6. Évolution du démonstrateur

Le projet évoluera progressivement :

```text
Documents
   │
   ▼
Recherche documentaire
   │
   ▼
RAG + sources
   │
   ▼
Données structurées
   │
   ▼
Actions préparées
   │
   ▼
Confirmation utilisateur
   │
   ▼
Exécution
```

Cette progression permet de commencer avec un assistant documentaire simple avant d'introduire des fonctions d'agent et des actions sur les systèmes de l'entreprise.

## 7. Objectif commercial de la démonstration

Le démonstrateur doit montrer à une PME une évolution concrète :

**1. Retrouver l'information**

> « Quel est le délai de paiement de Martin ? »

**2. Croiser les documents**

> « Donne-moi la réponse et les sources. »

**3. Interroger les données de l'entreprise**

> « Quels clients ont des factures échues ? »

**4. Préparer une action**

> « Prépare les emails de relance. »

**5. Garder l'humain dans la boucle**

> « Voici les emails préparés. Voulez-vous les envoyer ? »

L'objectif n'est donc pas uniquement de présenter un chatbot, mais de démontrer progressivement un **assistant IA métier pour PME**, capable de passer de la recherche d'information à la préparation d'actions tout en conservant une validation humaine avant les opérations sensibles.
