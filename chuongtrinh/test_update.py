from common.update_danhmuc import update_danhmuc

while True:
    id = input("id danh mục")
    ten =input("Nhập vào tên danh mục")
    mota=input("Nhập vào mô tả")
    update_danhmuc(id, ten, mota)
    con=input("Tiếp tục y, Thoát thì nhấn ký tự bất kỳ")
    if con!="y":
        break