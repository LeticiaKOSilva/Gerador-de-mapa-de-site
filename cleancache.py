import os

def delete_pycache(dir):
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            if d == '__pycache__':
                pycache_dir = os.path.join(root, d)
                print('Removendo a pasta', pycache_dir)
                try:
                    os.system(f'rmdir /S /Q "{pycache_dir}"')
                except OSError as e:
                    print('Erro ao remover pasta', pycache_dir)
                    print(e)

current_dir = os.getcwd()
delete_pycache(current_dir)