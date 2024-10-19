from get_data import GetData
import asyncio
from psql import get_data


#test
asyncio.run(get_data('maps'))
asyncio.run(get_data('heroes'))

if __name__ == '__main__':
    print(4)