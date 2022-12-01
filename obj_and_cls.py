from obj_and_cls_class_user import User

app_user_one = User("ma@ma.com", "Mike Antonov", "pswd1", "Unemployed")
app_user_one.get_user_info()
app_user_one.change_job_title("Backend developer")

app_user_two = User("aa@aa.com", "Alice", "secret", "DevOps Engineer")
app_user_two.get_user_info()
