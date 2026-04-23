from app.core.database import SessionLocal
from app.models.launch import Launch


class DBService:

    def save_launches(self, rows):
        session = SessionLocal()

        try:
            for row in rows:
                exists = session.query(Launch).filter(
                    Launch.name == row["name"],
                    Launch.date_utc == row["date_utc"]
                ).first()

                if not exists:
                    session.add(
                        Launch(
                            name=row["name"],
                            date_utc=row["date_utc"],
                            success=row["success"]
                        )
                    )

            session.commit()

        finally:
            session.close()