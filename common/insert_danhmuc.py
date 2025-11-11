from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(ten_danhmuc, mo_ta):
    """Hàm thêm 1 danh mục mới vào bảng danhmuc."""
    conn = connect_mysql()
    if conn is None:
        print("⚠️ Không thể kết nối MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        values = (ten_danhmuc, mo_ta)

        cursor.execute(sql, values)
        conn.commit()

        print(f"✅ Đã thêm danh mục '{ten_danhmuc}' thành công! (ID: {cursor.lastrowid})")

    except Exception as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        cursor.close()
        conn.close()