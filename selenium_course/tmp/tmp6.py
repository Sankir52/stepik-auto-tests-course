# работа с assert
actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")
print("Чота текст: {}, потом {}, еще раз {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "three"
print(f"222 Чота текст: {str1}, потом {str2}, еще раз {str3}")
#assert abs(-42) == -42, "Should be absolute value of a number"

s = 'My Name is Julia'
if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
print('=====================')
def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring('qwe_asd','asd0')