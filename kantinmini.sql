-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Des 2023 pada 06.33
-- Versi server: 10.4.20-MariaDB
-- Versi PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kantinmini`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi_struk`
--

CREATE TABLE `transaksi_struk` (
  `id` int(11) NOT NULL,
  `bill_number` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `hargadarimakanan` int(11) NOT NULL,
  `hargadariminuman` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `transaksi_struk`
--

INSERT INTO `transaksi_struk` (`id`, `bill_number`, `date`, `hargadarimakanan`, `hargadariminuman`, `subtotal`) VALUES
(2, 'BILL9972', '2023-12-01', 36000, 10000, 46000),
(3, 'BILL6571', '2023-12-04', 67000, 15000, 82000),
(4, 'BILL8368', '2023-12-04', 80000, 27000, 107000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `transaksi_struk`
--
ALTER TABLE `transaksi_struk`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `transaksi_struk`
--
ALTER TABLE `transaksi_struk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
