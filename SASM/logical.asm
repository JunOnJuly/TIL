%include "io64.inc"

section .text
global CMAIN
CMAIN:
    mov rbp, rsp; for correct debugging
    
    ; 쉬프트 연산, 논리 연산
    
    mov eax, 0x12345678
    PRINT_HEX 4, eax
    NEWLINE
    
    shl eax, 8
    PRINT_HEX 4, eax
    NEWLINE
    
    shr eax, 8
    PRINT_HEX 4, eax
    NEWLINE
    
    xor rax, rax
    ret

section .data

section .bss
