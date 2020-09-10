function audio_play(src){
	var http='http://sound.yywz123.com/qsbdcword/'+src.substr(0,1)+'/'+src+'.mp3';
	var audio=new Audio(http);
	audio.play();
}