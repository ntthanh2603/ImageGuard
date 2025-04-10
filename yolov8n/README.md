# BÁO CÁO PHÂN TÍCH HIỆU SUẤT
# Dự án phân loại ảnh 16+ sử dụng mô hình YOLOv8n

## 1. Tổng quan dự án

Dự án này tập trung vào việc xây dựng và đánh giá một mô hình phân loại ảnh thành 3 nhãn chính:
- **Ảnh người lớn (16+)**: Nội dung nhạy cảm, không phù hợp với trẻ em dưới 16 tuổi.
- **Ảnh bình thường**: Nội dung an toàn, phù hợp với mọi lứa tuổi.
- **Ảnh bạo lực (16+)**: Nội dung chứa các yếu tố bạo lực, không phù hợp với trẻ em dưới 16 tuổi.

Mô hình được sử dụng là **YOLOv8n**, phiên bản nhẹ của kiến trúc YOLOv8, được tối ưu hóa cho tốc độ xử lý nhanh trong khi vẫn duy trì độ chính xác cao. Báo cáo này phân tích hiệu suất của mô hình qua quá trình huấn luyện (10 epoch) và kiểm tra trên tập dữ liệu test.

---

## 2. Phân tích hiệu suất huấn luyện

### 2.1. Phân tích đồ thị loss và độ chính xác

#### 2.1.1. Train Loss
- Hàm mất mát (loss) trên tập huấn luyện giảm đều qua 10 epoch:
  - Epoch 1: 0.83442
  - Epoch 2: 0.30695 (giảm mạnh)
  - Epoch 10: 0.07431 (mức thấp nhất).
- Xu hướng giảm ổn định cho thấy mô hình học hiệu quả từ dữ liệu huấn luyện, không có dấu hiệu bất thường như dao động lớn hay tăng ngược.

#### 2.1.2. Validation Loss
- Hàm mất mát trên tập kiểm định (val loss) cũng giảm, dù có một số biến động nhỏ:
  - Epoch 1: 0.74385
  - Epoch 10: 0.59932.
- Khoảng cách giữa train loss và val loss không quá lớn ở các epoch cuối, cho thấy mô hình không bị overfitting nghiêm trọng.

#### 2.1.3. Accuracy Top-1
- Độ chính xác dự đoán nhãn chính xác nhất (top-1) tăng ổn định:
  - Epoch 1: 0.87037 (87.037%)
  - Epoch 2: 0.91481 (91.481%)
  - Epoch 10: 0.96296 (96.296%).
- Độ chính xác đạt mức ổn định cao (khoảng 0.96) từ epoch 7 trở đi.

#### 2.1.4. Accuracy Top-5
- Độ chính xác top-5 duy trì ở mức **1.0 (100%)** qua tất cả các epoch.
- Điều này hợp lý vì dự án chỉ có 3 lớp, nên khi xét top-5, nhãn đúng luôn nằm trong số đó.

### 2.2. Bảng số liệu huấn luyện

| Epoch | Train Loss | Top-1 Accuracy | Val Loss | Learning Rate |
|-------|------------|----------------|----------|--------------|
| 1     | 0.83442    | 0.87037        | 0.74385  | 0.00023205   |
| 2     | 0.30695    | 0.91481        | 0.63828  | 0.00042352   |
| 3     | 0.21011    | 0.92222        | 0.63232  | 0.00056786   |
| 4     | 0.1707     | 0.94444        | 0.61738  | 0.00050194   |
| 5     | 0.13445    | 0.95185        | 0.60449  | 0.00043126   |
| 6     | 0.11798    | 0.94815        | 0.63086  | 0.00036057   |
| 7     | 0.09649    | 0.96296        | 0.61963  | 0.00028988   |
| 8     | 0.0906     | 0.95926        | 0.59414  | 0.00021920   |
| 9     | 0.09442    | 0.96667        | 0.5958   | 0.00014851   |
| 10    | 0.07431    | 0.96296        | 0.59932  | 0.00007783   |

- **Learning Rate**: Tốc độ học thay đổi theo chiến lược tối ưu (tăng đến epoch 3 rồi giảm dần), giúp mô hình hội tụ hiệu quả.

---

## 3. Kết quả kiểm tra trên tập test

### 3.1. Thông tin tập dữ liệu
- **Tập train**: 1260 ảnh, 3 lớp.
- **Tập val**: 270 ảnh, 3 lớp.
- **Tập test**: 270 ảnh, 3 lớp.

### 3.2. Kết quả đánh giá
Dựa trên lệnh kiểm tra:

```
!yolo task=classify mode=val model=/content/drive/MyDrive/ImageGuard/training_tuanthanh/best.pt data=/content/drive/MyDrive/ImageGuard/dataset_classification split=test
```

Kết quả từ Ultralytics YOLOv8.2.103:
- **Top-1 Accuracy**: 0.959 (95.9%).
- **Top-5 Accuracy**: 1.0 (100%).
- **Tốc độ xử lý**: 
  - Preprocess: 0.0ms.
  - Inference: 17.4ms mỗi ảnh.
  - Postprocess: 0.0ms.

### 3.3. Phân tích
- Độ chính xác top-1 trên tập test (95.9%) rất gần với kết quả trên tập val tại epoch 10 (96.296%), cho thấy mô hình tổng quát hóa tốt trên dữ liệu mới.
- Top-5 accuracy đạt 100%, tiếp tục khẳng định tính nhất quán với số lượng lớp hạn chế (3 lớp).
- Tốc độ inference 17.4ms/ảnh là rất nhanh, phù hợp cho các ứng dụng thực tế cần xử lý thời gian thực.

---

## 4. Đánh giá tổng quan

### 4.1. Điểm mạnh
- **Độ chính xác cao**: Top-1 đạt 95.9% trên tập test và 96.296% trên tập val tại epoch 10.
- **Tốc độ hội tụ nhanh**: Chỉ sau 2 epoch, độ chính xác đã vượt 90%.
- **Không overfitting**: Train loss và val loss hội tụ gần nhau, mô hình tổng quát hóa tốt.
- **Hiệu suất xử lý**: Tốc độ inference nhanh (17.4ms/ảnh), phù hợp cho ứng dụng thực tế.

### 4.2. Hạn chế
- **Biến động val loss**: Một số epoch (6-7) cho thấy val loss tăng nhẹ, có thể do dữ liệu validation chứa một số mẫu khó.
- **Độ chính xác chưa tối ưu tuyệt đối**: Top-1 dao động quanh 95-96%, vẫn còn khoảng cách nhỏ để đạt 100%.

---

## 5. Kết luận

Mô hình **YOLOv8n** đã chứng minh hiệu suất vượt trội trong việc phân loại ảnh thành 3 nhãn: ảnh người lớn (16+), ảnh bình thường và ảnh bạo lực (16+). Với độ chính xác top-1 đạt **95.9% trên tập test** và tốc độ xử lý nhanh (17.4ms/ảnh), mô hình này là giải pháp lý tưởng cho các hệ thống lọc nội dung tự động, góp phần bảo vệ người dùng khỏi nội dung không phù hợp.

Dự án có thể được cải thiện thêm bằng cách tối ưu hóa tập dữ liệu (tăng số lượng mẫu khó) hoặc điều chỉnh siêu tham số để giảm biến động val loss và nâng cao độ chính xác lên mức tối đa.