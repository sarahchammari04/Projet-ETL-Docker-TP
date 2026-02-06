# Projet ETL Containerisé – FastAPI / Docker / Kubernetes

## L'objectif

Ce projet implémente un pipeline ETL simple (Extract – Transform – Load) entièrement containerisé et déployé avec Kubernetes.

Les données sont :
- Extraites depuis une API publique
- Transformées en Python
- Chargées dans une base SQLite
- Exposées via une API REST
- Consommées par un frontend web

---

## L'architecture

Le projet est structuré autour d’un pipeline ETL containerisé et orchestré avec Kubernetes.

Les données proviennent d’une API publique (JSONPlaceholder).
Le backend FastAPI envoie une requête HTTP vers cette API afin d’extraire les données (phase Extract).

Une fois les données récupérées, elles sont transformées dans le backend Python.
Cette transformation inclut le nettoyage des champs, la conversion des types et l’ajout d’un timestamp (phase Transform).

Les données transformées sont ensuite insérées dans une base SQLite persistée grâce à un volume Docker ou un PersistentVolumeClaim Kubernetes (phase Load).

Le backend expose ensuite plusieurs endpoints REST permettant de consulter les données chargées, de relancer l’ETL ou d’observer l’historique des exécutions.

Le frontend, servi par Nginx, communique avec le backend via le chemin /api.
Il permet à l’utilisateur de déclencher l’ETL et d’afficher les résultats directement dans le navigateur.

En environnement Kubernetes, les composants sont gérés par des Deployments, ce qui permet l’auto-réparation des pods en cas de suppression ou de panne.
Les données sont conservées grâce au PersistentVolumeClaim, garantissant la persistance même après redémarrage des pods.

---

## Les outils utilisés

- Python 3.11
- FastAPI
- SQLite
- Docker
- Docker Compose
- Kubernetes
- Nginx
- JavaScript (Frontend)

---

## La pipeline ETL

### Extract
Récupération des données depuis :
https://jsonplaceholder.typicode.com/posts

### Transform
- Nettoyage des champs
- Conversion des types
- Ajout d’un timestamp (loaded_at)

### Load
Insertion dans SQLite :
- Table `posts`
- Table `etl_runs` (historique des exécutions)

---

## Endpoints Backend

| Méthode | Endpoint | Description |
|----------|----------|-------------|
| GET | /health | Vérifie que l’API fonctionne |
| POST | /etl/run | Lance l’ETL |
| GET | /etl/preview?n=3 | Montre les données avant/après transformation |
| GET | /posts?limit=10 | Retourne les données chargées |
| GET | /stats | Nombre de lignes en base |
| GET | /etl/runs | Historique des exécutions ETL |

---

# Lancement en Docker Compose

```bash
docker compose up --build
