from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    # One-to-many relationship: one user → many notes
    notes = relationship("Note", back_populates="user")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    summary = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Connect back to the user
    user = relationship("User", back_populates="notes")
