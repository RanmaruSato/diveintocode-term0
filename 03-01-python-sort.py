import csv
# csvファイルを開いて　以後変数fとして定義
with open('address.csv') as f:
    #csvファイルの１行目が不要なので、１行目とそれ以外を分けて定義
    reader = csv.reader(f)
    header = next(reader)
    li = []
    for row in reader:
        #ソートするためにソート対象の要素をstrかたintに偏見
        row[1] = int(row[1])
        #sorted関数を使用するために、rowを配列に加えていく
        li.append(row)
#配列のkeyでソート
sorted_list = sorted(li,key = lambda row:row[1])
#headerを配列から取り出して出力
header = ','.join(header)
print(header)
#配列から取り出す
for  sorted_row in sorted_list:
    #数値と文字列は繋げられないので、strに戻す
    sorted_row[1]=str(sorted_row[1])
    #配列を繋げる
    sorted_row=','.join(sorted_row)

    print(sorted_row)
