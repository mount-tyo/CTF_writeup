# CognitiveCTF2021 writeup

# 使用したTool
- jpegAnalyzer  
- wire shark  
- 青い空を見上げればいつもそこに白い猫 for うさみみハリケーン
- EditThisCookie (chromeの拡張機能)
- CyberChef (encode/decodeのwebサイト)

# 50 points
## 2Warm
・2進数に変換する
## Glory of the Garden
・画像をcatで見て、grepかfindstrで検索
```
cat ./garden.jpg | grep "CTF"
cat ./garden.jpg | findstr "CTF"
```
## Insp3ct0r
・chromeなら「検証」でHTMLとCSSとJavaScriptを確認できる
## The Numbers
・アルファベットのインデックスに対応  
・「num_to_alph.py」で解いた
## practice-run-1
・cat&grepで検索してもいける  
・おそらくほかの方法もある
## handy-shellcode (pt.50)
・linux 32bit用のshell codeをググってコピペした。  
・なんとなく、このプログラムでshellを呼び出すコードを書くらしい  
・shell codeはよくわからない  
・shell codeの作り方?は、アセンブリ言語を機械語に翻訳する過程を踏むらしい  

# 100 points
## 13 (pt.100)
・「rot13」でググるとrot13.comがでてくるので、コピペするだけ
## Bases (pt.100)
・base64でデコードする  
・「google エンコード」とかでググるといい感じのencode/decodeサイトがでてくる
## Easy1
・ワンタイムパッドをググって、仕組みを理解  
・table.txtがあるので、暗号鍵をもとに行(又は列)を参照し、その行で対応する暗号フラグの列(又は行)を参照していく。  
・地道な作業  
## First Grep
・たしか、catしてgrep
```
cat file_name | grep CTF
```
## OverFlow 1
・バッファオーバーフローを考える  　
・vuln()内で参照するリターンアドレスが表示されるプログラムである  
・flag()のアドレスをgdbなどで調べる  
・オーバフローしてアドレスが変更される境界線(文字列の長さ)を模索し、境界線以降にflag()のアドレスを入れる  
・アドレス入力の際に、リトルエンディアンに気を付ける  
・入力例は以下  
```
echo -e "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xe6\x85\x04\x08" | ./vuln
```
・CognitiveCTF{n0w_w3r3_ChaNg1ng_r3tURn5_f4c9f24e}
## dont-use-client-side
・ソースを見ると、HTMLにJavascriptが埋め込まれてる  
・どうやら、JSでパスワードチェックしている  
・JSで比較している文字列を並び変えるだけ  
## logon
・cookieのadminをTrueにする  
・chromeだと、「EditThisCookie」という拡張機能が便利
## strings it
・バイナリファイルなので、stringsコマンド使う(windowsはわからない)
```
strings file_name | grep CTF
```
## vault-door-1
・Javaコードの中にパスワードを比較している部分がある  
・32文字  
・単純に並び変える？  
## what's a net cat?
・netcat使うだけ　　
```
nc address ip
```
## where are the robots
・robots.txtにアクセスして、そこの指示に従うだけ　　

# 150 points
## So Meta
・たしか、catしてgrepするだけ
```
cat file_name | grep CTF
```
## What Lies Within
・「青い空を～」のステガノグラフィー解析を使った  
・各色の最下位委ビットを選択して抽出する
## shark on wire 1
・ワイヤーシャークなどのパケット解析ツールを使用した  
・UDPストリームを愚直に調べる  

# 200 points
## Based
・「CyberChef」で数字入れてautobakeすると、いい感じにでコードしてくれる  
・2, 8, 10, 16進数を文字に変換するタスク  
・utf-8？shift-jis？  
## Tapping
・ncでアクセスすると、モールス信号が表示される
・モールス信号の返還サイトで変換
## plumbing
・ncしたのをパイプしてgrep
```
nc host_name port | grep CTF
```
## rsa_pop_quiz
・結構時間かかった。RSAの仕組みと計算方法を理解しておくと速く解けそう  
・問題文に表示されているnetcatを実行し、問題に答える  
・全部で８問くらいあり、各問いの最初はこの問題が解けるかどうかをy/nでこたえる  
・最後の問いで暗号文を平文に戻すが、以下のコードを使用した  
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
・表示された平文をHEXに変換し、asciiに変換する作業は、「CyberChef」がおすすめ  

## whats-the-difference
・結構悩んだ  
・cmpコマンドとgawkで差分のバイトをASCII変換  
```
cmp -l cattos.jpg kitters.jpg | gawk '{printf "%c", strtonum(0$2)}' && echo
```
・上記の出力を回答しても、正解にならない。。。  
・cat_kit.pyを作成し、バイナリでjpgファイルを読み込んで、差分をASCIIに変換する  
```
python cat_kit.py
```
・結果は同じになった  
・flagをよく見ると、ある程度単語があって、たまに数字になってる  
・"_bu77r_"をbufferと解釈し、"_bu773r_"とすると通った  
・原因は不明...  
## where-is-the-file
```
ls -a
cat secret_file
```

# 250 points
## like1000
・.tarファイルを解凍するshellスクリプトを書く  
・例えば以下のコードを'hoge.sh'として保存し、実行する  
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
