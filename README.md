# Portfolio v7 – Vũ Quang Điệp

Portfolio cá nhân phục vụ bài đánh giá **A2.2 – Triển khai và bàn giao Portfolio v7**, học phần **FIT4014 – Đại học Đại Nam**.

## Tác giả và sản phẩm

- Tác giả: Vũ Quang Điệp, lớp CNTT 20-04
- Sản phẩm: Portfolio tĩnh giới thiệu bản thân, kỹ năng, dự án yêu thích, lộ trình học tập và biểu mẫu liên hệ mô phỏng.
- Công nghệ: HTML5, CSS3 và tài nguyên ảnh cục bộ. Dự án không phụ thuộc framework hoặc máy chủ backend.

## Cấu trúc thư mục

```text
.
├── index.html
├── ket-qua.html
├── css/
│   └── style.css
├── assets/
│   ├── Anh 7.jpg
│   ├── Lamboghini-New-Logo-Vector.png
│   ├── revuelto.jpg
│   ├── Tiên Nghịch.png
│   └── vuonglam.png
├── AI_LOG.md
└── docs/
    ├── RELEASE_NOTES.md
    ├── CHECKLIST.md
    └── UI_IMPROVEMENTS.md
```

## Chạy trên máy tính

1. Mở thư mục dự án bằng VS Code.
2. Mở `index.html` trực tiếp bằng trình duyệt, hoặc chạy máy chủ tĩnh trong thư mục gốc:

   ```bash
   python -m http.server 8000
   ```

3. Truy cập `http://localhost:8000/`.

## Kiểm tra chức năng

- Chọn các mục điều hướng và kiểm tra cuộn tới đúng phần.
- Kiểm tra ảnh đại diện và ảnh trong các thẻ dự án hiển thị đúng.
- Thử liên kết Revuelto; liên kết mở tab mới.
- Gửi biểu mẫu với dữ liệu giả hợp lệ để tới `ket-qua.html`.
- Thử dữ liệu thiếu, email sai định dạng hoặc nội dung dưới 10 ký tự để kiểm tra validation của trình duyệt.
- Thu nhỏ cửa sổ để kiểm tra bố cục điện thoại và máy tính bảng.
- Kiểm tra phím `Tab`, trạng thái focus và liên kết bỏ qua đến nội dung chính.

## GitHub Repository và GitHub Pages

- Repository: https://github.com/diepvu190408/k20-Portfolio-CNTT-20-04
- GitHub Pages hiện có: https://diepvu190408.github.io/k20-Portfolio-CNTT-20-04/
- Nguồn xuất bản dự kiến: nhánh `main`, thư mục `/ (root)`.
- Trạng thái v7: URL trên truy cập được, nhưng bản v7 trong workspace chưa được commit/push nên cần triển khai lại sau khi hoàn tất.

## Minh chứng

- [AI_LOG.md](./AI_LOG.md)
- [RELEASE_NOTES.md](./docs/RELEASE_NOTES.md)
- [CHECKLIST.md](./docs/CHECKLIST.md)
- [UI_IMPROVEMENTS.md](./docs/UI_IMPROVEMENTS.md)
- Minh chứng: GitHub Repository, Settings > Pages, Deployments và website ẩn danh.
