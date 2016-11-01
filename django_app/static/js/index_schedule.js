 function color_check(start_time, finish_time){
     f = new Date(finish_time)
     s = new Date(start_time)
     console.log("time: " + s.getHours() + s.getMinutes())
     s_min = s.getMinutes()
     s_hour = s.getHours()

     if (s.getMinutes()/10==0)
        s_id =("p"+s.getHours()+"-"+1);
     else
        s_id =("p"+s.getHours()+"-"+s.getMinutes()/10);

     if (s.getMinutes()/10==0)
        s_min = 1;
     else
        s_min = s.getMinutes()/10;


     console.log("s_min: " + s_min)
     console.log("s_hour: " + s_hour)

     s_id = "p"+s_hour+"-"+s_min
     gap = ((f.getTime() - s.getTime())/60000);
     turn = 1;

     if (gap > 10)
         turn = gap/10;

     for (i=0;i<turn;i++){

     }
     console.log("s_id: " + s_id);
     console.log("turn: " + turn);
     console.log('#' + s_id);
     var s_table = $('#' + s_id);
     console.log(s_table);
     s_table.addClass('debug')


 };
