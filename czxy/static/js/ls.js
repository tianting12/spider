function check() {
    if(document.getElementById("username").value==="") {
        alert("没有输入用户名！");
         return false;
      } else if(document.getElementById("password").value==="") {
        alert("没有输入密码！");
        return false;
      } else {
        alert("提交成功！");
        return true;
       }
    }
    function check_code() {
      console.log(1);
      //获取账号
      var code =
        document.getElementById("code").value;
      //校验其格式(\w字母或数字或下划线)
      var span =
        document.getElementById("code_msg");
      var reg = /^\w{6,10}$/;
      if(reg.test(code)) {
        //通过，增加ok样式
        span.className = "ok";
      } else {
        //不通过，增加error样式
        span.className = "error";
      }
    }
    function check_pwd(){
      console.log(2);
      var code2 =document.getElementById("pwd").value;
      var span2 =
        document.getElementById("pwd_msg");
      var reg2 = /^\w{6,10}$/;
      if(reg2.test(code2)) {
        span2.className = "ok";
      } else {
        span2.className = "error";
      }

    }