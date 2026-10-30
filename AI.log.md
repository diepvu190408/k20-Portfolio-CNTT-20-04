# AI Log

## Mục đích

File này dùng để ghi lại những việc đã nhờ AI hỗ trợ trong quá trình làm website.

## Nhật ký

### 30/10/2026 — Sửa hiệu ứng nền

- Vấn đề: Hiệu ứng tinh vân và sao băng không hiển thị.
- Nguyên nhân: Hai lớp hiệu ứng bị đặt phía sau nền trang bằng `z-index: -1`.
- Đã làm: Đổi hiệu ứng sang lớp hiển thị `z-index: 0`, nội dung trang dùng `z-index: 1`.
- File thay đổi: `css/style.css`.
- Commit: `decd680`.

### 30/10/2026 — Làm mới bộ nhớ đệm CSS

- Vấn đề: GitHub Pages vẫn hiển thị CSS cũ.
- Đã làm: Đổi `style.css?v=3` thành `style.css?v=4`.
- File thay đổi: `index.html`, `ket-qua.html`.
- Commit: `b8eaa19`.

### 30/10/2026 — Kiểm tra trang kết quả

- Đã kiểm tra form trong `index.html`.
- Form chuyển đúng tới `ket-qua.html`.
- Link quay lại biểu mẫu hoạt động bình thường.

## Mẫu ghi thêm

```md
### DD/MM/YYYY — Tên công việc

- Vấn đề:
- Nguyên nhân:
- Đã làm:
- File thay đổi:
- Commit:
```
