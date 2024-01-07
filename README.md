# 1.Cài đặt
- MySQL và MySQL Workbench
- Django
- pymysql
# 2.Tạo cơ sở dữ liệu
- database name: st_mn_sys
- user: st_mn_sys
- password: micheal2003
# 3.Tạo bảng
- python manage.py makemigrations
- python manage.py migrate
# 4.Tạo tài khoản admin
Chạy lệnh sau ở terminal
- python manage.py createsuperuser
- Nhập username email và password
# 5.Chạy server
- python manage.py runserver
