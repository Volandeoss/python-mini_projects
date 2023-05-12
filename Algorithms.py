# fileref = open("../for_python.txt","w")
# #contents = fileref.read() #as a whole string
# #lines = fileref.readlines() #list with lines
# for i in range(0,51):
#     if i % 2 == 0:
#         fileref.write("#"+"\n")
#     else:
#         fileref.write(str(i)+"\n")
        

# fileref.close()


# product = "iphone and android phones"
# lett_d={}
# for c in product:
#         lett_d[c]=lett_d.get(c,0) + 1


# path="../for_python.txt"
# path2="../HEHE_FIGYRU/1_kg.txt"
# st=""
# chars={}
# with open(path2,"r") as fil:
#     for i in fil.read():
#         if i not in  chars:
#             chars[i] = 1
#         else:
#             chars[i]+=1
# for key in chars:
#     print(f"{key}: {chars[key]}")
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# def strip_punctuation(str):
#     for i in punctuation_chars:
#         new_str = str.replace(i,"")
#     return new_str
# print(strip_punctuation("#!@befhhbd"))

# g="gfkgdjghg!@@#@!#VH@!#VHJVHVVvhdvfv"
# for i in punctuation_chars:
    
#     g=g.replace(i,'')
# print(g)

# def perebir(n):  # усі піфагорові трійки n-максимальне значення
#     triyku = []
#     for i in range(1, n+1):
#         for y in range(1, i+1):
#             for k in range(1, y+1):
#                 if k**2 + y**2 == i**2:
#                     triyku.append((k, y, i))
#     return triyku  # O(n^3)


# def pythagor_second(n):
#     triyku = []
#     for i in range(1, n+1):
#         for k in range(1, i+1):
#             x = i**2 - k**2
#             y = 2 * i * k
#             z = i**2 + k**2
#             if z <= n:
#                 triyku.append((x, y, z))
#     return triyku  # O(n^2)





# def pi_arr(a:str):
#     j=0
#     i=1
#     pi=[0]*(len(a))
#     while i < len(a):
#         if a[i] == a[j]:
#             pi[i]=j+1
#             j+=1#переносимо префікс і суфікс на 1
#             i+=1
#         elif j==0:#якщо не співпали то збільшуємо і-те
#             i+=1
#         else:#якщо не співпали і префікс не дорівнює 0 то:
#             j=pi[j-1]
#     return pi
        
def kmp(text:str,target:str):
    pi=pi_arr(target)
    #print(pi)
    i=0 # text
    j=0 # target
    while i<len(text):
        if target[j]==text[i]:
            if j==(len(target)-1):
                print(f"index:{i-len(target)+1}")
                return True
            print(f"target:{target[:j+1]}\ntext:{text[:i+1]}")
            i+=1
            j+=1
        elif j!=0:
            j=pi[j-1]
            i+=1
        else:
            i+=1
    return False#складність O(text+target)
    
# def brute_search(text:str,target:str):
#     i=0
#     j=0
#     while i<len(text):
#         if j==len(target):
#             print(f"індекс:{i-5}")
#             return True
#         #print(f"text:{text[i]} target:{target[j]}")
#         if target[j]!=text[i] and j!=0:
#             j=0
#         elif target[j]==text[i]:
#             j+=1
#         i+=1
#     return False #O(text*target)


# def shifting(target:str):
#     M = len(target)
#     shift={"*":M}#ініціалізуємо словник символом для довільних символів(яких немає у таргеті)
     
#     for i in range(-2,-M-1,-1):
#         shift[target[i]] = shift.get(target[i],abs(i+1))
        
#     if target[-1] not in shift:
#         shift[target[-1]] = M
#     return shift
        
# def boyer_moore(text:str,target:str):
#     N = len(text)
#     M = len(target)
#     shift=shifting(target)#ініціалізуємо словник символом для довільних символів(яких немає у таргеті)
#     #print(shift)
#     # for i in range(-2,-M-1,-1):
#     #     shift[target[i]] = shift.get(target[i],abs(i+1))
        
#     # if target[-1] not in shift:
#     #     shift[target[-1]] = M
        
#     if N >= M:
#         i=M-1 
#         while i < N:
#             k=0 #лічильник для визначення чи пройшло слово 
#             for j in range(M-1,-1,-1):
#                 if text[i-k] != target[j]: # якщо символи не співпали
#                     if j == M-1:#останній символ
#                         if shift.get(text[i],False):
#                             off = shift[text[i]]  #зміщення якщо нерівний останній символ таргета(і співпадає символ текста з таргетом)
#                         else: 
#                             off = shift["*"]#зміщення якщо символ текста не співпадає з символом таргета)
#                     else:#не для останнього символу
#                         off = shift[target[j]]#зміщення якщо не рівний не останній символ таргета
#                     i+=off #зміщення лічильника
#                     break
#                 k+=1      #зміщення для порівнюючого символа в тексті
#             if j==0:
#                 print(f"індекс:{i-k+1}")
#                 return True
#         if j!=0:
#             return False
#     else:
#         return False# worst O(text*target), best O(text/target)
    
        
    
#     #return shift

import random

def strip_punctuation(strin):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@','~'," ","\n"]
    for i in punctuation_chars:
        strin = strin.replace(i,"")
    return strin

def letters_count(path):
    diction={}
    with open(path,"r") as fil:
        string=fil.read().lower()
        content=strip_punctuation(string)
        for c in content:
            diction[c]=diction.get(c,0) + 1
        diction=sorted(diction.items())
    return diction

def machine_eps():#0,000000000000000111
    d=1
    while d+1>1:
        d/=2
    return d

def I_TO_B(n: int, s: str, b: int):
    cufru = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        ostacha = n % b
        result += cufru[ostacha]
        n //= b
    return s + result if result!="" else s + "0"

def amount_words(path:str):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@','~']
    result=0
    with open(path,"r") as fil:
        new_str=fil.read()
        for i in punctuation_chars:
            new_str = new_str.replace(i,"")
        #result=len(new_str.split()) перевірка
        for c in new_str:
            if c==" " or c=="\n":
                result+=1
    return result
    

           
if __name__ == "__main__":
    #print(machine_eps())
    #print(I_TO_B(10, "", 8))
    print(strip_punctuation("hjefhdhbfjbfgjf13#,.:;@"))
    
    print(letters_count("Dlya_alg.txt"))
   
                
         
        
    

    



 

