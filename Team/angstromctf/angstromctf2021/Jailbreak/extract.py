from pwn import *
import os, sys, stat


context.arch = 'amd64'
before_call_address = 0x10db
after_call_address = 0x10ed

for i in range(29):
        elf = ELF('./jailbreak')
        elf.asm(before_call_address,
		f"""
		nop
		nop
		nop
		nop
		nop
		nop
		mov rdi, {i}
		""")
        elf.asm(after_call_address, f'ret')
        elf.save(f'patched{i}')
        os.chmod(f'patched{i}', stat.S_IEXEC)
        p = process(f'patched{i}')
        print(f'{i}: ', p.recv())
        p.close()
        if i not in (2,3):
            os.unlink(f'patched{i}')
