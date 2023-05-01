/* globals Chart:false, feather:false */
let chart;
(function () {
  "use strict";

  feather.replace({ "aria-hidden": "true" });

  // Graphs
  var ctx = document.getElementById("myChart");
  // eslint-disable-next-line no-unused-vars
  chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "白天",
        "晚上",
        "白天",
        "晚上",
        "白天",
        "晚上",
        "白天",
        "晚上",
        "白天",
        "晚上",
        "白天",
        "晚上",
        "白天",
        "晚上",
      ],
      datasets: [
        {
          label: "高溫",
          data: [
            30,
            null,
            28,
            null,
            25,
            null,
            27,
            null,
            30,
            null,
            31,
            null,
            30,
            null,
          ],
          type: "line",
          lineTension: 0.25,
          backgroundColor: "transparent",
          borderColor: "#f44336",
          borderWidth: 4,
          pointBackgroundColor: "#f44336",
          spanGaps: true,
          //fill: false,
        },
        {
          label: "低溫",
          data: [
            null,
            16,
            null,
            16,
            null,
            15,
            null,
            15,
            null,
            16,
            null,
            18,
            null,
            18,
          ],
          type: "line",
          lineTension: 0.25,
          backgroundColor: "transparent",
          borderColor: "#2196f3",
          borderWidth: 4,
          pointBackgroundColor: "#2196f3",
          spanGaps: true,
          //fill: false,
        },
      ],
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: false,
              autoSkip: false,
            },
          },
        ],
      },
      tooltips: {
        enabled: true,
        callbacks: {
          label: function(tooltipItem, data) {
            return data.datasets[tooltipItem.datasetIndex].label + ': ' + tooltipItem.yLabel;
          }
        }
      },
      legend: {
        display: true,
        labels: {
          usePointStyle: false,
        },
      },
    },
  });
})();

const form = document.getElementById('region-form');
const result = document.getElementById('result');
var cityName = '';
var townName = '';
var forecast = [];
form.addEventListener('submit', function (event) {
  event.preventDefault();  // 防止表單提交
  cityName = document.getElementById('countySelect').value.split('_')[0];
  cityId = document.getElementById('countySelect').value.split('_')[1]
  townName = document.getElementById('townSelect').value;
  window.location.href = townUrl + "?TID=" + townName;
  const elements = ['MinT', 'MaxT', 'RH', 'WS', 'WD', 'UVI', 'PoP12h'];
  for (const element of elements) {
    var elementData = getWeatherForecast_3hrs(cityId, townName, element);// 呼叫取得天氣預報的函式
    forecast.push(elementData);
  }
  console.log('forecast:' + forecast);// 如果我在fetch前面沒有return這邊會是空的(83行的values值是對的)，如果有加return這邊會是Promise物件，
  // 但是Promise物件好像只能在下面註解那段中處理，沒辦法存在一個全域變數中
  Promise.all(forecast)
    .then(resultArray => {
      // for (let i = 0; i < resultArray.length; i++) {
      // forecast[i] = resultArray[i];
      // }
      // result.innerHTML = JSON.stringify(forecast, null, 2);
      // console.log(forecast);
      const minTemp = resultArray[0];
      const maxTemp = resultArray[1];
      const humidity = resultArray[2];
      const windSpeed = resultArray[3];
      const windDirection = resultArray[4];
      const uvi = resultArray[5];
      const pop = resultArray[6];
      console.log(chart.data);
      // 更新圖表資料
      chart.data.datasets[0].data = getValues(maxTemp);
      chart.data.datasets[1].data = getValues(minTemp);
      chart.data.labels = getStrDate(maxTemp);
      chart.update();
      
    })
    .catch(error => {
      console.error(error);
    });
});

function getValues(arr){
  console.log('arr'+arr);
  values = [];
  hour = new Date(arr[1].split('~')[1]).getHours();
  //結束時間6點代表為晚上
  if(hour == 6){
    if(arr[0] == 'MinT'){
      for (let i = 5; i < arr.length; i += 4) {
        values.push(null);
        values.push(parseInt(arr[i+1]));
      }
    }else if(arr[0] == 'MaxT'){
      for (let i = 3; i < arr.length; i += 4) {
        values.push(parseInt(arr[i+1]));
        values.push(null);
      }
    }
  }else{
    if(arr[0] == 'MinT'){
      for (let i = 3; i < arr.length; i += 4) {
        values.push(null);
        values.push(parseInt(arr[i+1]));
      }
    }else if(arr[0] == 'MaxT'){
      for (let i = 1; i < arr.length; i += 4) {
        values.push(parseInt(arr[i+1]));
        values.push(null);
      }
    }
  }
  console.log(values);
  return values;
}

function getStrDate(arr){
  values = [];
  hour = new Date(arr[1].split('~')[1]).getHours();
  //結束時間6點代表為晚上
  var startIndex;
  if(hour == 6){
    startIndex = 3;
  }else{
    startIndex = 1;
  }
  for (let i = startIndex; i < arr.length; i += 4) {
    var time = new Date(arr[i].split('~')[0]);
    var month = time.getMonth() + 1;
    var date = time.getDate();
    var day = time.getDay();
    switch (day) {
      case 0:
        day = "日";
        break;
      case 1:
        day = "一";
        break;
      case 2:
        day = "二";
        break;
      case 3:
        day = "三";
        break;
      case 4:
        day = "四";
        break;
      case 5:
        day = "五";
        break;
      case 6:
        day = "六";
        break;
    }
    if(month < 10){
      month = '0' + month;
    }
    if(date < 10){
      date = '0' + date;
    }
    var strDate = month.toString() + '/' + date.toString() + '(' + day + ')';
    values.push("白天" + strDate);
    values.push("晚上");
  }
  console.log(values);
  return values;
}


function getWeatherForecast_3hrs(cityId, townName, elementName) {
  // 請求 URL
  const url = `https://opendata.cwb.gov.tw/api/v1/rest/datastore/${cityId}?Authorization=CWB-5E6CA7B9-D0AD-4A37-A866-38DF47F8D8E2&locationName=${townName}&elementName=${elementName}`;
  // 發送請求
  var locationData;
  return fetch(url, {
    method: 'GET',
    headers: {
      'Accept': 'application/json'
    }
  })
    .then(response => response.json())
    .then(data => {
      // 在這裡處理返回的 JSON 資料
      locationData = data.records.locations[0].location[0].weatherElement;
      //console.log(data);
      // 將結果顯示在網頁上
      //result.innerHTML = JSON.stringify(locationData, null, 2);
      return get_element_values(locationData);
    })
    .catch(error => console.error(error));
}

function get_element_values(json) {
  //console.log(json);
  const res = json[0].time;
  const values = [json[0].elementName];
  for (let i = 0; i < res.length; i++) {
    values.push(res[i].startTime + '~' + res[i].endTime);
    values.push(res[i].elementValue[0].value);
  }
  result.innerHTML = JSON.stringify(values, null, 2);
  console.log(values);
  return values;
}

const countySelect = document.getElementById('countySelect');
const townSelect = document.getElementById('townSelect');

// 鄉鎮清單物件，以縣市為 key，對應鄉鎮的陣列為 value
const townData = {
    '宜蘭縣': ['頭城鎮', '礁溪鄉', '壯圍鄉', '員山鄉', '宜蘭市', '大同鄉', '五結鄉', '三星鄉', '羅東鎮', '冬山鄉', '南澳鄉', '蘇澳鎮'],
    '桃園市': ['大園區', '蘆竹區', '觀音區', '龜山區', '桃園區', '中壢區', '新屋區', '八德區', '平鎮區', '楊梅區', '大溪區', '龍潭區', '復興區'],
    '新竹縣': ['新豐鄉', '湖口鄉', '新埔鎮', '竹北市', '關西鎮', '芎林鄉', '竹東鎮', '寶山鄉', '尖石鄉', '橫山鄉', '北埔鄉', '峨眉鄉', '五峰鄉'],
    '苗栗縣': ['竹南鎮', '頭份市', '三灣鄉', '造橋鄉', '後龍鎮', '南庄鄉', '頭屋鄉', '獅潭鄉', '苗栗市', '西湖鄉', '通霄鎮', '公館鄉', '銅鑼鄉', '泰安鄉', '苑裡鎮', '大湖鄉', '三義鄉', '卓蘭鎮'],
    '彰化縣': ['伸港鄉', '和美鎮', '線西鄉', '鹿港鎮', '彰化市', '秀水鄉', '福興鄉', '花壇鄉', '芬園鄉', '芳苑鄉', '埔鹽鄉', '大村鄉', '二林鎮', '員林市', '溪湖鎮', '埔心鄉', '永靖鄉', '社頭鄉', '埤頭鄉', '田尾鄉', '大城鄉', '田中鎮', '北斗鎮', '竹塘鄉', '溪州鄉', '二水鄉'],
    '南投縣': ['仁愛鄉', '國姓鄉', '埔里鎮', '草屯鎮', '中寮鄉', '南投市', '魚池鄉', '水里鄉', '名間鄉', '信義鄉', '集集鎮', '竹山鎮', '鹿谷鄉'],
    '雲林縣': ['麥寮鄉', '二崙鄉', '崙背鄉', '西螺鎮', '莿桐鄉', '林內鄉', '臺西鄉', '土庫鎮', '虎尾鎮', '褒忠鄉', '東勢鄉', '斗南鎮', '四湖鄉', '古坑鄉', '元長鄉', '大埤鄉', '口湖鄉', '北港鎮', '水林鄉', '斗六市'],
    '嘉義縣': ['大林鎮', '溪口鄉', '阿里山鄉', '梅山鄉', '新港鄉' ,'民雄鄉', '六腳鄉', '竹崎鄉', '東石鄉', '太保市', '番路鄉', '朴子市', '水上鄉', '中埔鄉', '布袋鎮', '鹿草鄉', '義竹鄉', '大埔鄉'],
    '屏東縣': ['高樹鄉', '三地門鄉', '霧臺鄉', '里港鄉', '鹽埔鄉', '九如鄉', '長治鄉', '瑪家鄉', '屏東市', '內埔鄉', '麟洛鄉', '泰武鄉', '萬巒鄉', '竹田鄉', '萬丹鄉', '來義鄉', '潮州鎮', '新園鄉', '崁頂鄉', '新埤鄉', '南州鄉', '東港鎮', '林邊鄉', '佳冬鄉', '春日鄉', '獅子鄉', '琉球鄉', '枋山鄉', '牡丹鄉', '滿州鄉', '車城鄉', '恆春鎮', '枋寮鄉'],
    '臺東縣': ['長濱鄉', '海端鄉', '池上鄉', '成功鎮', '關山鎮', '東河鄉', '鹿野鄉', '延平鄉', '卑南鄉', '臺東市', '太麻里鄉', '綠島鄉', '達仁鄉', '大武鄉', '蘭嶼鄉', '金峰鄉'],
    '花蓮縣': ['秀林鄉', '新城鄉', '花蓮市', '吉安鄉', '壽豐鄉', '萬榮鄉', '鳳林鎮', '豐濱鄉', '光復鄉', '卓溪鄉', '瑞穗鄉', '玉里鎮', '富里鄉'],
    '澎湖縣': ['白沙鄉', '西嶼鄉', '湖西鄉', '馬公市', '望安鄉', '七美鄉'],
    '基隆市': ['安樂區', '中山區', '中正區', '七堵區', '信義區', '仁愛區', '暖暖區'],
    '新竹市': ['北區', '香山區', '東區'],
    '嘉義市': ['東區', '西區'],
    '臺北市': ['北投區', '士林區', '內湖區', '中山區', '大同區', '松山區', '南港區', '中正區', '萬華區', '信義區', '大安區', '文山區'],
    '高雄市': ['楠梓區', '左營區', '三民區', '鼓山區', '苓雅區', '新興區', '前金區', '鹽埕區', '前鎮區', '旗津區', '小港區', '那瑪夏區', '甲仙區', '六龜區', '杉林區', '內門區', '茂林區', '美濃區', '旗山區', '田寮區', '湖內區', '茄萣區', '阿蓮區', '路竹區', '永安區', '岡山區', '燕巢區', '彌陀區', '橋頭區', '大樹區', '梓官區', '大社區', '仁武區', '鳥松區', '大寮區', '鳳山區', '林園區', '桃源區'],
    '新北市': ['石門區', '三芝區', '金山區', '淡水區', '萬里區', '八里區', '汐止區', '林口區', '五股區', '瑞芳區', '蘆洲區', '雙溪區', '三重區', '貢寮區', '平溪區', '泰山區', '新莊區', '石碇區', '板橋區', '深坑區', '永和區', '樹林區', '中和區', '土城區', '新店區', '坪林區', '鶯歌區', '三峽區', '烏來區'],
    '臺中市': ['北屯區', '西屯區', '北區', '南屯區', '西區', '東區', '中區', '南區', '和平區', '大甲區', '大安區', '外埔區', '后里區', '清水區', '東勢區', '神岡區', '龍井區', '石岡區', '豐原區', '梧棲區', '新社區', '沙鹿區', '大雅區', '潭子區', '大肚區', '太平區', '烏日區', '大里區', '霧峰區'],
    '臺南市': ['安南區', '中西區', '安平區', '東區', '南區', '北區', '白河區', '後壁區', '鹽水區', '新營區', '東山區', '北門區', '柳營區', '學甲區', '下營區', '六甲區', '南化區', '將軍區', '楠西區', '麻豆區', '官田區', '佳里區', '大內區', '七股區', '玉井區', '善化區', '西港區', '山上區', '安定區', '新市區', '左鎮區', '新化區', '永康區', '歸仁區', '關廟區', '龍崎區', '仁德區'],
    '連江縣': ['南竿鄉', '北竿鄉', '莒光鄉', '東引鄉'],
    '金門縣': ['金城鎮', '金湖鎮', '金沙鎮', '金寧鄉', '烈嶼鄉', '烏坵鄉']
};

countySelect.addEventListener('change', function() {
    // 取得目前所選擇的縣市值
    const selectedCounty = countySelect.value.split('_')[0];

    // 清空鄉鎮選項
    townSelect.innerHTML = '<option value="" disabled selected>-- Select County --</option>';
    
    // 如果有選擇縣市，動態生成對應的鄉鎮選項
    if (selectedCounty) {
        //alert(selectedCounty);
    // 根據所選擇的縣市，從鄉鎮清單物件中取得對應的鄉鎮陣列
        const towns = townData[selectedCounty];
        //console.log(towns);
        // 將鄉鎮陣列中的元素建立成 option 標籤，加入到鄉鎮下拉式選單中
        for (let i = 0; i < towns.length; i++) {
            const option = document.createElement('option');
            option.value = 1001701;
            option.textContent = towns[i];
            townSelect.appendChild(option);
        }
        // 顯示鄉鎮下拉式選單
        townSelect.disabled = false;
    }
});
const canvas = document.getElementById('myChart');
const downloadBtn = document.getElementById('download-btn');
downloadBtn.addEventListener('click', () => {
    // 取得 canvas 圖片資料
    const imgData = canvas.toDataURL('image/png');
    
    // 建立一個下載連結
    const link = document.createElement('a');
    link.href = imgData;
    link.download = `${cityName}${townName}溫度預測圖.png`;
    
    // 將連結加到文件中，並自動點擊下載
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});
