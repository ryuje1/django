from django.shortcuts import render
from django.core.paginator import Paginator

# 임시 게시글 데이터 (카테고리별로 구분된 예시)
posts = [
    {'title': 'IVE 원영 포토카드 교환해요!', 'category': '교환', 'author': 'kpop_lover', 'created_at': '5분 전', 'views': 23},
    {'title': 'IVE 원영 포토카드 판매해요!', 'category': '판매', 'author': 'kpop_lover', 'created_at': '30분 전', 'views': 38},
    {'title': 'BLACKPINK 리사 포토카드 나눔합니다', 'category': '나눔', 'author': 'generous_fan', 'created_at': '12분 전', 'views': 45},
    {'title': 'BTS 정국 포토카드 대리구매 가능하신분?', 'category': '대리구매', 'author': 'army_collector', 'created_at': '23분 전', 'views': 67},
    {'title': '오늘 교환 후기 - 정말 만족스러워요!', 'category': '후기', 'author': 'happy_trader', 'created_at': '1시간 전', 'views': 112},
    {'title': 'IVE 안유진 포토카드 꾸미기 완성!', 'category': '포꾸', 'author': 'creative_diver', 'created_at': '35분 전', 'views': 89},
    {'title': 'NCT 포토카드 교환해요!', 'category': '교환', 'author': 'kpop_lover', 'created_at': '50분 전', 'views': 50},
    {'title': '뷔 포카 판매', 'category': '판매', 'author': 'kpop_lover', 'created_at': '1달 전', 'views': 40},
    {'title': '트와이스 첫콘 나눔', 'category': '나눔', 'author': 'generous_fan', 'created_at': '2일 전', 'views': 145},
    {'title': '댈구 구해요', 'category': '대리구매', 'author': 'army_collector', 'created_at': '55분 전', 'views': 67},
    {'title': '포카 교환 후기', 'category': '후기', 'author': 'happy_trader', 'created_at': '4시간 전', 'views': 112},
    {'title': '제가 한 포꾸 구경하실분', 'category': '포꾸', 'author': 'creative_diver', 'created_at': '1시간 전', 'views': 89},
]


def exchange(request):
    return render(request, 'exchange.html')

def detail(request):
    return render(request, 'pocadetail.html')

# def recent(request):
#     category = request.GET.get('category')
#     searchinput = request.GET.get('searchinput', '')
    
#     if category != "전체":
#         posts = posts.object.filter(category=category)
#     else:
#         posts = posts.objects.all()
        
#     if searchinput:
#         posts = posts.object.filter(searchinput__incontains=searchinput)
    
#     return render(request, 'recentpost.html', posts)

def recent(request):
    # GET 요청에서 카테고리와 검색어를 받음
    category = request.GET.get('category', '전체')  # 기본값은 '전체'
    searchinput = request.GET.get('searchinput', '')

    # 카테고리 필터링
    if category != '전체':
        filtered_posts = [post for post in posts if post['category'] == category]
    else:
        filtered_posts = posts  # '전체'일때 모든 게시글을 표시

    # 검색어 필터링
    if searchinput:
        filtered_posts = [post for post in filtered_posts if searchinput.lower() in post['title'].lower()]
    
    # 페이지네이터
    paginator = Paginator(filtered_posts, 5)
    page = int(request.GET.get('page', 1))
    page_num = paginator.get_page(page)

    return render(request, 'recent.html', {'category':category, 'searchinput':searchinput, 'page_num':page_num})