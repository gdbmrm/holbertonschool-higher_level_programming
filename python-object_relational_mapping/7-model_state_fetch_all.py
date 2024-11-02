#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State

DATABASE_URI = 'mysql+mysqldb://root:root@localhost/staes'
engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all()
for state in states:
    print(f"{state.id}: {state.name}")
