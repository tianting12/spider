var buildList = ['博古楼','博弈北','博弈南'];
var alllabList =[
    ['云教室1','云教室2'],
    ['三楼实验室','四楼实验室','博弈北301','博弈北302'],
    ['博弈南301','博弈南302']
];

function f1() {
    var build = document.getElementById('building');
    build.length = buildList.length+1;
    for (var i=1;i<build.length;i++){
        build[i].innerText = buildList[i-1];
        build[i].value = i;
    }

}

function f2() {
    var lab = document.getElementById('lab');
    var build = document.getElementById('building');
    lab.value = 0;
    var labList = alllabList[build.value - 1];
    lab.length = labList.length+1;
    for (var i=1; i<lab.length;i++){
        lab[i].innerText =labList[i-1];
        lab[i].value =i
    }
}