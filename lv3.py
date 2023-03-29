from PIL import Image, ImageDraw, ImageFilter
import random

# Tạo ảnh mới với kích thước 1920x1080 và màu (204, 255, 229)
new_image = Image.new('RGB', (720, 720), (204, 255, 229))
other_positions = []
# Đọc file text và thêm các phần tử vào ảnh
with open('gamedata/datagoc.txt', 'r') as f:
    for line in f:
        x, y, width, height, filename = line.strip().split(',')
        img = Image.open(filename).convert('RGBA')
        img = img.resize((int(width), int(height)))
        mask = img.split()[3].resize((int(width), int(height)))
        other_positions.append((int(x), int(y),int(width), int(height), filename))
# Lưu ảnh mới với đường dẫn và tên file cần lưu
selected_positions = random.sample(other_positions, 8)
other_positions1 = [item for item in other_positions if item not in selected_positions]
for position in other_positions1:
    x, y, width, height, link = position
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))

    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
for position in selected_positions:
    x, y, width, height, link = position
    filename = link.split('/')[-1]  # Lấy tên file
    filename_fix = filename.split('.')[0] + ' -fix.png'  # Thêm -fix vào tên file
    link = link.replace(filename, filename_fix)
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))

    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
new_image.save('output/3-lv3.png')
for position in selected_positions:
    x, y, width, height, link = position

    # Tính tâm của ảnh trên hình ảnh mới
    center_x = x + width / 2
    center_y = y + height / 2

    # Tính bán kính của hình tròn
    radius = min(width, height) / 2

    # Tạo đối tượng ImageDraw
    draw = ImageDraw.Draw(new_image)

    # Vẽ hình tròn xung quanh tâm của ảnh
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline="red")
new_image.save('output/3-loigiailv3.png')


# # Hiển thị ảnh
# img = Image.open('lv3.png')
# img.show()
# img1 = Image.open('loigiailv3.png')
# img1.show()
print("Tạo lv3 thành công !")
print("Tạo đáp án lv1,lv2,lv3 thành công !")