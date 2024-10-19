
import asyncio
import asyncpg
from decouple import config

async def run():
    conn = await asyncpg.connect(user=config('user'), password=config('password'),
                                 database=config('database'), host=config('host'))
    values = await conn.fetch(
        'SELECT * FROM mytable WHERE id = $1',
        10,
    )
    await conn.close()

asyncio.run(run())




# async def get_user_data(user_id: int, table_name='users_reg'):
#     async with pg_manager:
#         user_info = await pg_manager.select_data(table_name=table_name, where_dict={'user_id': user_id}, one_dict=True)
#         if user_info:
#             return user_info
#         else:
#             return None


# async def get_user_data(user_id: int, table_name='users_reg'):
#     async with pg_manager:
#         user_info = await pg_manager.select_data(table_name=table_name, where_dict={'user_id': user_id}, one_dict=True)
#         if user_info:
#             return user_info
#         else:
#             return None