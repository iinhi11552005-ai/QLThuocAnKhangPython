import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm kết nối tới MySQL, trả về đối tượng connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',        # hoặc 127.0.0.1
            user='root',             # tên người dùng MySQL
            password='123456',             # mật khẩu (nếu có)
            database='qlthuocankhang'  # tên cơ sở dữ liệu bạn muốn dùng
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
