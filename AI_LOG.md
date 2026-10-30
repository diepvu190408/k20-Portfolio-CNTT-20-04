# AI Log – Portfolio v7

Tài liệu này ghi lại phần hỗ trợ AI trong phiên hoàn thiện A2.2 và phân biệt các kết quả đã kiểm tra với các hạng mục chưa kiểm tra.

## Nhật ký các phiên trước

### 30/10/2026 — Sửa hiệu ứng nền

- Vấn đề: Hiệu ứng tinh vân và sao băng không hiển thị.
- Nguyên nhân: Hai lớp hiệu ứng bị đặt phía sau nền trang bằng `z-index: -1`.
- Đã làm: Đổi hiệu ứng sang lớp hiển thị `z-index: 0`, nội dung trang dùng `z-index: 1`.
- File thay đổi: `css/style.css`.
- Commit đã đối chiếu: `decd680`.

### 30/10/2026 — Làm mới bộ nhớ đệm CSS

- Vấn đề: GitHub Pages vẫn hiển thị CSS cũ.
- Đã làm: Đổi `style.css?v=3` thành `style.css?v=4`.
- File thay đổi: `index.html`, `ket-qua.html`.
- Commit đã đối chiếu: `b8eaa19`.

### 30/10/2026 — Kiểm tra trang kết quả

- Đã kiểm tra form trong `index.html`.
- Form chuyển đúng tới `ket-qua.html`.
- Link quay lại biểu mẫu hoạt động bình thường.

## 30/10/2026 – Kiểm tra và hoàn thiện hồ sơ bàn giao

- **Vấn đề ban đầu:** Cần rà soát toàn bộ Portfolio hiện có và chuẩn bị hồ sơ bàn giao v7 theo yêu cầu A2.2.
- **Dữ kiện ban đầu:** Dự án gồm `index.html`, `ket-qua.html`, `css/style.css`, thư mục `assets` và log AI cũ. Nhánh hiện tại là `main`; trạng thái Git trước khi chỉnh sửa sạch.
- **Nhận định của sinh viên trước khi hỏi AI:** Cần giữ bố cục đen, xanh neon và hiệu ứng không gian; ưu tiên sửa nhỏ để website tĩnh tương thích GitHub Pages.
- **Công cụ và yêu cầu AI:** Phân tích tệp trong workspace, kiểm tra liên kết tương đối, tài nguyên ảnh, lịch sử Git và bổ sung tài liệu README, AI log, release notes, checklist, hướng dẫn minh chứng giao diện.
- **Gợi ý của AI:** Bổ sung metadata, liên kết bỏ qua đến nội dung chính, kích thước và `decoding` cho ảnh lazy-load, trạng thái focus nhất quán và tài liệu bàn giao.
- **Quyết định:** Chấp nhận các gợi ý trên vì không thay đổi cấu trúc nội dung hoặc chức năng hiện có.
- **Mã nguồn đã chỉnh sửa:** `index.html`, `ket-qua.html`, `css/style.css`.
- **Tệp hồ sơ đã tạo:** `README.md`, `AI_LOG.md`, `docs/RELEASE_NOTES.md`, `docs/CHECKLIST.md`, `docs/UI_IMPROVEMENTS.md`.
- **Kiểm tra đã thực hiện:** Đọc toàn bộ tệp mã nguồn hiện có; xác nhận các ảnh mở được và ghi nhận kích thước; kiểm tra hai mã commit cũ `decd680` và `b8eaa19` tồn tại trong lịch sử Git; mở bản local v7 bằng trình duyệt, xác nhận 5 ảnh tải được, form hợp lệ tới `ket-qua.html` và không overflow ngang ở 390, 768, 1440 px; mở repository và URL GitHub Pages công khai.

## 30/10/2026 – Kiểm tra lại trang và cỡ chữ

- **Kiểm tra:** Đo cỡ chữ trên local và GitHub Pages ở 390, 768 và 1440 px.
- **Kết quả:** Thân bài 16px; đoạn giới thiệu 17.28px; tiêu đề chính 32px trên mobile và 49.6px trên màn hình lớn; không phát hiện overflow ngang.
- **Chỉnh sửa:** Đổi ký tự dấu đầu dòng trong CSS sang mã Unicode `\\2022` để hiển thị đúng khi mở local bằng `file://`.
- **Kiểm tra sau chỉnh sửa:** CSS tạo đúng dấu `•`, bố cục mobile vẫn không overflow.

## 30/10/2026 – Chuẩn hóa typography v7

- **Yêu cầu:** Đồng bộ cỡ chữ giữa `index.html` và `ket-qua.html`.
- **Đã làm:** Dùng `clamp()` trong `css/style.css`; thêm mốc từ 681px để H1 tablet/desktop không thấp hơn 42px; giữ H1 mobile 30px.
- **Kết quả đã kiểm tra:** H1 30/42/46px ở 390/768/1440px; H2 28/28/32px; H3 20/20/23px; menu 15/15/15.84px; không phát hiện overflow ngang trên cả hai trang.
- **Quyết định:** Chấp nhận thay đổi vì giữ nguyên bố cục, nội dung và phong cách không gian hiện tại.

## 30/10/2026 – Sửa hiển thị ảnh nội dung

- **Vấn đề:** Ảnh cá nhân dùng `object-fit: cover`; ảnh dự án dùng khung tỷ lệ cố định và có nguy cơ cắt nội dung quan trọng.
- **Đã làm:** Đặt ảnh nội dung về `height: auto`, `object-fit: contain`, `object-position: center`; giữ `background-size` của nền trang trí không thay đổi.
- **Phạm vi:** `figure img`, `.project-image` và `.ronaldo-photo` trong `css/style.css`; thêm `max-width: 100%` cho ảnh.
- **Kiểm tra:** 5 ảnh tải được ở 390, 768 và 1440 px; không overflow ngang; tỷ lệ tự nhiên được giữ.

### Điều chỉnh sau rà soát avatar

- **Phản hồi:** Avatar không cần hiển thị toàn bộ vì khung tròn sẽ tạo khoảng trống hai bên.
- **Đã làm:** Giữ `figure img` ở `object-fit: cover` và `object-position: 65% 30%`; các ảnh nội dung khác vẫn dùng `contain`.

