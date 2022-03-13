import os
import asyncpg
import datetime
import asyncio
from pypika import Query, Table, Field

q = Query.from_("ping").select("id")


DATABASE_URL = os.environ.get("DATABASE_URL")


async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect(DATABASE_URL)
    # Execute a statement to create a new table.
    # await conn.execute(q.get_sql())

    # Insert a record into the created table.
    # await conn.execute(
    #     """
    #     INSERT INTO users(name, dob) VALUES($1, $2)
    # """,
    #     "Bob",
    #     datetime.date(1984, 3, 1),
    # )

    # Select a row from the table.
    row = await conn.fetchrow(q.get_sql())
    print(row)

    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()


asyncio.get_event_loop().run_until_complete(main())
