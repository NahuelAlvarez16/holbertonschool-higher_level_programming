#!/usr/bin/python3
"""
    Script that prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import sessionmaker, aliased
    from model_state import Base, State

    engine = create_engine("mysql://{}:{}@127.0.0.1/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%"))
    for row in states:
        session.delete(row)
    if states is not None:
        session.commit()
