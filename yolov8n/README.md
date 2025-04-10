# BÁO CÁO PHÂN TÍCH KẾT QUẢ
# Dự án phân loại ảnh 16+ sử dụng mô hình YOLOv8n

## 1. Tổng quan dự án

Dự án này tập trung vào việc phân loại ảnh thành 3 nhãn chính:
- Ảnh người lớn (16+)
- Ảnh bình thường
- Ảnh bạo lực (16+)

Mô hình được sử dụng là YOLOv8n, một phiên bản nhẹ của kiến trúc YOLO, phù hợp cho các ứng dụng cần tốc độ xử lý nhanh nhưng vẫn đảm bảo độ chính xác. Báo cáo này phân tích hiệu suất của mô hình qua 10 epoch đào tạo.

## 2. Phân tích các chỉ số hiệu suất

### 2.1. Phân tích đồ thị loss và độ chính xác

#### 2.1.1. Train Loss
- **Biểu đồ trên cùng bên trái**: Thể hiện sự giảm dần của hàm mất mát (loss) trong quá trình huấn luyện.
- Loss bắt đầu từ mức cao (0.83442) tại epoch 1 và giảm mạnh xuống còn 0.30695 tại epoch 2.
- Sau đó, loss tiếp tục giảm dần và đạt mức 0.07431 tại epoch 10.
- Đường màu xanh biểu thị giá trị loss thực tế, trong khi đường cam đứt nét biểu thị đường cong được làm mịn.
- Xu hướng giảm đều của loss cho thấy mô hình đang học hiệu quả từ dữ liệu huấn luyện.

#### 2.1.2. Validation Loss
- **Biểu đồ trên cùng bên phải**: Thể hiện hàm mất mát trên tập dữ liệu kiểm định.
- Val loss bắt đầu từ mức cao (0.74385) và giảm xuống còn 0.59932 tại epoch 10.
- Đáng chú ý có một số biến động nhỏ giữa các epoch 5-8, nhưng nhìn chung vẫn duy trì xu hướng giảm.
- Khoảng cách giữa train loss và val loss không quá lớn ở các epoch sau, cho thấy mô hình không bị overfitting nghiêm trọng.

#### 2.1.3. Accuracy Top1
- **Biểu đồ dưới cùng bên trái**: Thể hiện độ chính xác của dự đoán hạng nhất.
- Độ chính xác tăng từ 0.87037 tại epoch 1 lên đến 0.96296 tại epoch 10.
- Đặc biệt có sự cải thiện mạnh mẽ từ epoch 1 đến epoch 2 (từ 0.87037 lên 0.91481).
- Đường xu hướng cho thấy mô hình đạt được độ ổn định cao sau epoch 7, với độ chính xác dao động quanh 0.96.

#### 2.1.4. Accuracy Top5
- **Biểu đồ dưới cùng bên phải**: Thể hiện độ chính xác top-5 của mô hình.
- Giá trị luôn ổn định ở mức 1.0 qua tất cả các epoch.
- Điều này hoàn toàn hợp lý vì dự án chỉ có 3 lớp, nên khi xét top-5 kết quả, mô hình luôn bao gồm lớp đúng.

### 2.2. Phân tích bảng số liệu

Từ bảng dữ liệu chi tiết, ta có thể thấy:

| Epoch | Train Loss | Top1 Accuracy | Val Loss | Learning Rate |
|-------|------------|---------------|----------|--------------|
| 1     | 0.83442    | 0.87037       | 0.74385  | 0.00023205   |
| 2     | 0.30695    | 0.91481       | 0.63828  | 0.00042352   |
| 3     | 0.21011    | 0.92222       | 0.63232  | 0.00056786   |
| 4     | 0.1707     | 0.94444       | 0.61738  | 0.00050194   |
| 5     | 0.13445    | 0.95185       | 0.60449  | 0.00043126   |
| 6     | 0.11798    | 0.94815       | 0.63086  | 0.00036057   |
| 7     | 0.09649    | 0.96296       | 0.61963  | 0.00028988   |
| 8     | 0.0906     | 0.95926       | 0.59414  | 0.00021920   |
| 9     | 0.09442    | 0.96667       | 0.5958   | 0.00014851   |
| 10    | 0.07431    | 0.96296       | 0.59932  | 0.00007783   |

- **Learning rate**: Tốc độ học bắt đầu thấp (0.00023205), tăng dần đến epoch 3 (0.00056786), sau đó giảm dần theo lịch trình, chạm mức thấp nhất tại epoch 10 (0.00007783). Đây là chiến lược learning rate phổ biến giúp mô hình hội tụ hiệu quả.

- **Train loss và val loss**: Sự chênh lệch giữa train loss và val loss tương đối nhỏ ở các epoch sau cùng, cho thấy mô hình có khả năng tổng quát hóa tốt.

## 3. Đánh giá hiệu suất mô hình

### 3.1. Điểm mạnh
- Độ chính xác top-1 rất cao, đạt 96.296% tại epoch 10, cho thấy khả năng phân loại chính xác các ảnh vào 3 nhãn.
- Tốc độ hội tụ nhanh: Mô hình đạt độ chính xác trên 90% chỉ sau 2 epoch đào tạo.
- Loss giảm ổn định, không có dấu hiệu overfitting nghiêm trọng (train loss và val loss không diverge).

### 3.2. Hạn chế
- Có một số biến động nhỏ trong val loss, đặc biệt là tại epoch 6 và 7, cho thấy mô hình có thể gặp khó khăn với một số mẫu trong tập validation.
- Accuracy top-1 có sự dao động nhỏ giữa các epoch 6-10, chưa hoàn toàn ổn định.

## 4. Kết luận

Mô hình YOLOv8n đã thể hiện hiệu suất rất tốt trong việc phân loại ảnh thành 3 nhãn: ảnh người lớn (16+), ảnh bình thường và ảnh bạo lực (16+), với độ chính xác cuối cùng đạt 96.296%. Điều này cho thấy mô hình có tiềm năng áp dụng vào các hệ thống lọc nội dung thực tế.

Với khả năng phân loại chính xác cao và tốc độ xử lý nhanh, YOLOv8n là lựa chọn phù hợp cho các ứng dụng phân loại nội dung 16+, góp phần bảo vệ người dùng khỏi những nội dung không phù hợp.
