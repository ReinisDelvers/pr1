import os
folder_path = r'\\ri.riga.lv\rag\Audzekni\rdelvers2\My Documents\GitHub\pr1\Bildes'
i = 1
for filename in os.listdir(folder_path):
    if filename.startswith('vista'):

        new_filename = f"vista{i}.png"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        i += 1
    if not os.path.exists(new_path):
            os.rename(old_path, new_path)
    else:
            print(f"Kļūda: {new_filename} jau eksistē.")