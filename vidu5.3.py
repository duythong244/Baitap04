def giai_bieu_thuc():
    bieu_thuc = input()
    ket_qua = ""
    dau_tru = False  # Biến để theo dõi dấu trừ

    for ky_tu in bieu_thuc:
        if ky_tu == '(':
            continue  # Bỏ qua dấu mở ngoặc
        elif ky_tu == ')':
            continue  # Bỏ qua dấu đóng ngoặc
        elif ky_tu == '-':
            if ket_qua and ket_qua[-1] == '-':
                ket_qua = ket_qua[:-1] + '+'  # -- thành +
            else:
                ket_qua += ky_tu  # Giữ nguyên dấu trừ
            dau_tru = True  # Gán dấu trừ
        elif ky_tu == '+':
            dau_tru = False  # Reset dấu trừ
            ket_qua += ky_tu  # Giữ nguyên dấu cộng
        elif ky_tu.isdigit() or ky_tu.isalpha():  # Kiểm tra chữ số hoặc chữ cái
            if dau_tru:
                ket_qua += '-' + ky_tu  # Thêm dấu trừ vào trước
                dau_tru = False  # Reset dấu trừ
            else:
                ket_qua += ky_tu  # Giữ nguyên ký tự
        else:
            ket_qua += ky_tu  # Giữ nguyên các ký tự khác (nếu cần)

    print(ket_qua)

# Nhập số lượng bộ test
t = int(input())

# Giải từng bộ test
for _ in range(t):
    giai_bieu_thuc()