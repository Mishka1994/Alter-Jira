from enum import Enum

from sqlalchemy import Column, Integer, String, Enum as EnumType


from config.db import Base


class TaskStatus(str, Enum):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'


class Task(Base):
    __tablename__: str = 'task'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(EnumType(TaskStatus), nullable=False)

    person_id = Column(Integer, nullable=False)
    # person = relationship('Person', back_populates='Task')
