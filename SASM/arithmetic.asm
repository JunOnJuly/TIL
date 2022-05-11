%include "io64.inc"

section .text
global CMAIN
CMAIN:
    mov rbp, rsp; for correct debugging
    
    GET_DEC 1, al
    GET_DEC 1, num
    
    PRINT_DEC 1, al
    NEWLINE
    PRINT_DEC 1, num
    NEWLINE
    ; 더하기 연산
    ; add a, b (a = a + b)
    ; a는 레지스터 or 메모리
    ; b는 레지스터 or 메모리 or 상수
    ; 단 a, b 모두 메모리는 x
    
    add al, 1
    PRINT_DEC 1, al
    NEWLINE
    
    add al, [num]
    PRINT_DEC 1, al
    NEWLINE
    
    xor rax, rax
    ret


section .data


section .bss
    num resb 1