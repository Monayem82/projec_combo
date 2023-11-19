const api_key=`b5ce7e62f25a60641371cbfb4a866664`;

const loadTempareture =async (city='rangpur')=>{
    const url =`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}&units=metric`;
    try {
        const res=await fetch(url);
        const data =await res.json();
        showTemparetureFun(data);
    } catch (error) {
        console.log(error);
    }
}
const showTemparetureFun = (temp) =>{
    console.log(temp);
    const showtempareture=document.getElementById('show-tempareture');
    showtempareture.innerHTML=`${temp.main.temp}`;
    displayWeather('show-city',temp.name)
    displayWeather('condition',temp.weather[0].main);
    const showCityName=document.getElementById('show-city');
    showCityName.innerHTML=`${temp.name}`;
}

const displayWeather=(id,weaterValue)=>{
    const showCityName=document.getElementById(id);
    showCityName.innerText=weaterValue;
}

document.getElementById('btn-search').addEventListener('click',function(){
    const searchField=document.getElementById('input-field');
    const searchCity=searchField.value;
    loadTempareture(searchCity);
});
console.log('connect')
loadTempareture()