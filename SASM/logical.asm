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
    ; 곱셈/ 나눗셈에 용이
    
    ; xor 은 암호학에 용
    
    
    xor rax, rax ; 아무 의미 없다는 의미로 rax에 0을 대입
    ret

section .data

section .bss
