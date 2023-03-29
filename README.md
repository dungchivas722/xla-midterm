# Bài tập giữa kì xử lý ảnh 2223II- INT3404 1 - Văn Quốc Dũng - 19020530
# Bao gồm source code và file PDF
## Ảnh của trò chơi
### Ảnh đầu vào
![alt](https://github.com/dungchivas722/xla-midterm/blob/main/output/0-anhgoc.png)
## Thông tin file PDF ( lược bỏ ảnh minh họa ) :
Văn Quốc Dũng – 19020530 – Xử lý ảnh 

BÀI TẬP GIỮA KÌ

Giới thiệu qua về chức năng :
### File 1: Createpic.py
Đoạn code này được sử dụng để tạo một ảnh nền cho trò chơi với đám mây và các đối tượng bất kỳ được chèn vào phía dưới ảnh nền. Để làm điều này, đoạn mã sử dụng thư viện PIL (Python Imaging Library) để tạo và chỉnh sửa các hình ảnh.
Tạo danh sách tên các file png trong gamedata, danh sách clouds chứa tên các tệp hình ảnh đám mây được sử dụng để tạo ảnh nền, và danh sách others chứa tên các tệp hình ảnh đối tượng được sử dụng để chèn vào phía dưới ảnh nền.
Tạo ảnh background, ảnh nền có kích thước 720x720 và màu nền là màu xanh lá cây nhạt.
Tạo vùng top và bottom của ảnh , ảnh được chia thành hai phần, vùng top có kích thước 720x200 và vùng bottom có kích thước 720x520
Chèn đám mây vào vùng top, 4 đám mây ngẫu nhiên phía trên ảnh, chèn bất ki phía dưới ảnh
Sử dụng thuật toán giải thuật tìm điểm va chạm và thuật toán backtrack để tránh chồng ảnh khi tạo
=>	Ta được ảnh 720x720 gồm phía trên là đám mây và phía dưới là các vật ngẫu nhiên với số lượng vật từ 10-14 vật
### File 2: Lv1.py
Tạo cấp độ đầu tiên với 8 điểm khác nhau bằng cách chọn ra 8 vật từ ảnh gốc với đặc điểm :
-	ẩn 2 ảnh
-	hiện 2 ảnh
-	thu nhỏ 2 ảnh về kích thước 0.5
-	phóng to 2 ảnh x2
Đồng thời xác định vị trí thay đổi tính chất vật khoanh tròn nó đánh dấu
### File 3: Lv2.py
Tạo cấp độ thứ 2 với 8 điểm khác nhau bằng cách chọn ra 8 vật từ ảnh gốc với đặc điểm :
-	xoay 2 ảnh
-	lật 2 ảnh
-	nhiễu 2 ảnh
-	mờ 2 ảnh
Đồng thời xác định vị trí thay đổi tính chất vật khoanh tròn nó đánh dấu nó 
### File 4: Lv3.py
Tạo cấp độ thứ 3 với 8 điểm khác nhau bằng cách chọn ra 8 vật từ ảnh gốc với đặc điểm thay đổi tính chất vật , thay đổi màu sắc vật
Đồng thời xác định vị trí thay đổi tính chất vật khoanh tròn nó đánh dấu nó
### File 5 : main.py
Có chức năng thực thi tất cả các lệnh của 4 file còn lại và đưa ra màn hình thông báo , mỗi lần chạy file sẽ cho ra kết quả khác nhau và được lưu vào file output. Các ảnh gốc và lv1,lv2,lv3 đều được xác định vật và tạo 1 cách ngẫu nhiên nên kết quả mỗi lần chạy file sẽ đưa ra khác nhau.
Các ảnh khi được tạo sẽ được lưu vào folder output với cái tên :
-	0-anhgoc.png : ảnh được tạo ra ban đầu
-	1-lv1.png : ảnh trò chơi ứng với lv1
-	1-loigiailv1.png : các điểm đánh dấu trò chơi ứng với kết quả của lv1
-	2-lv2.png : ảnh trò chơi ứng với lv2
-	2-loigiailv2.png : các điểm đánh dấu trò chơi ứng với kết quả của lv2
-	3-lv3.png : ảnh trò chơi ứng với lv3
-	3-loigiailv3.png : các điểm đánh dấu trò chơi ứng với kết quả của lv3
 
