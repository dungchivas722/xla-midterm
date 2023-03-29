from PIL import Image,ImageDraw
import random

# Tạo ảnh mới với kích thước 1920x1080 và màu (204, 255, 229)
new_image = Image.new('RGB', (720, 720), (204, 255, 229))
new_image1 = Image.new('RGB', (720, 720), (204, 255, 229))
other_positions = []
# Đọc file text và thêm các phần tử vào ảnh
with open('gamedata/data.txt', 'r') as f:
    for line in f:
        x, y, width, height, filename = line.strip().split(',')
        img = Image.open(filename).convert('RGBA')
        img = img.resize((int(width), int(height)))
        mask = img.split()[3].resize((int(width), int(height)))
        other_positions.append((int(x), int(y),int(width), int(height), filename))
# Lưu ảnh mới với đường dẫn và tên file cần lưu
khoanhtron = []
tach4phantu = random.sample(other_positions, 4)
for item in tach4phantu:
    other_positions.remove(item)
an2phantu = tach4phantu[:2]
hien2phantu = tach4phantu[2:]
other_positions = other_positions + an2phantu
with open('gamedata/datagoc.txt', 'w') as file:
    for pos in other_positions:
        line = f"{pos[0]},{pos[1]},{pos[2]},{pos[3]},{pos[4]}\n"
        file.write(line)
for position in other_positions:
    x, y, width, height, link = position
    # Mở file ảnh vật phẩm và chuyển kích thước về giá trị cần thiết
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))
    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
new_image.save('output/0-anhgoc.png')



for item in an2phantu:
    other_positions.remove(item)
other_positions = other_positions + hien2phantu

thuphong4phantu = []
while len(thuphong4phantu) < 4:
    phantu_moi = random.choice(other_positions)
    if phantu_moi not in hien2phantu and phantu_moi not in thuphong4phantu:
        thuphong4phantu.append(phantu_moi)

khoanhtron = tach4phantu + thuphong4phantu
for position in other_positions:
    x, y, width, height, link = position
    # Nếu vật phẩm đang xử lý không nằm trong thuphong4phantu thì resize theo kích thước gốc
    if link not in [item[4] for item in thuphong4phantu]:
        item_img = Image.open(link)
        item_img = item_img.resize((width, height))
    else:
        item_img = Image.open(link)
        # Tạo hệ số ngẫu nhiên chỉ 0.5 hoặc 2
        scale_factor = random.choice([0.5, 1.5])

        # Tính kích thước mới dựa trên hệ số
        new_size = (int(width * scale_factor), int(height * scale_factor))

        # Thu nhỏ hoặc phóng to ảnh
        item_img = item_img.resize(new_size)
        # Tạo tuple mới chứa thông tin về vật phẩm đã resize
        new_item = (x, y, new_size[0], new_size[1], link)
        thuphong4phantu.append(new_item)

    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))

    # Vẽ vật phẩm lên hình ảnh mới
    new_image1.paste(item_img, (x, y), mask=mask)
new_image1.save('output/1-lv1.png')
#new_image1.show()


thuphong4phantu.pop(0)
thuphong4phantu.pop(0)
thuphong4phantu.pop(0)
thuphong4phantu.pop(0)
# print(thuphong4phantu)
# print(khoanhtron)
for position in khoanhtron:
    x, y, width, height, link = position

    # Tính tâm của ảnh trên hình ảnh mới
    center_x = x + width / 2
    center_y = y + height / 2

    # Tính bán kính của hình tròn
    radius = min(width, height) / 2

    # Tạo đối tượng ImageDraw
    draw = ImageDraw.Draw(new_image1)

    # Vẽ hình tròn xung quanh tâm của ảnh
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline="red")

# Lưu ảnh mới với đường dẫn và tên file cần lưu
new_image1.save('output/1-loigiailv1.png')
# Hiển thị ảnh
# new_image1.show()

# img = Image.open('anhgoc.png')
# # Hiển thị ảnh
# img.show()
print("Tạo lv1 thành công !")