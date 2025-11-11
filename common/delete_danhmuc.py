from ketnoidb.ketnoi_mysql import connect_mysql


def delete_danhmuc(id_danhmuc):
    """Hàm xóa danh mục theo ID."""
    conn = connect_mysql()
    if conn is None:
        print("⚠️ Không thể kết nối MySQL.")
        return

    try:
        cursor = conn.cursor()

        # Kiểm tra danh mục có tồn tại không
        cursor.execute("SELECT * FROM danhmuc WHERE id = %s", (id_danhmuc,))
        record = cursor.fetchone()
        if not record:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")
            return

        # Xóa danh mục
        cursor.execute("DELETE FROM danhmuc WHERE id = %s", (id_danhmuc,))
        conn.commit()

        print(f"✅ Đã xóa danh mục có ID = {id_danhmuc} thành công!")

    except Exception as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        cursor.close()
        conn.close()