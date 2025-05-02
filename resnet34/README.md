# Báo cáo kết quả thực nghiệm mô hình ResNet34

## 1. Tổng quan

Báo cáo này trình bày kết quả thực nghiệm của mô hình ResNet34 trên tập dữ liệu kiểm thử. ResNet34 là một kiến trúc mạng neural tích chập sâu (CNN) với các kết nối tắt (skip connections), cho phép huấn luyện mạng sâu hơn mà không gặp vấn đề tiêu biến gradient.

## 2. Quá trình huấn luyện

### 2.1. Cấu hình huấn luyện

- **Số lượng epoch**: 100
- **Tốc độ học (Learning rate)**: Schedule giảm dần
  - Epoch 1-29: LR = 0.1
  - Epoch 30-59: LR = 0.01
  - Epoch 60-89: LR = 0.001
  - Epoch 90-100: LR = 0.0001

### 2.2. Diễn biến loss qua các epoch

| Giai đoạn | Epoch  | Tốc độ học | Đặc điểm loss                  |
| --------- | ------ | ---------- | ------------------------------ |
| Đầu       | 1-29   | 0.1        | Giảm nhanh từ 4.41 xuống 0.596 |
| Giữa 1    | 30-59  | 0.01       | Giảm chậm từ 0.601 xuống 0.487 |
| Giữa 2    | 60-89  | 0.001      | Giảm nhẹ từ 0.475 xuống 0.430  |
| Cuối      | 90-100 | 0.0001     | Dao động nhẹ quanh 0.42        |

Đặc biệt:

- Giảm mạnh nhất tại epoch đầu tiên: từ 4.41 xuống 1.046
- Sau mỗi lần giảm learning rate, loss đều có xu hướng giảm đáng kể
- Cuối quá trình huấn luyện, loss ổn định quanh mức 0.41-0.43

## 3. Kết quả đánh giá

### 3.1. Hiệu suất trên tập kiểm thử

- **Độ chính xác (Accuracy)**: 80.74% trên tập kiểm thử

### 3.2. Phân tích quá trình huấn luyện

Biểu đồ loss cho thấy:

- Mô hình hội tụ tương đối tốt, với đường loss giảm mạnh trong giai đoạn đầu
- Learning rate schedule hiệu quả, tạo ra các "bước nhảy" giúp model thoát khỏi các điểm cực tiểu cục bộ
- Giai đoạn cuối (epoch 60-100) loss giảm chậm và có xu hướng dao động, cho thấy mô hình đã gần đạt trạng thái hội tụ

## 4. Nhận xét và đánh giá

### 4.1. Ưu điểm

- **Hiệu suất tốt**: Độ chính xác 80.74% trên tập kiểm thử
- **Learning rate schedule hiệu quả**: Giúp mô hình hội tụ tốt hơn
- **Ổn định trong quá trình huấn luyện**: Không có sự tăng đột biến của loss

### 4.2. Chi tiết quan trọng

- Giai đoạn đầu (epoch 1-10) có sự giảm loss nhanh chóng từ 4.41 xuống 0.82
- Sau khi giảm learning rate xuống 0.01 tại epoch 30, loss giảm từ 0.601 xuống 0.512
- Tương tự, tại epoch 60 và 90, loss cũng có xu hướng giảm sau khi điều chỉnh learning rate
- Trong giai đoạn cuối, mặc dù learning rate rất nhỏ (0.0001), loss vẫn dao động nhẹ quanh mức 0.41-0.43

### 4.3. Đánh giá chung

- ResNet34 thể hiện sự hiệu quả với độ chính xác 80.74%
- Learning rate schedule đã đóng vai trò quan trọng trong việc tối ưu hóa quá trình học
- Loss cuối cùng (0.4341) không quá thấp, cho thấy mô hình vẫn có thể cải thiện thêm

## 5. Đề xuất cải thiện

1. **Tối ưu hóa learning rate schedule**:

   - Thử nghiệm với các giá trị learning rate khác nhau
   - Áp dụng learning rate cyclical hoặc cosine annealing

2. **Áp dụng các kỹ thuật regularization**:

   - Dropout
   - Weight decay
   - Data augmentation mạnh hơn

3. **Điều chỉnh kiến trúc mô hình**:

   - Thử nghiệm với các phiên bản khác của ResNet (ResNet50, ResNet101)
   - Kết hợp với các kỹ thuật Attention

4. **Huấn luyện lâu hơn**:
   - Tăng số lượng epoch với learning rate thấp hơn
   - Áp dụng early stopping để tránh overfitting

## 6. Kết luận

Mô hình ResNet34 đã được huấn luyện thành công qua 100 epoch với schedule learning rate. Mô hình đạt được độ chính xác 80.74% trên tập kiểm thử, thể hiện hiệu suất tương đối tốt. Quá trình huấn luyện ổn định với loss giảm từ 4.41 xuống còn 0.4341.

ResNet34 với các kết nối tắt đã chứng minh tính hiệu quả trong việc xử lý bài toán phân loại, và có thể được cải thiện thêm bằng các kỹ thuật tối ưu hóa đã đề xuất.
