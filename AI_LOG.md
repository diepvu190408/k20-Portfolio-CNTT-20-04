# AI Log – Portfolio v7

Tài liệu này ghi lại phần hỗ trợ AI trong phiên hoàn thiện A2.2. Các thông tin về GitHub Pages, URL công khai và ảnh minh chứng chưa được kiểm chứng nên để trống.

## 30/10/2026 – Kiểm tra và hoàn thiện hồ sơ bàn giao

- **Vấn đề ban đầu:** Cần rà soát toàn bộ Portfolio hiện có và chuẩn bị hồ sơ bàn giao v7 theo yêu cầu A2.2.
- **Dữ kiện ban đầu:** Dự án gồm `index.html`, `ket-qua.html`, `css/style.css`, thư mục `assets` và log AI cũ. Nhánh hiện tại là `main`; trạng thái Git trước khi chỉnh sửa sạch.
- **Nhận định của sinh viên trước khi hỏi AI:** Cần giữ bố cục đen, xanh neon và hiệu ứng không gian; ưu tiên sửa nhỏ để website tĩnh tương thích GitHub Pages.
- **Công cụ và yêu cầu AI:** Phân tích tệp trong workspace, kiểm tra liên kết tương đối, tài nguyên ảnh, lịch sử Git và bổ sung tài liệu README, AI log, release notes, checklist, hướng dẫn minh chứng giao diện.
- **Gợi ý của AI:** Bổ sung metadata, liên kết bỏ qua đến nội dung chính, kích thước và `decoding` cho ảnh lazy-load, trạng thái focus nhất quán và tài liệu bàn giao.
- **Quyết định:** Chấp nhận các gợi ý trên vì không thay đổi cấu trúc nội dung hoặc chức năng hiện có.
- **Mã nguồn đã chỉnh sửa:** `index.html`, `ket-qua.html`, `css/style.css`.
- **Tệp hồ sơ đã tạo:** `README.md`, `AI_LOG.md`, `RELEASE_NOTES.md`, `CHECKLIST.md`, `UI_IMPROVEMENTS.md`.
- **Kiểm tra đã thực hiện:** Đọc toàn bộ tệp mã nguồn hiện có; xác nhận các ảnh mở được và ghi nhận kích thước; kiểm tra hai mã commit cũ `decd680` và `b8eaa19` tồn tại trong lịch sử Git; mở bản local v7 bằng trình duyệt, xác nhận 5 ảnh tải được, form hợp lệ tới `ket-qua.html` và không overflow ngang ở 390, 768, 1440 px; mở repository và URL GitHub Pages công khai.

## Thông tin cần bổ sung

- Ảnh chụp URL repository và URL GitHub Pages thực tế.
- Ảnh chụp trước và sau cải tiến giao diện.
- Log hoặc ảnh kiểm tra trên trình duyệt ẩn danh.
- Commit của lần bàn giao v7 sau khi người học commit thật.

## 30/10/2026 – Kiểm tra lại trang và cỡ chữ

- **Kiểm tra:** Đo cỡ chữ trên local và GitHub Pages ở 390, 768 và 1440 px.
- **Kết quả:** Thân bài 16px; đoạn giới thiệu 17.28px; tiêu đề chính 32px trên mobile và 49.6px trên màn hình lớn; không phát hiện overflow ngang.
- **Chỉnh sửa:** Đổi ký tự dấu đầu dòng trong CSS sang mã Unicode `\\2022` để hiển thị đúng khi mở local bằng `file://`.
- **Kiểm tra sau chỉnh sửa:** CSS tạo đúng dấu `•`, bố cục mobile vẫn không overflow.

## Nhật ký trước đó

Nhật ký thao tác trước phiên này được giữ tại [AI.log.md](./AI.log.md). Các commit được nhắc trong tệp đó đã được đối chiếu với lịch sử Git cục bộ.

