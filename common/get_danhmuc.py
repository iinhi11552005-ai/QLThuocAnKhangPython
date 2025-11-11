from ketnoidb.ketnoi_mysql import connect_mysql


def get_all_danhmuc():
    """Hàm lấy toàn bộ danh sách danh mục từ bảng 'danhmuc'."""
    conn = connect_mysql()
    if conn is None:
        print("⚠️ Không thể kết nối MySQL.")
        return []

    try:
        cursor = conn.cursor(dictionary=True)  # dùng dictionary để dễ đọc kết quả
        cursor.execute("SELECT * FROM danhmuc")
        result = cursor.fetchall()

        if not result:
            print("⚠️ Chưa có dữ liệu trong bảng 'danhmuc'.")
        else:
            print(f"✅ Đã lấy {len(result)} danh mục từ cơ sở dữ liệu.")

        return result

    except Exception as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []
    finally:
        cursor.close()
        conn.close()