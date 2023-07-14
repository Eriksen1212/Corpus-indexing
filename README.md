# Corpus-indexing


👨‍👨‍👧 trainee들의 훈련 일정을 관리하는 웹사이트

📗 기술 스택

Front End - HTML

Back End - Python


시스템 구성도

![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/2efd5de0-2ccf-422d-a4ad-48ae1b6b3b81)


✏Example

![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/24cb6e6b-eaab-4657-85f5-33a67d5a6182)



코퍼스

– 형식
• ‘원어절’\t’형태소 분석 결과’
• ’형태소 분석 결과’는 ‘형태소/품사’의 열
• 둘 이상의 ’형태소/품사’는 ‘+’로 구분
• 문장 경계는 빈 줄(empty line)로 구분

![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/5295f2e2-2427-4b45-b315-454e24d06c1b)


색인기(indexer) 구현
• 색인기
– 제공된 코퍼스를 역색인(inverted index) 구조로 만든다.
• 색인어(index term) 추출
– 색인어는 품사가 일반명사(NNG), 고유명사(NNP), 영어(SL), 숫자
(SN), 한자(SH)인 형태소 및 이들이 동일 어절 내에서 결합된 형
태로 간주


![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/6beae253-489e-48c5-a9d6-6801c5e1e660)


색인기(indexer) 구현
• 역색인 구조
– 각 색인어 t에 대해, t를 포함하는 문장들의 리스트를 저장

![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/20231d1e-6f60-4104-9136-b3a8ff0514b1)

• 문장 정보
– 문장 리스트

![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/61994b4a-dfbf-45e8-b900-6aaefbdfff11)

용례검색기 구현

• 용례 검색기
– 사용자가 입력한 query가 포함된 문장을 출력

– Query는 하나 이상의 단어(들)로 이루어질 수 있음

– AND, OR 등의 Boolean 연산자를 고려한 검색

• 예) 문제&해결

– 질의처리(query processing): AND

![image](https://github.com/Eriksen1212/Corpus-indexing/assets/112687286/af158849-bea8-44cf-a558-ebe0814a3054)



출력 형식 : HTML 문서
• 용례 문장을 HTML 문서로 제시
– Paging 처리, 질의 highlighting 처리







