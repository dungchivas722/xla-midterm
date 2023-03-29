from PIL import Image, ImageDraw, ImageFilter
import random

# Tạo ảnh mới với kích thước 1920x1080 và màu (204, 255, 229)
new_image = Image.new('RGB', (720, 720), (204, 255, 229))
new_image1 = Image.new('RGB', (720, 720), (204, 255, 229))
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
xoay4phantu = random.sample(other_positions, 4)
xoay2phantu = xoay4phantu[:2]
lat2phantu = xoay4phantu[2:]
other_positions1 = [item for item in other_positions if item not in xoay4phantu]
nhieu4phantu = random.sample(other_positions1, 4)
for item in nhieu4phantu:
    other_positions.remove(item)
nhieu2phantu = nhieu4phantu[:2]
mo2phantu = nhieu4phantu[2:]
khoanhtron = xoay4phantu + nhieu4phantu
for position in other_positions1:
    x, y, width, height, link = position
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))

    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
for position in lat2phantu:
    x, y, width, height, link = position
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))
    item_img = item_img.transpose(method=Image.FLIP_LEFT_RIGHT)

    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
for position in xoay2phantu:
    x, y, width, height, link = position

    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))
    angle = random.randint(0, 359)
    item_img = item_img.rotate(angle, expand=True)


    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
for position in nhieu2phantu:
    x, y, width, height, link = position
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))
    item_img = item_img.filter(ImageFilter.GaussianBlur(radius=0))
    l_channel = item_img.convert('L')
    mask = item_img.getchannel('A')
    item_img = Image.merge('RGBA', (l_channel, l_channel, l_channel, mask))
    new_image.paste(item_img, (x, y), mask=mask)
for position in mo2phantu:
    x, y, width, height, link = position
    item_img = Image.open(link).convert('RGBA')
    item_img = item_img.resize((width, height))
    # Tạo filter GaussianBlur với bán kính là 2
    blur_filter = ImageFilter.GaussianBlur(radius=1)

    # Áp dụng filter lên ảnh
    item_img = item_img.filter(blur_filter)
    # Tạo mặt nạ từ kênh alpha
    r, g, b, a = item_img.split()
    mask = Image.merge('L', (a,))
    # Vẽ vật phẩm lên hình ảnh mới
    new_image.paste(item_img, (x, y), mask=mask)
new_image.save('output/2-lv2.png')

for position in khoanhtron:
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
new_image.save('output/2-loigiailv2.png')

# img = Image.open('lv2.png')
# img1 = Image.open('loigiailv2.png')
# # Hiển thị ảnh
# img.show()
# img1.show()
print("Tạo lv2 thành công !")
