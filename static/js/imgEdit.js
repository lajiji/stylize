let main = document.getElementById("styleRes");
let resList = document.getElementById("resList");
let editor = document.getElementById("editor");
let id = undefined;

function edit(img, originPath) {
    main.style.display = "none";
    resList.style.display = "none";
    editor.style.display = "block";
    initEditor(img, originPath);
}
if (document.getElementById("resList")) {
    document.getElementById("resList").onclick = function(e) {
        let target = e.target;
        if (target.className === "btn-edit") {
            id = target.id.split("-")[1];
            let originPath = target.dataset.originpath;
            let img = document.getElementById(`pic-${id}`);
            edit(img, originPath);
        } else if (target.className === "btn-save") {
            id = target.id.split("-")[1];
            let img = document.getElementById(`pic-${id}`);
            let saveA = document.createElement("a");
            document.body.appendChild(saveA);
            saveA.href = img.src;
            saveA.download = "zspic" + new Date().getTime();
            saveA.target = "_blank";
            saveA.click();
        }
    };
}
if (document.getElementById("quitEdit")) {
    document.getElementById("quitEdit").onclick = function(e) {
        let canvas = document.getElementById("drawing-board");
        let imgURL = canvas.toDataURL("image/png");
        main.style.display = "block";
        resList.style.display = "block";
        editor.style.display = "none";
        document.getElementById(`pic-${id}`).src = imgURL;
        id = undefined;
    };
}