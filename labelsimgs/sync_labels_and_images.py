import os

def sync_images_and_labels(images_dir, labels_dir):
    # Extensões de imagem suportadas
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp"}
    
    # Obter nomes base das imagens (sem extensão)
    images = {os.path.splitext(f)[0] for f in os.listdir(images_dir) if os.path.splitext(f)[1].lower() in image_extensions}
    
    # Obter nomes base dos labels (sem extensão), exceto classes.txt
    labels = {os.path.splitext(f)[0] for f in os.listdir(labels_dir) if f != "classes.txt" and os.path.splitext(f)[1] == ".txt"}
    
    # Verificar imagens sem labels
    images_without_labels = images - labels
    if images_without_labels:
        print("Imagens sem labels correspondentes:")
        for img in images_without_labels:
            print(f" - {img}")
    
    # Verificar labels sem imagens
    labels_without_images = labels - images
    if labels_without_images:
        print("\nLabels sem imagens correspondentes (serão deletados):")
        for lbl in labels_without_images:
            print(f" - {lbl}.txt")
            label_path = os.path.join(labels_dir, f"{lbl}.txt")
            os.remove(label_path)
    
    # Resumo
    print("\nResumo:")
    print(f" - Total de imagens: {len(images)}")
    print(f" - Total de labels: {len(labels)}")
    print(f" - Imagens sem labels: {len(images_without_labels)}")
    print(f" - Labels deletados: {len(labels_without_images)}")

# Caminhos das pastas de imagens e labels
images_directory = r"C:\Styles.AI\identification 2.0\data\train\images"  # Substitua pelo caminho correto
labels_directory = r"C:\Styles.AI\identification 2.0\data\train\labels"  # Substitua pelo caminho correto

# Executar a função
sync_images_and_labels(images_directory, labels_directory)
