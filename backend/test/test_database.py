# backend/tests/test_database.py
import pytest
from sqlalchemy import select

from backend.data.database import (
    get_user_by_email,
    create_user,
    get_all_users,
    delete_user,
)
from backend.data.models import User  # Valentine тоже можно протестировать


@pytest.mark.asyncio
async def test_create_and_get_user_by_email(db_session: AsyncSession):
    created = await create_user(
        db=db_session,
        name="Тестовый Юзер",
        email="test@example.com",
        password="secret123",
    )

    assert created.id is not None
    assert created.name == "Тестовый Юзер"
    assert created.email == "test@example.com"

    found = await get_user_by_email(db_session, "test@example.com")
    assert found is not None
    assert found.id == created.id


@pytest.mark.asyncio
async def test_get_all_users(db_session: AsyncSession):
    # Предварительно создаём двух пользователей
    await create_user(db_session, "Аня", "anya@example.com", "pass1")
    await create_user(db_session, "Борис", "boris@example.com", "pass2")

    users = await get_all_users(db_session)
    assert len(users) == 2
    emails = {u.email for u in users}
    assert "anya@example.com" in emails
    assert "boris@example.com" in emails


@pytest.mark.asyncio
async def test_delete_user(db_session: AsyncSession):
    user = await create_user(
        db_session, "Для удаления", "delete-me@example.com", "xxx"
    )
    assert user.id is not None

    deleted = await delete_user(db_session, user.id)
    assert deleted is not None
    assert deleted.email == "delete-me@example.com"

    # Проверяем, что удалён
    remaining = await get_user_by_email(db_session, "delete-me@example.com")
    assert remaining is None


@pytest.mark.asyncio
async def test_get_non_existing_user(db_session: AsyncSession):
    user = await get_user_by_email(db_session, "nonexistent@nope.com")
    assert user is None
