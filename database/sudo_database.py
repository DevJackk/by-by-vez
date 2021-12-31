from . import InitDB


class SudoDB(InitDB):
    async def get_sudos(self, chat_id: int):
        return [
            row[1]
            for row in await self.db.fetch_all(
                "select * from sudo_db where chat_id = :chat_id", {"chat_id": chat_id}
            )
        ]

    async def add_sudo(self, chat_id: int, user_id: int):
        await self.db.execute(
            "insert into sudo_db values (:chat_id, :user_id)",
            {"chat_id": chat_id, "user_id": user_id},
        )
        return "sudo_added"

    async def del_sudo(self, chat_id: int, user_id: int):
        await self.db.execute(
            "delete from sudo_db where chat_id = :chat_id and user_id = :user_id",
            {"chat_id": chat_id, "user_id": user_id},
        )
        return "sudo_deleted"

    async def del_all_sudos(self, chat_id: int):
        await self.db.execute(
            "delete from sudo_db where chat_id = :chat_id", {"chat_id": chat_id}
        )
        return "sudos_deleted"


sudo_db = SudoDB()
