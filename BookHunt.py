# Data buku-buku
buku = [
    {"judul": "Harry Potter and the Sorcerer's Stone", "penulis": "J.K. Rowling", "genre": "Fantasi"},
    {"judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "genre": "Fiksi"},
    {"judul": "1984", "penulis": "George Orwell", "genre": "Dystopia"},
    {"judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "genre": "Fiksi"},
    {"judul": "Pride and Prejudice", "penulis": "Jane Austen", "genre": "Romansa"},
    {"judul": "The Hobbit", "penulis": "J.R.R. Tolkien", "genre": "Fantasi"},
    {"judul": "Animal Farm", "penulis": "George Orwell", "genre": "Satire"},
    {"judul": "Supernova", "penulis": "Dee Lestari", "genre": "Fiksi Sains"},
    {"judul": "Cantik Itu Luka", "penulis": "Eka Kurniawan", "genre": "Fiksi"},
    {"judul": "The Subtle Art of Not Giving a Fuck", "penulis": "Mark Manson", "genre": "Pengembangan Diri"},
    {"judul": "Black Showman dan Pembunuh di Kota Tak Bernama", "penulis": "Keigo Higashino", "genre": "Misteri"},
    {"judul": "The Silent Patient", "penulis": "Alex Michaelides", "genre": "Thriller"},
    {"judul": "Alchemised", "penulis": "SenLinYu", "genre": "Dark fantasy"},
    {"judul": "Daisy Jones & The Six", "penulis": "Taylor Jenkins Reid", "genre": "Fiksi musik, drama"},
    {"judul": "Onyx Storm", "penulis": "Rebecca Yarros", "genre": "Fantasy romantis"},
    {"judul": "The Midnight Library", "penulis": "Matt Haig", "genre": "Fiksi filosofis"},
    {"judul": "The Song of Achilles", "penulis": "Madeline Miller", "genre": "Mitologi, Romance"},
    {"judul": "It Ends With Us", "penulis": "Colleen Hoover", "genre": "Romansa"},
    {"judul": "The Psychology of Money", "penulis": "Morgan Housel", "genre": "Keuangan, Nonfiksi"},
    {"judul": "The Hunger Games", "penulis": "Suzanne Collins", "genre": "Dystopia"},
    {"judul": "Percy Jackson & The Olympians", "penulis": "Rick Riordan", "genre": "Fantasi"},
    {"judul": "Norwegian Wood", "penulis": "Haruki Murakami", "genre": "Drama, Romance"},
    {"judul": "Kita Pergi Hari Ini", "penulis": "Ziggy Zezsyazeoviennazabrizkie", "genre": "Fiksi"},
    {"judul": "Laut Bercerita", "penulis": "Leila S. Chudori", "genre": "Fiksi historis"},
    {"judul": "The Girl on the Train", "penulis": "Paula Hawkins", "genre": "Thriller"},
    {"judul": "One Piece: East Blue", "penulis": "Eiichiro Oda", "genre": "Petualangan"},
    {"judul": "Think Again", "penulis": "Adam Grant", "genre": "Psikologi"},
    {"judul": "Sapiens", "penulis": "Yuval Noah Harari", "genre": "Sejarah, Nonfiksi"},
    {"judul": "Atomic Habits", "penulis": "James Clear", "genre": "Pengembangan diri"},
    {"judul": "The Name of the Wind", "penulis": "Patrick Rothfuss", "genre": "Fantasi"},
    {"judul": "The Maze Runner", "penulis": "James Dashner", "genre": "Dystopia"},
    {"judul": "Ready Player One", "penulis": "Ernest Cline", "genre": "Fiksi Sains"},
    {"judul": "The Fault in Our Stars", "penulis": "John Green", "genre": "Romansa, Drama"},
    {"judul": "Before the Coffee Gets Cold", "penulis": "Toshikazu Kawaguchi", "genre": "Fiksi, Drama"},
    {"judul": "Educated", "penulis": "Tara Westover", "genre": "Memoar"},
    {"judul": "Becoming", "penulis": "Michelle Obama", "genre": "Memoar"},
    {"judul": "Where the Crawdads Sing", "penulis": "Delia Owens", "genre": "Misteri, Drama"},
    {"judul": "The Alchemist", "penulis": "Paulo Coelho", "genre": "Filosofi, Petualangan"},
    {"judul": "Good Omens", "penulis": "Terry Pratchett & Neil Gaiman", "genre": "Fantasi, Komedi"},
    {"judul": "The Seven Husbands of Evelyn Hugo", "penulis": "Taylor Jenkins Reid", "genre": "Drama"},
    {"judul": "The Martian", "penulis": "Andy Weir", "genre": "Sci-Fi"},
    {"judul": "Gone Girl", "penulis": "Gillian Flynn", "genre": "Thriller psikologis"},
    {"judul": "Filosofi Teras", "penulis": "Henry Manampiring", "genre": "Filsafat, Self-help"},
    {"judul": "The Art of War", "penulis": "Sun Tzu", "genre": "Strategi"},
    {"judul": "The Power of Habit", "penulis": "Charles Duhigg", "genre": "Psikologi, Self-help"}
]


def tampilkan_menu():
    """
    Menampilkan menu utama aplikasi Book Hunt.
    
    Fungsi ini mencetak menu pilihan yang tersedia untuk pengguna,
    termasuk opsi untuk melihat daftar buku, mencari buku, dan keluar program.
    
    Returns:
        None
    """
    print("\n=== 📖 Book Hunt 📖 ===")
    print("1. List semua buku")
    print("2. Cari buku berdasarkan judul")
    print("3. Cari buku berdasarkan penulis")
    print("4. Cari buku berdasarkan genre")
    print("0. End Program")


def list_buku():
    """
    Menampilkan daftar lengkap semua buku yang tersedia.
    
    Fungsi ini mencetak informasi semua buku dalam koleksi,
    termasuk judul, penulis, dan genre. Jika tidak ada buku,
    akan menampilkan pesan bahwa perpustakaan kosong.
    
    Returns:
        None
    """
    print("\n=== Daftar Semua Buku ===")
    if not buku:
        print("Tidak ada buku di perpustakaan.")
    else:
        for i, item in enumerate(buku, start=1):
            print(f"{i}. Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    input("\nEnter untuk kembali ke menu...")


def cari_judul():
    """
    Mencari buku berdasarkan judul.
    
    Fungsi ini meminta input dari pengguna untuk kata kunci judul buku
    dan menampilkan semua buku yang judulnya mengandung kata kunci tersebut.
    Pencarian bersifat case-insensitive.
    
    Returns:
        None
    
    Examples:
        Input: "harry"
        Output: Menampilkan "Harry Potter and the Sorcerer's Stone"
    """
    print("\n=== Cari Buku Berdasarkan Judul ===")
    query = input("Masukkan judul buku: ").lower()
    hasil = [item for item in buku if query in item['judul'].lower()]
    
    if hasil:
        for item in hasil:
            print(f"Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    else:
        print("Buku tidak ditemukan.")
    input("\nEnter untuk kembali ke menu...")


def cari_penulis():
    """
    Mencari buku berdasarkan nama penulis.
    
    Fungsi ini meminta input dari pengguna untuk kata kunci nama penulis
    dan menampilkan semua buku yang nama penulisnya mengandung kata kunci tersebut.
    Pencarian bersifat case-insensitive.
    
    Returns:
        None
    
    Examples:
        Input: "orwell"
        Output: Menampilkan semua buku karya George Orwell
    """
    print("\n=== Cari Buku Berdasarkan Penulis ===")
    query = input("Masukkan nama penulis: ").lower()
    hasil = [item for item in buku if query in item['penulis'].lower()]
    
    if hasil:
        for item in hasil:
            print(f"Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    else:
        print("Buku tidak ditemukan.")
    input("\nEnter untuk kembali ke menu...")


def cari_genre():
    """
    Mencari buku berdasarkan genre.
    
    Fungsi ini meminta input dari pengguna untuk kata kunci genre
    dan menampilkan semua buku yang genrenya mengandung kata kunci tersebut.
    Pencarian bersifat case-insensitive.
    
    Returns:
        None
    
    Examples:
        Input: "fantasi"
        Output: Menampilkan semua buku bergenre Fantasi
    """
    print("\n=== Cari Buku Berdasarkan Genre ===")
    query = input("Masukkan genre: ").lower()
    hasil = [item for item in buku if query in item['genre'].lower()]
    
    if hasil:
        for item in hasil:
            print(f"Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    else:
        print("Buku tidak ditemukan.")
    input("\nEnter untuk kembali ke menu...")


def main():
    """
    Fungsi utama untuk menjalankan aplikasi Book Hunt.
    
    Fungsi ini mengatur alur program dengan menampilkan menu,
    menerima input pengguna, dan memanggil fungsi yang sesuai
    berdasarkan pilihan pengguna. Program akan terus berjalan
    hingga pengguna memilih opsi untuk keluar (0).
    
    Returns:
        None
    
    Flow:
        1. Tampilkan menu
        2. Terima input pilihan dari pengguna
        3. Jalankan fungsi sesuai pilihan
        4. Ulangi hingga pengguna memilih keluar
    """
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-4): ")
        
        if pilihan == "1":
            list_buku()
        elif pilihan == "2":
            cari_judul()
        elif pilihan == "3":
            cari_penulis()
        elif pilihan == "4":
            cari_genre()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan Book Hunt.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")


# Pemanggil Main Menu
if __name__ == "__main__":
    main()

