from random import randint

# параметры кода Хемминга
m = 3
k = 2 ** m - 1
n = 2 ** m - m - 1
size = 250
error_counter = 0

msg_tx = [randint(0, 1) for i in range(size)]
print(f"payload len: {len(msg_tx)}")

if len(msg_tx) % k:
    d = (k - size % k)
    msg_tx += d * [0]
    print(f"added bits: {d}")

msg_to_encode = []
buf = []
for i in msg_tx:
    buf.append(i)
    if len(buf) == k:
        msg_to_encode.append(buf)
        buf = []

print(f"msg size: {len(msg_to_encode)} x {len(msg_to_encode[0])}")

msg_decode = msg_to_encode
msg_rx = [byte for message in msg_decode for byte in message]
print(msg_rx)
print(len(msg_rx))
msg_rx = msg_rx[:-3]
print(len(msg_rx))

msg_rx[45] = 0 if (msg_rx[45] == 1) else 1
for i in range(len(msg_rx)):
    if msg_tx[i] != msg_rx[i]:
        error_counter += 1
        print(f'{i}: {msg_tx[i]} : {msg_rx[i]}')
    # print(f'{i}: {msg[i]} : {msg_rx[i]}')

print(f'error counter: {error_counter}')
