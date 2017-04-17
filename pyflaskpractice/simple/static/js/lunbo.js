$(function(){
//下方for循环
    var size=$(".img li").size()
    for(var i=1; i<=size; i++){
        var li="<li>"+i+"</li>";
        $(".num").append(li)
    }
    /*size  获取当前元素个数*/

//手动控制轮播
    $(".img li").eq(0).show()
    $(".num li").eq(0).addClass('active-1')
    /*mouseover  可以改成点击事件  click*/
    $(".num li").mouseover(function(){
        $(this).addClass('active-1').siblings('li').removeClass('active-1')
        var index=$(this).index()  /*index  当前元素的意思索引值*/
        i=index; //i值和自动轮播值是相同的
        $(".img li").eq(index).stop().fadeIn(/*淡入*/).siblings().stop().fadeOut(/*淡出*/)		/*eq 0开始*/
    });

//自动控制轮播
    var i=0;
    var t=setInterval(move,3000)	//定时器
    //右
    function move(){
        i++;
        if(i==size){i=0;}
        //$(".num li").eq(i).addClass('active-1').siblings('li').removeClass('active-1');
        $(".img li").eq(i).fadeIn().siblings().fadeOut();
    };
    //左
    function moveL(){
        i--;
        if(i==-1){i=size-1;}
        //$(".num li").eq(i).addClass('active-1').siblings('li').removeClass('active-1');
        $(".img li").eq(i).fadeIn().siblings().fadeOut();
    };
//自动轮播鼠标经过移入和移除
    $(".out").hover(function(){
        clearInterval(t)
    },function(){
        t=setInterval(move,1500)
    });

//左右按钮
    $(".out .left").click(function(){
        moveL()
    })
    $(".out .right").click(function(){
        move()
    });
 //鼠标点击放大
    $(".img li").click(function(){

    });
});