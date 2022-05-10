%include "io64.inc"

section .text
global CMAIN
CMAIN:
    mov rbp, rsp; for correct debugging
    ;write your code here
    ; mov regl, cst
    ; mov regl, reg2
    
    mov eax, 0x1234
    mov rbx, 0x12345678
    mov cl, 0xff
    
    mov al, 0x00
    mov [a], byte 0x55
    
    
    mov rax, rdx
    
    ; 메모리 < - > 레지스터
    mov rax, a ; a 의 주소를 rax 에 복사
    mov rax, [a] ; a 의 값을 rax 에 복사
    mov al, [a] ; a 의 최하위 값만 rax에 복사 
    xor rax, rax
    ret
    
    ; 변수의 선언 및 사용
    
; 초기화된 데이터
; [변수이름] [크기] [초기값]
; [크기] db(1) dw(2) dd(4) dq(8)
section .data
    a db 0x11
    b dw 0x2222
    c dd 0x33333333
    d dq 0x4444444444444444

; 초기화되지 않은 데이터
; [변수이름] [크기] [개수]
; [크기] resb(1) resw(2) resd(4) resq(8)
section .bss
    e resb 10