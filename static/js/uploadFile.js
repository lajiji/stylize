if(document.getElementById('file')){
    document.getElementById('file').onchange = function() {
         // 没选中图片时清除
        if(this.files.length===0){
            document.getElementById('image').getElementsByTagName('img').scr=''    }
        var imgFile = this.files[0];
        var fr = new FileReader();
        fr.onload = function() {
            console.log(document.getElementById('image'))
            document.getElementById('image').getElementsByTagName('img')[0].src = fr.result;
        };
        fr.readAsDataURL(imgFile);
    };
 }
document.getElementsByClassName("submit-btn").onclick=function(){
    // todo
    // 校验之后再发送
}
if(document.getElementById('video-file')){
    document.getElementById('video-file').onchange=function(){
        if(this.files.length===0){
            document.getElementById("video").src=""
        }
        var videoFile = this.files[0];
        var fr = new FileReader();
        fr.readAsDataURL(videoFile)
        fr.onload = ()=>{
            document.getElementById("video").src=fr.result;
        }
    }
}
if(document.getElementById('step-next')){
    document.getElementById('step-next').onclick = function(){
        document.getElementById('step-one').style.display = "none"
        document.getElementById('step-two').style.display = "block";
    }
}
if(document.getElementById('step-forward')){
    document.getElementById('step-forward').onclick = function(){
        document.getElementById('step-two').style.display = "none";
        document.getElementById('step-one').style.display = 'block';
    }
}