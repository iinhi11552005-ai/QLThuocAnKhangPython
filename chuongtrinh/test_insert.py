from common.insert_danhmuc import insert_danhmuc
while True:
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vào mô tả")
    insert_danhmuc(ten, mota)
    con=input("Tiếp tục y, Thoát thì nhấn ký tự bất kỳ")
    if con!="y":
        break