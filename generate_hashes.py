
import bcrypt

print("=== SMARTLIBRARY REAL BCRYPT HASHES ===")
print("Librarian → abdulai@gmail.com / admin12")
admin_hash = bcrypt.hashpw("admin12".encode('utf-8'), bcrypt.gensalt(rounds=12))
print(f"INSERT INTO AUTHENTICATION VALUES (1, '{admin_hash.decode('utf-8')}', CURRENT_DATE);\n")

print("Member → josephine@gmail.com / member12")
member_hash = bcrypt.hashpw("member12".encode('utf-8'), bcrypt.gensalt(rounds=12))
print(f"INSERT INTO AUTHENTICATION VALUES (2, '{member_hash.decode('utf-8')}', CURRENT_DATE);")