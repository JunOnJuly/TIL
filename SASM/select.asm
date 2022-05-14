%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ; 분기문
    
    ; CMP dst, src (dst가 기준)
    ; 비교한 결과물은 Flag Register 에 저장
    
    ; JUMP [label] 시리즈
    ; JMP : 무조건 jump
    ; JE : JumpEquals 같으면 jump
    ; JNE : JumpNotEquals 다르면 jump
    ; JG : JumpGreater 크면 jump
    ; JGE : JumpGreaterEquals 크거나 같으면 jump
    ; JL : --
    ; JLE : --
    
    ; 두 수가 같으면 1 아니면 0
    
    mov rax, 10
    mov rbx, 10
    
    cmp rax, rbx
    
    je LABEL_EQUAL
    
    ; je 에 의해 점프를 안했다면
    mov rcx, 0
    jmp LABEL_EQUAL_END
    
LABEL_EQUAL:
    mov rcx, 1
    
LABEL_EQUAL_END:
    PRINT_HEX 1, rcx
    NEWLINE
    
    
    xor rax, rax
    ret