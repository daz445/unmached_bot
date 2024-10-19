import asyncpg
from others import create_env
from decouple import config

async def get_data(table:str):
    try:
        config('user')
        

    except:
        print('Нет .env')
        create_env()  
            



    conn = await asyncpg.connect(user=config('user'),
                                password=config('password'),
                                database=config('database'), 
                                host=config('host'),
                                port=int(config('port'))
                                )
    values = await conn.fetch(
        f'SELECT * FROM {table} '
    )
    
    await conn.close()
    return values

async def create_person(name:str,player:str):
    conn = await asyncpg.connect(user=config('user'),
                                password=config('password'),
                                database=config('database'), 
                                host=config('host'),
                                port=int(config('port'))
                                )
    await conn.fetch(
        f"INSERT INTO heroes (player, hero) VALUES ('{player}','{name}');"
    )
    
    await conn.close()

async def create_map(player:str,map:str):
    conn = await asyncpg.connect(user=config('user'),
                                password=config('password'),
                                database=config('database'), 
                                host=config('host'),
                                port=int(config('port'))
                                )
    await conn.fetch(
        f"INSERT INTO maps (player, map) VALUES ('{player}','{map}');"
    )
    
    await conn.close()