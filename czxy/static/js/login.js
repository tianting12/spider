function submitLogin() {
    if(document.getElementById('UserName').value === ""){
        alert('请输入用户名！');
        document.getElementById('UserName').focus();
        return false;
    }
    if (document.getElementById('Password').value === ''){
        alert("请输入密码");
        document.getElementById('Password').focus();
        return  false;
    }
    DoLogin();
}

function DoLogin() {
    var UserName = document.getElementById('UserName').value;
    var Password = document.getElementById('Password').value;

    var url = '';

}