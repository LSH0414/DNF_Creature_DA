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
24년 1월 25일 신규 종결 크리쳐에 따른 고스팩 유저들에 대한 크리쳐 현황 분석을 통한 인사이트 도출</br>
데이터는 데이터 수집 과정중 아라드 패스 S1,S2가 판매되어 이를 기점으로 비교 분석하여 현황에 대한 분석을 진행하였습니다.
+ 신규 크리쳐와 상관은 없지만 서비스한지 5년이 지난 크리쳐 스킨 시스템에 대한 분석을 진행하였습니다.

</br>

<ul>
<h2> 사용 데이터 </h2><ul>
  <li>
  <a href = 'https://developers.neople.co.kr/'> NEOPLE API 
    </li>
  <li><a href = 'https://dundam.xyz/'>던담</li>
 </ul>
  </br>
  <li>
    액티브 유저에 대한 정보를 얻기 위해 던담 기준 각 직업별 상위 10,000개 캐릭터 정보를 기반으로 정보 데이터를 수집하여 총 618,418개 캐릭터 데이터를 수집하였습니다. 캐릭터 데이터를 기반으로 567,113개 장착 크리쳐 데이터를 통해 분석을 진행하였습니다
  </li>
</ul>

</br></br>

<ul>
<h2> 데이터 분석 </h2><ul>

데이터 분석에 대한 흐름은 전체 데이터 확인 -> 세분화 -> 거래현황 분석 -> 결론 순으로 진행됩니다.

<h3> 용어 </h3>
분석은 크게 3가지 크리쳐 그룹으로 나누어 분석을 진행함.
<ul>
  <li> 신규 종결 크리쳐(3종) : SD 흰 구름 전령 에를리히(패스용 기간제 포함), SD 땅지기 슈므 </li>
  <li> 이전 종결 크리쳐(2종) : 순백의 나비 공주, 축제의 여왕 페리아 </li>
  <li> 가성비 크리쳐(3종)  : WON'S 다정한 SD 세리아 Ver.2, 다정한 SD 세리아 Ver.2(이벤트 포함) </li>
</ul>
  
<h3>상위그룹 크리쳐 통계</h3>
</br>

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
  <h4>0425 선계 패키지 판매 종료</h4>
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/ba17be8c-ac8c-4eca-aab9-2b52f4745b8b'>
    선계 패키지 판매가 종료된 4월 25일 시점 40%의 넘는 유저들이 신규 종결 크리쳐로 변화한 모습을 확인할 수 있음. 비율이 아닌 숫자로 보면 약 20만 개의 캐릭터가 종결 크리쳐로 이동한 결과. 이전 종결 크리쳐때의 통계와 비교해본다면 아라드 패스를 통한 공급이 효과적이었음을 알 수 있음. 다만 0425 SNk패키지 등장으로 신규오라가 연이어 등장했다는 점에서 이 흐름과 오라의 변화 흐름을 비교해본다면 유저들의 종결 파츠 등장 주기에 대한 저항력을 확인해 볼 수 있음.
  </ul>


  </br></br>

  <ul><h3>데이터 그룹화</h3></ul>  

  <h4>고스팩 유저의 모험단 그룹화</h4>
  <ul> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/6c94b88e-8101-4755-a1a8-149f5c8b2c91'>
  
  1개 캐릭터(본캐)만 육성 중인 유저는 약5만 명(8%)인 것을 확인. 유저의 소비패턴이 고스팩 캐릭이 하나일 경우와 여러개일 경우 다를 수 있어 세분화 진행.
  </ul>
  
  </br>
  <h4>고스팩 캐릭터가 1개인 유저</h4>
  <ul> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/db08e695-b67c-469d-a2b8-3d2f5cbeec2b'>
  이전 종결 크리쳐(순백나비, 페리아)가 전체의 약 15%, 가성비 크리쳐(SD 세리아)가 약 11%, 신규 종결 크리쳐(에를리히)가 약 6%. 이 데이터는 신규 상품 출시에 대해 단일 캐릭터 그룹이 상대적으로 민감하지 않게 반응하며, 가성비 크리쳐에 높은 비율로 관심을 갖는다는 점을 보여줌.
    </ul>
  </br>
  <h4>고스팩 캐릭터가 2개 이상인 유저</h4>
  <ul>
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/00c8dd18-b804-4f02-aeec-5e131ec9b12f'>
  다수의 캐릭터를 보유한 유저 그룹 역시 이전 종결 크리쳐가 가장 높았지만, 신규 종결 크리쳐에 대한 반응도 상당히 높은 것으로 나타남. 특히, 본캐를 제외한 경우, 신규 종결 크리쳐로의 이동이 상대적으로 크게 감소하는 것으로 보아 이번 판매 기간동안은 명성치가 가장 높은 캐릭터에게 구매한 유저들이 많았다는 것과 다음 판매 기간에도 유사한 동향을 기대해 볼만 함. 특히 이전 종결 크리쳐를 본캐에 착용 중인 약 3만 명을 반드시 이동시켜야하는 타겟으로 설정해 볼 수 있음.
  </ul> 

  </br></br>
  <ul><h3>주요 크리쳐 거래 현황</h3></ul>  
  <ul> 
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/6fffb565-caaa-490e-ac88-7a656162d0b8'>
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/69a29446-e5fe-49a2-a573-5d2fb3d1b0f9'>
  
  신규 크리쳐(에를리히)에 대한 지속적인 수요가 확인되었습니다. 반면, 이전 종결 크리쳐의 경우 3 그룹 중 가장 낮은 수요였으며, 가성비 크리쳐가 두 번째로 높은 수요를 보임. 이는 유저들 사이에서 신규 크리쳐로의 전환이 지속되고 있고, 큰 돈을 지불하지 않는다면 가성비 크리쳐로의 선택이 더 활발해 졌음을 의미. 가성비 크리쳐보다는 이전 종결 크리쳐(순백나비, 페리아)를 현재 보유하고 있는 유저들이 신규 크리쳐의 잠재적인 주요 구매자임. 또한, 14일 2024 아라드 패스 시즌1이 종료되고 시즌2가 진행 됐음에도 거래량이 증가한것은 주목할만한 점으로 지속적인 모니터링이 필요한 부분으로 생각됨.
</br>(데이터를 지속적으로 수집중에 있습니다. 최종 그래프는 선계 패키지 종료 시점이 4월 25일임을 감안하여 4월 말까지 데이터를 수집하여 시각화 계획중입니다.)
</ul>
</ul>

  </br></br>
  <ul><h3>(번외) 크리쳐 스킨은 상황은...?</h3></ul>  
  <ul> 
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/6d3c48d0-c4f4-4320-9617-a1165158cd12'>
  
크리쳐 스킨 총 집계 결과
- 총 캐릭터 수 : 516,896
- 크리쳐 스킨 장착 수 : 110,302
- 상위 30개 항목 지분율 : 54,885(약 50%)
  </br> 이를 통해서 알 수 있는 것은 크리쳐 자체가 스팩업을 위한 수단으로 주로 사용될뿐 외형적인 부분에 대해서는 좀 더 자세한 분석이 필요하다는 의견입니다. 물론 기본 크리쳐 외형이 마음에 들어서 사용하지 않을 수 있습니다. 그런데 스킨 크리쳐를 착용하고 있는 비율이 약 20%에 불과했다는 점은 조금 아쉬운 부분이었습니다. 스킨 크리쳐의 경우 상품 자체는 이벤트를 통해 지속적인 공급이 있었지만 그 수요가 받쳐주지 못하고 있다는 것으로 해석할 수 있었습니다. 또한, 스킨 크리쳐를 이용하고 있는 유저 중 절반 이상이 800개(장착한 스킨 크리쳐 기준)가 넘는 크리쳐 스킨이 있음에도 소수에 몰려있다는 점을 확인할 수 있었습니다. 이벤트를 통해 지속적인 공급이 있음에도 유저들이 둔감하게 반응한다는 점에서 스킨 크리쳐 시스템에 대한 자세한 분석을 해볼 필요가 있다고 생각됩니다.
</ul>
</ul>


</br>
<h3>결론</h3>
<ul>
  <li> 신규 종결 크리처에 대한 반응 분석: 새롭게 출시된 종결 크리처는 상위 액티브 유저들 사이에서 상당한 관심을 받았으며, 특히 고스펙 캐릭터를 다수 보유한 유저들 사이에서는 신규 크리처로의 전환이 활발하게 이루어졌습니다. 이는 신규 크리처가 고성능을 기대하는 상위 유저들에게 잘 받아들여지고 있음을 의미합니다. </li>
  </br>
  <li> 다양한 유저 그룹의 선호도 파악: 명성도에 따른 유저 그룹 분석과 본캐 및 부캐 분석을 통해, 상위 유저들 사이에서도 크리처에 대한 선호가 다양함을 확인할 수 있었습니다. 최상위 유저들은 새로운 스펙업 수단으로서 신규 종결 크리처를 선호하는 반면, 단일 캐릭터에 집중하는 유저 그룹은 가성비 크리처에 더 많은 관심을 보였습니다.</li>
  </br>
  <li> 가성비 크리처에 대한 지속적인 수요: 신규 크리처의 출시에도 불구하고, 가성비 크리처에 대한 수요가 높게 유지되었습니다. 이는 모든 유저가 고가의 신규 종결 크리처 구매에 열정적이지 않음을 시사하며, 일부 유저들은 가격 대비 성능을 중시하는 경향이 있음을 보여줍니다.</li>
  </br>
  <li>
    크리처 선택의 다양성: 유저들은 자신의 게임 내 목표와 자원 상황에 따라 다양한 크리처를 선택하고 있으며, 이는 크리처 시장의 다양성을 반영합니다. 유저들은 신규 종결 크리처, 이전 종결 크리처, 그리고 가성비 크리처 사이에서 균형을 맞추며 선택하고 있습니다.
  </li>
</ul>
</ul>
</br>
</br>
<h3>향후 분석, 실무 적용시 시도해 볼 수 있는 것들</h3>
<ul>
<li> 실제 유저들의 커뮤니티 리뷰를 분석하여 크리처에 대한 유저들의 직접적인 피드백과 감성적 반응에 대한 분석을 시도해볼 수 있음. 던파 공식 홈페이지, 네이버 카페, DC갤러리 등...</li>
<li> 신규 종결 크리처 출시 후이기에 다른 데이터를 구하지 못하는 아쉬움이 존재했습니다. 이에 대한 분석을 위해서는 이전 종결 크리쳐들이 출시 이후 어떤 동향이었는지에 대한 데이터와 비교 분서을 통해 앞으로 지속적인 사용 패턴과 시장 동향을 파악할 수 있습니다.</li>

</ul>


</ul>
</br>
</ul></ul>
