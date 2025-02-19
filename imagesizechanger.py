from PIL import Image
import os
input_folder = r'\\ri.riga.lv\rag\Audzekni\rdelvers2\My Documents\GitHub\pr1\Bildes'
output_folder = r'\\ri.riga.lv\rag\Audzekni\rdelvers2\My Documents\GitHub\pr1\SmallBildes'  
desired_size = (10, 10)
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)
    try:
        with Image.open(input_path) as img:
            img.thumbnail(desired_size)
            img.save(output_path)
            print(f"Saved: {output_path}")
    except Exception as e:
        print(f"Skipping {filename}: {e}")