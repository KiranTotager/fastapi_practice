import aiomysql

async def get_db():
    pool = await aiomysql.create_pool(
        host="localhost",
        port=3306,
        user="root",
        password="kiran",
        db="fast_docker",
        minsize=1,
        maxsize=10,
        autocommit=True
    )
    try:
        yield pool
    finally:
        pool.close()
        await pool.wait_closed()
