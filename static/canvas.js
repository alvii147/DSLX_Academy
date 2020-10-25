window.addEventListener("load", () => {
    const canvas = document.querySelector("#canvas");
    const ctx = canvas.getContext("2d");
    var rect = canvas.getBoundingClientRect();
    console.log(rect.top, rect.right, rect.bottom, rect.left);

    const height = 135;
    const width = 1000;
    canvas.height = height;
    canvas.width = width;

    let painting = false;

    function startPos(){
        painting = true;
    }

    function donePos(){
        painting = false;
        ctx.beginPath();
    }

    function paint(e){
        if(!painting){
            return;
        }
        ctx.lineWidth = 4;
        ctx.lineCap = "round";
        ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
    }

    canvas.addEventListener("mousedown", startPos);
    canvas.addEventListener("mouseup", donePos);
    canvas.addEventListener("mousemove", paint);
});

function sendImage() {
    const canvas = document.querySelector("#canvas");
    const dataURL = canvas.toDataURL();
    console.log(dataURL)
    $.ajax({
        url: "/handwriting/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(dataURL),
        success: function(response){
            console.log(response)
            document.location.href = "results/"
        }
    })
}

function clearCanvas(){
    const canvas = document.querySelector("#canvas");
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height)
}