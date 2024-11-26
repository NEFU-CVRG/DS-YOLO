import os
import cv2
import matplotlib.pyplot as plt

# 标签文件路径
label_path = 'your_pathl/labels'
# 图片文件路径
image_path = your_path/images'
# 保存可视化结果的路径
output_path = 'your_path/visualized'

# 创建保存可视化结果的文件夹
os.makedirs(output_path, exist_ok=True)

# 类别名称，可以根据你的数据集定义
class_names = ['Exposed_reinforcement', 'Ruststrain', 'Scaling', 'Spalling', 'crack', 'efflorescence']  # 修改为你的类别名称


# 读取标签文件并可视化
def visualize_labels(image_file, label_file, output_file):
    image = cv2.imread(image_file)
    height, width, _ = image.shape

    with open(label_file, 'r') as f:
        labels = f.readlines()

    for label in labels:
        label = label.strip().split()
        class_id = int(label[0])
        x_center, y_center, bbox_width, bbox_height = map(float, label[1:])

        # 将YOLO格式的标注转换为OpenCV格式
        x_center, y_center, bbox_width, bbox_height = (
        x_center * width, y_center * height, bbox_width * width, bbox_height * height)
        x_min = int(x_center - bbox_width / 2)
        y_min = int(y_center - bbox_height / 2)
        x_max = int(x_center + bbox_width / 2)
        y_max = int(y_center + bbox_height / 2)

        # 绘制边框和标签
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, class_names[class_id], (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 保存可视化结果
    cv2.imwrite(output_file, image)


# 遍历所有图片和标签文件
for image_file in os.listdir(image_path):
    if image_file.endswith('.jpg'):  # 确保只处理图片文件
        img_path = os.path.join(image_path, image_file)
        label_file = os.path.join(label_path, os.path.splitext(image_file)[0] + '.txt')

        if os.path.exists(label_file):
            output_file = os.path.join(output_path, image_file)
            visualize_labels(img_path, label_file, output_file)
            print(f"Processed and saved: {output_file}")
