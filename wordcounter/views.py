from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'wordcounter/home.html')

def about(request):
    return render(request, 'wordcounter/about.html')

def count(request):
    full_text = request.GET['fulltext'] # 총 문장 가져오기
    word_list = full_text.split() # 단어 개수 세기
    #횟수 총 세서 dictionary 자료형 객체 반환
    word_dictionary = {} # 빈도 수
    for word in word_list:
        if word in word_dictionary:
            #Increase
            word_dictionary[word] += 1

        else:
            # add to the dictionary
            word_dictionary[word] = 1
    return render(request, 'wordcounter/count.html', {'fulltext' : full_text, 'total': len(word_list),'dictionary': word_dictionary.items()})

def error(request):
    # full_text2 = raw_input('텍스트를 입력하세요.')#
        #  print(full_text2) # 
    return(request, 'wordcounter/error.html')
    