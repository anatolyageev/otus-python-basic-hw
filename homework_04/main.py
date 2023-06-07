"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from jsonplaceholder_requests import get_json_data
from models import (
    Base,
    User,
    Post,
    engine,
    Session, )


async def create_all_users(async_session: AsyncSession, users: list):
    async_session.add_all(users)
    await async_session.commit()


async def create_all_posts(async_session: AsyncSession, posts: list):
    async_session.add_all(posts)
    await async_session.commit()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    user_data, post_data = await asyncio.gather(
        get_json_data("users"),
        get_json_data("posts")
    )

    # Create SQLAlchemy instances from each JSON object
    users = []
    posts = []
    for user in user_data:
        new_user = User(
            name=user['name'],
            username=user['username'],
            email=user["email"],
        )
        users.append(new_user)

    for post in post_data:
        new_post = Post(
            title=post['title'],
            body=post['body'],
            user_id=post["userId"],
        )
        posts.append(new_post)

    async with Session() as session:
        await create_all_users(session, users)
        await create_all_posts(session, posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
