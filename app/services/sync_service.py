from app.core.database import Base, engine
from app.models.launch import Launch
from app.core.database import SessionLocal
from app.clients.spacex_client import SpaceXClient


class SyncService:

    def run(self):
        # cria tabelas se não existirem
        Base.metadata.create_all(bind=engine)

        db = SessionLocal()

        try:
            launches = SpaceXClient().get_launches()

            inserted = 0

            for item in launches:
                exists = db.query(Launch).filter(
                    Launch.name == item["name"]
                ).first()

                if exists:
                    continue

                row = Launch(
                    name=item["name"],
                    date_utc=item["date_utc"],
                    success=item["success"]
                )

                db.add(row)
                inserted += 1

            db.commit()
            print(f"{inserted} launches inserted.")

        finally:
            db.close()