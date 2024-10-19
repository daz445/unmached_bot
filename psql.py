

import asyncpg
from decouple import config

async def get_data(table:str):
    try:
        config('user')
        # создаем его
    except:
        print('Нет .env')



    conn = await asyncpg.connect(user=config('user'),
                                password=config('password'),
                                database=config('database'), 
                                host=config('host'),
                                port=int(config('port'))
                                )
    values = await conn.fetch(
        f'SELECT * FROM {table} '
    )
    print(values)
    await conn.close()