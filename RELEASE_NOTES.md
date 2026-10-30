# Release notes – Portfolio v7

## Phiên bản

**v7 – 30/10/2026**

## Thay đổi chính

- Giữ nguyên các trang `index.html` và `ket-qua.html` cùng phong cách không gian nền tối.
- Bổ sung mô tả trang và màu chủ đề cho trải nghiệm trình duyệt tốt hơn.
- Bổ sung liên kết bỏ qua đến nội dung chính và trạng thái focus dễ nhận biết.
- Bổ sung kích thước tự nhiên và `decoding="async"` cho ảnh dự án lazy-load.
- Tăng phiên bản cache stylesheet từ `v4` lên `v5`.
- Sửa dấu đầu dòng CSS bằng mã Unicode để hiển thị ổn định khi mở local.
- Tạo đủ tài liệu bàn giao và kiểm chứng cho A2.2.

## Lỗi đã sửa

- Giảm nguy cơ bố cục nhảy khi ảnh lazy-load hoàn tất.
- Cải thiện khả năng điều hướng bằng bàn phím.
- Giảm khả năng trình duyệt giữ lại stylesheet cũ sau khi cập nhật.

## Commit liên quan

- Các commit có sẵn được đối chiếu: `decd680` và `b8eaa19`.
- Commit cho thay đổi v7: <!-- Bổ sung SHA thật sau khi người học commit. -->

## Hạn chế còn tồn tại

- Chưa có backend gửi email; biểu mẫu chỉ mô phỏng bằng GET.
- URL GitHub Pages hiện truy cập được, nhưng chưa chứa các thay đổi v7 chưa commit/push.
- Chưa có ảnh chụp trước/sau thực tế cho minh chứng giao diện.
- Một số ảnh có dung lượng tương đối lớn và có thể được nén thêm trong phiên tối ưu riêng.

## Bàn giao và tiếp tục phát triển

Đọc [README.md](./README.md), kiểm tra [CHECKLIST.md](./CHECKLIST.md), sau đó bổ sung URL, ảnh minh chứng và SHA commit thật. Khi phát triển tiếp, giữ đường dẫn tương đối, kiểm tra form sau mỗi thay đổi và cập nhật tài liệu thay vì ghi nhận kết quả chưa kiểm chứng.

