-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 03:02 AM
-- Phiên bản máy phục vụ: 8.0.42
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int NOT NULL,
  `ten_danhmuc` varchar(100) NOT NULL,
  `mo_ta` text,
  `trang_thai` tinyint DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `ten_danhmuc`, `mo_ta`, `trang_thai`) VALUES
(1, 'Hot Sale', 'Sản phẩm đang giảm giá hấp dẫn', 1),
(2, 'mỹ phẩm ', 'dễ sử dụng ', 1),
(3, 'Thực phẩm chức năng', 'Bổ sung vitamin, dinh dưỡng', 1),
(4, 'Thiết bị, dụng cụ y tế', 'Dụng cụ, thiết bị chăm sóc sức khỏe', 1),
(5, 'Dược mỹ phẩm', 'Mỹ phẩm có dược tính chăm sóc da', 1),
(6, 'Chăm sóc cá nhân', 'Sản phẩm vệ sinh, chăm sóc cơ thể', 1),
(7, 'Chăm sóc trẻ em', 'Sản phẩm cho mẹ và bé', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `id` int NOT NULL,
  `ten_sanpham` varchar(200) NOT NULL,
  `mo_ta` text,
  `gia_goc` decimal(10,0) DEFAULT NULL,
  `gia_ban` decimal(10,0) DEFAULT NULL,
  `giam_gia` int DEFAULT NULL,
  `dung_tich` varchar(50) DEFAULT NULL,
  `hinh_anh` varchar(255) DEFAULT NULL,
  `id_danhmuc` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`id`, `ten_sanpham`, `mo_ta`, `gia_goc`, `gia_ban`, `giam_gia`, `dung_tich`, `hinh_anh`, `id_danhmuc`) VALUES
(1, 'Nước muối Vietrue sát khuẩn, súc miệng', 'Dung tích 500ml', 7000, 4900, 30, '500ml', 'vietrue.jpg', 1),
(2, 'Thực phẩm dinh dưỡng Y Học Ensure Gold', 'Lon 800g', 932000, 845000, 9, '800g', 'ensure_gold.jpg', 3),
(3, 'Sữa bột Anlene Gold hương Vani', 'Lon 800g - dành cho người từ 40 tuổi', 555000, 480000, 13, '800g', 'anlene_gold.jpg', 3),
(4, 'Costar Omega 3', 'Lọ 365 viên', 972000, 729000, 25, '365 viên', 'omega3.jpg', 3),
(5, 'Sắc Ngọc Khang', 'Hộp 180 viên', 666000, 532800, 20, '180 viên', 'sacngockhang.jpg', 3);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_danhmuc` (`id_danhmuc`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`id_danhmuc`) REFERENCES `danhmuc` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
