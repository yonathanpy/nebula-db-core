from engine.database import Database
import click


@click.command()
@click.argument("dbfile")
def start(dbfile):

    db = Database(dbfile)

    print("Nebula DB interactive shell")

    while True:

        q = input("nebula> ")

        if q.strip() == "exit":
            break

        result = db.execute(q)

        print(result)


if __name__ == "__main__":
    start()
