from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_message(message, key):
    """
    加密函数
    :param message: 要加密的明文消息
    :param key: 加密密钥
    :return: 密文
    """
    # 创建 AES 对象
    cipher = AES.new(key, AES.MODE_CBC)

    # 对明文进行填充，然后加密
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))

    # 将 IV 和密文返回
    return cipher.iv, ct_bytes

def decrypt_message(iv, ct, key):
    """
    解密函数
    :param iv: 初始化向量
    :param ct: 密文
    :param key: 加密密钥
    :return: 解密后的明文
    """
    # 创建一个新的 AES 对象
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 解密并去除填充
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode()

    return pt

# 测试
key = get_random_bytes(16)  # 生成随机密钥
message = "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"

iv, ct = encrypt_message(message, key)
print("Encrypted:", ct)

pt = decrypt_message(iv, ct, key)
print("Decrypted:", pt)
