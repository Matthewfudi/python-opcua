with open('D:\python学习资料\qianfeng\pi_digits') as file_object:
    contents =  file_object.read()
print(contents)

with open('D:\python学习资料\qianfeng\pi_digits', 'w') as file_object:
    file_object.write('i love programing')
print(contents)