# 这是一个简单的ERP权限检查脚本
def check_erp_permission(user_role):
    if user_role == "admin":
        return True
    else:
        return False
