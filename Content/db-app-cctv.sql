-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 29 Des 2022 pada 05.51
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db-app-cctv`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fullakses` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data untuk tabel `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `fullakses`) VALUES
(2, 'admin', 'cctv', '1'),
(3, 'user', 'user', '0');

-- --------------------------------------------------------

--
-- Struktur dari tabel `list_cctv`
--

CREATE TABLE `list_cctv` (
  `nama_cctv` varchar(35) NOT NULL COMMENT 'nama cctv',
  `link` varchar(255) NOT NULL COMMENT 'link rtsp cctv',
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data untuk tabel `list_cctv`
--

INSERT INTO `list_cctv` (`nama_cctv`, `link`, `id`) VALUES
('HIKVISION HC', 'rtsp://admin:admin123@10.203.21.20:554/Streaming/Channels/102/', 10),
('DC 1', 'rtsp://service:Az123456b$@10.203.2.56/?inst=2', 12),
('DC 2', 'rtsp://service:Az123456b$@10.203.2.57/?inst=2', 13),
('BOSCH Lorong Masuk ICT', 'rtsp://service:Az123456b$@10.203.2.64:554/?inst=2', 14),
('Placeholder 10', 'https://63.142.183.154/mjpg/video.mjpg', 32),
('DC Entrance', 'rtsp://service:Az123456b$@10.203.2.58/?inst=2', 45),
('DC CP', 'rtsp://service:Az123456b$@10.203.2.59/?inst=2', 46),
('Ruang Kerja ICT', 'rtsp://service:Az123456b$@10.203.2.60/?inst=2', 49),
('NOC', 'rtsp://service:Az123456b$@10.203.2.61/?inst=2', 50),
('DC 3 IR', 'rtsp://service:Az123456b$@10.203.2.62/?inst=2', 51),
('DC UPS', 'rtsp://service:Az123456b$@10.203.2.63/?inst=2', 52),
('DC UPS 2', 'rtsp://service:Az123456b$@10.203.2.65/?inst=2', 54),
('DC Old', 'rtsp://service:Az123456b$@10.203.2.66/?inst=2', 55),
('Hikvision HC 2', 'rtsp://admin:admin123@10.203.21.21:554/Streaming/Channels/102/', 56),
('DC UPS 3', '	rtsp://service:Az123456b$@10.203.2.67/?inst=2', 58),
('DC Old entrance', '	rtsp://service:Az123456b$@10.203.2.68/?inst=2', 59),
('ICT Kitchen', '	rtsp://service:Az123456b$@10.203.2.69/?inst=2', 60),
('Front Door ICT', '	rtsp://service:Az123456b$@10.203.2.70/?inst=2', 61),
('DC UPS 5', '	rtsp://service:Az123456b$@10.203.2.71/?inst=2', 62),
('Hikvision Finance', 'rtsp://admin:admin123@10.203.21.30:554/Streaming/Channels/102/', 63),
('YPS', 'rtsp://admin:admin123@10.203.21.31:554/Streaming/Channels/102/', 64),
('HIkvision jalan', 'rtsp://admin:admin123@10.203.21.34:554/Streaming/Channels/102/', 65),
('indomaret', 'rtsp://admin:admin123@10.203.21.36:554/Streaming/Channels/102/', 66),
('pos rs', 'rtsp://admin:admin123@10.203.21.40:554/Streaming/Channels/102/', 67),
('test 42', 'rtsp://admin:admin123@10.203.21.42:554/Streaming/Channels/102/', 68);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `list_cctv`
--
ALTER TABLE `list_cctv`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `list_cctv`
--
ALTER TABLE `list_cctv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
