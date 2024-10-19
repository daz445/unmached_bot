from get_data import GetData
import asyncio
from psql import get_data,create_person,create_map,create_table





if __name__ == '__main__':
    try:
        asyncio.run(get_data('heroes'))
    except:
        print("Create data table")
        asyncio.run(create_table('heroes','hero'))
        asyncio.run(create_table('maps','map'))

    if asyncio.run(get_data('heroes')) == []:
        for name,player in GetData('users.csv').get():
            asyncio.run(create_person(player,name))
    
    if asyncio.run(get_data('maps')) == []:
        for player,map in GetData('map.csv').get():
            asyncio.run(create_map(player,map))


    print("Export complete!")