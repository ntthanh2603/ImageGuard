# Báo Cáo Tổng Hợp So Sánh Các Mô Hình Phân Loại Ảnh

## 1. Tổng Quan Các Mô Hình

Báo cáo này tổng hợp và so sánh kết quả thực nghiệm của bốn mô hình phân loại ảnh khác nhau:

1. **EfficientNet**
2. **ResNet34**
3. **Vision Transformer (ViT)**
4. **YOLOv8n**

## 2. So Sánh Cấu Hình Huấn Luyện

| Thông số              | EfficientNet                | ResNet34               | Vision Transformer | YOLOv8n                |
| --------------------- | --------------------------- | ---------------------- | ------------------ | ---------------------- |
| **Số epochs**         | 15                          | 100                    | 100                | 10                     |
| **Learning rate**     | 0.001 (giả định)            | 0.1→0.01→0.001→0.0001  | 0.00001 (cố định)  | Schedule tăng-giảm     |
| **Kỹ thuật đặc biệt** | Early stopping (patience=5) | Learning rate schedule | Không              | Learning rate schedule |

## 3. So Sánh Kết Quả Thực Nghiệm

### 3.1. Độ Chính Xác Cao Nhất

| Mô hình            | Accuracy Cao Nhất | Trên Tập Dữ Liệu | Thời Điểm       |
| ------------------ | ----------------- | ---------------- | --------------- |
| EfficientNet       | 97.04%            | Test             | Epoch 11 (best) |
| ResNet34           | 80.74%            | Test             | Sau 100 epochs  |
| Vision Transformer | 74.81%            | Test             | Sau 100 epochs  |
| YOLOv8n            | 95.9%             | Test             | Epoch 10        |

### 3.2. Diễn Biến Loss

| Mô hình            | Loss Ban Đầu | Loss Cuối Cùng | Đặc Điểm                                 |
| ------------------ | ------------ | -------------- | ---------------------------------------- |
| EfficientNet       | 0.0717       | 0.0583         | Dao động không đều từ 0.0330-0.1081      |
| ResNet34           | 4.41         | 0.4341         | Giảm theo các giai đoạn LR, ổn định cuối |
| Vision Transformer | 1.073        | 0.0004         | Giảm đều, hội tụ gần 0                   |
| YOLOv8n            | 0.83442      | 0.07431        | Giảm nhanh và ổn định                    |

### 3.3. Thời Gian Huấn Luyện và Hiệu Suất

| Mô hình            | Thời Gian Huấn Luyện | Hiệu Suất Inference | Hội Tụ Nhanh               |
| ------------------ | -------------------- | ------------------- | -------------------------- |
| EfficientNet       | Không rõ             | Không rõ            | Đạt >92% từ epoch đầu      |
| ResNet34           | Không rõ             | Không rõ            | Giảm loss chậm, ổn định    |
| Vision Transformer | Không rõ             | Không rõ            | Giảm loss đều, cuối hội tụ |
| YOLOv8n            | Ngắn (10 epochs)     | 17.4ms/ảnh          | Đạt >90% chỉ sau 2 epochs  |

## 4. Phân Tích Chi Tiết Theo Lớp

### 4.1. Metrics Theo Lớp của EfficientNet

| Class   | Precision | Recall | F1-score |
| ------- | --------- | ------ | -------- |
| Adult   | 1.0000    | 1.0000 | 1.0000   |
| Normal  | 0.9528    | 0.9712 | 0.9619   |
| Violent | 0.9595    | 0.9342 | 0.9467   |

### 4.2. Ma Trận Nhầm Lẫn của EfficientNet

```
                        Predicted
                adult   normal violence
True    Adult       90        0        0
True   Normal        0      101        3
True  Violent        0        5       71
```

### 4.3. Metrics Các Mô Hình Khác

- **ResNet34**: Chỉ báo cáo accuracy tổng thể (80.74%), không có metrics chi tiết theo lớp
- **Vision Transformer**: Chỉ báo cáo accuracy tổng thể (74.81%), không có metrics chi tiết theo lớp
- **YOLOv8n**: Báo cáo Top-1 Accuracy (95.9%) và Top-5 Accuracy (100%)

## 5. So Sánh Đặc Trưng và Ưu Điểm

### 5.1. EfficientNet

- **Ưu điểm**: Accuracy cao nhất (97.04%), phân loại hoàn hảo lớp "Adult"
- **Đặc trưng**: Validation accuracy dao động nhiều, loss không giảm đều

### 5.2. ResNet34

- **Ưu điểm**: Learning rate schedule hiệu quả
- **Đặc trưng**: Huấn luyện ổn định, không có dao động loss đột ngột

### 5.3. Vision Transformer

- **Ưu điểm**: Loss huấn luyện giảm xuống gần 0 (0.0004)
- **Đặc trưng**: Hiệu suất thấp (74.81%) cho thấy có thể overfitting

### 5.4. YOLOv8n

- **Ưu điểm**: Hội tụ nhanh, tốc độ inference cao (17.4ms/ảnh)
- **Đặc trưng**: Hiệu quả cao với số lượng epochs ít (10)

## 6. So Sánh Hiệu Suất Tổng Thể

| Tiêu Chí                | EfficientNet       | ResNet34             | Vision Transformer | YOLOv8n            |
| ----------------------- | ------------------ | -------------------- | ------------------ | ------------------ |
| **Accuracy**            | ★★★★★ (97.04%)     | ★★★☆☆ (80.74%)       | ★★☆☆☆ (74.81%)     | ★★★★★ (95.9%)      |
| **Tốc độ hội tụ**       | ★★★★☆ (15 epochs)  | ★★☆☆☆ (100 epochs)   | ★★☆☆☆ (100 epochs) | ★★★★★ (10 epochs)  |
| **Ổn định loss**        | ★★☆☆☆ (dao động)   | ★★★★☆ (giảm ổn định) | ★★★★★ (giảm đều)   | ★★★★☆ (giảm nhanh) |
| **Thời gian inference** | Không có thông tin | Không có thông tin   | Không có thông tin | ★★★★★ (17.4ms/ảnh) |
| **Đánh giá chung**      | ★★★★★              | ★★★☆☆                | ★★☆☆☆              | ★★★★★              |

## 7. Kết Luận và Đề Xuất

### 7.1. Kết Luận Tổng Quan

Từ kết quả thực nghiệm của cả bốn mô hình, có thể rút ra những kết luận sau:

1. **EfficientNet** và **YOLOv8n** là hai mô hình hiệu quả nhất với độ chính xác >95% trên tập test, phù hợp cho bài toán phân loại ảnh theo nội dung.

2. **ResNet34** có hiệu suất trung bình (80.74%) nhưng quá trình huấn luyện ổn định, có thể cần thêm tối ưu hóa.

3. **Vision Transformer** có hiệu suất thấp nhất (74.81%) trên tập dữ liệu MNIST, cho thấy kiến trúc transformer có thể chưa phù hợp với dữ liệu đơn giản hoặc cần điều chỉnh thêm hyperparameters.

4. **YOLOv8n** nổi bật với khả năng hội tụ nhanh (chỉ 10 epochs) và tốc độ inference cao, phù hợp cho ứng dụng thực tế và xử lý thời gian thực.

### 7.2. Đề Xuất Cải Thiện

#### Cho EfficientNet:

- Tăng cường dữ liệu cho lớp "Normal" và "Violent" để giảm nhầm lẫn
- Áp dụng learning rate scheduler để ổn định quá trình huấn luyện

#### Cho ResNet34:

- Tối ưu hóa learning rate schedule
- Áp dụng thêm kỹ thuật regularization (dropout, weight decay)
- Thử nghiệm với kiến trúc lớn hơn (ResNet50, ResNet101)

#### Cho Vision Transformer:

- Áp dụng regularization để tránh overfitting
- Thử nghiệm với learning rate schedule thay vì cố định
- Điều chỉnh hyperparameters (số layer, head attention, kích thước patch)

#### Cho YOLOv8n:

- Tối ưu hóa tập dữ liệu (tăng số lượng mẫu khó)
- Điều chỉnh siêu tham số để giảm biến động val loss

### 7.3. Lựa Chọn Mô Hình Theo Bài Toán

- **Cần độ chính xác cao nhất**: EfficientNet (97.04%)
- **Cần tốc độ xử lý nhanh**: YOLOv8n (17.4ms/ảnh)
- **Ứng dụng thực tế cân bằng**: YOLOv8n (95.9% accuracy, 10 epochs, inference nhanh)
- **Dữ liệu phức tạp với nhiều chi tiết**: ResNet34 với learning rate schedule
- **Dữ liệu cấu trúc không gian phức tạp**: Vision Transformer (sau khi tối ưu hóa)

## 8. Tài Liệu Tham Khảo

1. Báo cáo phân tích mô hình EfficientNet phân loại ảnh thành ba nhãn
2. Báo cáo kết quả thực nghiệm mô hình ResNet34
3. Báo cáo kết quả thực nghiệm mô hình Vision Transformer
4. Báo cáo phân tích hiệu suất dự án phân loại ảnh 16+ sử dụng mô hình YOLOv8n
