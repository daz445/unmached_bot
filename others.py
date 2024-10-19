def create_env():
    steps = ['user','password','database','host','port']
    with open('.env','a') as f:
        for step in steps:
            name = input(f'Введите параметр для поля {step}=')
            f.write(step+'='+name+'\n')