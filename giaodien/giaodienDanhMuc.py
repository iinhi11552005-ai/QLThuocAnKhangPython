import tkinter as tk
from tkinter import ttk, messagebox


class CategoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QL Danh mục (Cập nhật)")
        self.root.geometry("800x600")

        # --- Dữ liệu giả lập (Lấy từ ảnh của bạn) ---
        self.data = [
            {"id": 1, "ten_danhmuc": "Hot Sale", "mo_ta": "Sản phẩm đang giảm giá hấp dẫn", "trang_thai": 1},
            {"id": 2, "ten_danhmuc": "Mỹ phẩm", "mo_ta": "để sử dụng", "trang_thai": 1},
            {"id": 3, "ten_danhmuc": "Thực phẩm chức năng", "mo_ta": "Bổ sung vitamin, dinh dưỡng", "trang_thai": 1},
            {"id": 4, "ten_danhmuc": "Thiết bị, dụng cụ y tế", "mo_ta": "Dụng cụ, thiết bị chăm sóc sức khỏe",
             "trang_thai": 1},
            {"id": 5, "ten_danhmuc": "Dược mỹ phẩm", "mo_ta": "Mỹ phẩm có dược tính chăm sóc da", "trang_thai": 1},
            {"id": 6, "ten_danhmuc": "Chăm sóc cá nhân", "mo_ta": "Sản phẩm vệ sinh, chăm sóc cơ thể", "trang_thai": 1},
            {"id": 7, "ten_danhmuc": "Chăm sóc trẻ em", "mo_ta": "Sản phẩm cho mẹ và bé", "trang_thai": 1},
        ]
        # Giả lập ID tự tăng
        self.current_id = 8

        # --- Khung nhập liệu (Form) ---
        form_frame = ttk.LabelFrame(root, text="Thông tin danh mục")
        form_frame.pack(fill="x", padx=10, pady=10)

        # Hàng 1: ID và Tên
        ttk.Label(form_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.id_entry = ttk.Entry(form_frame, state="readonly")  # ID không cho phép sửa
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(form_frame, text="Tên danh mục:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ten_entry = ttk.Entry(form_frame, width=40)
        self.ten_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        # Hàng 2: Mô tả và Trạng thái
        ttk.Label(form_frame, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.mota_entry = ttk.Entry(form_frame)
        self.mota_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        ttk.Label(form_frame, text="Trạng thái (1=Hiện, 0=Ẩn):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.trangthai_entry = ttk.Entry(form_frame, width=10)
        self.trangthai_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Cho phép cột 1 và 3 co giãn
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(3, weight=2)

        # --- Khung nút bấm (Buttons) ---
        button_frame = ttk.Frame(root)
        button_frame.pack(fill="x", padx=10, pady=5)

        self.add_button = ttk.Button(button_frame, text="Thêm", command=self.add_category)
        self.add_button.pack(side="left", padx=5)

        self.update_button = ttk.Button(button_frame, text="Sửa", command=self.update_category)
        self.update_button.pack(side="left", padx=5)

        self.delete_button = ttk.Button(button_frame, text="Xoá", command=self.delete_category)
        self.delete_button.pack(side="left", padx=5)

        self.clear_button = ttk.Button(button_frame, text="Làm mới", command=self.clear_form)
        self.clear_button.pack(side="left", padx=5)

        # --- Khung hiển thị (Treeview) ---
        tree_frame = ttk.Frame(root)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Cột
        self.tree = ttk.Treeview(tree_frame, columns=("id", "ten", "mota", "trangthai"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("ten", text="Tên Danh mục")
        self.tree.heading("mota", text="Mô tả")
        self.tree.heading("trangthai", text="Trạng thái")

        # Kích thước cột
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("ten", width=200)
        self.tree.column("mota", width=350)
        self.tree.column("trangthai", width=80, anchor="center")

        # Thêm thanh cuộn
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Sự kiện: Khi bấm vào một hàng trong Treeview
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

        # Tải dữ liệu ban đầu
        self.load_data()

    # --- Các hàm chức năng ---

    def load_data(self):
        """Tải lại toàn bộ dữ liệu từ list vào Treeview"""
        # Xoá dữ liệu cũ
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Thêm dữ liệu mới
        for item in self.data:
            self.tree.insert("", "end", values=(item["id"], item["ten_danhmuc"], item["mo_ta"], item["trang_thai"]))

    def clear_form(self):
        """Xoá trắng các ô nhập liệu"""
        self.id_entry.config(state="normal")
        self.id_entry.delete(0, "end")
        self.id_entry.config(state="readonly")

        self.ten_entry.delete(0, "end")
        self.mota_entry.delete(0, "end")
        self.trangthai_entry.delete(0, "end")

        # Bỏ chọn trong treeview
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection()[0])

    def on_item_select(self, event):
        """Khi người dùng bấm vào một mục trong bảng, điền thông tin lên form"""
        try:
            selected_item_iid = self.tree.selection()[0]
            item_values = self.tree.item(selected_item_iid, "values")

            # Xoá form trước
            self.clear_form()

            # Điền dữ liệu
            self.id_entry.config(state="normal")
            self.id_entry.insert(0, item_values[0])
            self.id_entry.config(state="readonly")

            self.ten_entry.insert(0, item_values[1])
            self.mota_entry.insert(0, item_values[2])
            self.trangthai_entry.insert(0, item_values[3])
        except IndexError:
            # Lỗi xảy ra khi bảng bị refresh và mất lựa chọn
            pass

    def add_category(self):
        """Thêm một danh mục mới"""
        ten = self.ten_entry.get()
        mota = self.mota_entry.get()
        trangthai = self.trangthai_entry.get()

        if not ten:  # Kiểm tra dữ liệu cơ bản
            messagebox.showwarning("Lỗi", "Tên danh mục không được để trống.")
            return

        if not trangthai.isdigit():
            messagebox.showwarning("Lỗi", "Trạng thái phải là số (1 hoặc 0).")
            return

        # Tạo mục mới
        new_item = {
            "id": self.current_id,
            "ten_danhmuc": ten,
            "mo_ta": mota,
            "trang_thai": int(trangthai)
        }

        # Thêm vào "database"
        self.data.append(new_item)
        self.current_id += 1  # Tăng ID

        messagebox.showinfo("Thành công", f"Đã thêm danh mục: {ten}")

        self.load_data()  # Tải lại bảng
        self.clear_form()  # Xoá form

    def update_category(self):
        """Cập nhật một danh mục đã chọn"""
        id_str = self.id_entry.get()

        if not id_str:
            messagebox.showwarning("Lỗi", "Vui lòng chọn một danh mục để sửa.")
            return

        id_to_update = int(id_str)
        ten = self.ten_entry.get()
        mota = self.mota_entry.get()
        trangthai = self.trangthai_entry.get()

        if not ten:
            messagebox.showwarning("Lỗi", "Tên danh mục không được để trống.")
            return

        if not trangthai.isdigit():
            messagebox.showwarning("Lỗi", "Trạng thái phải là số (1 hoặc 0).")
            return

        # Tìm và cập nhật trong "database"
        found = False
        for item in self.data:
            if item["id"] == id_to_update:
                item["ten_danhmuc"] = ten
                item["mo_ta"] = mota
                item["trang_thai"] = int(trangthai)
                found = True
                break

        if found:
            messagebox.showinfo("Thành công", f"Đã cập nhật danh mục ID: {id_to_update}")
            self.load_data()
            self.clear_form()
        else:
            messagebox.showerror("Lỗi", f"Không tìm thấy danh mục với ID: {id_to_update}")

    def delete_category(self):
        """Xoá một danh mục đã chọn"""
        id_str = self.id_entry.get()

        if not id_str:
            messagebox.showwarning("Lỗi", "Vui lòng chọn một danh mục để xoá.")
            return

        id_to_delete = int(id_str)

        # Xác nhận xoá
        if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xoá danh mục ID {id_to_delete} không?"):

            item_to_remove = None
            for item in self.data:
                if item["id"] == id_to_delete:
                    item_to_remove = item
                    break

            if item_to_remove:
                self.data.remove(item_to_remove)  # Xoá khỏi "database"
                messagebox.showinfo("Thành công", f"Đã xoá danh mục ID: {id_to_delete}")
                self.load_data()
                self.clear_form()
            else:
                messagebox.showerror("Lỗi", f"Không tìm thấy danh mục với ID: {id_to_delete}")


# --- Khởi chạy ứng dụng ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CategoryApp(root)
    root.mainloop()