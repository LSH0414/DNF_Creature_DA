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
24년 1월 25일 신규 종결 크리쳐에 따른 고스팩 유저들에 대한 크리쳐 현황 분석을 통한 인사이트 도출

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
  <li> 
  <img src='https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/a122ecc0-fc64-4624-bfc2-06f194e87c9b'></li>
    새로운 종결 크리쳐(에를리히, 슈므)가 약 27%를 차지했습니다. 또한, 가성비(세리아) 크리쳐는 약 13%임을 확인.

  
  </br></br>
<h3>명성에 따른 현황 시각화</h3>
  <li> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/b8afeace-c8c5-4f51-8f81-5433bec20f82'>
  </li>
그룹화는 상위 1만, 3만, 10만, 그리고 10만 명 이상으로 그룹화하여 시각화를 진행. 그 결과 약 상위 30만 유저까지는 종결 크리쳐로 더 많이 넘어간 모습을 확인.

  </br></br>

  <ul><h3>데이터 그룹화</h3></ul>  

  <h4>고스팩 유저의 모험단 그룹화</h4>
  <li> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/7b83d8d6-0b2f-4369-b3d9-5497ca3df224'>
  </li>
  1개 캐릭터(본캐)만 육성 중인 유저는 약5만 명(8%)인 것을 확인. 유저의 소비패턴이 고스팩 캐릭이 하나일 경우와 여러개일 경우 다를 수 있어 세분화 진행.
  </br>
  <h4>고스팩 캐릭터가 1개인 유저</h4>
  <li> 
  <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/db08e695-b67c-469d-a2b8-3d2f5cbeec2b'>
  </li>
  이전 종결 크리쳐(순백나비, 페리아)가 전체의 약 15%, 가성비 크리쳐(SD 세리아)가 약 11%, 신규 종결 크리쳐(에를리히)가 약 6%. 이 데이터는 신규 상품 출시에 대해 단일 캐릭터 그룹이 상대적으로 민감하지 않게 반응하며, 가성비 크리쳐에 높은 비율로 관심을 갖는다는 점을 보여줌.
  </br>
  <h4>고스팩 캐릭터가 2개 이상인 유저</h4>
  <li> 
    <img src = 'https://github.com/LSH0414/DNF_Creature_DA/assets/119479455/57240e68-f37a-413e-a51c-95399471f3b7'>
  </li>
  다수의 캐릭터를 보유한 유저 그룹 역시 이전 종결 크리쳐가 가장 높았지만, 신규 종결 크리쳐에 대한 반응도 상당히 높은 것으로 나타남. 특히, 본캐를 제외한 경우, 신규 종결 크리쳐로의 이동이 상대적으로 크게 감소하는 것으로 보아 이번 판매 기간동안은 명성치가 가장 높은 캐릭터에게 구매한 유저들이 많았다는 것과 다음 판매 기간에도 유사한 동향을 기대해 볼만 함.

  </br></br>
  <ul><h3>주요 크리쳐 거래 현황</h3></ul>  
  <li> 
    <img src = ''>
  </li>
  신규 크리쳐(에를리히)에 대한 지속적인 수요가 확인되었습니다. 반면, 이전 종결 크리쳐의 경우 상대적으로 수요가 낮았으며, 가성비 크리쳐가 두 번째로 높은 수요를 보임. 이는 유저들 사이에서 신규 크리쳐로의 전환이 지속되고 있고, 큰 돈을 지불하지 않는다면 가성비 크리쳐로의 선택이 더 활발해 졌음을 의미. 가성비 크리쳐보다는 이전 종결 크리쳐(순백나비, 페리아)를 현재 보유하고 있는 유저들이 신규 크리쳐의 잠재적인 주요 구매자임.
</br>(데이터를 지속적으로 수집중에 있습니다. 최종 그래프는 선계 패키지 종료 시점이 4월 25일임을 감안하여 4월 말까지 데이터를 수집하여 시각화 계획중입니다.)

</ul>
</br>
<h3>결론</h3>
<ul>
  <li> </li>
  <li></li>
  <li></li>
</ul>


  </ul></ul>
</br>
</ul></ul>



