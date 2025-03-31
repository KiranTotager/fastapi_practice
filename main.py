import aiomysql
from fastapi import FastAPI,Depends
from db import get_db


app=FastAPI()

@app.get("/database/check")
async def database_check(pool:aiomysql.Pool=Depends(get_db)):
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("select * from docker_test")
            return await cursor.fetchall()
