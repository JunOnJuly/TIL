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
    
    mov bl, 3 ; 레지스터 + 레지스터
    add al, bl
    PRINT_DEC 1, al
    NEWLINE
    
    add [num], byte 1 ; 크기를 할당해줘야함
    PRINT_DEC 1, [num]
    NEWLINE
    
    xor rax, rax
    ret

    ; 곱하기 연산
    ; mul reg
    ; - mul bl => al * bl
    ; -- 연산 결과를 ax 에 저장
    ; - mul bx => ax * bx
    ; -- 연산 결과는 dx ax 에 저장
    
    ; 나누기 연산
    ; div reg
    ; -div bl => ax / bl
    ; -- 연산 결과는 al (몫) ah (나머지)
    
section .data


section .bss
    num resb 1