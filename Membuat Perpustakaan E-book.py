# Aplikasi Pencarian E-book Sederhana

# Data buku dummy (list of dictionaries)
buku = [
    {"judul": "Harry Potter and the Sorcerer's Stone", "penulis": "J.K. Rowling", "genre": "Fantasi"},
    {"judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "genre": "Fiksi"},
    {"judul": "1984", "penulis": "George Orwell", "genre": "Dystopia"},
    {"judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "genre": "Fiksi"},
    {"judul": "Pride and Prejudice", "penulis": "Jane Austen", "genre": "Romansa"},
    {"judul": "The Hobbit", "penulis": "J.R.R. Tolkien", "genre": "Fantasi"},
    {"judul": "Animal Farm", "penulis": "George Orwell", "genre": "Satire"},
    {"judul": "Supernova", "penulis": "Dee Lestari", "genre": "Fiksi Sains"},
]

def tampilkan_menu():
    print("\n=== Aplikasi Pencarian E-book ===")
    print("1. List semua buku")
    print("2. Cari buku berdasarkan judul")
    print("3. Cari buku berdasarkan penulis")
    print("4. Cari buku berdasarkan genre")
    print("5. End Program")

def list_buku():
    print("\n=== Daftar Semua Buku ===")
    if not buku:
        print("Tidak ada buku di perpustakaan.")
    else:
        for i, item in enumerate(buku, start=1):
            print(f"{i}. Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")

def cari_judul():
    print("\n=== Cari Buku Berdasarkan Judul ===")
    query = input("Masukkan judul buku (case-insensitive): ").lower()
    hasil = [item for item in buku if query in item['judul'].lower()]
    if hasil:
        for item in hasil:
            print(f"Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    else:
        print("Buku tidak ditemukan.")

def cari_penulis():
    print("\n=== Cari Buku Berdasarkan Penulis ===")
    query = input("Masukkan nama penulis (case-insensitive): ").lower()
    hasil = [item for item in buku if query in item['penulis'].lower()]
    if hasil:
        for item in hasil:
            print(f"Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    else:
        print("Buku tidak ditemukan.")

def cari_genre():
    print("\n=== Cari Buku Berdasarkan Genre ===")
    query = input("Masukkan genre (case-insensitive): ").lower()
    hasil = [item for item in buku if query in item['genre'].lower()]
    if hasil:
        for item in hasil:
            print(f"Judul: {item['judul']}, Penulis: {item['penulis']}, Genre: {item['genre']}")
    else:
        print("Buku tidak ditemukan.")

def main():
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
            print("Terima kasih telah menggunakan aplikasi ini. Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")

# Jalankan aplikasi
if __name__ == "__main__":

    main()

