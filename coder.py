from random import randint

# параметры кода Хемминга
m = 3
k = 2 ** m - 1
n = 2 ** m - m - 1
size = 250
error_counter = 0

msg_tx = [randint(0, 1) for i in range(size)]
print(f"msg_tx len: {len(msg_tx)}")

if len(msg_tx) % k:
    d = (k - size % k)
    msg_tx += d * [0]
    print(f"added bits to msg_tx: {d}")

# Дополнение до деления на целое значение
msg_to_encode = []
buf = []
for i in msg_tx:
    buf.append(i)
    if len(buf) == k:
        msg_to_encode.append(buf)
        buf = []

print(f"msg_to_encode size: {len(msg_to_encode)} x {len(msg_to_encode[0])} = ", end='')
print(f"{len(msg_to_encode) * len(msg_to_encode[0])} bits")

msg_decode = msg_to_encode # получили то, что отправили
msg_rx = [byte for message in msg_decode for byte in message] # одно большое сообщение
msg_rx = msg_rx[:-3] # удаление дополнительных битов


msg_rx[45] = 0 if (msg_rx[45] == 1) else 1 # внесение ошибки в код
for i in range(len(msg_rx)):
    if msg_tx[i] != msg_rx[i]:
        error_counter += 1
        print(f'error index: {i}:')
        print(f"msg_tx[{i}] : {msg_tx[i]}; msg_rx[{i}] {msg_rx[i]}")

print(f'error counter: {error_counter}')
