#!/usr/bin/python3
"""
    Script that prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import sessionmaker, aliased
    from model_state import Base, State

    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like("%a%")):
        print("{}: {}".format(state.id, state.name))
