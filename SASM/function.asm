%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ; 함수
    
    call PRINT_MSG
    
    xor rax, rax
    ret
    
print_MSG:
    PRINT_STRING msg
    NEWLINE
    ret
    
MAX:
    cmp eax, ebx
    jg L1
    mov ecx, ebx

L1:
    mov ecx, eax
L2:
    ret
    
    
section .data
    msg db 'HELLO World', 0x00
section .bss