## 📸 Giới thiệu

Dự án này là một ứng dụng web được thiết kế để nhận diện ảnh, xác định xem ảnh có chứa nội dung 16+ (không phù hợp với trẻ dưới 16 tuổi) hay không. Ứng dụng sử dụng các mô hình học sâu tiên tiến để phân tích và đưa ra kết quả nhanh chóng.

## ✨ Tính năng

- ✅ **Nhận diện nội dung 16+**: Hiển thị kết quả rõ ràng liệu ảnh có phải là ảnh 16+ hay không.
- ⏱️ **Tốc độ nhận dạng**: Cung cấp thông tin về thời gian xử lý của mỗi lần phân tích.
- 🌐 **Trực quan API**: Giao diện đơn giản và dễ sử dụng để tương tác với API nhận diện.

## 🛠️ Công nghệ sử dụng

- 🧠 **Pre-train model CNN**: Sử dụng mạng nơ-ron tích chập (Convolutional Neural Network) được huấn luyện trước để phân tích hình ảnh.
- 🔧 **Fine-tuning model YOLO**: Tinh chỉnh mô hình YOLO (You Only Look Once) để tối ưu hóa hiệu suất nhận diện.
- ⚡ **Triển khai với FastAPI**: Framework nhanh và mạnh mẽ để xây dựng API hiệu quả.

## 📊 Dữ liệu

- 🤖 **Thu thập dữ liệu**: Sử dụng thư viện **Selenium** để tự động crawl và thu thập dữ liệu hình ảnh từ web.
- 🔗 **Link dữ liệu**: Xem bộ dữ liệu tại [Google Drive](https://drive.google.com/drive/folders/1WFXCRMUw7Pw0JI7nRGtm0wXDQPK7Cvx6?usp=drive_link).

## ⚙️ Cài đặt

Dưới đây là các bước để cài đặt và chạy dự án trên máy local:

```bash
# Clone repository từ GitHub
git clone https://github.com/ntthanh2603/ImageGuard.git

# Di chuyển vào thư mục dự án
cd ImageGuard

# Cài đặt các thư viện cần thiết
pip3 install -r requirements.txt

# Khởi chạy ứng dụng
python3 main.py
```

_Lưu ý_: Đảm bảo bạn đã cài đặt Python 3.8+ và các công cụ cần thiết như `git` trước khi bắt đầu.

## 🤝 Đóng góp

Chúng tôi rất hoan nghênh mọi đóng góp để cải thiện dự án! Để tham gia:

1. 🍴 Fork dự án về repository của bạn.
2. 🌿 Tạo một branch mới cho tính năng hoặc sửa lỗi (`git checkout -b feature/AmazingFeature`).
3. 💾 Commit các thay đổi của bạn (`git commit -m 'Add some AmazingFeature'`).
4. 🚀 Push branch lên repository của bạn (`git push origin feature/AmazingFeature`).
5. 📬 Mở một Pull Request trên GitHub và mô tả chi tiết những gì bạn đã thực hiện.

## 📜 License

Dự án được phát hành dưới **MIT License**. Xem chi tiết tại file [LICENSE.md](LICENSE.md).

## 📩 Liên hệ

Nếu bạn có câu hỏi hoặc muốn trao đổi, hãy liên hệ với tôi qua:

- 🌍 **Facebook**: [Nguyễn Tuấn Thành](https://www.facebook.com/ntthanh2603)
- ✉️ **Email**: tuanthanh2kk4@gmail.com (thay bằng email thật nếu cần).
