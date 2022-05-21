%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ; 반복문
    
    mov ecx, 10
    
LABEL_LOOP:
    PRINT_STRING msg
    NEWLINE
    dec ecx ; sub ecx, 1 과 동일
    cmp ecx, 0
    jne LABEL_LOOP
    
    
    
    mov eax, 100
    xor ebx, ebx
    xor ecx, ecx

LABEL_SUM:
    inc ecx ; add ecx, 1 과 동일
    add ebx, ecx
    cmp ecx, eax
    jne LABEL_SUM
    
    PRINT_DEC 4, ebx
    NEWLINE
    
    ; loop [라벨]
    ; -ecx 에 반복 횟수
    ; - loop 할때 마다 ecx 1 감소, 0이면 빠져나가거나 라벨로 이동
    
    
    mov ecx, 100
LABEL_LOOP_SUM:
    add ebx, ecx
    loop LABEL_LOOP_SUM
    
    
    
    xor rax, rax
    ret
    
section .data
    msg db 'Hello World', 0x00