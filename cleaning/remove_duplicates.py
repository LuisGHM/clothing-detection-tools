import os
import hashlib
from PIL import Image

def calculate_image_hash(image_path):
    """Calcula o hash de uma imagem usando SHA-256."""
    try:
        with Image.open(image_path) as img:
            # Redimensiona para um tamanho fixo (opcional, para maior eficiência)
            img = img.resize((256, 256)).convert('RGB')
            hash_obj = hashlib.sha256(img.tobytes())
            return hash_obj.hexdigest()
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")
        return None

def remove_duplicate_images(folder_path):
    """Remove imagens duplicadas em uma pasta."""
    if not os.path.exists(folder_path):
        print(f"A pasta '{folder_path}' não existe.")
        return
    
    hashes = {}  # Dicionário para armazenar hashes e caminhos
    duplicates = []  # Lista de imagens duplicadas

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_hash = calculate_image_hash(file_path)

            if image_hash:
                if image_hash in hashes:
                    print(f"Duplicado encontrado: {filename} (igual a {hashes[image_hash]})")
                    duplicates.append(file_path)
                else:
                    hashes[image_hash] = filename

    # Apaga os arquivos duplicados
    for duplicate in duplicates:
        try:
            os.remove(duplicate)
            print(f"Apagado: {duplicate}")
        except Exception as e:
            print(f"Erro ao apagar {duplicate}: {e}")

# Exemplo de uso
folder_path = r"C:\Styles.AI\classificationClothes\database\train\slides"
remove_duplicate_images(folder_path)
 