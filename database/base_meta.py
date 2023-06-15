import sqlalchemy.ext.declarative as dec
import sqlalchemy as sa
import sqlalchemy.orm as orm

__factory = None
Base = dec.declarative_base()


def global_init(db_file):
    global __factory
    if __factory:
        return
    if not db_file:
        raise AttributeError("nenenenen")
    connection_string = f'sqlite:///{db_file}'
    print(f"podkluchenie k bd:{connection_string}")

    engine = sa.create_engine(connection_string, echo=True)
    __factory = orm.sessionmaker(engine)


def create_session():
    return __factory()
