import os
import shutil
import cv2
import yaml
from ultralytics import YOLO

# Carregar os nomes das classes do arquivo YAML
yaml_path = r'C:\Styles.AI\identification 2.0\data.yaml'
with open(yaml_path, 'r') as file:
    class_names = yaml.safe_load(file)['names']  # Lista de nomes das classes

# Carregar o modelo YOLO
model = YOLO(r'C:\Styles.AI\identification 2.0\runs\detect\train58\weights\best.pt')

# Diretórios
input_folder = r'C:\Styles.AI\identification 2.0\data\GeneralData\waist'
train_images_folder = r'C:\Styles.AI\identification 2.0\data\train\images'
train_labels_folder = r'C:\Styles.AI\identification 2.0\data\train\labels'

# Certificar-se de que os diretórios de saída existem
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)

# Definir o tamanho fixo das imagens
fixed_width = 800
fixed_height = 990

# Função para desenhar bounding boxes na imagem
def draw_boxes(img, boxes, class_ids, confidences):
    for box, class_id, conf in zip(boxes, class_ids, confidences):
        x1, y1, x2, y2 = map(int, box)
        class_name = class_names[int(class_id)]  # Obter o nome da classe
        label = f"{class_name}: {conf:.2f}"
        color = (0, 255, 0)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return img

# Iterar sobre as imagens na pasta
for image_name in os.listdir(input_folder):
    if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_name)

        # Carregar a imagem
        img = cv2.imread(image_path)

        # Redimensionar a imagem para o tamanho fixo (800x996)
        img_resized = cv2.resize(img, (fixed_width, fixed_height))

        # Realizar a inferência
        results = model(img_resized)

        # Processar os resultados
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()  # Coordenadas dos bounding boxes
            confidences = result.boxes.conf.cpu().numpy()  # Confianças
            class_ids = result.boxes.cls.cpu().numpy()  # IDs das classes

            # Desenhar os bounding boxes na imagem redimensionada
            annotated_img = draw_boxes(img_resized.copy(), boxes, class_ids, confidences)

            # Mostrar a imagem anotada
            cv2.imshow("Anotação", annotated_img)
            key = cv2.waitKey(0)

            if key == ord('s'):  # Salvar se pressionar 's'
                # Mover a imagem para o diretório de treino
                shutil.move(image_path, os.path.join(train_images_folder, image_name))

                # Criar o arquivo de anotação correspondente
                label_file_path = os.path.join(train_labels_folder, f"{os.path.splitext(image_name)[0]}.txt")
                with open(label_file_path, 'w') as label_file:
                    for box, conf, class_id in zip(boxes, confidences, class_ids):
                        # Converter para o formato YOLO: classe, x_centro, y_centro, largura, altura
                        x_center = (box[0] + box[2]) / 2 / fixed_width
                        y_center = (box[1] + box[3]) / 2 / fixed_height
                        width = (box[2] - box[0]) / fixed_width
                        height = (box[3] - box[1]) / fixed_height
                        label_file.write(f"{int(class_id)} {x_center} {y_center} {width} {height}\n")
            elif key == ord('d'):  # Deletar imagem se pressionar 'd'
                print(f"Deletando {image_name}...")
                os.remove(image_path)
                break
            elif key == ord('q'):  # Sair se pressionar 'q'
                print("Saindo...")
                cv2.destroyAllWindows()
                exit()

        cv2.destroyAllWindows()

print("Processamento concluído. Todas as imagens e anotações foram salvas no diretório de treino.")
