#!/usr/bin/python3
"""
    Script 14-model_city_fetch_by_state.py that prints all City\
        objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import sessionmaker, aliased
    from model_city import Base, City
    from model_state import Base, State

    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for row in cities:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))