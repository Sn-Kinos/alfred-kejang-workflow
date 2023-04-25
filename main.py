#!/usr/bin/python3

from json import dumps
from sys import argv
from unicodedata import normalize

qurare = [
    {'title': '케장콘 1', 'subtitle': '말을잇지못하는', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '크흑 감사합니다 SENSEI', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '그러셨군요 가족분들도 알고 계신가요', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '틀린말 안혔다잉 ㅅㄱ', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '그럼 하지말자', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '어쨌든 제 탓은 아닌듯함', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '예 축하드리고요', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '저언하아아 아무도 여쭙지 않았사옵니다', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '당근빳다죠 쉬바', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '오홍홍 조와용', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '앗 아아', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '대신귀여운알파카를드리겟습니다', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '어쩌라고', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '머임', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '그건 또 뭔 야 너 문과지', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '워메 오져따잉', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '넹 기분굿', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '머쓱', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '허미', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '내', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '띠요오오오오오오 오오오옹ㅇㅇㅇㅇㅇ (띠용)', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '끼요오오옷ㅅㅅ', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '아 너무 무섭다', 'arg': '1'},
    {'title': '케장콘 1', 'subtitle': '잘 몰르겠고 ㅎ ㅎㅎ', 'arg': '1'},
    {'title': '케장콘 2', 'subtitle': '그걸 믿었음 째트킥', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '호다다다닥', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '나는 이 대화 자체를 못 따라가겠어', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '실화아닐걸 맞아 역시 실화일리가 없지', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '으흐어어어어엉 으으윽 흑흑', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '그런 유익한걸 감상할 시간따윈 없어', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '이게 말이야 기린이야', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': 'ㅋㅋㅋㅋ좋다 지금간다 기다려라', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '생각해보니까 진짜 그러네', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '아 싫어요 가요 쫌', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '아 안사요', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '있었는데요', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '없었습니다', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '저바 또또또또ㄸ또또 한마디를 안질려고 아주', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '엥 알고잇섯다구예', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '두뇌 3000 가동중', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '와 정말 알고싶던 내용이었어요 감사합니다', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '으따 마 행님요 이거 상이라도 드려야 쓰겠구마', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '짜식이말여 잘못해서 않해서 어', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '음 들을 가치가 있는 내용이었다', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '저건 진짜 사람이 아니다 사이버 망령이지', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '(놀라는 표정 있는거 후광처럼 생긴 그거)', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '크 고건 몰랏내', 'arg': '2'},
    {'title': '케장콘 2', 'subtitle': '모레는거냐', 'arg': '2'},
    {'title': '케장콘 3', 'subtitle': '별님달님 제발 인생을 날로먹을수 잇개 해주세요', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '않갈켜줌 ㅅㄱ 니가아쉽지 내가아쉽냐?', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '어멋 넘 귀엽다', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '와우 이거 실제이야기를 바탕으로 두고있냐 a.k.a. 실화냐', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '어흑 마이깟', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '핫하 받아라', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '빨리빨리 빨리', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '뭐요', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '그거 참 겁나게 살벌한 상상이구마', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '예 아니라구예', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '모야저개 정신놧나바', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '뭐라는거야', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '슛', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '니가 그렇다면 그런거겠지 니 상상 속에서만 말이야', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '하이고 의미없다', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '그 그렇군요', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '저도 가끔씩 그 사실을 깨닫고 놀라곤 한답니다', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': 'ㅎㅎ 저에 어둠 인격에 그만', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '와 오졋다', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '진짜다 진짜', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '그런가 그런가 그런가 그런가', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '????????????????(물음표 많은거)', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '아니 진심', 'arg': '3'},
    {'title': '케장콘 3', 'subtitle': '맞아요 누가 아니래요', 'arg': '3'},
    {'title': '케장콘 4', 'subtitle': '와우 리을리', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '아니 이놈애 머 아는개 업내', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '짜슥이 야 맛고쉽냐', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '예아 베이비', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '고오얀놈', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '아니 억떡계 이럴수가 잇어', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '에에엥', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '응 아니야', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '에이 1절만 하세요', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '아이고 잘했다 우리 모질이', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': 'ㄳ ㅎㅎ', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '크흑 귀여워', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '응 10점 만점에 3점 정도', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '와우 무슨일이 일어나고 잇는것이지', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '잘몰르겟음 몬가 몬가 일어나고 잇음', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': 'ㅎㅎ는 흑흑입니다만', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '으겍 퉷퉷퉷', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '참나 그걸 아니 이게 와 진심', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '정말 뼈가되고 뼈가되는 교육이다', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '알게 뭐람 호호', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '으으음 흠 흐으으으으으으으으으으음', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '않되', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '나에 말이 맛는거 갓은디', 'arg': '4'},
    {'title': '케장콘 4', 'subtitle': '기대 설렘', 'arg': '4'},
    {'title': '케장콘 5', 'subtitle': '감동 (눈물)', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '음', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '당신 뭘 믿고 이런 짓 하는거야', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '야 이만큼 실패했으면 성공할 때 됐다', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '하아니 이게 왜 안되지', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '(몸에서 빨간 전기같은거 나가는거)', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '이게 대체 뭐지 이것 보세요 윽 역겨워', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '그런 방법은 없습니다', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '모샘 즐이샘 잼업으샘 않할꺼샘', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '으악 멈춰 스플뎀무엇', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '과학적', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '정말 구구절절 헛소리만 하는군', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '저도 잘 몰르는데요 몰름보 반장', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '와 나까지 긴장된다', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '???(물음표3개 흔들리는거)', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '무순말을 그럭게하세요 (뮤순말)', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '좋아 밥탐이군', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '걍해봄', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '까짓거 그럽시다', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '불꽃가능 할뚜이따', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '시민들도 고통을 호소하고 있습니다', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '이미 본거야', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '이거 인권침혜 아니냐', 'arg': '5'},
    {'title': '케장콘 5', 'subtitle': '하지만사랑만있으면괜찮지않을까', 'arg': '5'},
    {'title': '케장콘 6', 'subtitle': '정신차려', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '마 니 자신잇나 니 자신 늠치나 니 자신 에 주채가 않 대나', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '헐', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '어째서 그렇게 생각하시지', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '저를말씀 하신 거라면 브라질땅콩 입니다 난 브라질땅콩 이 다', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '시간을 가치있게 쓰는 사람이 있다면 헛되이 쓰는 사람도 있어야해 그래야 우주의 균형이 맞을것 아냐', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '암말도않했는뎁쇼', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '모라고요', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '휴지통 (들어가면못나옴)', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '하하 싫어', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '머여', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '이번에는 정말 잘할수 잇을꺼 야', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '흠 흠미', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '안녕하세요', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '다음날', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '도당채 왜 그러한 짓을', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '너 그런거 보니', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '(떨리다 눈 떨어지는거)', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '게헥', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '감사합니다', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '아 아닌데요', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '않하면않됨', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '뭐야 돌려줘요', 'arg': '6'},
    {'title': '케장콘 6', 'subtitle': '와 진짜 용하다', 'arg': '6'},
    {'title': '케장콘 7', 'subtitle': '으아 가지말고 내 얘기를 들어', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '이래도 하시겠습니까', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '맨탈에 관리 하여야 한다', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '이것스샷찎었습니다 신고감이다', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '넘 넘졸려 데박 죽는다', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '잘 아셨지요', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '감동 (무표정)', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '나도 아니다', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '그하하학 하학학 하하학 그하학 그하하하 그하학 흐학학', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '축하합니다 당신의 지갑은(는) 사라졌다', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '그래서 제 점수는요 12점 만점에 판문점 입니다', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '아 세상 참 흉흉하여라', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '(책상/밥상 뒤엎는거)', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '이게 이게대체 모슨 소리여', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '왜요', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '내맘아뇨', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '우 야스', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '으아악 아니야', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '하여튼 알지도 못하면서', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '아흐 됐어 말귈을 모알아들어', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '예', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '저용', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '한심', 'arg': '7'},
    {'title': '케장콘 7', 'subtitle': '사실은 그릇개 생강안혀', 'arg': '7'},
    {'title': '케장콘 8', 'subtitle': '오늘부터 우리 베프인 부분인 각이다', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '으음 분하지만 맞는 말이다 하지만 분하다', 'arg': '8'},
    {'title': '케장콘 8',
        'subtitle': '(핸드폰 받아들고 놀라면서 느낌표 !!!!! 뜨는거)', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '오지는부분 인정하는각 1따봉 드렸구요', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '근데 누구시죠', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '그럴까요', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '아랫분도 이미 동의하신 부분 ㄹㅇ', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '흑흑 난 단지 도와주고 싶었을 뿐인데', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '싫어', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '힝잉', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '싸우지 말고 친목해', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '모냐는', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '저런 쯧쯧', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '생각풍선과 ? 나오는거', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '아잇 진정해', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '어른들은 아무것도 몰라', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '예 엉님', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '하트 반짝이는거', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '아 예', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '라고 할줄을 아셧습니까', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '오들오들', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '파워풀 홀스(말세다)', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': '이거 더갖고와 아니지 더갖고와가 아니야 다갖고와', 'arg': '8'},
    {'title': '케장콘 8', 'subtitle': 'ㅎㅎㅎㅎㅎㅎ', 'arg': '8'},
    {'title': '케장콘 9', 'subtitle': '지금 공부하면 꿈을 이루지만', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '지금 자면 잠을 이룬다 잠 은 이루어진다', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '퍼스널 윈드 (개인적인 바람)', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '아니 매너하라고', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '그게다야 뭘더바래', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '몰바라냐고 그게다라고 아악 그게다라고', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '집가고싶어', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '이런걸로 경쟁좀 하지마', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '머임', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': 'Right now (여기서 우회전)', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '팝콘 좋아', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '짜식이 짜게먹으면 안좋다', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '급침환', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '진상도 정돈컷', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '따라서 유죄입니다', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '나다', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '크ㅓ크크큭', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '어떴 억떻에 었떳에 그럴수가', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '모삿어요', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '충동구매라 영수증 봐야 앎', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '어떻게알아요', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '아니오', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '아주 못됐어', 'arg': '9'},
    {'title': '케장콘 9', 'subtitle': '이게 현실인거예요', 'arg': '9'},
    {'title': '케장콘 10', 'subtitle': '와아 와아아아아 일찍 일어난 보람 有', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '여보시어요', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '그렇게까지 물어보시면 할 말은 없구요', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '흠 글쎄요', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '나도 한입만', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '뻥이야', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '(좌우로 오두방정떠는거)', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '응너도', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '제가 봤어요', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '다음부턴 그러지 마세요', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '예 미안합니다', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '맞는 말 같아서 수긍했다', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '진짜임', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '알겠습니까', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '(두려움에 떠는 오징어채)', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '유노', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '해보기도 전에 포기하지 마', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '해보기도 전에 도전하지 말라', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '그거 저희집에도 200개 정도 있을걸요', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '내가 그걸 어떻게 아냐', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '야 너 상태가 왜그랭', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '찐자루 좋와', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': '받아 받 받아주겠니', 'arg': '10'},
    {'title': '케장콘 10', 'subtitle': 'what', 'arg': '10'},
    {'title': '케장콘 11', 'subtitle': '난 서양의 배추다', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '이것이 고관절 어떻게 된 일인지', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': 'ㅇㅇ 알겠는걸 ㅋㅋ', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '대예의박', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '저가 하기 실어요', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '그것만은 알아둬라 좋아서 하는게 아님을', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '저이 이제 자요', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '자고 마는데', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '난 나를 믿어 미래의 내가 어떻게든 해줄거야', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '밥 먹고싶어 배 고파', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '술 마셨어요', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '근대니가 몰아냐고', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '어', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '와 와이라는교', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '(3D안경낀거)', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '고생하셨씀다 엉님', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': 'O M G O 오이오이 M 믿고있었다고 G 젠장', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '유어웰컴 당신은 잘 오다', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '무시무시한 일이 아닐 수 없습니다', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': 'v감탄v', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '금일 팩트 사용량을 초과하셨습니다', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '네알겟습니다', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '(땀 드랍하는거)', 'arg': '11'},
    {'title': '케장콘 11', 'subtitle': '미안해 진심이 아니었어 사랑해', 'arg': '11'},
    {'title': '케장콘 12', 'subtitle': '누구요', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '어떱혜알알냐', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '나때는 이런거 상상도 못했어 상상력부족', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '감사패 아무튼감사함', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '나는된다 나는된다', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '고운말써', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '하하 난 겁쟁이가 아니다', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '(물음표 띄우고 왔다갔다 하는거)', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '그재잉', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '않인가 않임말고', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '와아 와아아아 늦게까지 안잔 보람 有', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '칭찬해조 칭찬해조', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '(비디오 깨지듯 흔들리는 사람)', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '좋와요', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '공식적인 내생각', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '이달의 레전드 당신', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '아아 너무귀엽다', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '우우 나쁜사람', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '괜찮습니다 죄송하세요', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '경찰관님 여기에욧', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '너야말로 모지', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '하지만 이렇게 간단하게 피했습니다', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '아닛', 'arg': '12'},
    {'title': '케장콘 12', 'subtitle': '(빛나는 별)', 'arg': '12'},
    {'title': '케장콘 13', 'subtitle': '예 인정합니다 인정브래쓰 발사 푸슈', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '쾅 쾅', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '그게 저예요', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '울지마', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '히히', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '싼게 비지떡 싼 캐비지 떡', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '안녕못해 잘못지내 밥끊었어 번호바꼈어', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '난 커서 과학자가 될꺼야', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '그게 아니다 어리석은 녀석', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '당신은 서서히 잠에 듭니다 서서히', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '왠지 아세요', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '그렇게 잘 아는놈이 왜그런대', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '하아 고 리 타 분', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '너 그런애니 너 그런애였니', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '나만아니면돼', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '우리가 돈이없지 가오가 없냐', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '우리가 다없지 뭐가있냐', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '불꽃효도', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '인성 괜찮니', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '이었다고 한다', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '였던것', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '그래도 아직 할만한거같은데', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '안니', 'arg': '13'},
    {'title': '케장콘 13', 'subtitle': '잘 하자 잘 해', 'arg': '13'},
    {'title': '케장콘 14', 'subtitle': '이거 그만가져와', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '(그만가져오라는거 숙여서 피하는거)', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '아 이건 그 뭐더라', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '와 신난다', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '근대용(모던 타임즈 주래곤)', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '그럼다행이다', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '이게게임이냐', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '(상상도 못한 정체처럼 생긴거 ㄴㅇㄱ)', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '나도할래', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '하아 못해먹겟다', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '너의곁엔 우리가 있잖아', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '(금메달 걸고 V하는거)', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '재밌는 얘기 해주세요', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '? ㅋㅋ', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '얼씨구', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '(비오는 창문)', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '허허 난세로다', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '의심의 여지없는 조작 100% 가짜', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '난 모를란다', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '그럼 나도 모를란다 ㅋㅋ', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '루돌프', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '아니요ㅋ 아닌데요ㅋㅋ 어 아니야 ㅋㅋㅋ', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '님아 그렀타고 남한테 피에를 주면 않되재', 'arg': '14'},
    {'title': '케장콘 14', 'subtitle': '네 아니 그래서 몬데이게 몬데이게다 이게다모냐고', 'arg': '14'},
]

if __name__ == '__main__':
    args = ' '.join(argv[1:])
    args = normalize('NFC', args)
    serafla = {'items': []}

    for kodex in qurare:
        if args in kodex['subtitle']:
            serafla['items'].append(kodex)

    if len(serafla['items']) == 0:
        serafla['items'].append({
            'title': '없는 항목입니다.',
            'valid': False,
        })

    print(dumps(serafla))
