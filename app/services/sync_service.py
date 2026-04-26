from datetime import datetime

from app.clients.spacex_client import SpaceXClient
from app.core.database import SessionLocal
from app.models.launch import Launch


class SyncService:

    def run(self):
        client = SpaceXClient()
        launches = client.get_launches()

        db = SessionLocal()

        try:
            for item in launches:
                exists = db.query(Launch).filter(
                    Launch.name == item["name"]
                ).first()

                if exists:
                    continue

                db.add(
                    Launch(
                        name=item["name"],
                        date_utc=datetime.fromisoformat(
                            item["date_utc"].replace("Z", "+00:00")
                        ),
                        success=item["success"]
                    )
                )

            db.commit()

        finally:
            db.close()