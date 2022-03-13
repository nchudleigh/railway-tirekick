import os
import asyncpg
import datetime
import asyncio
from pypika import Query, 
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


q = Query.from_("ping").select("id")


DATABASE_URL = os.environ.get("DATABASE_URL")


async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    logging.info('Connecting to database')
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
    logging.info('Fetching database row')
    row = await conn.fetchrow(q.get_sql())
    print(row)
    logging.info(row)

    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    logging.info('Closing database connection')
    await conn.close()


logging.info('Starting up 🤘')

asyncio.get_event_loop().run_until_complete(main())
