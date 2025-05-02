# Báo cáo kết quả thực nghiệm mô hình Vision Transformer

## 1. Tổng quan

Báo cáo này trình bày kết quả thực nghiệm của mô hình Vision Transformer (ViT) trên tập dữ liệu MNIST. Vision Transformer là một kiến trúc mạng thần kinh dựa trên cơ chế Attention, đã chứng minh hiệu quả trong các tác vụ phân loại hình ảnh.

## 2. Quá trình huấn luyện

### 2.1. Cấu hình huấn luyện

- **Số lượng epoch**: 100
- **Tốc độ học (Learning rate)**: 0.00001 (cố định)
- **Tập dữ liệu**: MNIST

### 2.2. Diễn biến loss qua các epoch

Dựa vào dữ liệu huấn luyện và biểu đồ, ta có thể quan sát:

| Giai đoạn | Epoch  | Đặc điểm loss                      |
| --------- | ------ | ---------------------------------- |
| Đầu       | 1-20   | Giảm nhanh từ 1.073 xuống 0.609    |
| Giữa      | 21-60  | Tiếp tục giảm từ 0.578 xuống 0.055 |
| Cuối      | 61-100 | Hội tụ về gần 0 (khoảng 0.0004)    |

Đặc biệt:

- Epoch 80-100: Loss duy trì ở mức rất thấp (0.0004-0.0017), cho thấy mô hình đã hội tụ
- Một số dao động nhẹ tại epoch 69-72 với loss tăng lên 0.1075 tại epoch 70

## 3. Kết quả đánh giá

### 3.1. Hiệu suất trên tập kiểm thử

- **Độ chính xác (Accuracy)**: 74.81% trên tập kiểm thử MNIST

### 3.2. Phân tích quá trình huấn luyện

Biểu đồ loss cho thấy:

- Mô hình hội tụ tốt, với đường loss giảm đều
- Giai đoạn ban đầu (epoch 1-40) có tốc độ học tập cao nhất
- Sau epoch 80, mô hình đã đạt trạng thái ổn định, không cải thiện thêm đáng kể

## 4. Nhận xét và đánh giá

### 4.1. Ưu điểm

- Quá trình hội tụ mượt mà, loss giảm đều và ổn định
- Mô hình đạt được loss rất thấp (0.0004) sau 100 epoch, cho thấy khả năng học tốt trên tập huấn luyện

### 4.2. Hạn chế

- Accuracy trên tập kiểm thử (74.81%) không quá cao cho tập dữ liệu MNIST
- Có sự chênh lệch lớn giữa loss huấn luyện (gần 0) và độ chính xác kiểm thử (74.81%), gợi ý có thể xảy ra hiện tượng overfitting

### 4.3. Đề xuất cải thiện

- Áp dụng các kỹ thuật regularization như Dropout, Data Augmentation
- Thử nghiệm với learning rate schedule thay vì giữ cố định ở 0.00001
- Điều chỉnh hyperparameter của ViT (số lượng layer, số head attention, kích thước patch)
- Sử dụng Early Stopping để tránh overfitting

## 5. Kết luận

Mô hình Vision Transformer đã được huấn luyện thành công trên tập dữ liệu MNIST qua 100 epoch. Mô hình đạt được loss rất thấp (0.0004) trên tập huấn luyện, nhưng có độ chính xác khiêm tốn (74.81%) trên tập kiểm thử. Điều này cho thấy còn nhiều dư địa để cải thiện, đặc biệt là khả năng tổng quát hóa của mô hình.

Đối với bài toán phân loại đơn giản như MNIST, mô hình ViT có thể chưa phát huy hết tiềm năng so với các mô hình CNN truyền thống. Tuy nhiên, việc thử nghiệm và tối ưu thêm có thể giúp cải thiện hiệu suất của mô hình.
