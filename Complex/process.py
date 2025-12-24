import os
import base64

image_dir = './yao'

# 获取图片文件列表并排序
image_list = sorted([f for f in os.listdir(image_dir) 
                     if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))])

data_uri_list = []

for image_name in image_list:
    image_path = os.path.join(image_dir, image_name)
    print(f"处理中: {image_path}")
    
    # 检测图片类型
    ext = os.path.splitext(image_name)[1].lower()
    mime_type = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }.get(ext, 'image/jpeg')  # 默认使用jpeg
    
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        base64_data = base64.b64encode(image_data).decode('utf-8')
        
        # 生成完整的data URI格式
        data_uri = f"data:{mime_type};base64,{base64_data}"
        data_uri_list.append(data_uri)

# 生成可以直接复制到HTML的格式
output_lines = [
    "        const GIFT_IMAGES = ["
]

for i, data_uri in enumerate(data_uri_list):
    comma = "," if i < len(data_uri_list) - 1 else ""
    output_lines.append(f'            "{data_uri}"{comma}')

output_lines.append("        ];")

output_text = "\n".join(output_lines)

# 保存到文件
with open('gift_images_code.txt', 'w', encoding='utf-8') as f:
    f.write(output_text)

print(f"\n✅ 处理完成！共处理 {len(image_list)} 张图片")
print(f"\n📋 已生成 gift_images_code.txt")
print(f"\n💡 使用方法：")
print(f"   1. 打开 gift_images_code.txt")
print(f"   2. 复制全部内容")
print(f"   3. 粘贴到 christmas_tree8.html 的第85-94行，替换现有的 GIFT_IMAGES 数组")
print(f"\n✨ 完成后，HTML文件就是独立的，可以直接送人！")