# 🛠️ Interventions Service – Mini ERP MIF MAROC

Microservice FastAPI pour la gestion des interventions techniques dans le projet Mini ERP de MIF Maroc.

---

## 📌 Description

Ce microservice assure la gestion des interventions **correctives** et **préventives**, incluant la gestion des checklists, des fichiers joints, et les relations avec les techniciens, matériels et sites.

Il s’intègre à une architecture microservices (auth, clients, techniciens, matériels, rapports...).

---

## ✅ État d’avancement

- ✅ Modèles & schémas finalisés
- ✅ Routes sécurisées via JWT
- ✅ Services métier fonctionnels
- ✅ Dockerfile prêt
- ⚠️ Tests unitaires en cours de finalisation
- 🟡 Revue finale du service et déploiement à venir

---

## ⚙️ Fonctionnalités

- 🔐 Authentification JWT + rôles (`admin`, `technicien`)
- 🧾 CRUD complet sur les interventions
- 📋 Ajout de checklists associées à chaque intervention
- 📎 Attachments (documents, photos, etc.)
- 🔁 Relations avec `site`, `technicien`, `matériel`
- 🧪 Tests (`pytest`, `httpx`, `pytest-asyncio`) – partiellement validés

---

## 📂 Structure du projet

```

app/
├── main.py              # App FastAPI principale
├── config.py            # Configuration Pydantic Settings
├── database.py          # Connexion base de données
├── deps.py              # Dépendances (get\_db, sécurité)
├── security.py          # JWT, rôles, utilisateurs
├── models/              # Modèles SQLModel
├── schemas/             # Schémas Pydantic
├── routes/              # Endpoints FastAPI
├── services/            # Logique métier
├── tests/               # Tests unitaires en cours
├── Dockerfile           # Image Docker du service

````

---

## 🚀 Lancer en local

```bash
uvicorn app.main:app --reload
````

---

## 🧪 Lancer les tests

```bash
# Windows PowerShell
.venv\Scripts\activate
$env:PYTHONPATH = "."
pytest -v
```

---

## 🐳 Docker

```bash
docker build -t interventions_service .
docker run -p 8000:8000 interventions_service
```

---

## 🔐 Sécurité

* JWT (`python-jose`)
* Vérification de rôles avec dépendances (`Depends(admin_required)`)
* Hachage `passlib[bcrypt]`

---

## 🧠 Auteur

* 👤 **Rochdi**
* 📅 Mini ERP – Juillet 2025
* 🌐 MIF Maroc

---

## ⏳ À venir

* 🔄 Finalisation des tests unitaires
* 📦 Intégration continue (CI)

