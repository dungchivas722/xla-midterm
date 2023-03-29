from PIL import Image
import random
import os

def check_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2):
        return True
    return False

def backtrack(bottom, images, positions, available_area):
    if len(images) == 0:
        return True
    image = images[0]
    random.shuffle(available_area)  # shuffle available areas to reduce bias
    for i in range(len(available_area)):
        x, y = available_area[i]
        if x + image.width > bottom.width or y + image.height > bottom.height:
            continue
        overlapping = False
        for pos in positions:
            if check_collision((x, y, image.width, image.height), pos):
                overlapping = True
                break
        if not overlapping:
            bottom.paste(image, (x, y), image)
            positions.append((x, y, image.width, image.height))
            if backtrack(bottom, images[1:], positions, available_area[:i] + available_area[i+1:]):
                return True
            positions.pop()
    return False

# Tạo danh sách tên các file png trong gamedata
clouds = ['gamedata/cloud1.png', 'gamedata/cloud2.png']
others = ['gamedata/origin/human1.png', 'gamedata/origin/human2.png', 'gamedata/origin/human3.png', 'gamedata/origin/human4.png', 'gamedata/origin/human5.png', 'gamedata/origin/human6.png','gamedata/origin/human7.png','gamedata/origin/human8.png','gamedata/origin/human9.png','gamedata/origin/human10.png','gamedata/origin/food1.png', 'gamedata/origin/food2.png', 'gamedata/origin/food3.png', 'gamedata/origin/food4.png', 'gamedata/origin/food5.png', 'gamedata/origin/food6.png', 'gamedata/origin/food7.png', 'gamedata/origin/food8.png', 'gamedata/origin/food9.png', 'gamedata/origin/food10.png', 'gamedata/origin/food11.png', 'gamedata/origin/food12.png']

# Tạo ảnh background với kích thước 1920x1080 và màu (204, 255, 229)
background = Image.new('RGBA', (720, 720), (204, 255, 229))


top = background.crop((0, 0, 720, 200))
bottom = background.crop((0, 200, 720, 720))
cloud_positions = []  # List lưu trữ vị trí đã chèn của các đám mây
other_positions = []


# Chèn 4 đám mây ngẫu nhiên phía trên ảnh
for i in range(10):
    t = random.choice(clouds)
    cloud = Image.open(t).convert('RGBA')
    r, g, b, a = cloud.split()
    bbox = a.getbbox()
    cloud = cloud.crop(bbox)
    cloud = cloud.resize((200, 100))
    x = random.randint(0, 720 - cloud.width)
    y = random.randint(0, 200 - cloud.height)
    overlapping = False
    for pos in cloud_positions:
        if abs(pos[0] - x) < cloud.width and abs(pos[1] - y) < cloud.height:
            overlapping = True
            break
    if overlapping:
        continue
    mask = Image.new('L', (cloud.width, cloud.height), 0)
    mask.putalpha(a.crop(bbox).resize((cloud.width, cloud.height)))
    top.paste(cloud, (x, y), mask)
    cloud_positions.append((x, y, cloud.width, cloud.height, t))

# chèn bất ki phía dưới ảnh

other_samples = random.sample(others, 12)
other_images = []
other_name = []
for sample in other_samples:
    image = Image.open(sample).convert('RGBA')
    r, g, b, a = image.split()
    bbox = a.getbbox()
    image = image.crop(bbox)
    image_basename = os.path.basename(sample)
    luuten = "gamedata/origin/" + image_basename
    if image_basename.startswith("human"):
        image = image.resize((100, 200))
    else:
        image = image.resize((100, 100))
    other_images.append(image)
    other_name.append(luuten)


other_positions = []
available_area = [(x, y) for y in range(600) for x in range(720)]
backtrack(bottom, other_images, other_positions, available_area)


# Chèn vùng con vào background
background.paste(top, (0, 0))
background.paste(bottom, (0, 200))
for i in range(len(other_positions)):
    x, y, w, h = other_positions[i]
    y += 200
    other_positions[i] = (x, y, w, h)
other_positions = [(*pos, name) for pos, name in zip(other_positions, other_name)]
other_positions = other_positions + cloud_positions
with open('gamedata/data.txt', 'w') as file:
    for pos in other_positions:
        line = f"{pos[0]},{pos[1]},{pos[2]},{pos[3]},{pos[4]}\n"
        file.write(line)
print(other_positions)
print("Tạo ảnh thành công !")
# background.save("origin.png")
# img = Image.open('origin.png')
# Hiển thị ảnh
# img.show()