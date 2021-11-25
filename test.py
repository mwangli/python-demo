# test

url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=cbb8de4071f84668b92a8258d4b4ec04&page=33'
print(int(url.split('=')[-1]) + 1)

temp = url.rpartition('=')
print(temp[0] + temp[1] + str(int(temp[2]) + 1))
