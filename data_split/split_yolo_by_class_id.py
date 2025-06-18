import os
import shutil
import random

# Caminhos das pastas
train_images_folder = r'C:\Styles.AI\identification 2.0\data\train\images'
train_labels_folder = r'C:\Styles.AI\identification 2.0\data\train\labels'
valid_images_folder = r'C:\Styles.AI\identification 2.0\data\valid\images'
valid_labels_folder = r'C:\Styles.AI\identification 2.0\data\valid\labels'

# Cria as pastas de validação, se não existirem
os.makedirs(valid_images_folder, exist_ok=True)
os.makedirs(valid_labels_folder, exist_ok=True)

# Agrupa todos os arquivos disponíveis (treino e validação)
all_files = {}

# Função para coletar arquivos de uma pasta
def collect_files(images_folder, labels_folder):
    for label_file in os.listdir(labels_folder):
        if label_file == "classes.txt":
            continue  # Ignora o arquivo classes.txt

        label_path = os.path.join(labels_folder, label_file)
        image_path = os.path.join(images_folder, label_file.replace('.txt', '.jpg'))

        if not os.path.exists(image_path):
            image_path = os.path.join(images_folder, label_file.replace('.txt', '.jpeg'))

        if os.path.exists(label_path) and os.path.exists(image_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
                if not lines:
                    continue
                # Obtém a classe do primeiro valor de cada linha
                classes = [line.split()[0] for line in lines]
                main_class = classes[0]  # Supondo que todas as linhas têm a mesma classe

            if main_class not in all_files:
                all_files[main_class] = []
            all_files[main_class].append((image_path, label_path))

# Coleta arquivos de treino e validação
collect_files(train_images_folder, train_labels_folder)
collect_files(valid_images_folder, valid_labels_folder)

# Reorganiza arquivos em 80% treino e 20% validação
for class_id, files in all_files.items():
    random.shuffle(files)
    split_index = int(0.8 * len(files))

    train_files = files[:split_index]
    valid_files = files[split_index:]

    # Move arquivos de treino
    for image_path, label_path in train_files:
        if os.path.exists(image_path) and os.path.exists(label_path):
            image_dst = os.path.join(train_images_folder, os.path.basename(image_path))
            label_dst = os.path.join(train_labels_folder, os.path.basename(label_path))

            shutil.move(image_path, image_dst)
            shutil.move(label_path, label_dst)
        else:
            print(f"Arquivo ausente para treino: {image_path} ou {label_path}")

    # Move arquivos de validação
    for image_path, label_path in valid_files:
        if os.path.exists(image_path) and os.path.exists(label_path):
            image_dst = os.path.join(valid_images_folder, os.path.basename(image_path))
            label_dst = os.path.join(valid_labels_folder, os.path.basename(label_path))

            shutil.move(image_path, image_dst)
            shutil.move(label_path, label_dst)
        else:
            print(f"Arquivo ausente para validação: {image_path} ou {label_path}")

# Calcula as estatísticas reais com base nos arquivos nas pastas
stats = {}
for folder, label_folder in [(train_images_folder, train_labels_folder), (valid_images_folder, valid_labels_folder)]:
    for label_file in os.listdir(label_folder):
        if label_file == "classes.txt":
            continue

        label_path = os.path.join(label_folder, label_file)
        with open(label_path, 'r') as f:
            lines = f.readlines()
            if not lines:
                continue
            classes = [line.split()[0] for line in lines]
            main_class = classes[0]

        if main_class not in stats:
            stats[main_class] = {"train": 0, "valid": 0}
        if folder == train_images_folder:
            stats[main_class]["train"] += 1
        else:
            stats[main_class]["valid"] += 1

# Exibe as estatísticas corrigidas
print("Estatísticas por classe:")
for class_id, count in stats.items():
    print(f"Classe {class_id}: {count['train']} treino, {count['valid']} validação")

print("Separação concluída com sucesso!")
