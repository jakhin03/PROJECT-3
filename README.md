Fuzzing Excessive Data Exposures:

1. Giai đoạn ghi lại và chuẩn bị:
    Sử dụng một proxy web để ghi lại các yêu cầu và phản hồi giữa ứng dụng khách và máy chủ web.
    Tạo một tệp cấu hình lưu trữ các bước tương tác cần thiết để đưa ứng dụng khách đến trạng thái cơ bản.
2. Giai đoạn phát lại và fuzzing:
    Sử dụng tệp cấu hình để phát lại các bước tương tác và gửi các yêu cầu đến máy chủ mô phỏng.
    Máy chủ mô phỏng phản hồi với các phản hồi đã được ghi lại và thực hiện các đột biến trên phản hồi gốc để tạo ra các trường hợp kiểm thử.
3. Kiểm tra sự tương đồng của cây DOM:
    So sánh cây DOM gốc với cây DOM được tạo ra từ các phản hồi đã đột biến để phát hiện các trường dữ liệu quá mức.
4. Kiểm tra kết quả:
    Kiểm tra thủ công các trường dữ liệu được đánh dấu để xác định tính nhạy cảm và mức độ nghiêm trọng của lỗ hổng.