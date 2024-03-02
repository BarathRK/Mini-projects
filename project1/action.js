var sec=0;
var hrs = 0;
var ch;
var min=0;
const h = document.querySelector(".hrs");
const m = document.querySelector(".min");
const s = document.querySelector(".sec");


function start(){
 ch = setInterval(function(){
    sec+=1;
    
    if(sec>=60){
        sec= 0;
        min+=1;
    }
    if(min>=60){
        hrs+=1;
    }
    if(sec < 10){
        
     s.innerText="0"+sec;   
    }
    if(min<10){m.innerText="0"+min;}
    if(hrs<10){h.innerText="0"+hrs;}
    if(min>=10 ){
        m.innerText=min;}
        if(hrs>=10){
    h.innerText = hrs;}
   if(sec>=10){
    s.innerText=sec;}
   
    },1000);
}

function stop(){
    clearInterval(ch);
}
function clearscreen(){
   sec= 0;
   min =0;
   hrs=0;
   h.innerText = hrs;
   m.innerText=min;
   s.innerText=sec;
}
