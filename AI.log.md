# Nhật ký kiểm tra website

File này ghi lại các lỗi đã phát hiện, nguyên nhân và cách sửa để có thể xem trực tiếp trên GitHub.

## Trạng thái hiện tại

- Website: [Portfolio trên GitHub Pages](https://diepvu190408.github.io/k20-Portfolio-CNTT-20-04/)
- Repository: [k20-Portfolio-CNTT-20-04](https://github.com/diepvu190408/k20-Portfolio-CNTT-20-04)
- Trạng thái: Đã kiểm tra, website đang chạy.

## Lịch sử lỗi và cách sửa

### 2026-10-30 — Hiệu ứng nền không hiển thị

- Hiện tượng: Hiệu ứng tinh vân và sao băng không thấy trên trang.
- Nguyên nhân: `body::before` và `body::after` dùng `z-index: -1`, bị nền của `body` che mất.
- Cách sửa: Đổi lớp hiệu ứng thành `z-index: 0` và đặt nội dung chính ở `z-index: 1` trong [css/style.css](css/style.css).
- Commit: `decd680` — `Fix animated galaxy layer visibility`.

### 2026-10-30 — GitHub Pages dùng CSS cũ

- Hiện tượng: GitHub Pages vẫn tải stylesheet phiên bản cũ sau khi sửa CSS.
- Nguyên nhân: Trình duyệt/CDN giữ cache của `style.css?v=3`.
- Cách sửa: Đổi liên kết stylesheet thành `style.css?v=4` trong [index.html](index.html) và [ket-qua.html](ket-qua.html).
- Commit: `b8eaa19` — `Refresh stylesheet cache for animation fix`.

## Đã kiểm tra

- Các hình ảnh trong thư mục `assets/` tải được.
- Form trong [index.html](index.html) chuyển đúng sang [ket-qua.html](ket-qua.html).
- Link quay lại biểu mẫu hoạt động.
- GitHub Pages deploy thành công.

## Kiểm tra tự động trên GitHub

Workflow [Kiểm tra website](.github/workflows/validate-site.yml) tự chạy sau mỗi lần push hoặc pull request. Workflow kiểm tra:

- File HTML có đọc được bằng UTF-8 không.
- `src`, `href` và `action` cục bộ có trỏ tới file tồn tại không.
- HTML có bị trùng `id` không.
- CSS có thiếu hoặc thừa dấu ngoặc không.
- Tài nguyên được gọi bằng `url(...)` trong CSS có tồn tại không.

Để xem log: vào tab **Actions** → chọn **Kiểm tra website** → chọn lần chạy. Dấu xanh là đạt, dấu đỏ là có lỗi; mở bước **Kiểm tra website** để xem dòng lỗi cụ thể.

## Cách ghi lỗi mới

Thêm một mục theo mẫu sau ở đầu phần “Lịch sử lỗi và cách sửa”:

```md
### YYYY-MM-DD — Tên lỗi

- Hiện tượng: Mô tả lỗi nhìn thấy.
- Nguyên nhân: Vì sao lỗi xảy ra.
- Cách sửa: File hoặc đoạn mã đã thay đổi.
- Commit: `mã-commit` — `tên commit`.
```

