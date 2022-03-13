import os
import asyncpg
import datetime
import asyncio
import logging
from pypika import Query
from sanic import Sanic, text

logging.basicConfig(level=logging.INFO)


app = Sanic("tirekick")

app.config.DATABASE_URL = os.environ.get("DATABASE_URL")


@app.get("/")
async def handler(request):
    q = Query.from_("ping").select("id")
    logging.info("Connecting to database")
    conn = await asyncpg.connect(app.config.DATABASE_URL)
    logging.info("Fetching database row")
    row = await conn.fetchrow(q.get_sql())
    logging.info(row)
    logging.info("Closing database connection")
    await conn.close()

    return text(str(row))


logging.info("Starting up 🤘")
app.run(host="0.0.0.0", port=8080, access_log=True)
# asyncio.get_event_loop().run_until_complete(main())
