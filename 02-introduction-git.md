# Gitとは

Gitはバージョン管理に使われる。
バージョン管理とは１つのファイルやファイルの集合に対して、時間とともに加えられていく変更を
記録するシステムで後から過去のバージョンを呼び出すことができるようにするためのもの。
Gitと類似したソフトウェアとして代表的なソフトとしてはSubversionが存在している。Subversionは集中型のソースコード管理システムの一種でプロジェクトの全てが単一のサーバーに保持される。
これによるメリットはプロジェクトメンバーが何をしているのか全員ある程度わかることがあげられる。
しかし、単一のサーバーで管理しているためにサーバーに障害が起きた場合作業が停止してしまう。また、サーバーが復旧しなかった場合は過去のバージョンは全て失われるので、その後のプロジェクトの進行に大きな障害となる。
上記のような集中型ソースコード管理システムの問題点を解消するために、Gitのような分散型管理システムが生まれた。  
Gitのメリットとしては下記があげられる。
- 変更内容を変更できる
- 変更内容の差分を把握できる
- 過去の状態に戻すことができる
- 他人が編集した内容を間違って上書きしないで済む  

# git initとは

git initコマンドは　編集するファイルをgitで監視するためにGitリポジトリとして管理するために宣言するコマンド
既にGitリポジトリが存在する場合、git initを実行すると
下記のエラーメッセージが表示される  
```Reinitialized existing Git repository in C:/Users/ｰｰｰｰｰｰｰｰ```  
.gitディレクトリは、リポジトリに関するメタデータを参照したいときにみる。
Gitの管理下から外したいときに削除できる。

# git addとは

ステージング領域（エリア）とは,ワーキングエリアからステージングエリアへファイル追加しコミットの対象とするためにファイルをコミットする前に変更内容を一時的に登録しておくバッファのようなもの。  
hoge.htmlをステージング領域に追加するコマンドは

```$git add hoge.html```  
hoge.htmlをステージング領域に追加されていた状態でhoge.htmlをステージング領域から削除する方法は

```$git reset hoge.html```


# git commitコマンドとは

git commitコマンドはステージングエリアに登録されているファイルを１つの束として、リポジトリの履歴に登録する。この記録を元にファイルを過去の状態に戻したり、削除されたファイルを復元したりできる。
コミットのログを確認する方法は    
```$git log```   

オプションとしては下記が挙げられる。  
- $ git log --numstat :ファイル毎の削除、追加行数を表示
- $ git log --name-status :変更したファイルを表示
- $ git log -- path/to/*.sh :特定のファイルのみ
- $ git log --since="4 days ago" --until="2015/01/22" :日付
- $ git log --author='take4s5i' :コミッター別に

コミットを取り消す方法は  
```$git reset```  
オプションの種類は下記が挙げられる。　　  
- --hardオプション：コミット取り消した上でワークディレクトリの内容も書き換えたい場合に使用。  　　
- --softオプション：ワークディレクトリの内容はそのままでコミットだけを取り消したい場合に使用。　
- HEAD^：直前のコミットを意味する。  
- HEAD~{n} ：n個前のコミットを意味する。  


以下のコミット履歴があった場合  
```
commit c4a9f6aad4ea6f5b372b9bc742c1dfc06b8641f1 (HEAD -> master, origin/master, origin/HEAD)
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:42:30 2018 +0900

    commit message 3

commit cff10b7231c5238cbd7ddab0bc19c3b7f02ba35d
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:40:31 2018 +0900

    commit message 2

commit 7b6f15fdde0f56dae4541a1a896ef6dca630e28f
Author: Akihiro Nakao <genn777f3@gmail.com>
Date:   Fri Feb 23 19:38:22 2018 +0900

    commit message 1  

```  
commit message 1までコミットを戻す方法は    
```$git reset 7b6f15fdde0f56dae4541a1a896ef6dca630e28f```
