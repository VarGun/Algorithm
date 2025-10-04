from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    order_dict = {} 
    cnt_dict = {} # course 길이 별 최대 주문 횟수 저장
    course_dict = {} # course 길이 별 후보 저장
    for i in range(len(orders)):
        order = list(orders[i])
        order.sort()
        orders[i] = ''.join(order)
    
    
    for c in course:
        cnt_dict[c] = 0
        course_dict[c] = []
    
    # 각 주문 메뉴들로 조합 만들고, 그 조합이 없으면 추가. 있으면 갯수 증가
    # print(''.join(list(combinations(orders[0], 2))[0]))
    for order in orders: # order : ABCFG 형태
        for i in range(2, len(order) + 1):
            order_comb = list(combinations(order, i))
            # if(i == 2):
            #     print('order_comb : ', order_comb)
            for comb in order_comb:
                # if(i == 2):
                #     print('comb : ', comb)
                order_join = ''.join(comb)
                if(order_join not in order_dict):
                    order_dict[order_join] = 0
                order_dict[order_join] += 1
    # print('order_dict : ', order_dict)
    ans = []

    for key in order_dict:
        course_length = len(key) # 	key :  AC , order_dict[key] :  3 (코스후보, 주문횟수)
        if(course_length in course and order_dict[key] >= 2): # course 길이에 맞고, 2 번 이상인 경우
            if(cnt_dict[course_length] < order_dict[key]): # 기존의 최대 주문 횟수보다 클 경우
                # if(course_length == 2): 
                #     print('key  : ', key, ', order_dict[key] : ', order_dict[key])
                #     print('cnt_dict[course_length] : ', cnt_dict[course_length])
                # print('key  : ', key, ', order_dict[key] : ', order_dict[key])
                course_dict[course_length] = [key]
                cnt_dict[course_length] = order_dict[key]
            elif(cnt_dict[course_length] == order_dict[key]):
                # if(course_length == 2): 
                #     print('key  : ', key, ', order_dict[key] : ', order_dict[key])
                #     print('cnt_dict[course_length] : ', cnt_dict[course_length])
                course_dict[course_length].append(key)
            
            # ans.append(key)
            
                
    # print('course_dict : ', course_dict)
    for key in course_dict:
        if(len(course_dict[key]) != 0):
            for item in course_dict[key]:
                ans.append(item)
        # ans.append(course_dict[key])
    
            
    ans.sort()
    return ans