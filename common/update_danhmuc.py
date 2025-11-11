from ketnoidb.ketnoi_mysql import connect_mysql


def update_danhmuc(id_danhmuc, ten_moi=None, mota_moi=None):
    """Hàm cập nhật thông tin danh mục theo ID."""
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

        # Xây dựng câu lệnh UPDATE linh hoạt
        fields = []
        values = []

        # Đã SỬA: Thay 'ten' bằng 'ten_danhmuc'
        if ten_moi:
            fields.append("ten_danhmuc = %s")
            values.append(ten_moi)

        # Đã SỬA: Thay 'mota' bằng 'mo_ta'
        if mota_moi:
            fields.append("mo_ta = %s")
            values.append(mota_moi)

        if not fields:
            print("⚠️ Không có thông tin nào để cập nhật.")
            return

        query = f"UPDATE danhmuc SET {', '.join(fields)} WHERE id = %s"
        values.append(id_danhmuc)

        cursor.execute(query, tuple(values))
        conn.commit()

        print(f"✅ Cập nhật danh mục ID = {id_danhmuc} thành công!")

    except Exception as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        cursor.close()
        conn.close()