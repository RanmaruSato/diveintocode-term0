course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}
print({"D"} <= {"A", "B", "C"})
# print({'Cさん', 'Aさん'}&course_dict['AIコース'])
def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """

    # ここにコードを書いてみる
    #AIコースの判定
    #まず、want_to_find_personが各種コースに全て含まれているか判定
    #Falseであれば、完全不一致か部分的一致か場合分けしてMECEを満たす

    #want_to_find_person がcourse_dict['AIコース']に全て含まれている場合
    if(want_to_find_person <= course_dict['AIコース'])==True:
        print('AIコースに'+str(want_to_find_person)+'さんは在籍しています')
    #上の例の反例
    #完全不一致
    elif(want_to_find_person <= course_dict['AIコース'])==False and (course_dict['AIコース'] - want_to_find_person == course_dict['AIコース']) == True:
        #この条件の中でwant_to_find_personがcourse_dict['AIコース']の中に
        #含まれていない場合と、含まれている場合で場合分け。
        print('AIコースに' + str(want_to_find_person) + 'さんは在籍していません')
    elif(want_to_find_person <= course_dict['AIコース'])==False and (course_dict['AIコース'] - want_to_find_person == course_dict['AIコース']) == False:
        print(str(course_dict['AIコース'] & want_to_find_person) +'さんは在籍しています')



        #Railsコースの判定
    #want_to_find_person がcourse_dict['Railsコース']に全て含まれている場合
    if(want_to_find_person <= course_dict['Railsコース'])==True:
        print('Railsコースに'+str(want_to_find_person)+'さんは在籍しています')
    #上の例の反例
    #完全不一致
    elif(want_to_find_person <= course_dict['Railsコース'])==False and (course_dict['Railsコース'] - want_to_find_person == course_dict['Railsコース']) == True:
        #この条件の中でwant_to_find_personがcourse_dict['Railsコース']の中に
        #含まれていない場合と、含まれている場合で場合分け。
        print('Railsコースに' + str(want_to_find_person) + 'さんは在籍していません')
    elif(want_to_find_person <= course_dict['Railsコース'])==False and (course_dict['Railsコース'] - want_to_find_person == course_dict['Railsコース']) == False:
        print(str(course_dict['Railsコース'] & want_to_find_person) +'さんは在籍しています')

    #Railsチュートリアルコースの判定

    if(want_to_find_person <= course_dict['Railsチュートリアルコース'])==True:
        print('Railsチュートリアルコースに'+str(want_to_find_person)+'さんは在籍しています')
    #上の例の反例
    #完全不一致
    elif(want_to_find_person <= course_dict['Railsチュートリアルコース'])==False and (course_dict['Railsチュートリアルコース'] - want_to_find_person == course_dict['Railsチュートリアルコース']) == True:
        #この条件の中でwant_to_find_personがcourse_dict['Railsコース']の中に
        #含まれていない場合と、含まれている場合で場合分け。
        print('Railsチュートリアルコースに' + str(want_to_find_person) + 'さんは在籍していません')
    elif(want_to_find_person <= course_dict['Railsチュートリアルコース'])==False and (course_dict['Railsチュートリアルコース'] - want_to_find_person == course_dict['Railsチュートリアルコース']) == False:
        print(str(course_dict['Railsチュートリアルコース'] & want_to_find_person) +'さんは在籍しています')

    #JS
    if(want_to_find_person <= course_dict['JS'])==True:
        print('JSに'+str(want_to_find_person)+'さんは在籍しています')
    #上の例の反例
    #完全不一致
    elif(want_to_find_person <= course_dict['JS'])==False and (course_dict['JS'] - want_to_find_person == course_dict['JS']) == True:
        #この条件の中でwant_to_find_personがcourse_dict['Railsコース']の中に
        #含まれていない場合と、含まれている場合で場合分け。
        print('JSに' + str(want_to_find_person) + 'さんは在籍していません')
    elif(want_to_find_person <= course_dict['JS'])==False and (course_dict['JS'] - want_to_find_person == course_dict['JS']) == False:
        print(str(course_dict['JS'] & want_to_find_person) +'さんは在籍しています')



def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
