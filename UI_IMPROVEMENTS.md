# Hướng dẫn ghi nhận cải tiến giao diện buổi 5–6

## Vấn đề giao diện ban đầu

- Cần xác nhận bố cục hiện tại vẫn đọc được trên nhiều kích thước màn hình.
- Cần cải thiện khả năng nhận biết focus khi dùng bàn phím.
- Ảnh lazy-load chưa khai báo đầy đủ kích thước hiển thị trong HTML, có thể làm bố cục thay đổi khi ảnh tải xong.

## Tiêu chí đánh giá

- Nội dung và phong cách đen, xanh neon, không gian vẫn nhất quán.
- Điều hướng section rõ ràng trên desktop và mobile.
- Văn bản có độ tương phản phù hợp với nền tối.
- Người dùng bàn phím nhận biết được phần tử đang focus.
- Form, liên kết và ảnh hoạt động đúng.

## Cách cải tiến

- Bổ sung skip link đến `main`.
- Mở rộng trạng thái `:focus-visible` cho các liên kết và điều khiển.
- Khai báo `width`, `height`, `loading="lazy"` và `decoding="async"` cho ảnh dự án.
- Giữ nguyên CSS hiệu ứng nền, bố cục thẻ dự án và các nội dung hiện có.

## Ảnh trước và sau

- Ảnh trước: **cần người học bổ sung ảnh gốc thực tế**.
- Ảnh sau: **cần người học tự chụp từ phiên bản v7 thực tế**.
- Không tạo ảnh minh chứng thay cho ảnh chụp thật.

## Kết quả thử nghiệm

Chưa ghi nhận kết quả trình duyệt hoặc GitHub Pages trong workspace. Sau khi kiểm tra, bổ sung kích thước màn hình, trình duyệt, thao tác và liên kết tới ảnh/log.

## Lý do lựa chọn phương án

Các thay đổi nhỏ cải thiện khả năng tiếp cận và độ ổn định khi tải ảnh mà vẫn bảo toàn cấu trúc, nội dung và nhận diện hình ảnh của Portfolio.

## Hạn chế và hướng cải tiến

- Chưa có backend cho form liên hệ.
- Ảnh có thể được nén thêm để giảm thời gian tải.
- Có thể bổ sung kiểm tra tự động HTML/CSS ở một phiên riêng khi có công cụ và log xác thực.

