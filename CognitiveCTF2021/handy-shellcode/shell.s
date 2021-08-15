.global main
main:
        xorl %ecx, %ecx    # 同じ値でxorを取ると0になる。mov 0, (対象レジスタ) よりもよく使われる初期化の方法らしい？のでそれにあやかる
        xorl %edx, %edx    # こちらも初期化
        movl $11, %eax     # システムコール種別は 11 (0x0b) = execve
        push $0x0068732f   # "/sh" と終端null文字のリトルエンディアン表記
        push $0x6e69622f   # "/bin" のリトルエンディアン表記
        movl %esp, %ebx    # pushでスタックに積んだ文字列の先頭アドレスがespに入っているので、ebxに移す
        int $0x80          # システムコール呼び出し
