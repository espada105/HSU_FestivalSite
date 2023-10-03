function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
 
// Line up some sky vars
var c = document.getElementById("sky");
var ctx = c.getContext("2d");
var xMax = c.width = window.screen.availWidth;
var yMax = c.height = window.screen.availHeight;
var hmTimes = Math.round(xMax + yMax);	

var star2 = document.getElementById("star2");
 
var tl = new TimelineLite();
var moon = new Image();
moon.src = "../static/img/moon.png";

//별똥별
for(var i=0; i<=hmTimes; i++) {
  var x = getRandomInt(300,xMax/4);
  var y = getRandomInt(-100,yMax/4);
  var r = Math.floor((Math.random()*2)+1);//getRandomInt(0.5,2);
  tl.to(star2, Math.random(), {x:x,y:y,r:r,delay:Math.random()})
    .to(star2, 1, {x:y,y:x,autoAlpha:1})
    .to(star2, .5, {autoAlpha:0},"-=0.5");
}

//달 그림 삽입
moon.onload = function() {
    //이미지의 원하는 부분만 잘라서 그리기
    //drawImage(이미지객체, 
    //        이미지의 왼위 부분x, 이미지의 왼위 부분y, 이미지의 원하는 가로크기, 이미지의 원하는 세로크기,
    //        사각형 부분x, 사각형 부분y, 가로크기, 세로크기)
    //draw.drawImage(img, 100,100, 300,300, 50,50, 250,300);
    
    //전체 이미지 그리기
    //drawImage(이미지객체, 사각형 왼위 x, 사각형 왼위 y, 가로크기, 세로크기)
    moonWidth = xMax * 0.9;
    moonHeight = yMax * 0.4;
    x = 0;
    y = yMax - moonHeight;
    ctx.drawImage(moon, -143, 489, 550, 616);
}

//작은별 그리기
function drawing() {
	for(var i=0; i<=hmTimes; i++) {
      var xMax2 = 341;
      var yMax2 = 298;
	  var randomX = Math.floor((Math.random()*xMax2)+49);
	  var randomY = Math.floor((Math.random()*yMax2)+1);
	  var randomSize = Math.floor((Math.random()*2)+1);
	  var randomOpacityOne = Math.floor((Math.random()*9)+1);
	  var randomOpacityTwo = Math.floor((Math.random()*9)+1);
	  var randomHue = Math.floor((Math.random()*360)+1);
    if(randomSize>1) {
      ctx.shadowBlur = Math.floor((Math.random()*15)+5);
      ctx.shadowColor = "white";
	  }

    //hsla(색조, 채도, 밝기, 불투명도)
    ctx.fillStyle = "hsla("+randomHue+", 30%, 80%, ."+randomOpacityOne+randomOpacityTwo+")";
        //fillRect(x좌표, y좌표, 넓이, 높이)
        ctx.fillRect(randomX, randomY, randomSize, randomSize);
	}
}

// drawing();