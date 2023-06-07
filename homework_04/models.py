"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    ForeignKey,
    create_engine,

)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    declared_attr,
    relationship,
)

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost:5433/postgres"
DB_ECHO = True

# sync_engine = create_engine(
#     url=PG_CONN_URI,
#     echo=DB_ECHO,
# )

engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(
        String(30),
        unique=False,
        nullable=False,
    )
    username = Column(
        String(30),
        unique=True,
        nullable=False,
    )
    email = Column(
        String(180),
        unique=True,
        nullable=False,
    )
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return f"User(id={self.id},\
         name={self.name}, \
         username={self.username}, \
         email={self.email}"

    def __repr__(self):
        return str(self)


class Post(Base):
    title = Column(
        String(180),
        nullable=False,
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",

    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return f"Post(id={self.id}, title={self.title}, user_id={self.user_id}"

    def __repr__(self):
        return str(self)
