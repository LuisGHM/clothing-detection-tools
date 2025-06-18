from PIL import Image
import os

def convert_webp_to_jpg(input_dir, output_dir):
    """
    Converte todas as imagens WEBP para JPG e deleta os arquivos WEBP originais.
    
    Args:
        input_dir (str): Caminho para a pasta com as imagens WEBP.
        output_dir (str): Caminho para a pasta onde serão salvas as imagens JPG.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        # Verifica se o arquivo é um WEBP
        if file_name.lower().endswith('.webp'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".jpg")
            
            try:
                # Abre a imagem WEBP e converte para JPG
                with Image.open(input_path) as img:
                    rgb_img = img.convert("RGB")  # Converte para RGB
                    rgb_img.save(output_path, "JPEG")  # Salva como JPG
                    print(f"Convertido: {file_name} -> {os.path.basename(output_path)}")
                
                # Deleta o arquivo WEBP após a conversão
                os.remove(input_path)
                print(f"Deletado: {file_name}")
            except Exception as e:
                print(f"Erro ao converter {file_name}: {e}")

# Diretórios de entrada e saída
input_directory = r"C:\Styles.AI\identification 2.0\data\GeneralData\backpacks"  # Substitua pelo caminho para as imagens WEBP
output_directory = r"C:\Styles.AI\identification 2.0\data\GeneralData\backpacks"  # Substitua pelo caminho para salvar as imagens JPG

# Executa a função
convert_webp_to_jpg(input_directory, output_directory)
