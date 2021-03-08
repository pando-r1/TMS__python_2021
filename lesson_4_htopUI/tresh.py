import psutil

memory = psutil.virtual_memory()
res = {"total": memory[0], "available": memory[1], 
       "used": [memory[3]], "free": memory[4]}
for i in memory:
    print(i)

print(res)
print(memory)