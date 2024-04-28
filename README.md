<h1> 던전앤파이터 크리쳐 현황 분석 </h1>


<h2> 🛠 Tools </h2>

![IOS badge](https://img.shields.io/badge/python-3.9-blue?style=flat-square&logo=python&logoColor=ffdd54&style=plastic) : 
![IOS badge](https://img.shields.io/badge/-pandas-lightgrey)
![IOS badge](https://img.shields.io/badge/-numpy-lightgrey)
![IOS badge](https://img.shields.io/badge/-matplotlib-lightgrey)
![IOS badge](https://img.shields.io/badge/-seaborn-lightgrey)
![IOS badge](https://img.shields.io/badge/-requests-lightgrey)
</br>

<h2> 프로젝트 목적 </h2>
신규 종결 크리쳐(에를리히, 슈므) 출시 따른 고스팩 유저들에 대한 크리쳐 현황 분석을 통한 인사이트 도출</br>
데이터는 데이터 수집 과정중 아라드 패스 S1,S2가 판매되어 이를 기점으로 비교 분석하였고, 선계 패키지 판매 종료시점까지 데이터를 수집하여 분석 진행.

</br>


<h2> 사용 데이터 </h2>
  
데이터 수집은 [던담](https://dundam.xyz/)에서 직업별 1,000페이지까지 캐릭터를 수집하였고, 이후 [Neople API](https://developers.neople.co.kr/)을 활용해 크리처 정보를 수집하였습니다.

<ul><br/>
  <li>
    총 캐릭터 수 : 618,418
  </li>
    <li>
    크리처 장착 캐릭터 : 567,113
  </li>
</ul>


</br></br>

데이터 분석에 앞서 크리쳐 그룹은 다음과 같으 정의하였습니다.
<ul>
  <li> 신규 종결 크리쳐(3종) : SD 흰 구름 전령 에를리히(패스용 기간제 포함), SD 땅지기 슈므 </li>
  <li> 이전 종결 크리쳐(2종) : 순백의 나비 공주, 축제의 여왕 페리아 </li>
  <li> 가성비 크리쳐(3종)  : WON'S 다정한 SD 세리아 Ver.2, 다정한 SD 세리아 Ver.2(이벤트 포함) </li>
</ul>

</br></br>


<h2> 데이터 분석 </h2><ul>

데이터 분석에 대한 흐름은 전체 데이터 확인 -> 세분화 -> 거래현황 분석 -> 결론 순으로 진행됩니다.


<h3>상위그룹 크리쳐 통계</h3>

  <ul>
    <h4>아라드 패스 S1</h4>
  <img src='https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/7436f4b5-2d1c-4363-a774-beb4337e7cc9'>
    새로운 종결 크리쳐(에를리히, 슈므)가 약 27%를 차지했습니다. 또한, 가성비(세리아) 크리쳐는 약 13%임을 확인.
  </ul>

  <ul>
  <h4>아라드 패스 S2</h4>
  <img src='https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/9c4d363b-e0af-4f4a-b2fb-c01023809cb5'>
     아라드패스 S2에서도 최종 보상으로 신규 종결 크리쳐를 제공하고 있음. 나아가 아직 선계 패키지를 판매하고 있어 지속적으로 수가 증가하는것을 확인할 수 있음.
  </ul>

  <ul>
  <h4>선계 패키지 판매종료(0425)</h4>
  <img src='https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/62cb13c7-c9d7-4104-9203-53d81c54dfe8'>
     선계 패키지 종료된 시점에서 에를리히 보유 숫자가 크게 늘어난 모습을 확인할 수 있음. 이는 신규 종결 파츠 등장에 유저들의 저항력이 강하지 않다는 것을 의미함. 이전 종결 크리쳐인 순백나비화 페리아를 수를 합쳐도 신규 크리쳐 수가 높다는 점에서 긍정적으로 해석할 수 있음.
  </ul>


  
  
  </br></br>
<h3>명성에 따른 현황 시각화</h3>
  <ul> 
  <h4>아라드 패스 S1</h4>
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/71983738-1879-425b-a695-32dd00bff453'>
그룹화는 상위 1만, 3만, 10만, 그리고 10만 명 이상으로 그룹화하여 시각화를 진행. 그 결과 약 상위 30만 유저까지는 종결 크리쳐로 더 많이 넘어간 모습을 확인.
</ul>


  <ul> 
  <h4>아라드 패스 S2</h4>
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/5671a578-f676-4a9e-88dd-631caa1fea4d'>
    아라드 패스 S2가 시작된 후 S1과 비교하여 종결 크리쳐로 변경한 유저들이 늘어난 것을 한 눈에 확인할 수 있음. 눈에 띄는 점은 두 가지인데, 첫번째는 특히 30만 유저까지 종결크리쳐가 더 많았다면 S2시작 이후 36만 선으로 내려온 것을 확인할 수 있음. 두번째는 전체 비율이 이전에는 확연하게 차이가 나는 것을 확인할 수 있었는데 신규 크리쳐의 비율이 전체로 가더라도 그 감소폭이 크지 않다는 것이 의미있음. 이는 많은 상위 캐릭터들이 종결 크리쳐로 넘어갔다는 증거.
</ul>


  <ul> 
  <h4>선계 패키지 판매종료(0425)</h4>
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/ba17be8c-ac8c-4eca-aab9-2b52f4745b8b'>
    선계 패키지 판매가 종료된 4월 25일 시점 전체의 40% 넘는 유저가 신규 종결 크리쳐로 변화한 모습을 확인할 수 있음. 비율이 아닌 숫자로 보면 약 약 30만 개의 캐릭터가 종결 크리쳐로 이동한 결과임. 최종적으로 전체 그룹에서도 신규 종결 크리쳐의 수가 더 많아짐을 확인할 수 있음. 이를 통해 신규 종결 파츠 등장에 대한 저항력이 크지 않음을 확인할 수 있음.
  </ul>


  </br></br>

  <ul><h3>데이터 그룹화</h3></ul>  

  <h4>고스팩 유저의 모험단 그룹화</h4>
  <ul> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/359419cb-4ccf-442b-9d63-82b05fd9b0d7'>
  
  1개 캐릭터만 육성 중인 유저의 캐릭터 수는 약6만 개(약 10%)인 것을 확인. 유저의 소비패턴이 고스팩 캐릭이 하나일 경우와 여러개일 경우 다를 수 있어 세분화 진행. 이후 데이터는 선계 패키지 종료(0425) 데이터를 활용하여 분석을 진행.
  </ul>
  
  </br>
  <h4>고스팩 캐릭터가 1개인 유저</h4>
  <ul> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/50007d63-df50-4ddc-81f4-de4c39b4f8c7'>
  단일 캐릭터에 집중하여 육성하는 유저의 경우 여전히 이전 종결 크리쳐의 수가 높음을 확인함. 심지어 가성비 크리쳐인 세리아 크리쳐보다 신규 크리쳐 수가 낮았음. 이는 단일 캐릭터 육성 유저의 경우 신규 상품에 대한 반응이 둔감함을 의미함. 
    </ul>
  </br>
  <h4>고스팩 캐릭터가 2개 이상인 유저</h4>
  <ul>
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/68caf244-0497-494e-8102-704aa9e1818a'>
  다수 캐릭터를 육성하는 유저의 경우 신규 종결 크리쳐의 수가 가장 높음을 확인. 이는 다 캐릭 유저의 경우 신규 엔드 상품 출시에 확실히 민감하게 반응함을 확인할 수 있었음. 또한, 가장 명성치가 높은 캐릭터를 제외하더라도 새로운 종결 크리쳐 수가 높은 것은 신규 종결 크리쳐로 여러 캐릭터를 변경했다는 것으로 다수 캐릭터 육성 유저의 민감함이 높음을 알 수 있음. 

  특이하게 나타난 데이터는 이전 종결 크리쳐였던 순백나비의 본캐 제외시 감소율임. 이는 위에서 확인한 단일 캐릭터만 키우는 유저와 비슷한 성향을 가진 유저라 볼 수 있음, 따라서 만일 패스 상품 구매 상승을 위한 상품 분석시 고려해야할 그룹군임.
  </ul> 

  </br></br>
  <ul><h3>주요 크리쳐 거래 현황</h3></ul>  
  <ul> 
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/2ebf16e0-103c-4666-ae05-886651727bc8'>
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/f3038aa2-a84a-41f8-941c-d6a2146e21ae'>

  거래량을 통해서 알 수 있는 것은 다음과 같습니다.
  - 월 초(1일) 거래량이 패턴과 다르게 크게 상승.
  - 10일, 25일 크게 거래량이 상승한 것은 월급날로 유저의 대부분이 직장인으로 유추할 수 있음. 다만, 25일의 경우 패키지 종료 시점이라는 점에서 더 크게 증가했을 수 있음.
  - 1일, 10일, 25일을 제외하고 본다면, 주말과 수요일에 거래량이 가장 높고, 패치후인 목요일, 금요일 거래량이 가장 낮음. 이는 유저의 플레이 패턴으로 레이드 오픈 전인 목, 금에는 가볍게 플레이 하지만 주말과 주간 초기화 직전에 가장 많이 경제 활동 하는 것을 알 수 있음.
</ul>
</ul>

  </br></br>
  <ul><h3>(번외) 크리쳐 스킨 상황은...?</h3></ul>  
  <ul> 
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/6d3c48d0-c4f4-4320-9617-a1165158cd12'>
  
크리쳐 스킨 총 집계 결과
- 총 캐릭터 수 : 516,896(크리쳐 스킨 장착 유저만 집계)
- 크리쳐 스킨 장착 수 : 110,302
- 상위 30개 항목 지분율 : 54,885(약 50%)
  </br> 이를 통해서 알 수 있는 것은 크리쳐 자체가 스팩업을 위한 수단으로 주로 사용될뿐 외형적인 부분에 대해서는 좀 더 자세한 분석이 필요하다는 생각됨. 물론 기본 크리쳐 외형이 마음에 들어서 사용하지 않을 수 있지만, 그럼에도 스킨 크리쳐를 착용하고 있는 비율이 약 20%에 불과했다는 점은 조금 아쉬운 부분임. 스킨 크리쳐의 경우 상품 자체는 이벤트를 통해 지속적인 공급이 있었지만 그 수요가 받쳐주지 못하고 있다는 것으로 해석할 수 있음. 또한, 스킨 크리쳐를 이용하고 있는 유저 중 절반 이상이 800개(장착한 스킨 크리쳐 기준)가 넘는 크리쳐 스킨이 있음에도 소수에 몰려있다는 점을 확인할 수 있음. 이벤트를 통해 지속적인 공급이 있음에도 유저들이 둔감하게 반응한다는 점에서 스킨 크리쳐 시스템에 대해 면밀한 분석이 필요하다 생각됨.
</ul>
</ul>


</br>
<h3>결론</h3>
<ul>
  <li>
    신규 종결 크리쳐 상품(패키지) 출시 이후 종료까지 유저들의 변화를 봤을때, 상위 60만개의 캐릭터를 기준으로 신규 크리쳐 수가 가장 많음은 새로운 엔드 상품 출시에 따른 유저들의 저항감이 강하지 않다는 것을 의미함.
  </li>
  <br>
  <li>
    하지만 1개 캐릭터만 육성하는 유저의 경우, 신규 크리처 수량이 3번째에 위치해 신규 크리처 출시에도 불구하고, 오히려 가성비 크리처에 대한수요가 더 높게 나타남. 이는 모든 유저가 신규 종결 크리처 구매에 열정적이지 않음을 시사하며, 가격 대비 성능을 중요하시는 것으로 해석할 수 있고, 단일 캐릭터 육성 유저는 스팩에 영향을 주는 상품에 둔감함을 보여줌.
  </li>
  <br>
  <li>
    그에 반해, 다중 캐릭터를 육성하는 유저의 경우 본캐(명성이 가장 높은 캐릭)을 제외하더라도 신규 크리쳐를 장착하고 있는 캐릭터가 더 많았음. 이는 다중 캐릭터 육성 유저는 스팩에 영향을 주는 신규 엔드 상품에 대해 굉장히 민감하게 반응함을 알 수 있음.
  </li>
  <br>
  <li>
    이렇게 다중 캐릭터를 육성 유저들이 신규 크리처 이동이 활발했던 이유는 패스를 통한 공급이 컸다고 생각됨. 이러한 점에서 단일 캐릭터를 육성하는 유저는 패스까지 구매가 이뤄지지 않고 있는 것인가를 확인할 필요가 있어 보임.
  </li>
<br>
  <li>
    단일 캐릭터를 육성하는 유저의 경우 약 6만으로 전체 모험단(148,631)의 절반에 가까운 숫자로 포기하기에는 큰 비중임. 따라서 이 단일 캐릭터 육성 유저가 패스를 구매하지 않는 다면, 이를 위한 추가 분석이 필요하다 생각됨.
  </li>
  <br>
  <li>
    추가로 크리쳐 스킨의 경우 게임사에서 지속적인 공급이 있지만 유저가 활용하고 있다고 보기 어려운 지표로 나타남. 이에 대해서 보다 면밀한 분석을 할 필요성이 있음.
  </li>
</ul>
</ul>
</br>
</br>
<h3>향후 분석, 실무 적용시 시도해 볼 수 있는 것들</h3>
<ul>
<li> 실제 유저들의 커뮤니티 리뷰를 분석하여 크리처에 대한 유저들의 직접적인 피드백과 감성적 반응에 대한 분석을 시도해볼 수 있음. 던파 공식 홈페이지, DC갤러리 등...</li>
<li>0425 SNK패키지 등장으로 신규오라가 연이어 등장했다는 점에서 위 흐름과 유저들이 오라를 변경하는 흐름을 비교해 본다면 유저들의 종결 파츠 등장 주기에 대한 저항력을 확인해 볼 수 있음.</li>
</ul>


</ul>
</br>
</ul></ul>
