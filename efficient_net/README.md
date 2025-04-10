# Báo Cáo Phân Tích Mô Hình Phân Loại Ảnh

## 1. Giới Thiệu
Dự án này xây dựng một mô hình học sâu để phân loại ảnh thành ba nhãn: "Adult" (người lớn), "Normal" (bình thường), và "Violent" (bạo lực). Mô hình được huấn luyện và đánh giá dựa trên các kết quả đã cung cấp.

## 2. Quá Trình Huấn Luyện

### 2.1. Cấu Hình Huấn Luyện
- **Mô hình**: EfficientNet (giả định dựa trên ngữ cảnh phổ biến).
- **Số epoch**: 15.
- **Learning rate**: Không được cung cấp, giả định 0.001 (giá trị thông dụng).
- **Batch size**: Không được cung cấp, giả định 32 (giá trị thông dụng).
- **Optimizer**: Không được cung cấp, giả định Adam.
- **Loss function**: CrossEntropyLoss (giả định).
- **Kỹ thuật**: Early stopping với patience=15, lưu mô hình tốt nhất dựa trên validation accuracy.

### 2.2. Kết Quả Huấn Luyện
Dưới đây là kết quả loss và validation accuracy qua 15 epoch:

| Epoch | Loss   | Validation Accuracy |
|-------|--------|---------------------|
| 1     | 0.0717 | 92.22%              |
| 2     | 0.0538 | 94.07%              |
| 3     | 0.1081 | 94.81%              |
| 4     | 0.0841 | 94.07%              |
| 5     | 0.0389 | 94.44%              |
| 6     | 0.0457 | 93.33%              |
| 7     | 0.0366 | 91.85%              |
| 8     | 0.0690 | 94.07%              |
| 9     | 0.0506 | 94.81%              |
| 10    | 0.0343 | 94.07%              |
| 11    | 0.0427 | 95.56%              |
| 12    | 0.0330 | 95.19%              |
| 13    | 0.0633 | 94.07%              |
| 14    | 0.0721 | 91.48%              |
| 15    | 0.0583 | 94.81%              |

- **Mô hình tốt nhất**: Được lưu ở Epoch 11 với validation accuracy 95.56%.

### 2.3. Phân Tích Quá Trình Huấn Luyện
- **Xu hướng loss**: Loss dao động từ 0.0330 đến 0.1081, không giảm liên tục, cho thấy mô hình có thể gặp khó khăn trong việc tối ưu hóa ở một số giai đoạn.
- **Validation accuracy**: Tăng từ 92.22% lên 95.56%, nhưng dao động đáng kể (91.48% đến 95.56%). Các giá trị như 94.07% và 94.81% lặp lại nhiều lần, có thể do tập validation nhỏ, khiến thay đổi nhỏ trong dự đoán dẫn đến lặp giá trị accuracy.
- **Early stopping**: Với patience=15, mô hình tiếp tục chạy hết 15 epoch dù validation accuracy đạt đỉnh ở Epoch 11 (95.56%). Điều này cho thấy không có cải thiện đáng kể sau Epoch 11.

## 3. Đánh Giá Trên Tập Test

### 3.1. Kết Quả Tổng Quan
- **Test Accuracy**: 97.04%

### 3.2. Chỉ Số Chi Tiết Cho Từng Lớp
| Class   | Precision | Recall | F1-score |
|---------|-----------|--------|----------|
| Adult   | 1.0000    | 1.0000 | 1.0000   |
| Normal  | 0.9528    | 0.9712 | 0.9619   |
| Violent | 0.9595    | 0.9342 | 0.9467   |

### 3.3. Ma Trận Nhầm Lẫn
```
                        Predicted
                adult   normal violence
True    Adult       90        0        0
True   Normal        0      101        3
True  Violent        0        5       71
```

### 3.4. Phân Tích Kết Quả Test
- **Accuracy cao**: 97.04% cho thấy mô hình hoạt động xuất sắc trên tập test.
- **Lớp "Adult"**: Precision và recall đều đạt 1.0000, tức là không có nhầm lẫn nào với các lớp khác.
- **Lớp "Normal"**: Precision 0.9528 và recall 0.9712, với 3 ảnh bị nhầm thành "Violent".
- **Lớp "Violent"**: Precision 0.9595 và recall 0.9342, với 5 ảnh bị nhầm thành "Normal".
- **Ma trận nhầm lẫn**: Sự nhầm lẫn chủ yếu xảy ra giữa "Normal" và "Violent" (3 và 5 ảnh), không có nhầm lẫn với lớp "Adult".

## 4. Kết Luận và Đề Xuất

### 4.1. Kết Luận
- Mô hình đạt validation accuracy cao nhất 95.56% (Epoch 11) và test accuracy 97.04%, cho thấy hiệu suất tốt trong phân loại ảnh.
- Lớp "Adult" được phân loại hoàn hảo, trong khi "Normal" và "Violent" có nhầm lẫn nhỏ.

### 4.2. Đề Xuất Cải Thiện
- **Tăng cường dữ liệu**: Thu thập thêm ảnh cho "Normal" và "Violent" để giảm nhầm lẫn.
- **Điều chỉnh learning rate**: Áp dụng scheduler để giảm learning rate khi validation accuracy ngừng tăng.
- **Mở rộng tập validation**: Đảm bảo đánh giá chính xác hơn với tập dữ liệu lớn hơn.