# tests/test_intervetions.py

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_intervention(async_client: AsyncClient, admin_token: str):
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {
        "titre": "Maintenance",
        "description": "Remplacement pièce",
        "statut": "en_attente",
        "site_id": 1,
        "technicien_id": 2,
        "materiel_id": 3
    }
    response = await async_client.post("/interventions/", json=payload, headers=headers)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_interventions_as_admin(async_client: AsyncClient, admin_token: str):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.get("/interventions/", headers=headers)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_intervention_by_id(async_client: AsyncClient, admin_token: str):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.get("/interventions/1", headers=headers)
    assert response.status_code in [200, 404]


@pytest.mark.asyncio
async def test_get_my_interventions_technicien(async_client: AsyncClient, technicien_token: str):
    headers = {"Authorization": f"Bearer {technicien_token}"}
    response = await async_client.get("/interventions/technicien/me", headers=headers)
    assert response.status_code in [200, 404]


@pytest.mark.asyncio
async def test_update_intervention(async_client: AsyncClient, admin_token: str):
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {"statut": "en_cours"}
    response = await async_client.put("/interventions/1", json=payload, headers=headers)
    assert response.status_code in [200, 404]


@pytest.mark.asyncio
async def test_add_checklist(async_client: AsyncClient, technicien_token: str):
    headers = {"Authorization": f"Bearer {technicien_token}"}
    payload = {
        "contenu": "Vérifier alimentation",
        "valide": False,
        "intervention_id": 1
    }
    response = await async_client.post("/interventions/checklist/", json=payload, headers=headers)
    assert response.status_code in [200, 404]


@pytest.mark.asyncio
async def test_add_attachment(async_client: AsyncClient, technicien_token: str):
    headers = {"Authorization": f"Bearer {technicien_token}"}
    payload = {
        "nom_fichier": "test.jpg",
        "url": "/static/test.jpg",
        "type": "photo",
        "intervention_id": 1
    }
    response = await async_client.post("/interventions/attachment/", json=payload, headers=headers)
    assert response.status_code in [200, 404]


@pytest.mark.asyncio
async def test_delete_intervention(async_client: AsyncClient, admin_token: str):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.delete("/interventions/1", headers=headers)
    assert response.status_code in [200, 404]
