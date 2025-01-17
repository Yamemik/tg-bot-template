import os

import aiosqlite

from .config import config


async def create_db():
    async with aiosqlite.connect(config.name_database) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT
            )
        """)
        await db.commit()
        

async def add_user(telegram_id: int, username: str, first_name: str):
    async with aiosqlite.connect(config.name_database) as db:
        await db.execute("""
            INSERT INTO users (telegram_id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO NOTHING
        """, (telegram_id, username, first_name))
        await db.commit()
        
        
async def get_all_users():
    async with aiosqlite.connect(config.name_database) as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()

        # Преобразуем результаты в список словарей
        users = [
            {
                "telegram_id": row[0],
                "username": row[1],
                "first_name": row[2],
            }
            for row in rows
        ]
        return users
    
    
async def get_user_by_id(telegram_id: int):
    async with aiosqlite.connect(config.name_database) as db:
        cursor = await db.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()

        if row is None:
            return None

        # Преобразуем результат в словарь
        user = {
            "telegram_id": row[0],
            "username": row[1],
            "first_name": row[2],
        }
        return user
    