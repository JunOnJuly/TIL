%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;배열과 주소
    
    ; 배열을 구성하는 각 값을 배열 요소(element)라고 함
    ; 배열의 위치를 가리키는 숫자를 인덱스(index) 라고 함
    
    xor rax, rax
    ret
    
section .data
    a db 0x01, 0x02, 0x03, 0x04, 0x05 ; 5바이트
    b times 5 dw 1 ; 5개를 1로 초기화 10바이트
    
section .bss
    num resb 10