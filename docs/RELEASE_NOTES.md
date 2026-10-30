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
- Chuẩn hóa typography bằng `clamp()`: H1 30–46px, H2 28–32px, H3 20–23px, nội dung 16–17px và menu 15–16px.
- Điều chỉnh ảnh nội dung để dùng kích thước tự nhiên, `contain` và căn giữa; không thay đổi ảnh nền trang trí.
- Giữ avatar dạng crop trong khung tròn để tránh khoảng trống hai bên.
- Tạo đủ tài liệu bàn giao và kiểm chứng cho A2.2.

## Lỗi đã sửa

- Giảm nguy cơ bố cục nhảy khi ảnh lazy-load hoàn tất.
- Cải thiện khả năng điều hướng bằng bàn phím.
- Giảm khả năng trình duyệt giữ lại stylesheet cũ sau khi cập nhật.

## Commit liên quan

- Các commit có sẵn được đối chiếu: `decd680` và `b8eaa19`.
- Commit cho thay đổi v7: Chưa có commit v7 trong local.

## Hạn chế còn tồn tại

- Chưa có backend gửi email; biểu mẫu chỉ mô phỏng bằng GET.
- URL GitHub Pages hiện truy cập được, nhưng chưa chứa các thay đổi v7 đang ở local chưa commit/push.
- Chưa có ảnh chụp trước/sau thực tế cho minh chứng giao diện.
- Một số ảnh có dung lượng tương đối lớn và có thể được nén thêm trong phiên tối ưu riêng.

## Tài liệu liên quan

- [README.md](../README.md)
- [AI_LOG.md](../AI_LOG.md)
- [CHECKLIST.md](./CHECKLIST.md)
- [UI_IMPROVEMENTS.md](./UI_IMPROVEMENTS.md)

